"""
HPM single-binary launcher.

The frozen .exe runs in one of three modes depending on argv:
    HPM.exe                 -> GUI (default; participant + RA mode)
    HPM.exe --bridge ...    -> Pavlovia/Arduino bridge (headless)
    HPM.exe --pipeline ...  -> Post-session analysis pipeline (headless)

The GUI's subprocess calls are monkey-patched at startup (see frozen_runtime_hook.py)
so that when it tries to run [sys.executable, "-u", "pavlovia_arduino_bridge_v5_2_2.py"]
it gets rewritten to [sys.executable, "--bridge"] and re-enters this dispatcher.
"""
import os
import sys
import runpy


def _bundled_script_path(name: str) -> str:
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, "desktop", "gui", name)


def _run_module_as_main(path: str) -> None:
    sys.argv[0] = path
    runpy.run_path(path, run_name="__main__")


def main() -> int:
    args = sys.argv[1:]

    if args and args[0] == "--bridge":
        sys.argv = [sys.argv[0]] + args[1:]
        _run_module_as_main(_bundled_script_path("pavlovia_arduino_bridge_v5_2_2.py"))
        return 0

    if args and args[0] == "--pipeline":
        sys.argv = [sys.argv[0]] + args[1:]
        _run_module_as_main(_bundled_script_path("psychophysiology_pipeline_v7_17_2.py"))
        return 0

    _run_module_as_main(_bundled_script_path("hpm_gui_v18.py"))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except BaseException:
        import traceback
        traceback.print_exc()
        try:
            input("\n[debug build] Press Enter to close this window...")
        except EOFError:
            pass
        sys.exit(1)
