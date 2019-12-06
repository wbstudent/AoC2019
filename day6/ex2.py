orbites = [line.rstrip('\n') for line in open("./ex2input")]
# orbites = [line.rstrip('\n') for line in open("./ex2testinput")]
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
# for object in pathBeforeObjectByObject.keys():
#     if object == "COM":
#         continue
#     objectBefore = pathBeforeObjectByObject[object]
#     while objectBefore != "COM":
#         totalOrbites += 1
#         objectBefore = pathBeforeObjectByObject[objectBefore]
#     totalOrbites += 1
myPathToCom = ["YOU"]
objectBefore = pathBeforeObjectByObject["YOU"]
while objectBefore:
    myPathToCom.insert(0, objectBefore)
    objectBefore = pathBeforeObjectByObject[objectBefore]
santaPathToCom = ["SAN"]
objectBefore = pathBeforeObjectByObject["SAN"]
while objectBefore:
    santaPathToCom.insert(0, objectBefore)
    objectBefore = pathBeforeObjectByObject[objectBefore]
lastCommonElement = ""
for idx, cosmicObject in enumerate(santaPathToCom):
    if myPathToCom[idx] == cosmicObject:
        lastCommonElement = cosmicObject
santaSeparationStart = santaPathToCom.index(lastCommonElement)
santaWay = len(santaPathToCom[santaSeparationStart+1:])
myWay = len(myPathToCom[santaSeparationStart+1:])
# mySeparationStart = myPathToCom.index(lastCommonElement)
print(santaWay + myWay - 2)
