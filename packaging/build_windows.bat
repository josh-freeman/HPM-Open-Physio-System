@echo off
setlocal enabledelayedexpansion

rem ============================================================================
rem  Build HPM.exe on Windows.
rem  Run from the repository root:   packaging\build_windows.bat
rem  Requires: Python 3.11 (64-bit) installed and on PATH.
rem  Output:   dist\HPM\HPM.exe   (ship the entire dist\HPM folder)
rem ============================================================================

cd /d "%~dp0\.."

where py >nul 2>&1
if errorlevel 1 (
    echo [error] Python launcher 'py' not found. Install Python 3.11 64-bit from python.org.
    exit /b 1
)

echo === [1/5] Creating build venv (.venv-build) ===
if not exist .venv-build (
    py -3.11 -m venv .venv-build
    if errorlevel 1 exit /b 1
)
call .venv-build\Scripts\activate.bat

echo === [2/5] Upgrading pip + installing runtime requirements ===
python -m pip install --upgrade pip wheel setuptools
if errorlevel 1 exit /b 1
python -m pip install -r requirements.txt
if errorlevel 1 exit /b 1

echo === [3/5] Installing PyInstaller ===
python -m pip install "pyinstaller>=6.6"
if errorlevel 1 exit /b 1

echo === [4/5] Cleaning previous build ===
if exist build rmdir /s /q build
if exist dist  rmdir /s /q dist

echo === [5/5] Running PyInstaller ===
pyinstaller --noconfirm --clean packaging\HPM.spec
if errorlevel 1 (
    echo [error] PyInstaller failed. See output above.
    exit /b 1
)

echo.
echo ============================================================================
echo  Build complete.
echo  Bundle:  dist\HPM\
echo  Launch:  dist\HPM\HPM.exe
echo.
echo  To distribute:
echo    1. Zip the entire dist\HPM folder.
echo    2. Optionally bundle drivers\ alongside (CH340 / CP2102 installers).
echo    3. Optionally run packaging\make_installer.bat to produce HPM-Setup.exe
echo       (requires Inno Setup; see packaging\README_FOR_BUILDER.md).
echo ============================================================================
endlocal
