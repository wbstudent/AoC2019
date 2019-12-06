mylist2 = []
with open('./ex1Input.txt') as input:
    for value in input:
        mylist2 = [int(x) for x in value.split(',')]
pos = 0
mylist2[1] = 12
mylist2[2] = 2
while mylist2[pos] != 99:
    command = mylist2[pos]
    if command == 1:
        val = mylist2[mylist2[pos + 1]] + mylist2[mylist2[pos + 2]]
        mylist2[mylist2[pos + 3]] = val
    if command == 2:
        val = mylist2[mylist2[pos + 1]] * mylist2[mylist2[pos + 2]]
        mylist2[mylist2[pos + 3]] = val
    pos += 4
print(mylist2[0])
