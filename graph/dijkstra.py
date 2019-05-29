#!/usr/bin/python3

import collections

### __subs__ ###

def dijkstra(Queue, VertexCost):
    
    best    = 255

    while Queue:

        start = Queue.popleft()
        print('Working with vertex %s' % start)

        for i in Graph[start]:
            if Graph[start][i] + VertexCost[start] < VertexCost[i]:
                VertexCost[i] = Graph[start][i] + VertexCost[start]
                Queue.append(i)

### __main__ ###

# each edge named twice
Graph = {'A': {'B': 2, 'C': 1},
         'B': {'A': 2, 'D': 1, 'G': 8},
         'C': {'A': 1, 'E': 2},
         'D': {'B': 1, 'F': 1, 'E': 1},
         'E': {'C': 2, 'D': 1, 'F': 5},
         'F': {'D': 1, 'E': 5, 'G': 2},
         'G': {'B': 8, 'F': 2}
        }

Queue = collections.deque()

# Best costs for vertexes, initially "infinity"
VertexCost = {'A': 255, 'B': 255, 'C': 255, 'D': 255, 'E': 255, 'F': 255, 'G': 255} 
Path = []

# Edges and their cost:
#for i in Graph:
#    for j in Graph[i]:
#        print(i, j, Graph[i][j])

# The start vertex init:
VertexCost['A'] = 0
Queue.append('A')

dijkstra(Queue, VertexCost)

# Costs to each vertex from Start (i.e. 'A')
print(VertexCost)