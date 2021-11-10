#!/usr/bin/python3
import leglight
import sys


def main(color):
    allLights = leglight.discover(3)
    #print(allLights)
#    print(f'Color is : {type(color)}')
    for lights in allLights:
        newTemp=lights.isTemperature + int(color)
        if newTemp > 6900:
            newTemp = 6900
        if newTemp < 2900:
            newTemp = 2900
        lights.color(newTemp)
        print(f'{lights.name}: {lights.isTemperature}')        


if __name__ == '__main__':
#    print(f'Args : {len(sys.argv)} ')
    if len(sys.argv) == 2 :
        if (int(sys.argv[1])<0 ):
#            print(f'Negative increase!')
            main(int(sys.argv[1]))
        else:
#            print(f'Positive increase, we change to -1 !')
            main(-1 * int(sys.argv[1]))
    else:
        main(-100)
