import re

mylist = []
counter = 0
with open('./ex1Input.txt') as input:
    for value in range(146810, 612564): # +1
        stringValue = str(value)
        try:
            double = re.search(r"(.)\1", stringValue).group(0)
        except:
            continue
        # print(len(str(value)))
        if len(double) > 0:
            hell = True
            for digitpos in range(0, len(stringValue) - 1):
                if int(stringValue[digitpos+1]) < int(stringValue[digitpos]):
                    hell = False
            if hell:
                counter += 1
                print(stringValue)
        # double2 = re.search(r"(\w)\1*", str(value), re.IGNORECASE)
print(counter)
