orbites = [line.rstrip('\n') for line in open("./ex1input")]
#orbites = [line.rstrip('\n') for line in open("./testInput")]
pathBeforeObjectByObject = {}
for orbite in orbites:
    mainObject = orbite.split(")")[0]
    orbitingObject = orbite.split(")")[1]
    if mainObject not in pathBeforeObjectByObject.keys():
        pathBeforeObjectByObject[mainObject] = []
    if orbitingObject not in pathBeforeObjectByObject.keys():
        pathBeforeObjectByObject[orbitingObject] = []
    pathBeforeObjectByObject[orbitingObject] = mainObject
totalOrbites = 0
for object in pathBeforeObjectByObject.keys():
    if object == "COM":
        continue
    objectBefore = pathBeforeObjectByObject[object]
    while objectBefore != "COM":
        totalOrbites += 1
        objectBefore = pathBeforeObjectByObject[objectBefore]
    totalOrbites += 1
print(totalOrbites)
