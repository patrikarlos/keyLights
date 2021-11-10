#!/usr/bin/python3
import leglight
allLights = leglight.discover(3)
print(allLights)

for light in allLights:
    light.on()

