; Inno Setup script for HPM Open Physio System.
; Produces HPM-Setup.exe — a single double-clickable installer the PI runs once.
; Build with: iscc packaging\HPM_installer.iss   (after a successful PyInstaller build)
; Get Inno Setup (free): https://jrsoftware.org/isdl.php

#define MyAppName        "HPM Open Physio System"
#define MyAppVersion     "1.0.0"
#define MyAppPublisher   "HPM"
#define MyAppURL         "https://github.com/adamrcobb/HPM-Open-Physio-System"
#define MyAppExeName     "HPM.exe"

[Setup]
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
SetupIconFile=icon.ico

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
