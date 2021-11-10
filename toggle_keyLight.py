#!/usr/bin/python3
import leglight
allLights = leglight.discover(3)
print(allLights)

for light in allLights:
    if (light.isOn):
        light.off()
    else: 
        light.on()
    

