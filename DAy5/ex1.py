mylist2 = []
with open('./ex1Input.txt') as input:
    for value in input:
        mylist2 = [int(x) for x in value.split(',')]
pos = 0
# mylist2[1] = i
# mylist2[2] = j
mode = 0
inputt = 5
while mylist2[pos] != 99:
    commandStr = str(mylist2[pos])
    for i in range(0, 5-len(commandStr)):
        commandStr = "0" + commandStr
    command = int(commandStr[-2:])
    if command == 99:
        break # readjust
    modesStr = commandStr[0:3]
    modes = [int(char) for char in modesStr]
    if command == 1:
        val1 = mylist2[mylist2[pos + 1]] if modes[2] == 0 else mylist2[pos + 1]
        val2 = mylist2[mylist2[pos + 2]] if modes[1] == 0 else mylist2[pos + 2]
        mylist2[mylist2[pos + 3]] = val1 + val2
        pos += 4
    if command == 2:
        val1 = mylist2[mylist2[pos + 1]] if modes[2] == 0 else mylist2[pos + 1]
        val2 = mylist2[mylist2[pos + 2]] if modes[1] == 0 else mylist2[pos + 2]
        mylist2[mylist2[pos + 3]] = val1 * val2
        pos += 4
    if command == 3:
        pose = mylist2[pos+1]
        mylist2[pose] = inputt
        pos += 2
    if command == 4:
        pose = mylist2[pos + 1]
        print(mylist2[pose])
        # inputt = mylist2[pos + 1]
        pos += 2
    if command == 5:
        param = mylist2[mylist2[pos + 1]] if modes[2] == 0 else mylist2[pos + 1]
        if param != 0:
            pos = mylist2[mylist2[pos + 2]] if modes[1] == 0 else mylist2[pos + 2]
        else:
            pos += 3
    if command == 6:
        param = mylist2[mylist2[pos + 1]] if modes[2] == 0 else mylist2[pos + 1]
        if param == 0:
            pos = mylist2[mylist2[pos + 2]] if modes[1] == 0 else mylist2[pos + 2]
        else:
            pos += 3
    if command == 7:
        param1 = mylist2[mylist2[pos + 1]] if modes[2] == 0 else mylist2[pos + 1]
        param2 = mylist2[mylist2[pos + 2]] if modes[1] == 0 else mylist2[pos + 2]
        val3 = mylist2[pos + 3]
        if param1 < param2:
            mylist2[val3] = 1
        else:
            mylist2[val3] = 0
        pos += 4
    if command == 8:
        param1 = mylist2[mylist2[pos + 1]] if modes[2] == 0 else mylist2[pos + 1]
        param2 = mylist2[mylist2[pos + 2]] if modes[1] == 0 else mylist2[pos + 2]
        val3 = mylist2[pos + 3]
        if param1 == param2:
            mylist2[val3] = 1
        else:
            mylist2[val3] = 0
        pos += 4
    # if command == 3:
    #     if mode == 0:
    #         print(3)
    #     else:
    #         print(3)
    # if command == 4:
    #     if mode == 0:
    #         print(4)
    #     else:
    #         print(3)

print(mylist2[4])
