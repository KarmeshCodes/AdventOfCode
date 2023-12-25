def day7():
    path = []
    dirSizeDict = {}
    finalTotal = 0
    part2Total = 0
    with open('day7/inputDay7.txt') as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip()
            lineSplit = line.split(' ')
            if(lineSplit[0] == '$'): #it is a command
                if(lineSplit[1] == 'ls'):
                    continue
                elif(lineSplit[1] == 'cd' and lineSplit[2] == '..'):
                    path.pop()
                elif(lineSplit[1] == 'cd' and lineSplit[2] == '/'):
                    path = ['/']
                else:
                    path.append(lineSplit[2])
            else:
                if(lineSplit[0] != 'dir'):
                    current_path = ''
                    for item in path:
                        if item != '/' and current_path != '/':
                            current_path += '/'
                        current_path += item
                        dirSizeDict[current_path] = dirSizeDict.get(current_path,0) + int(lineSplit[0])
    for item in dirSizeDict.items():
        if(item[1] <= 100000):
            finalTotal += item[1]
    print('answer for part 1:' + str(finalTotal))

    spaceNeeded = 30000000 - (70000000 - dirSizeDict['/'])
    directorySizeToDelete = float('inf')
    for item in dirSizeDict.items():
        if item[1] >= spaceNeeded:
            directorySizeToDelete = min(directorySizeToDelete, item[1])
    
    print('answer for part 2: ' + str(directorySizeToDelete))
day7()

            

