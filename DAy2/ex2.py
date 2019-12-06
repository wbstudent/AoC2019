mylist2 = []
for i in range(100):
    for j in range(100):
        with open('./ex1Input.txt') as input:
            for value in input:
                mylist2 = [int(x) for x in value.split(',')]
        pos = 0
        mylist2[1] = i
        mylist2[2] = j
        while mylist2[pos] != 99:
            command = mylist2[pos]
            if command == 1:
                val = mylist2[mylist2[pos + 1]] + mylist2[mylist2[pos + 2]]
                mylist2[mylist2[pos + 3]] = val
            if command == 2:
                val = mylist2[mylist2[pos + 1]] * mylist2[mylist2[pos + 2]]
                mylist2[mylist2[pos + 3]] = val
            pos += 4
        if mylist2[0] == 19690720:
            print(i, j)
print(mylist2[0])
