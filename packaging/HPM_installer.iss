; Inno Setup script for HPM Open Physio System.
; Produces HPM-Setup.exe — a single double-clickable installer the PI runs once.
; Build with: iscc packaging\HPM_installer.iss   (after a successful PyInstaller build)
; Get Inno Setup (free): https://jrsoftware.org/isdl.php

#define MyAppName        "HPM Open Physio System"
#define MyAppVersion     "1.0.5"
#define MyAppPublisher   "HPM"
#define MyAppURL         "https://github.com/josh-freeman/HPM-Open-Physio-System"
#define MyAppExeName     "HPM.exe"

[Setup]
; AppId is the upgrade key — same AppId across versions means Inno Setup
; recognizes any subsequent install as an upgrade of the existing one
; instead of a side-by-side install. Do NOT regenerate this between releases.
AppId={{E1B4F2C8-9D6E-4A3B-8C1D-5F7E9A0B2C3D}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
DefaultDirName={autopf}\HPM
DefaultGroupName=HPM
DisableProgramGroupPage=yes
OutputBaseFilename=HPM-Setup
Compression=lzma2/ultra64
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=lowest
PrivilegesRequiredOverridesAllowed=dialog
UninstallDisplayIcon={app}\{#MyAppExeName}
; SetupIconFile is intentionally omitted; drop a 256x256 packaging\icon.ico
; and re-add the line above to brand the installer.

; --- Upgrade behavior --------------------------------------------------------
; If a running HPM.exe is detected, ask the user to close it and shut it down
; cleanly so the installer can replace files in {app}\.
CloseApplications=yes
RestartApplications=no
; A unique mutex name lets us also detect a running instance via a runtime
; check inside the launcher (HPM.exe sets this mutex on startup if extended).
AppMutex=Global\HPM-Open-Physio-System-Mutex
; Always overwrite previous-version files cleanly (PyInstaller bundle layout
; can change between versions; leftover stale files cause subtle import bugs).
DirExistsWarning=no
UsePreviousAppDir=yes
UsePreviousGroup=yes
UsePreviousLanguage=yes
UninstallRestartComputer=no
; Allow reinstall on top of itself without complaining.
DisableDirPage=auto
DisableReadyPage=no
DisableFinishedPage=no
; Required so the upgrade wipes stale files left from older PyInstaller layouts
[InstallDelete]
Type: filesandordirs; Name: "{app}\_internal"
Type: filesandordirs; Name: "{app}\desktop"
Type: files;          Name: "{app}\*.dll"
Type: files;          Name: "{app}\*.pyd"

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "Create a &desktop shortcut"; GroupDescription: "Additional shortcuts:"

[Files]
Source: "..\dist\HPM\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; Bundle Arduino USB-serial drivers for one-time install (optional)
Source: "drivers\*";    DestDir: "{app}\drivers"; Flags: ignoreversion recursesubdirs skipifsourcedoesntexist
Source: "..\README.md"; DestDir: "{app}"; Flags: ignoreversion
Source: "README_FOR_PI.txt"; DestDir: "{app}"; Flags: ignoreversion isreadme

[Icons]
Name: "{group}\HPM";              Filename: "{app}\{#MyAppExeName}"
Name: "{group}\HPM (read me)";    Filename: "{app}\README_FOR_PI.txt"
Name: "{group}\Uninstall HPM";    Filename: "{uninstallexe}"
Name: "{autodesktop}\HPM";        Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "Launch HPM"; Flags: nowait postinstall skipifsilent
