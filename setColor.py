#!/usr/bin/python3
import leglight
import sys


def main(argv):
    allLights = leglight.discover(3)
    #print(allLights)
    color = int(sys.argv[1])
    
    for lights in allLights:
        lights.color(color)



if __name__ == '__main__':
    #    print(f'Args : {len(sys.argv)} ')
    if len(sys.argv) == 2 : 
        main(sys.argv[1:])
    else:
        print(f'Needs one argumments.')
        print(f'{sys.argv[0]} <color_temp>')
