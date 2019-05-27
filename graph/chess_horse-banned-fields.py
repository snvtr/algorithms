#!/usr/bin/python3

# simple chess horse movement via non-oriented Graph, with restriction

### __subs__ ###

def bfs_banned(ThisLevel, level):

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
            if j not in Banned:
                NextLevel.append(j)
    level += 1
    if len(Touched) > 63: # all the fields are touched by the horse
        return
    else:
        bfs_banned(NextLevel, level)

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
Banned = ['22','33','44','55','66']

# Simple: add banned fields as already touched!

for i in Banned:
    Board[i] = {}
    for j in Board.keys():
        try:
            Board[j].remove(i)
        except:
            pass
    Touched.add(i)
    Counter[i] = -1

# debug:
for i in '12345678':
    for j in '12345678':
        print('i: %s, j: %s :: %r' % (i, j, Board[i+j]))


# start with one-element list and level=0,
# DO NOT START WITH A BANNED FIELD

bfs_banned([start], level)

for i in Counter.keys():
    print('Key: %s, Value: %s' % (i, Counter[i]))
