================================================================================
  HPM Open Physio System  —  read me
================================================================================

Welcome. This is everything you need to run a session.

--------------------------------------------------------------------------------
  STEP 1 — Plug in the hardware (once, in this order)
--------------------------------------------------------------------------------

  Battery pack ─► USB hub ─► laptop
                  USB hub ─► USB power blocker ─► HPM box
                  USB hub ─► Elgato webcam

  Confirm the green LED is on the front of the HPM box.

--------------------------------------------------------------------------------
  STEP 2 — First time only:  install the Arduino driver
--------------------------------------------------------------------------------

  Open the "drivers" folder next to this file. Run the installer that matches
  your HPM box (CH340 for most clones, CP2102 for some, FTDI for a few).
  If you don't know which one, run them all — they don't conflict.
  This only has to be done once per laptop.

--------------------------------------------------------------------------------
  STEP 3 — Launch HPM
--------------------------------------------------------------------------------

  Double-click "HPM" on your desktop.

  The first time you launch it, Windows may show a "Windows protected your PC"
  warning because the app isn't code-signed yet. Click "More info" → "Run anyway".
  This warning will not appear on subsequent launches.

--------------------------------------------------------------------------------
  STEP 4 — Run a session through the wizard
--------------------------------------------------------------------------------

  The HPM window opens to the Setup Wizard. Follow it stage by stage:

    1. Subject ID            — type a participant identifier
    2. Hardware Check        — tick all four boxes (only when each is true)
    3. Signal Quality        — 30-second baseline; check the live trace
    4. Launch Experiment     — opens Pavlovia in your browser

  In the top-right corner of the window, switch the mode to "Participant Mode"
  before handing the laptop to the participant. Switch back to "RA Mode" when
  they finish.

--------------------------------------------------------------------------------
  STEP 5 — Find your data
--------------------------------------------------------------------------------

  Each session writes a folder to:
      Documents\HPM\sessions\<subject>_<date>_<time>\

  Open the file named  physiodata_Fig01_ecg_qrs_diagnostic.png  first.
  It tells you whether the recording is usable.

--------------------------------------------------------------------------------
  Common issues
--------------------------------------------------------------------------------

  HPM box has no LED                  → Try a different USB port. Replace
                                        the cable. Check the battery pack.

  Wizard won't advance past           → One of the four boxes is not actually
  Hardware Check                       true. The Faraday cage box is the
                                        one most often missed.

  EDA reading shows ~40 µS stuck      → The 3.5 mm jack isn't fully seated.
                                        Push it in until it clicks.

  No heart rate visible               → Electrode lost adhesion. Re-apply
                                        with fresh hydrogel pad.

  "Bridge: STOPPED" mid-session       → USB cable came loose. Stop, re-seat
                                        the power blocker, restart.

--------------------------------------------------------------------------------
  Need help?
--------------------------------------------------------------------------------

  Project source and issue tracker:
      https://github.com/adamrcobb/HPM-Open-Physio-System
