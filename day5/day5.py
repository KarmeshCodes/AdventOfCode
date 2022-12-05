def day5part1():
    with open('day5/inputDay5.txt') as f:
        lines = f.readlines()
        baseStartIndex = 0
        finalList = []
        numberOfBases = int(len(lines[0]) / 4)
        for i in range(numberOfBases):
            finalList.append([])

        for line in lines:
            if line.strip() == '':
                break
            else:
                baseStartIndex += 1
        print(baseStartIndex)
        for i in range(baseStartIndex-2,-1,-1):
            line = lines[i]
            counter = 0
            for j in range(1,int(len(line)),4):
                if(line[j] != '' and line[j] != ' '):
                    finalList[counter].append(line[j])
                counter += 1
        numberOfLoops = 0
        for line in lines:
            if(numberOfLoops > baseStartIndex):
                lineSplit = line.split(' ')
                for i in range(int(lineSplit[1])):
                    num = finalList[int(lineSplit[3])-1].pop()
                    finalList[int(lineSplit[5])-1].append(num)
            numberOfLoops += 1
    print(finalList)

def day5part2():
    with open('day5/inputDay5.txt') as f:
        lines = f.readlines()
        baseStartIndex = 0
        finalList = []
        numberOfBases = int(len(lines[0]) / 4)
        for i in range(numberOfBases):
            finalList.append([])

        for line in lines:
            if line.strip() == '':
                break
            else:
                baseStartIndex += 1
        print(baseStartIndex)
        for i in range(baseStartIndex-2,-1,-1):
            line = lines[i]
            counter = 0
            for j in range(1,int(len(line)),4):
                if(line[j] != '' and line[j] != ' '):
                    finalList[counter].append(line[j])
                counter += 1
        numberOfLoops = 0
        for line in lines:
            if(numberOfLoops > baseStartIndex):
                lineSplit = line.split(' ')
                listToExtend = []
                for i in range(int(lineSplit[1])):
                    num = finalList[int(lineSplit[3])-1].pop()
                    listToExtend.append(num)
                for i in range(int(len(listToExtend)-1),-1,-1):
                    finalList[int(lineSplit[5])-1].append(listToExtend[i])
            numberOfLoops += 1
    print(finalList)

day5part1()
day5part2()