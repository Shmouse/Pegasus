# Pegasus

### Overview

This script emulates the hardware function of the Target BluEye emergency services alert system. The concept is to use a rtl-sdr compatible radio receiver to continuously scan the typical emergency band radio frequencies using `rtl_power_fftw` as a scanning frontend to rtl-sdr, and then filter/process the scan results for potential emergency radio sources. Pegasus will only work on an up-to-date Raspbian.

Pegasus is automatically configured for TETRA airwave frequencies in the UK.

### Usage & Installation
1. Clone the repository
2. Run the pegasus_setup.sh file to install all dependancies and add Pegasus to autostart
3. Plug in your USB RTL-SDR device.
4. Run the pegasus.py file.
