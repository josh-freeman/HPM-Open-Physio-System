"""
Runtime hook injected into the frozen bundle.

Two jobs:
1. Rewrite subprocess.Popen calls so that GUI requests for the bridge/pipeline
   .py files are translated into re-invocations of HPM.exe with --bridge / --pipeline.
2. Provide a no-op stand-in for the GUI's existence checks against bundled .py
   files (the files live inside _MEIPASS, not next to the .exe).
"""
import os
import sys
import subprocess

_BRIDGE_NAME = "pavlovia_arduino_bridge_v5_2_2.py"
_PIPELINE_NAME = "psychophysiology_pipeline_v7_17_2.py"

_orig_popen = subprocess.Popen


def _rewrite_args(args):
    if not args or not isinstance(args, (list, tuple)):
        return args
    parts = list(args)
    # The GUI invokes either [sys.executable, "-u", "<path>/<script>.py", ...]
    # or [sys.executable, "<path>/<script>.py", ...]. Detect the script name.
    for i, p in enumerate(parts):
        if not isinstance(p, str):
            continue
        base = os.path.basename(p)
        if base == _BRIDGE_NAME:
            return [sys.executable, "--bridge", *parts[i + 1 :]]
        if base == _PIPELINE_NAME:
            return [sys.executable, "--pipeline", *parts[i + 1 :]]
    return args


class _PatchedPopen(_orig_popen):
    def __init__(self, args, *a, **kw):
        super().__init__(_rewrite_args(args), *a, **kw)


subprocess.Popen = _PatchedPopen


# Make os.path.exists report True for the bundled helper scripts even when
# the GUI checks alongside HPM.exe instead of inside _MEIPASS.
_orig_exists = os.path.exists
_meipass = getattr(sys, "_MEIPASS", None)


def _patched_exists(path):
    if _meipass and isinstance(path, str):
        base = os.path.basename(path)
        if base in (_BRIDGE_NAME, _PIPELINE_NAME):
            return os.path.isfile(os.path.join(_meipass, "desktop", "gui", base))
    return _orig_exists(path)


os.path.exists = _patched_exists
