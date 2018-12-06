import numpy as np

def readFile(filename) -> list:
    file_data = open(filename)
    data = list(map(lambda x: x, file_data))
    return data

def unpackClaim(claim: str) -> list:
    claimID = claim.split('@')[0].strip()[1:]
    startPoint = claim.split('@')[1].split(':')[0].strip()
    size = claim.split('@')[1].split(':')[1].strip()
    startX = int(startPoint.split(',')[0])
    startY = int(startPoint.split(',')[1])
    sizeX = int(size.split('x')[0])
    sizeY = int(size.split('x')[1])
    return [claimID, startX, startY, sizeX, sizeY]


def getRectSInches(claim: str) -> list:
    startX, startY, sizeX, sizeY = unpackClaim(claim)[1:]
    sInchesList = []
    for x in range(startX, startX + sizeX):
        for y in range(startY, startY + sizeY):
            sInchesList.append([x, y])
    return sInchesList


def overlayRect(canvas: list, claim: str) -> list:
    sInchesList = getRectSInches(claim)
    for eachElem in sInchesList:
        xCoor = eachElem[0]
        yCoor = eachElem[1]
        canvas[yCoor][xCoor] += 1
    return(canvas)


def createOutputCanvas(data) -> list:
    canvas = np.zeros([1000, 1000])
    for claim in data:
        canvas = overlayRect(canvas, claim)
    return canvas


def isOverlapped(canvas: list, claim: str) -> int:
    claimID, startX, startY, sizeX, sizeY = unpackClaim(claim)
    for x in range(startX, startX + sizeX):
         for y in range(startY, startY + sizeY):
             if canvas[y][x] != 1:
                 return 0 
    return claimID


def solution1(data) -> int:
    canvas = createOutputCanvas(data)
    return np.count_nonzero(canvas > 1)


def solution2(data) -> int:
    canvas = createOutputCanvas(data)
    for claim in data:
        rect = isOverlapped(canvas, claim)
        if rect != 0:
            return rect



filename = 'input.txt'
data = readFile(filename)
print(solution1(data))
print(solution2(data))
