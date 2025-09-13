# -*- mode: python ; coding: utf-8 -*-

from platform import system

VERSION = "v5.0.0"
ICON = "icons/icon.png"
BINARIES = []
NAME = f"Media_Downloader_{VERSION}"

match system():
    case "Windows":
        BINARIES.extend([("ffmpeg.exe", "."), ("ffprobe.exe", ".")])

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=BINARIES,
    datas=[(ICON, 'icons')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name=NAME,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=ICON,
)
