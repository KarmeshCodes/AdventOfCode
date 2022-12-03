def day3part1():
    finalSum = 0
    with open('day3/inputDay3.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            containerOne = line[0:int((len(line)/2))]
            containerTwo = line[int((len(line)/2)):int(len(line))]
            alreadyCountedChars = []
            for letter in containerOne:
                for letterInside in containerTwo:
                    if letterInside == letter and letter.isupper() and letter not in alreadyCountedChars:
                        finalSum += ord(letter) - 38
                        alreadyCountedChars.append(letter)
                    elif letterInside == letter and letter.islower() and letter not in alreadyCountedChars:
                        finalSum += ord(letter) - 96
                        alreadyCountedChars.append(letter)
    
    print(finalSum)

def day3part2():
    finalSum = 0
    with open('day3/inputDay3.txt', 'r') as f:
        lines = f.readlines()
        numberOfLines = int(len(lines))
        for i in range(0,numberOfLines,3):
            alreadyCounted = []
            firstLine = list(lines[i]);
            for letter in lines[i+1]:
                for letter2 in lines[i+2]:
                    if letter == letter2 and letter.isupper() and letter in firstLine and letter not in alreadyCounted:
                        finalSum += ord(letter) - 38
                        alreadyCounted.append(letter)
                    if letter == letter2 and letter.islower() and letter in firstLine and letter not in alreadyCounted:
                        finalSum += ord(letter) - 96
                        alreadyCounted.append(letter)
    print(finalSum)



day3part1()
day3part2()