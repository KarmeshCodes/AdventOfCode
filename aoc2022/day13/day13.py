def day13part1():
    with open('day13/inputDay13.txt','r') as f:
        lines = f.readlines()
        arrOfAllPairs = []
        pairs = []
        for i in range(len(lines)):
            line = lines[i].strip()
            print(line)
            if not line.strip():
                arrOfAllPairs.append(pairs)
                pairs = []
            else:
                pairs.append(line)
        if(len(pairs) != 0):
            arrOfAllPairs.append(pairs)

def isList(input): #have to make sure we pass in a string
    if(input[0] == '[' and input[len(input)-1] == ']'):
        return True
    return False

def isPairInRightOrder(left,right):
    if(len(right) < len(left)):
        return False
    elif(len(left) < len(right)):
        return True
    else:
        for i in range(len(right)):
            rightValue = right[i]
            leftValue = left[i]
            if(isList(rightValue) and isList)
