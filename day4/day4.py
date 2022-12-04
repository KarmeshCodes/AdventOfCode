def day4part1(filename):
    finalCount = 0
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace(',','A')
            line = line.replace('-','A')
            line = line.strip()
            lineList = line.split('A')
            elf1 = set(range(int(lineList[0]),int(lineList[1])+1))
            elf2 = set(range(int(lineList[2]),int(lineList[3])+1))
            matches = elf1.intersection(elf2)
            if len(matches) == len(elf2) or len(matches) == len(elf1): # checking if it overlaps everything
                finalCount += 1
    print(finalCount)

def day4part2(filename):
    finalCount = 0
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace(',','A')
            line = line.replace('-','A')
            line = line.strip()
            lineList = line.split('A')
            elf1 = set(range(int(lineList[0]),int(lineList[1])+1))
            elf2 = set(range(int(lineList[2]),int(lineList[3])+1))
            matches = elf1.intersection(elf2)
            if len(matches) != 0: # no need to check for length because even 1 overlap counts.
                finalCount += 1
    print(finalCount)

day4part1('day4/inputDay4.txt')
day4part2('day4/inputDay4.txt')