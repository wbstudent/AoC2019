import itertools

def readList():
    list = []
    with open('./ex1Input.txt') as input:
        for value in input:
            list = [int(x) for x in value.split(',')]
    return list


# perm = list(itertools.permutations([0, 1, 2, 3, 4]))
perm = [[9,8,7,6,5]]
maxOutput = 0
for givPerm in perm:
    pos = 0
    prevOutput = 0
    inputt = []
    for phase in givPerm:
        inputCounter = 0
        inputt = [phase, prevOutput]
        mylist2 = readList()
        pos = 0
        runn = True
        # mylist2[1] = phase
        # mylist2[2] = prevOutput
        # inputt = prevOutput
        while mylist2[pos] != 99 and runn:
            commandStr = str(mylist2[pos])
            for i in range(0, 5-len(commandStr)):
                commandStr = "0" + commandStr
            command = int(commandStr[-2:])
            if command == 99:
                command = 100
                break # readjust
            modesStr = commandStr[0:3]
            modes = [int(char) for char in modesStr]
            if command == 1:
                val1 = mylist2[mylist2[pos + 1]] if modes[2] == 0 else mylist2[pos + 1]
                val2 = mylist2[mylist2[pos + 2]] if modes[1] == 0 else mylist2[pos + 2]
                mylist2[mylist2[pos + 3]] = val1 + val2
                pos += 4
            elif command == 2:
                val1 = mylist2[mylist2[pos + 1]] if modes[2] == 0 else mylist2[pos + 1]
                val2 = mylist2[mylist2[pos + 2]] if modes[1] == 0 else mylist2[pos + 2]
                mylist2[mylist2[pos + 3]] = val1 * val2
                pos += 4
            elif command == 3:
                pose = mylist2[pos+1]
                mylist2[pose] = inputt[inputCounter]
                inputCounter += 1
                pos += 2
            elif command == 4:
                pose = mylist2[pos + 1]
                print(mylist2[pose])
                prevOutput = mylist2[pose]
                pos += 2
                runn = False
            elif command == 5:
                param = mylist2[mylist2[pos + 1]] if modes[2] == 0 else mylist2[pos + 1]
                if param != 0:
                    pos = mylist2[mylist2[pos + 2]] if modes[1] == 0 else mylist2[pos + 2]
                else:
                    pos += 3
            elif command == 6:
                param = mylist2[mylist2[pos + 1]] if modes[2] == 0 else mylist2[pos + 1]
                if param == 0:
                    pos = mylist2[mylist2[pos + 2]] if modes[1] == 0 else mylist2[pos + 2]
                else:
                    pos += 3
            elif command == 7:
                param1 = mylist2[mylist2[pos + 1]] if modes[2] == 0 else mylist2[pos + 1]
                param2 = mylist2[mylist2[pos + 2]] if modes[1] == 0 else mylist2[pos + 2]
                val3 = mylist2[pos + 3]
                if param1 < param2:
                    mylist2[val3] = 1
                else:
                    mylist2[val3] = 0
                pos += 4
            elif command == 8:
                param1 = mylist2[mylist2[pos + 1]] if modes[2] == 0 else mylist2[pos + 1]
                param2 = mylist2[mylist2[pos + 2]] if modes[1] == 0 else mylist2[pos + 2]
                val3 = mylist2[pos + 3]
                if param1 == param2:
                    mylist2[val3] = 1
                else:
                    mylist2[val3] = 0
                pos += 4
    if prevOutput > maxOutput:
        maxOutput = prevOutput
    print("\n\n" + str(maxOutput))
