def day9():
    positionSet = set()
    with open('day9/inputDay9.txt','r') as f:
        lines = f.readlines()
        head_location = [0,0]
        tailLocations = []
        for i in range(9):
            tailLocations.append([0,0])
        for line in lines:
            dir,moves= line.strip().split(' ')
            for i in range(int(moves)):
                head_location,tailLocations[0] = makeMoves(head_location,tailLocations[0],dir)
                for j in range(1,9):
                    tailLocations[j-1],tailLocations[j] = makeMoves(tailLocations[j-1],tailLocations[j],dir)
                positionSet.add((tailLocations[8][0],tailLocations[8][1]))
                print(tailLocations)
    print(len(positionSet))
                
def makeMoves(head_location,tail_location,dir):
    if(dir == 'R'):
        head_location[1] += 1
        if(not isNextTo(head_location,tail_location)):
            if(head_location[0] != tail_location[0] and head_location[1] != tail_location[1]):
                tail_location[0] = head_location[0]
                tail_location[1] += 1
            else:
                tail_location[1] += 1
    if(dir == 'L'):
        head_location[1] -= 1
        if(not isNextTo(head_location,tail_location)):
            if(head_location[0] != tail_location[0] and head_location[1] != tail_location[1]):
                tail_location[0] = head_location[0]
                tail_location[1] -= 1
            else:
                tail_location[1] -= 1
    if(dir == 'U'):
        head_location[0] += 1
        if(not isNextTo(head_location,tail_location)):
            if(head_location[0] != tail_location[0] and head_location[1] != tail_location[1]):
                tail_location[0] += 1
                tail_location[1] = head_location[1]
            else:
                tail_location[0] += 1
    if(dir == 'D'):
        head_location[0] -= 1
        if(not isNextTo(head_location,tail_location)):
            if(head_location[0] != tail_location[0] and head_location[1] != tail_location[1]):
                tail_location[0] -= 1
                tail_location[1] = head_location[1]
            else:
                tail_location[0] -= 1
    return (head_location,tail_location)

def isNextTo(head,tail):
    if(head[0] == tail[0] and (head[1] == tail[1]+1 or head[1] == tail[1]-1)):
        return True
    if(tail[0]+1 == head[0] or tail[0]-1 == head[0]):
        if(tail[1] == head[1] or tail[1] == head[1]-1 or tail[1] == head[1]+1):
            return True
    if(head[0] == tail[0] and head[1] == tail[1]):
        return True
    return False


day9()

