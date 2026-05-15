# PyInstaller spec for HPM Open Physio System.
# Build:  pyinstaller --noconfirm packaging\HPM.spec
# Output: dist\HPM\HPM.exe  (one-folder bundle; ship the whole dist\HPM folder)
#
# One-file (single .exe) is possible by changing EXE(...) below to use
# COLLECT-less mode, but cold-start is slower because PyInstaller has to
# extract ~400MB to a temp dir on every launch. One-folder is recommended.

# ruff: noqa
import os
from PyInstaller.utils.hooks import (
    collect_all,
    collect_data_files,
    collect_submodules,
)

block_cipher = None
ROOT = os.path.abspath(os.path.join(SPECPATH, ".."))
GUI_DIR = os.path.join(ROOT, "desktop", "gui")

# Heavy scientific deps need full collection so their data files travel with the bundle.
nk_datas, nk_bins, nk_hidden = collect_all("neurokit2")
sk_datas, sk_bins, sk_hidden = collect_all("sklearn")
sm_datas, sm_bins, sm_hidden = collect_all("statsmodels")
sb_datas, sb_bins, sb_hidden = collect_all("seaborn")
mpl_datas, mpl_bins, mpl_hidden = collect_all("matplotlib")

datas = []
datas += nk_datas + sk_datas + sm_datas + sb_datas + mpl_datas
# Bundle the helper Python files so the launcher can dispatch into them.
datas += [
    (os.path.join(GUI_DIR, "hpm_gui_v18.py"), "desktop/gui"),
    (os.path.join(GUI_DIR, "pavlovia_arduino_bridge_v5_2_2.py"), "desktop/gui"),
    (os.path.join(GUI_DIR, "psychophysiology_pipeline_v7_17_2.py"), "desktop/gui"),
]

binaries = nk_bins + sk_bins + sm_bins + sb_bins + mpl_bins

hiddenimports = []
hiddenimports += nk_hidden + sk_hidden + sm_hidden + sb_hidden + mpl_hidden
hiddenimports += [
    # Tkinter submodules — PyInstaller often misses ttk/messagebox/filedialog
    "tkinter",
    "tkinter.ttk",
    "tkinter.messagebox",
    "tkinter.filedialog",
    "tkinter.font",
    "tkinter.simpledialog",
    "tkinter.scrolledtext",
    # Hardware
    "serial.tools.list_ports",
    "serial.tools.list_ports_windows",
    # WebSocket bridge
    "websockets",
    "websockets.legacy",
    "websockets.legacy.server",
    "asyncio",
    # Scientific stack — many lazy submodules
    "scipy.signal",
    "scipy.interpolate",
    "scipy.ndimage",
    "scipy.stats",
    "cv2",
    "PIL._tkinter_finder",
    "pandas",
    "pandas._libs.tslibs.base",
]

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
        "tornado", "zmq",
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
    console=True,         # DEBUG: terminal window stays open so tracebacks are visible.
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
