#!/usr/bin/env python3
#PROJECT PEGASUS TETRA DETECTION
splash=r"""
                  <<<<>>>>>>           .----------------------------.
                _>><<<<>>>>>>>>>       /               _____________)
       \|/      \<<<<<  < >>>>>>>>>   /            _______________)
 -------*--===<=<<           <<<<<<<>/         _______________)
       /|\     << @    _/      <<<<</       _____________)
              <  \    /  \      >>>/      ________)  ____
                  |  |   |       </      ______)____((- \\\\
                  o_|   /        /      ______)         \  \\\\    \\\\\\\
                       |  ._    (      ______)           \  \\\\\\\\\\\\\\\\
                       | /       `----------'    /       /     \\\\\\\\\
               .______/\/     /                 /       /          \\\
              / __.____/    _/         ________(       /\
             / / / ________/`---------'         \     /  \_
            / /  \ \                             \   \ \_  \
           ( <    \ \                             >  /    \ \
            \/      \\_                          / /       > )
                     \_|                        / /       / /
                                              _//       _//
                                             /_|       /_|
#################################################################################
       _|_|_|    _|_|_|_|    _|_|_|    _|_|      _|_|_|  _|    _|    _|_|_|  
       _|    _|  _|        _|        _|    _|  _|        _|    _|  _|        
       _|_|_|    _|_|_|    _|  _|_|  _|_|_|_|    _|_|    _|    _|    _|_|    
       _|        _|        _|    _|  _|    _|        _|  _|    _|        _|  
       _|        _|_|_|_|    _|_|_|  _|    _|  _|_|_|      _|_|    _|_|_|    
################################################################################"""

#IMPORTS#
import argparse
import logging
from datetime import datetime
import os
import subprocess as sp
from os import devnull
from collections import deque
from math import sqrt

#ARGS#
parser = argparse.ArgumentParser(description='Pegasus Usage')
parser.add_argument("-d", "--debug", action="store_true", dest="debug", help="Enable debugging information.")
args = parser.parse_args()

#GLOBALS#
__doc__ = "pegasus"
dvnll = open(devnull, 'wb')
#Frequencies. Would need multiple RTL-SDR dongles to scan the entire TETRA Airwave range.
freqmin = 380000000 #Minimum frequency in the ranges
freqmax = 382500000 #Maximum freqeuncy in the range
#Program globals.
powerfftw_path = "/usr/local/bin/rtl_power_fftw"
spect = "-f " + str(freqmin) + ":" + str(freqmax) #Some more options
otherargs = "-c -t 1" #Some options
thresh = -39 #The dBm threshold to begin triggering alerts. Alert will adjust accordingly.
averages = [] #Our list for average dBm calculation.
maxav = 1000 #The amount of numbers we hold as averages until we refresh our averages list.
sigstrength = 0 #Signal strength variable for later use.

#SCRIPT#
#Start up rtl_power_fftw with our inputs.
rpf = sp.Popen([powerfftw_path, spect, "-c", "-t 1", "-q", "-r 2400000"], stdout=sp.PIPE, stderr=dvnll, shell=False)

try:
	#Start the program!
	print(splash)
	if (args.debug):
		print("Pegasus is running in debugger mode and will display debug information.")
	if not (args.debug):
		print("\rSignal Strength: [                   ]", end='')

	#Start parsing the output
	for line in iter(rpf.stdout.readline, ''):
		now = datetime.now()
		line = line.decode("utf-8")
		# Ignore garbage output
		if not ('#' in line or not line.strip()):
			floats = list(map(float, line.split()))
			if (args.debug):
				print(now.strftime("%m/%d/%Y %H:%M:%S: ") + str(floats[1]))
			averages.append(floats[1])
			avg = sum(averages)/len(averages)
			#If we're over the threshold!
			if(avg > thresh and len(averages)>10):
				if (args.debug):
					print("TETRA Signal beyond threshold! Check logs for info.")
				if not (args.debug):
					if (avg > thresh and avg < thresh+5):
						print("\rSignal Strength: [|||                ]\r", end='')
						sigstrength=1
					if (avg > thresh+5 and avg < thresh+10):
						print("\rSignal Strength: [||| |||            ]\r", end='')
						sigstrength=2
					if (avg > thresh+10 and avg < thresh+15):
						print("\rSignal Strength: [||| ||| |||        ]\r", end='')
						sigstrength=3
					if (avg > thresh+15 and avg < thresh+20):
						print("\rSignal Strength: [||| ||| ||| |||    ]\r", end='')
						sigstrength=4
					if (avg > thresh+20 and avg < thresh+25):
						print("\rSignal Strength: [||| ||| ||| ||| |||]\r", end='')
						signstrength=5
				f = open("tetradetections.txt", "a")
				f.write(now.strftime("%m/%d/%Y %H:%M:%S") + ": A TETRA signal of: " + str(round(floats[1],2)) + " was logged by Pegasus at frequency: " + str(floats[0]) + "Hz \n")
				f.close

			#Display current average and reset averages list.
			if(len(averages)>maxav):
				if (avg < thresh and not args.debug):
					print("\rSignal Strength: [                   ]     Average: " + str(round(avg,2)) + "\r", end='')
				if (args.debug):
					print("The average dBm is: " + str(avg))
				averages = []

#END SCRIPT#
except (KeyboardInterrupt, SystemExit): # Press ctrl-c
	rpf.kill()
	print("Stopping Pegasus...")
