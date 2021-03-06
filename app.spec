# -*- mode: python ; coding: utf-8 -*-

import sys
import os

from kivy_deps import sdl2, glew

from kivymd import hooks_path as kivymd_hooks_path

path = os.path.abspath("D:\\Kriptogafi-Modern")

datas=[
    ('D:\Kriptogafi-Modern\Logo.png', 'data'),
    ('D:\Kriptogafi-Modern\Credit.png', 'data'),
]

a = Analysis(
    ["app.py"],
    pathex=[path],
    datas = datas,
    hookspath=[kivymd_hooks_path],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
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
    name="Kriptografi Modern",
    console=True,
)