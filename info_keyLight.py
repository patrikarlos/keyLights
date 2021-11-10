#!/usr/bin/python3
import leglight
allLights = leglight.discover(3)
#print(allLights)

for lights in allLights:
#    print(lights)
#    print(lights.__dict__)
    print(f"{lights.name}")    
    print(f"Address    = {lights.address}:{lights.port} {lights.server}")    
    print(f"Firmware   = {lights.firmwareVersion}")
    print(f"Brightness = {lights.isBrightness}")
    print(f"Color Temp = {lights.isTemperature}")
    if lights.isOn == 0:
        print('Status = OFF')
    else:
        print('Status = ON')
    
#    for k, v in lights.__dict__:
#        print(k, v)
