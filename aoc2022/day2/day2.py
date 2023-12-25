#rock-1 paper-2 scissor- 3
mapOfValues = {
        'A' : 1,
        'B' : 2,
        'C' : 3,
        'X' : 1,
        'Y' : 2,
        'Z' : 3
    }
def day2part1():
    finalScore = 0
    with open('day2/inputDay2.txt','r') as f:
        lines = f.readlines()
        for line in lines:
            opponent = line[0]
            myPlay = line[2]
            finalScore += mapOfValues[myPlay]
            if mapOfValues[opponent] == mapOfValues[myPlay]: #draw
                finalScore += 3
            if myPlay == 'X' and opponent == 'C':
                finalScore += 6
            if myPlay == 'Y' and opponent == 'A':
                finalScore += 6
            if myPlay == 'Z' and opponent == 'B':
                finalScore += 6

    print('day 1 answer: ' + str(finalScore))

def day2part2():
    finalScore = 0
    with open('day2/inputDay2.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            opponent = line[0]
            myPlay = line[2]
            if myPlay == 'Y': #draw situation
                finalScore += 3
                finalScore += mapOfValues[opponent]
            elif myPlay == 'X':
                if opponent == 'A':
                    finalScore += 3
                elif opponent == 'B':
                    finalScore += 1
                else:
                    finalScore += 2
            else:
                finalScore += 6
                if opponent == 'A':
                    finalScore += 2
                elif opponent == 'B':
                    finalScore += 3
                else:
                    finalScore += 1
    print('day 2 answer: ' + str(finalScore))

day2part1()
day2part2()
#part 1 answer - 9651
#part 2 answer - 10560