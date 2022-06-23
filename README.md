# Pegasus

### Overview

Pegasus is a light-weight python script designed for scanning TETRA airwave frequencies using an RTL-SDR device and a properly configured Linux machine. While their are limitations with RTL-SDR, it is still a suitable method for detecting nearby TETRA devices.

### Dependencies:
```
- libfftw3-dev
- libtclap-dev
- librtlsdr-dev
- libusb-1.0-0-dev
- cmake
- rtl-sdr (keenerd experimental branch: https://github.com/keenerd/rtl-sdr.git)
- rtl_power_fftw: https://github.com/AD-Vega/rtl-power-fftw.git |
```

### Usage & Installation
1. Clone the repository using `sudo git clone https://github.com/Shmouse/Pegasus`
2. Run the pegasus_setup.sh file to install all dependancies.
3. Plug in your USB RTL-SDR device.
4. Run the pegasus.py file.

### Options
`--d` or `--debug` - Puts Pegasus into debug mode, will display dBm values across the whole range so it their changes can be easily monitored.
