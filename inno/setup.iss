#define AppName                  "Media Downloader"
#define AppSpaceLessName         "MediaDownloader"
#define AppExeName               "MediaDownloader.exe"
#define AppVersion               "5.0.0"
#define AppVersionPrefix         "v"
#define PublisherName            "Marko Pejić"
#define PublisherSpaceLessName   "MarkoPejic"
#define PublisherURL             "https://markopejic.com"
#define AppURL                   "https://downloader.markopejic.com"
#define StartYearCopyright       "2024"
#define CurrentYear              GetDateTimeString('yyyy','','')

[Setup]
AppId={{F6E216EA-9AAE-43D0-88A3-01182BEAE877}
AppName={#AppName}
AppVersion={#AppVersion}
AppVerName={#AppName} {#AppVersionPrefix}{#AppVersion}

AppCopyright={#StartYearCopyright}-{#CurrentYear}  {#PublisherName}
AppPublisher={#PublisherName}

AppPublisherURL={#PublisherURL}
AppSupportURL={#AppURL}
AppUpdatesURL={#AppURL}

VersionInfoDescription={#AppName} {#AppVersionPrefix}{#AppVersion} Installer
VersionInfoProductName={#AppName}
VersionInfoVersion={#AppVersion}

DefaultDirName={autopf}\{#AppSpaceLessName}
OutputBaseFilename={#AppName} {#AppVersionPrefix}{#AppVersion} Installer
OutputDir=..\dist

UninstallDisplayIcon={app}\{#AppExeName}
SetupIconFile=..\icons\icon.ico

DisableDirPage=yes
DisableProgramGroupPage=yes

ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible

SolidCompression=yes
Compression=lzma

WizardStyle=modern
CloseApplications=yes
PrivilegesRequired=lowest

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
Source: "..\dist\{#AppSpaceLessName}\{#AppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\dist\{#AppSpaceLessName}\_internal\*"; DestDir: "{app}\_internal\"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{autoprograms}\{#AppName}"; Filename: "{app}\{#AppExeName}"

[Registry]
Root: HKCU; Subkey: Software\{#PublisherSpaceLessName}\{#AppSpaceLessName}; Flags: uninsdeletekey

[Run]
Filename: "{app}\{#AppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(AppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

