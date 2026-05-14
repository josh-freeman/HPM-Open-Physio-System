@echo off
rem Build the single-file HPM-Setup.exe installer using Inno Setup.
rem Prereq: 1) packaging\build_windows.bat has already been run successfully
rem         2) Inno Setup 6 is installed (https://jrsoftware.org/isdl.php)

cd /d "%~dp0\.."

set "ISCC=C:\Program Files (x86)\Inno Setup 6\ISCC.exe"
if not exist "%ISCC%" set "ISCC=C:\Program Files\Inno Setup 6\ISCC.exe"

if not exist "%ISCC%" (
    echo [error] Inno Setup not found. Install from https://jrsoftware.org/isdl.php
    exit /b 1
)

if not exist dist\HPM\HPM.exe (
    echo [error] dist\HPM\HPM.exe missing. Run packaging\build_windows.bat first.
    exit /b 1
)

"%ISCC%" packaging\HPM_installer.iss
if errorlevel 1 exit /b 1

echo.
echo Installer written to: packaging\Output\HPM-Setup.exe
echo Hand this single file to the PI.
