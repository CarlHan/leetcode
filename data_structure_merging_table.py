# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))
ans = max(lines)

def getParent(table):
    # find parent and compress path
    while(table != parent[table]):
        table = getParent(parent[table])
    return table

def merge(destination, source):
    global ans
    realDestination, realSource = getParent(destination), getParent(source)
    if realDestination == realSource:
        return False
    else:
        if rank[realDestination] > rank[realSource]:
            parent[realSource] = realDestination
            lines[realDestination] += lines[realSource]
            lines[realSource] = 0
        else:
            parent[realDestination] = realSource
            lines[realSource] += lines[realDestination]
            if rank[realDestination] == rank[realSource]:
                rank[realSource] += 1
    return True
    # merge two components
    # use union by rank heuristic 
    # update ans with the new maximum table size
    #remember:the rows of table has no connection with our shape of tree, i+j=j+i
    #our tree would just influence the height which associate with running time of program
    #remember assign 0 to lines[x] which has been merged into another tree.



for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    ans = max(lines)
    print(ans)
    
