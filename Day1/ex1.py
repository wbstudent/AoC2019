import math

def fuelMassRec(mass):
    mass2 = math.floor(mass/3) - 2
    if mass2 <= 0:
        return 0
    else:
        return mass2 + fuelMassRec(mass2)

sum = 0
with open('./ex1Input.txt') as input:
    for value in input:
        fuelNeeded = math.floor(int(value)/3) - 2
        sum += fuelNeeded + fuelMassRec(int(fuelNeeded))
print(sum)



