#!/usr/bin/python3


### __subs__ ###

def bfs(Voisins, level):

    Neighbours = set()

    for i in Voisins:
        for j in Board[i]:
            Neighbours.add(j)
        if i not in Hierarchy.keys():
            Hierarchy[i] = level
    level += 1
    if level > 63:
        return
    else:
        bfs(Neighbours, level)

### __main__ ###

# filling the chessboard with possible horse movements. The result is a non-oriented graph.
Board = { i+j: set() for i in '12345678' for j in '12345678' }

for i in range(1,9):
    for j in range(1,9):
        if 0 < i-2 < 9:
            if 0 < j-1 < 9:
                Board[str(i)+str(j)].add(str(i-2)+str(j-1))
            if 0 < j+1 < 9:
                Board[str(i)+str(j)].add(str(i-2)+str(j+1))

        if 0 < i-1 < 9:
            if 0 < j-2 < 9:
                Board[str(i)+str(j)].add(str(i-1)+str(j-2))
            if 0 < j+2 < 9:
                Board[str(i)+str(j)].add(str(i-1)+str(j+2))

        if 0 < i+1 < 9:
            if 0 < j+2 < 9:
                Board[str(i)+str(j)].add(str(i+1)+str(j+2))
            if 0 < j-2 < 9:
                Board[str(i)+str(j)].add(str(i+1)+str(j-2))

        if 0 < i+2 < 9:
            if 0 < j+1 < 9:
                Board[str(i)+str(j)].add(str(i+2)+str(j+1))
            if 0 < j-1 < 9:
                Board[str(i)+str(j)].add(str(i+2)+str(j-1))

# debug:
for i in '12345678':
    for j in '12345678':
        print('i: %s, j: %s :: %r' % (i, j, Board[i+j]))


start = '33'
Hierarchy = {}
level = 0

bfs(Board[start], level)

for i in sorted(Hierarchy.keys()):
    print('Key: %s, Value: %s.' % (i, Hierarchy[i]))
