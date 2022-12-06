def day6part1():
    with open('day6/inputDay6.py', 'r') as f:
        lines = f.readlines()
        if(len(lines) > 0):
            inputString = lines[0]
            for i in range(len(inputString)-3):
                substring = inputString[i:i+4]
                uniqueCharSet = []
                for char in substring:
                    if char not in uniqueCharSet:
                        uniqueCharSet.append(char)
                    else:
                        break
                if(len(uniqueCharSet) == 4):
                    print(i+4)
                    break

def day6part2():
    with open('day6/inputDay6.py', 'r') as f:
        lines = f.readlines()
        if(len(lines) > 0):
            inputString = lines[0]
            for i in range(len(inputString)-11):
                substring = inputString[i:i+14]
                uniqueCharSet = []
                for char in substring:
                    if char not in uniqueCharSet:
                        uniqueCharSet.append(char)
                    else:
                        break
                if(len(uniqueCharSet) == 14):
                    print(i+14)
                    break

day6part1()
day6part2()