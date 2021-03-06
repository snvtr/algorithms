#!/usr/bin/python3

# simple chess horse movement, without restriction

### __subs__ ###

def bfs(ThisLevel, level):

# - increase Touched node counter when node is in ThisLevel
# - add node to the Touched set
# - build list of values for the next level and increase level by 1
# - call bfs until all nodes are not in Touched set

    NextLevel = []

    for i in ThisLevel:
        if i not in Touched:
            Counter[i] = level
            Touched.add(i)
        for j in Board[i]:
            NextLevel.append(j)
    level += 1
    if len(Touched) > 63:
        return
    else:
        bfs(NextLevel, level)

### __main__ ###

# filling the chessboard with possible horse movements. The result is a non-oriented graph.
Board = { i+j: set() for i in '12345678' for j in '12345678' }
Counter = {  i+j: 0 for i in '12345678' for j in '12345678' }
Touched = set()

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
        
start = '11'
level = 0
count = 0

# debug:
for i in '12345678':
    for j in '12345678':
        print('i: %s, j: %s :: %r' % (i, j, Board[i+j]))


# start with one-element list and level=0

bfs([start], level)

for i in Counter.keys():
    print('Key: %s, Value: %s' % (i, Counter[i]))
