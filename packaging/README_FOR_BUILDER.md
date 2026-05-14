# Packaging HPM as a Windows .exe

Goal: hand a non-technical PI **one file** they double-click. No terminal,
no Python install, no `pip`.

## What gets produced

| Artifact                          | Size    | What it is                                   |
|-----------------------------------|---------|----------------------------------------------|
| `dist/HPM/HPM.exe` + `dist/HPM/`  | ~400 MB | One-folder PyInstaller bundle                |
| `packaging/Output/HPM-Setup.exe`  | ~150 MB | Single double-clickable installer (Inno Setup) |

The PI gets `HPM-Setup.exe`. They run it once. They get a desktop shortcut and
a Start Menu entry. They never see Python.

## What the build does

`launcher.py` is a tiny dispatcher. The frozen `HPM.exe` runs in one of three
modes depending on its argv:

```
HPM.exe                 -> launches the Tkinter GUI
HPM.exe --bridge ...    -> runs pavlovia_arduino_bridge_v5_2_2.py headless
HPM.exe --pipeline ...  -> runs psychophysiology_pipeline_v7_17_2.py headless
```

`frozen_runtime_hook.py` monkey-patches `subprocess.Popen` inside the GUI so
that when it tries to spawn `[sys.executable, "-u", "<bridge>.py"]`, the call
is rewritten to `[sys.executable, "--bridge"]` and re-enters the dispatcher.
This means **no source changes** to the GUI — the upstream code stays clean.

## Prerequisites on the build machine (Windows only)

1. **Windows 10 or 11, 64-bit.** PyInstaller produces native `.exe`; you
   cannot cross-compile from macOS or Linux.
2. **Python 3.11 64-bit** from python.org. Tick "Add to PATH" during install.
3. **Inno Setup 6** from <https://jrsoftware.org/isdl.php> (only needed if you
   want the single `HPM-Setup.exe` installer instead of a zipped folder).
4. **Git for Windows** — obvious.

## Build, step by step

```cmd
git clone https://github.com/adamrcobb/HPM-Open-Physio-System.git
cd HPM-Open-Physio-System

rem 1. Build the .exe bundle
packaging\build_windows.bat

rem 2. (Optional) Add an icon. Drop a 256x256 .ico file at packaging\icon.ico
rem    and re-run step 1.

rem 3. (Optional) Bundle Arduino USB-serial drivers. Drop the vendor .exe
rem    installers into packaging\drivers\ before running the installer build.
rem    Recommended: CH340, CP2102, FTDI. The PI runs them once.

rem 4. Build the installer
packaging\make_installer.bat
```

The resulting `packaging\Output\HPM-Setup.exe` is what you ship.

## Code signing (optional but recommended)

Without a signature, Windows SmartScreen shows the PI a "Windows protected
your PC" warning the first time they launch. They have to click *More info →
Run anyway*. This is annoying but not blocking — `README_FOR_PI.txt` warns them.

To eliminate the warning, sign both `HPM.exe` and `HPM-Setup.exe` with a
code-signing certificate. Sectigo and DigiCert sell them; standard certs are
~$80–$300/year, EV certs (which clear SmartScreen instantly with no reputation
build-up) are $300–$500/year. Sign with `signtool`:

```cmd
signtool sign /tr http://timestamp.digicert.com /td sha256 /fd sha256 ^
  /a dist\HPM\HPM.exe
signtool sign /tr http://timestamp.digicert.com /td sha256 /fd sha256 ^
  /a packaging\Output\HPM-Setup.exe
```

Run signing **after** PyInstaller and **after** Inno Setup, in that order.

## Things that will go wrong on the first build, and the fix

| Symptom                                             | Fix                                                                        |
|-----------------------------------------------------|----------------------------------------------------------------------------|
| `ModuleNotFoundError: No module named 'cv2'` at runtime | Add `cv2` to `hiddenimports` in `HPM.spec` (already done).                |
| GUI launches but bridge silently fails              | The runtime hook isn't loading. Confirm `HPM.spec` references `frozen_runtime_hook.py` in `runtime_hooks=[...]`. |
| Bundle is huge (~600 MB)                            | Add more entries to the `excludes=[...]` list in `HPM.spec`.              |
| Tkinter window opens then immediately closes        | Run `HPM.exe` from a `cmd` window once with `console=True` in the spec to see the traceback. Switch back to `console=False` after fixing. |
| Antivirus flags `HPM.exe` as suspicious             | This happens with all PyInstaller bundles. Either submit to your vendor for whitelisting, or sign it. |

## Updating

When upstream releases a new version, re-pull the repo, re-run
`build_windows.bat` and `make_installer.bat`. The PI runs the new
`HPM-Setup.exe` over the top of the old install — Inno Setup handles the
upgrade.

## CI

If you want this to build automatically on push, GitHub Actions has a
`windows-latest` runner. The workflow is roughly:

```yaml
on: [push]
jobs:
  build:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.11" }
      - run: packaging\build_windows.bat
      - uses: actions/upload-artifact@v4
        with:
          name: HPM-windows
          path: dist/HPM/
```

That gives you a fresh `HPM.exe` on every commit. Cheap and reliable.
