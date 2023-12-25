from collections import defaultdict

def populateDic():
    with open('day11/inputDay11.txt') as f:
        lines = f.readlines()
        monkeyDictionary = defaultdict(dict)
        monkeyCounter = 0
        lineCounter = 0
        for line in lines:
            line1 = line.rstrip().split(' ')
            if(len(line1) == 1):
                monkeyCounter += 1
                lineCounter = 0
                continue
            if(lineCounter == 0):
                monkeyDictionary[monkeyCounter]['inspectionCount'] = 0
            if(lineCounter == 1):
                line2 = line.rstrip().split(':')
                innerLine = line2[1].strip().split(', ')
                monkeyDictionary[monkeyCounter]['items'] = innerLine
            if(lineCounter == 2):
                line3 = line.rstrip().split('= ')[1]
                monkeyDictionary[monkeyCounter]['formula'] = line3
            if(lineCounter == 3):
                monkeyDictionary[monkeyCounter]['divisible'] = line.rstrip().split('by ')[1]
            if(lineCounter == 4):
                monkeyDictionary[monkeyCounter]['trueThrow'] = line.rstrip().split('monkey ')[1]
            if(lineCounter == 5):
                monkeyDictionary[monkeyCounter]['falseThrow'] = line.rstrip().split('monkey ')[1]
            
            lineCounter += 1

        return monkeyDictionary


def executeRound(monkeyDict,mod):
    for key in monkeyDict:
        items = monkeyDict[key]['items']
        for item in items:
            monkeyDict[key]['inspectionCount'] += 1
            old = int(item)
            newWorryLevel = eval(monkeyDict[key]['formula'])
            divisible = int(monkeyDict[key]['divisible'])
            newWorryLevel %=mod
            if(newWorryLevel % divisible == 0):
                throwTo = int(monkeyDict[key]['trueThrow'])
                monkeyDict[throwTo]['items'].append(newWorryLevel)
            else:
                throwTo = int(monkeyDict[key]['falseThrow'])
                monkeyDict[throwTo]['items'].append(newWorryLevel)
        monkeyDict[key]['items'] = []
    return monkeyDict


def part2Answer():
    initialDict = populateDic()
    mod = 1
    for key in initialDict:
        mod *= int(initialDict[key]['divisible'])
    monkeyInspectionCounter = []
    maxVal = 0
    secondMax = 0
    for i in range(10000):
        initialDict = executeRound(initialDict,mod)
    for key in initialDict:
        if initialDict[key]['inspectionCount'] > maxVal:
            secondMax = maxVal
            maxVal = initialDict[key]['inspectionCount']
        elif initialDict[key]['inspectionCount'] > secondMax:
            secondMax = initialDict[key]['inspectionCount']
    print(maxVal*secondMax)

part2Answer()
