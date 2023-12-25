def day1part1():
    with open('./inputday1.txt', 'r') as f:
        total = 0
        content = f.readlines()
        for line in content:
            insideNum = ''
            for character in line:
                if(character.isdigit()):
                    insideNum += character
            if(len(insideNum) == 1):
                total += int(insideNum + insideNum)
            else:
                total += int(insideNum[0] + insideNum[len(insideNum)-1])
        return total

def day1part2():
    with open('./inputday1.txt', 'r') as f:
        content = f.readlines()
        total = 0
        spelledOutNumber = {'one':'1','two': '2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
        for line in content:
            insideSpelledNum = ''
            actualInsideNum = ''
            for character in line:
                if(character.isdigit()):
                    actualInsideNum += character
                else:
                    insideSpelledNum += character
                    if insideSpelledNum in spelledOutNumber.keys():
                        actualInsideNum += spelledOutNumber[insideSpelledNum]
                        insideSpelledNum = ''
            if(len(actualInsideNum) == 1):
                total += int(actualInsideNum + actualInsideNum)
            else:
                total += int(actualInsideNum[0] + actualInsideNum[len(actualInsideNum)-1])
            print(actualInsideNum)
        return total


#print(day1part1())
print(day1part2())