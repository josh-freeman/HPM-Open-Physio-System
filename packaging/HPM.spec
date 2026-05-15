# PyInstaller spec for HPM Open Physio System.
# Build:  pyinstaller --noconfirm packaging\HPM.spec
# Output: dist\HPM\HPM.exe  (one-folder bundle; ship the whole dist\HPM folder)
#
# Strategy: heavy hammer. We collect_all() every scientific dependency rather
# than hand-listing submodules, because PyInstaller's auto-detection misses
# many lazy/dynamic imports in this stack. The bundle is bigger (~500 MB)
# but we trade size for "it just works on the first launch on every machine."

# ruff: noqa
import os
from PyInstaller.utils.hooks import (
    collect_all,
    collect_data_files,
    collect_submodules,
    collect_dynamic_libs,
)

block_cipher = None
ROOT = os.path.abspath(os.path.join(SPECPATH, ".."))
GUI_DIR = os.path.join(ROOT, "desktop", "gui")


def gather(name):
    """Best-effort collect_all that doesn't crash if a package isn't installed."""
    try:
        return collect_all(name)
    except Exception:
        return [], [], []


datas, binaries, hiddenimports = [], [], []

# Every heavy scientific dep gets the full treatment. This is the most reliable
# way to keep PyInstaller from missing a submodule on a fresh Windows machine.
for pkg in (
    "neurokit2",
    "sklearn",
    "statsmodels",
    "seaborn",
    "matplotlib",
    "pandas",
    "numpy",
    "scipy",
    "cv2",
    "PIL",
    "websockets",
    "serial",
):
    d, b, h = gather(pkg)
    datas += d
    binaries += b
    hiddenimports += h

# Bundle the helper Python files so the launcher can dispatch into them.
datas += [
    (os.path.join(GUI_DIR, "hpm_gui_v18.py"), "desktop/gui"),
    (os.path.join(GUI_DIR, "pavlovia_arduino_bridge_v5_2_2.py"), "desktop/gui"),
    (os.path.join(GUI_DIR, "psychophysiology_pipeline_v7_17_2.py"), "desktop/gui"),
]

# Explicit hidden imports that PyInstaller's hooks don't always pick up.
hiddenimports += [
    # Tkinter — first thing the GUI imports
    "tkinter",
    "tkinter.ttk",
    "tkinter.messagebox",
    "tkinter.filedialog",
    "tkinter.font",
    "tkinter.simpledialog",
    "tkinter.scrolledtext",
    # Matplotlib backend — must be hidden-imported or backend selection fails silently
    "matplotlib.backends.backend_tkagg",
    "matplotlib.backends.backend_agg",
    # Asyncio loop policies on Windows
    "asyncio",
    "asyncio.windows_events",
    "asyncio.proactor_events",
    # Websockets server stack
    "websockets.legacy",
    "websockets.legacy.server",
    "websockets.server",
    "websockets.protocol",
    "websockets.exceptions",
    # Serial port enumeration on Windows
    "serial.tools.list_ports",
    "serial.tools.list_ports_windows",
    # Misc PyInstaller-on-scientific-Python pitfalls
    "PIL._tkinter_finder",
    "pkg_resources.py2_warn",
    "pkg_resources.markers",
]

# Many tkinter installs need the binary collection too.
binaries += collect_dynamic_libs("cv2")

a = Analysis(
    [os.path.join(SPECPATH, "launcher.py")],
    pathex=[ROOT, GUI_DIR],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    runtime_hooks=[os.path.join(SPECPATH, "frozen_runtime_hook.py")],
    excludes=[
        "PyQt5", "PyQt6", "PySide2", "PySide6",
        "IPython", "jupyter", "notebook",
        "tornado", "zmq", "pytest",
    ],
    noarchive=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="HPM",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,            # UPX trips Windows Defender; not worth it.
    console=True,         # DEBUG: terminal stays open so we catch any remaining errors.
                          # Flip to False for the final non-debug release.
    disable_windowed_traceback=False,
    icon=os.path.join(SPECPATH, "icon.ico") if os.path.exists(os.path.join(SPECPATH, "icon.ico")) else None,
    version=os.path.join(SPECPATH, "version_info.txt") if os.path.exists(os.path.join(SPECPATH, "version_info.txt")) else None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name="HPM",
)
