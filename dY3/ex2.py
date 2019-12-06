firstWire = []
secondWire = []
with open('./ex1Input.txt') as input:
    firstWire = [str(x) for x in input.readline().split(',')]
    firstWire[len(firstWire)-1] = firstWire[len(firstWire)-1][:-1]
    secondWire = [str(x) for x in input.readline().split(',')]
FPairs = {}
SPairs = {}
currentX = 0
currentY = 0
steps = 0
for coord in firstWire:
    direction = coord[0]
    distance = int(coord[1:])
    if direction == "R":
        for step in range(0, distance):
            currentX += 1
            steps += 1
            FPairs[(currentX, currentY)] = steps
    if direction == "L":
        for step in range(0, distance):
            currentX -= 1
            steps += 1
            FPairs[(currentX, currentY)] = steps
    if direction == "U":
        for step in range(0, distance):
            currentY += 1
            steps += 1
            FPairs[(currentX, currentY)] = steps
    if direction == "D":
        for step in range(0, distance):
            currentY -= 1
            steps += 1
            FPairs[(currentX, currentY)] = steps
currentX = 0
currentY = 0
steps = 0
for coord in secondWire:
    direction = coord[0]
    distance = int(coord[1:])
    if direction == "R":
        for step in range(0, distance):
            currentX += 1
            steps += 1
            SPairs[(currentX, currentY)] = steps
    if direction == "L":
        for step in range(0, distance):
            currentX -= 1
            steps += 1
            SPairs[(currentX, currentY)] = steps
    if direction == "U":
        for step in range(0, distance):
            currentY += 1
            steps += 1
            SPairs[(currentX, currentY)] = steps
    if direction == "D":
        for step in range(0, distance):
            currentY -= 1
            steps += 1
            SPairs[(currentX, currentY)] = steps
minDist = 999999999999999
for a in FPairs.keys():
    if a in SPairs.keys():
        dist = FPairs[a] + SPairs[a]
        if dist < minDist:
            minDist = dist
print(minDist)
# minDist = 999999999999999
# for x, y in s:
#     dist = abs(x) + abs(y)
#     if dist < minDist:
#         minDist = dist
# print(minDist)