def day10part1():
    signalStrength = 0
    cycleCount = 0
    sizeOfX = 1
    firstCycle = 20
    with open('day10/inputDay10.txt','r') as f:
        lines = f.readlines()
        for line in lines:
            line= line.rstrip().split(' ')
            if line[0] == 'noop':
                cycleCount += 1
                if(firstCycle == cycleCount):
                    signalStrength += (firstCycle * sizeOfX)
                    firstCycle += 40
            elif line[0] == 'addx':
                for i in range(2):
                    if i==0:
                        cycleCount += 1
                        if(firstCycle == cycleCount): 
                            signalStrength += (firstCycle * sizeOfX)      
                            firstCycle += 40
                    else:
                        cycleCount +=1
                        if(firstCycle == cycleCount):
                            signalStrength += (firstCycle * sizeOfX)      
                            firstCycle += 40
                        sizeOfX = sizeOfX + (int(line[1]))
    
    print(signalStrength)

def day10part2():
    spritePositions = [0,1,2]
    crtArray = [[]]
    currRow = 0
    cycleCount = 0
    with open('day10/inputDay10.txt','r') as f:
        lines = f.readlines()
        for line in lines:
            line= line.rstrip().split(' ')
            if line[0] == 'noop':
                isItLit = isLit(spritePositions,cycleCount%40)
                if isItLit:
                    crtArray[currRow].append('#')
                else:
                    crtArray[currRow].append('.')
                cycleCount += 1
                if cycleCount%40 == 0 and cycleCount!=0:
                    crtArray.append([])
                    currRow += 1
            elif line[0] == 'addx':
                for i in range(2):
                    if i==0:
                        isItLit = isLit(spritePositions,cycleCount%40)
                        if isItLit:
                            crtArray[currRow].append('#')
                        else:
                            crtArray[currRow].append('.')
                        cycleCount += 1
                        if cycleCount%40 == 0 and cycleCount!=0:
                            crtArray.append([])
                            currRow += 1
                    else:
                        numToMove = line[1]
                        isItLit = isLit(spritePositions,cycleCount%40)
                        if isItLit:
                            crtArray[currRow].append('#')
                        else:
                            crtArray[currRow].append('.')
                        cycleCount += 1
                        if cycleCount%40 == 0 and cycleCount!=0:
                            crtArray.append([])
                            currRow += 1
                        spritePositions[0] = spritePositions[0] + int(numToMove)
                        spritePositions[1] = spritePositions[1] + int(numToMove)
                        spritePositions[2] = spritePositions[2] + int(numToMove)
    finalArr = []
    for item in crtArray:
        innerString = ''
        for letter in item:
            if letter == '.':
                innerString += ' '
            else:
                innerString += '#'
        finalArr.append(innerString)
    for item in finalArr:
        print(item)

def isLit(spritePos,currPos):
    return currPos == spritePos[0] or currPos == spritePos[1] or currPos == spritePos[2]

day10part1()
day10part2()
