

cat << "EOF"
                  <<<<>>>>>>           .----------------------------.
                _>><<<<>>>>>>>>>       /               _____________)
       \|/      \<<<<<  < >>>>>>>>>   /            _______________)
 -------*--===<=<<           <<<<<<<>/         _______________)
       /|\     << @    _/      <<<<</       _____________)
              <  \    /  \      >>>/      ________)  ____
                  |  |   |       </      ______)____((- \\\\
                  o_|   /        /      ______)         \  \\\\    \\\\\\\
                       |  ._    (      ______)           \  \\\\\\\\\\\\\\\\
                       | /       `----------'    /       /     \\\\\\\
   \\
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
#################################################################################

                   Welcome to the Pegasus first time set-up!
---------------------------------------------------------------------------------
Pegasus is a TETRA scanner intended for use with portable computers
and RTL-SDR receivers to detect and warn drivers of nearby emergency
vehicles. It acts as extra sensory perception so users can continue to
be safe on the roads.

Notes: 
-This set-up is useless without the relevant hardware, but will perform a complete software setup to get you up and running.
-Pegasus does not perform any unlawful acts and if used alone, is not illegal within the UK.
-Pegasus does not decrypt, output or save any information it receives, it only uses signal strength to give a reading.
---------------------------------------------------------------------------------
EOF

read -rsp $'Press any key to start Pegasus installation...\n\n' -n1 key
printf "Installing dependancy packages..."

sudo apt-get -qq --yes install libfftw3-dev
sudo apt-get -qq --yes install libtclap-dev
sudo apt-get -qq --yes install librtlsdr-dev
sudo apt-get -qq --yes install libusb-1.0-0-dev
sudo apt-get -qq --yes install cmake
sudo apt-get -qq --yes install rtl-sdr
sudo git clone https://github.com/AD-Vega/rtl-power-fftw.git
cd rtl-power-fftw
sudo mkdir build
cd build
sudo cmake ..
sudo make install

printf "Dependancy packages installed, calling Pegasus..."
cd
sudo git clone https://github.com/Shmouse/Pegasus.git

printf "Pegasus called, adding to autostart... (only works on raspbian)\n"
echo '@lxterminal -e sudo python3 ~/Pegasus/pegasus.py' >> /etc/xdg/lxsession/LXDE-pi/autostart

printf "\nPegasus has been installed and added to autostart, connect your RTL-SDR USB device and reboot to start scanning!\n"
