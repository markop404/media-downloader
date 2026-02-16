#requires -Version 7

using namespace System.Runtime.InteropServices
using namespace System.IO

$ErrorActionPreference = "Stop"

if ([RuntimeInformation]::OSArchitecture -ne [Architecture]::X64) {
    Write-Error "Only x86_64 builds are supported."
    exit 1
}

$arch = [RuntimeInformation]::OSArchitecture.ToString().ToLower()
$sw = [System.Diagnostics.Stopwatch]::StartNew()
$resources = "resources\windows"
$appName = "MediaDownloader"
$appBundleDir = Join-Path "dist" $appName
$outputPath = Join-Path "dist" "${appName}_${arch}.msix"
$deps = Get-Content (Join-Path $resources "deps.json") | ConvertFrom-Json
$manifest = [xml](Get-Content (Join-Path $resources "AppxManifest.xml"))
$tempBinDir = ".tmp\bin"
$tempDownloadsDir = ".tmp\dl"
$tempExpandDir = ".tmp\expand"
$pythonBuildVenv = ".tmp\buildenv"
$buildFiles = @(
    "build"
    "$appName.spec"
    $pythonBuildVenv
    $tempBinDir
    $tempExpandDir
)
$pyinstallerArgs = @(
    "scripts\run.py"
    "--name", $appName
    "--windowed"
    "--icon", "resources\icon.png"
    "--noconfirm"
    "--clean"
)

function Remove-PathRecursive {
    param(
        [Parameter(Mandatory, ValueFromPipeline)]
        [string[]]$Path
    )
    process {
        foreach ($item in $Path) {
            if (Test-Path $item) {
                Remove-Item -Recurse -Force $item
            }
        }
    }
}

function Get-FileHashString {
    param(
        [Parameter(Mandatory, ValueFromPipeline)]
        [string[]]$Path
    )
    return (Get-FileHash $Path).Hash.ToLower()
}

function New-DirectoryIfMissing {
    param(
        [Parameter(Mandatory, ValueFromPipeline)]
        [string[]]$Path
    )
    process {
        foreach ($item in $Path) {
            if (-not (Test-Path $item)) {
                New-Item -ItemType Directory $item
            }
        }
    }
}

function Invoke-CommandOrExit {
    param(
        [Parameter(Mandatory)]
        [scriptblock]$Command
    )
    & $Command
    if ($LASTEXITCODE -ne 0) { exit 2 }
}

Remove-PathRecursive ($buildFiles + "dist")
New-DirectoryIfMissing $tempBinDir, $tempDownloadsDir, $tempExpandDir

foreach ($dep in $deps) {
    $expectedHash = $dep.sources.$arch.sha256
    $url = $dep.sources.$arch.url
    $downloadFileName = [Path]::GetFileName($url)
    $downloadFilePath = Join-Path $tempDownloadsDir $downloadFileName
    $alreadyDownloaded = Test-Path $downloadFilePath
    
    if (
        -not $alreadyDownloaded -or (
            $alreadyDownloaded -and
            (Get-FileHashString $downloadFilePath) -ne $expectedHash
        )
    ) {
        Remove-PathRecursive $downloadFilePath
        Invoke-WebRequest $url -OutFile $downloadFilePath
        $calculatedHash = Get-FileHashString $downloadFilePath
        if ( $calculatedHash -ne $expectedHash ) {
            Write-Error (
                "Hashes for `"$($dep.name)`" don't match: " +
                "expected `"$expectedHash`", got `"$calculatedHash`"."
            )
            exit 3
        }
    }
    
    if ("files" -in $dep.PSObject.Properties.Name) {
        $expandedArchivePath = Join-Path $tempExpandDir ([Path]::GetFileNameWithoutExtension($url))
        Expand-Archive $downloadFilePath -DestinationPath $expandedArchivePath
        foreach ($file in $dep.files) {
            Move-Item (Join-Path $expandedArchivePath $file) $tempBinDir
            $pyinstallerArgs += "--add-binary", ((Join-Path $tempBinDir ([Path]::GetFileName($file))) + ":.")
        }
        Remove-PathRecursive $expandedArchivePath
    } else {
        Copy-Item $downloadFilePath $tempBinDir
        $pyinstallerArgs += "--add-binary", ((Join-Path $tempBinDir $downloadFileName) + ":.")
    }
}

Invoke-CommandOrExit { python -m venv $pythonBuildVenv }
. (Join-Path $pythonBuildVenv "Scripts\Activate.ps1")
Invoke-CommandOrExit { pip install . --group build }
$version = (python -c "from media_downloader import VERSION; print(VERSION)") `
    -replace '^[^\d]*(?<major>\d+)\.(?<minor>\d+)\.(?<patch>\d+).*$', `
             '${major}.${minor}.${patch}'
Invoke-CommandOrExit { pyinstaller $pyinstallerArgs }
deactivate

Remove-PathRecursive $buildFiles

$manifest.Package.Identity.Version = $version + ".0"
$manifest.Package.Identity.ProcessorArchitecture = $arch
$manifest.Save((Join-Path (Resolve-Path $appBundleDir) "AppxManifest.xml"))
Copy-Item -Recurse (Join-Path $resources "resources*.pri") $appBundleDir
Copy-Item -Recurse (Join-Path $resources "icons") $appBundleDir

Invoke-CommandOrExit { MakeAppx pack /d $appBundleDir /p $outputPath }

Write-Host
Write-Host "--------------------------------------------------------------"
Write-Host "$outputPath - $((Get-Item $outputPath).Length / 1MB) MB"
Write-Host "Build finished in $($sw.Elapsed)"
Write-Host