#!/usr/bin/env python3
#PROJECT PEGASUS TETRA DETECTION

import argparse
import logging
from datetime import datetime
import os
import subprocess as sp
from os import devnull
from collections import deque
from math import sqrt

print('Loading Pegasus...')

__doc__ = "pegasus"


dvnll = open(devnull, 'wb')
freqmin = 380000000
freqmax = 382500000
powerfftw_path = "/usr/local/bin/rtl_power_fftw"
spect = "-f " + str(freqmin) + ":" + str(freqmax)
otherargs = "-c -t 1"
thresh = -56

rpf = sp.Popen([powerfftw_path, spect, "-c", "-t 1", "-q"], stdout=sp.PIPE, shell=False)
try:
	print("Pegasus is now running...")
	for line in iter(rpf.stdout.readline, ''):
		now = datetime.now()
		line = line.decode("utf-8")
		# Ignore garbage output
		if not ('#' in line or not line.strip()):
			floats = list(map(float, line.split()))
			print(now.strftime("%m/%d/%Y %H:%M:%S: ") + str(floats[1]))
			if(floats[1] < thresh):
				print("NEARBY TETRA SIGNAL DETECTED")
				f = open("tetradetections.txt", "a")
				f.write(now.strftime("%m/%d/%Y %H:%M:%S") + ": A TETRA signal stronger than " + str(thresh) + "dB was detected at this time by Pegasus at frequency: " + str(floats[0]) + "Hz \n")
				f.close

except (KeyboardInterrupt, SystemExit): # Press ctrl-c
	rpf.kill()
	print("Buh-bye")
