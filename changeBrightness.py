#!/usr/bin/python3
import leglight
import sys


def main(argv):
    allLights = leglight.discover(3)
    #print(allLights)
    colorChange = int(sys.argv[1])
    
    for lights in allLights:
        print(f"{lights.name}")  
        print(f"Brightness = {lights.isBrightness}")
        if colorChange > 0:
            print(f'increase {colorChange}')
            lights.incBrightness(colorChange)
        else:
            bob = abs(colorChange)
            print(f'decrease {bob}')
            lights.decBrightness(bob)

if __name__ == '__main__':
    #    print(f'Args : {len(sys.argv)} ')
    if len(sys.argv) == 2 : 
        main(sys.argv[1:])
    else:
        print(f'Needs one argument')
        print(f'{sys.argv[0]} <change bightnesss>')
