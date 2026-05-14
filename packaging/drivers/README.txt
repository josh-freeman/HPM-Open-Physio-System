Drop Arduino USB-serial driver installers here before running make_installer.bat.

The PI runs whichever matches their HPM box (running all three is harmless):

  CH341SER.EXE          — most cheap Arduino clones (CH340/CH341 USB chip)
                          https://www.wch-ic.com/downloads/CH341SER_EXE.html

  CP210x_Universal_Windows_Driver.zip
                        — Silicon Labs CP2102/CP2104
                          https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers

  CDM-v2.xx.xx-WHQL-Certified.exe
                        — FTDI FT232RL (genuine Arduinos and many official boards)
                          https://ftdichip.com/drivers/vcp-drivers/

If this folder is empty at install time, the Inno Setup script silently skips
the drivers/ section. You can ship the installer without them and tell the PI
to install drivers separately, but bundling them is friendlier.
