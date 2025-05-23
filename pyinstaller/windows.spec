# -*- mode: python ; coding: utf-8 -*-

VERSION = "v4.1.2"
ICON = "icons/icon.png"
BINARIES = [("ffmpeg.exe", "."), ("ffprobe.exe", ".")]
NAME = f"Media_Downloader_{VERSION}"


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
