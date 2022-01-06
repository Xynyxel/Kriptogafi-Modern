	# -*- mode: python ; coding: utf-8 -*-

import sys
import os


from kivy_deps import sdl2, glew
from kivymd import hooks_path as kivymd_hooks_path

path = os.path.abspath("D:/Kriptogafi-Modern")
path_data = os.path.abspath("D:/Kriptogafi-Modern")
a = Analysis(
    ["app.py"],
    pathex=[path],
    binaries=[],
    datas=[(path_data, "resources")],
    hiddenimports=['pkg_resources.py2_warn'],
    hookspath=[kivymd_hooks_path,
    "D:/Kriptogafi-Modern"],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False
)
pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
    debug=False,
    strip=False,
    upx=True,
    name="Tutorial",
    console=False,
)