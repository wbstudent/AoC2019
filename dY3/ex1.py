firstWire = []
secondWire = []
with open('./ex1Input.txt') as input:
    firstWire = [str(x) for x in input.readline().split(',')]
    firstWire[len(firstWire)-1] = firstWire[len(firstWire)-1][:-1]
    secondWire = [str(x) for x in input.readline().split(',')]
FPairs = []
SPairs = []
currentX = 0
currentY = 0
for coord in firstWire:
    direction = coord[0]
    distance = int(coord[1:])
    if direction == "R":
        for step in range(0, distance):
            currentX += 1
            FPairs.append((currentX, currentY))
    if direction == "L":
        for step in range(0, distance):
            currentX -= 1
            FPairs.append((currentX, currentY))
    if direction == "U":
        for step in range(0, distance):
            currentY += 1
            FPairs.append((currentX, currentY))
    if direction == "D":
        for step in range(0, distance):
            currentY -= 1
            FPairs.append((currentX, currentY))
currentX = 0
currentY = 0
for coord in secondWire:
    direction = coord[0]
    distance = int(coord[1:])
    if direction == "R":
        for step in range(0, distance):
            currentX += 1
            SPairs.append((currentX, currentY))
    if direction == "L":
        for step in range(0, distance):
            currentX -= 1
            SPairs.append((currentX, currentY))
    if direction == "U":
        for step in range(0, distance):
            currentY += 1
            SPairs.append((currentX, currentY))
    if direction == "D":
        for step in range(0, distance):
            currentY -= 1
            SPairs.append((currentX, currentY))
s = list(set(FPairs).intersection(SPairs))
minDist = 999999999999999
for x, y in s:
    dist = abs(x) + abs(y)
    if dist < minDist:
        minDist = dist
print(minDist)