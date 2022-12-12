from collections import deque
grid = []
startPosition = ()
endPosition = ()
visited = set()
pathQueue = deque()
with open('day12/inputDay12.txt','r') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        l = lines[i].rstrip()
        innerList = []
        for j in range(len(l)):
            if l[j]=='S':
                startPosition = (i,j)
                innerList.append('a')
            elif l[j] == 'E':
                endPosition = (i,j)
                innerList.append('z')
            else:
                innerList.append(l[j])
        grid.append(innerList)
    visited.add(startPosition)
    pathQueue.append((0,endPosition[0],endPosition[1]))  
    while pathQueue:
        d,r,c = pathQueue.popleft()
        for nr,nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
            if(nr < 0 or nc < 0 or nr>=len(grid) or nc>=len(grid[0])):
                continue
            if (nr,nc) in visited:
                continue
            if ord(grid[nr][nc])-ord(grid[r][c])<-1:
                continue
            if grid[nr][nc] == 'a':
                print(d+1)
                exit(0)
            visited.add((nr,nc))
            pathQueue.append((d+1,nr,nc))
