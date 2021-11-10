# keyLights
Some simple scripts to control Corsair KeyLights. Relies on leglight module. 

Requires leglight, https://pypi.org/project/leglight/. 
pip(3) install leglight


All scripts works on ALL detected keyLights.
Nothing is kept in memory, everything is read on run. 


info_keyLight.py shows various information about (detected) keyLights.

setColor.py sets a specific color (temperature).

warmerColor.py increases the color with +100 if not specified, otherwise it changes with the specified amount. +X to make it X degrees warmer, -Y to make it Y degrees cooler.

coolerColor.py decreses the color with 100 if not specified, otherwise it changes the color with the specified amount. Note that this ALWAYS adjust to a degrese. Hence, give it -1000 lowers by 1000. Give it 500, it also lowers by 500.

changeColor.py increases or decreases the color by the specified amount.

changeBrightness.py increase or decrease the brightness, by the input amount.

turn Change the status of the lights.

turnOff_keyLights.py  turn off the lights.
turnOn_keyLights.py  turn on the lights.

