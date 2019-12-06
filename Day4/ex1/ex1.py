import re

mylist = []
counter = 0
with open('./ex1Input.txt') as input:
    for value in range(146810, 612564): # +1
        stringValue = str(value)
        lastdigit = stringValue[0]
        # badCode = True
        foundDouble = False
        foundDoubleReal = False
        forbiddenSnacsk = []
        for digitpos in range(1, len(stringValue)):
            if int(lastdigit) <= int(stringValue[digitpos]):
                if stringValue[digitpos] == lastdigit:
                    foundDouble = True
                    if stringValue[digitpos] in forbiddenSnacsk:
                        foundDouble = False
                    forbiddenSnacsk.append(stringValue[digitpos])
                else:
                    if foundDouble:
                        foundDoubleReal = True
                lastdigit = stringValue[digitpos]
            else:
                foundDouble = False
                foundDoubleReal = False
                break
        if foundDouble or foundDoubleReal:
            print(stringValue)
            counter += 1

print(counter)
