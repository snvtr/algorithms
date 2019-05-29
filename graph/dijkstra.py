#!/usr/bin/python3

import collections

### __subs__ ###

def dijkstra(Queue, VertexCost):
    
    best    = 255

    while Queue:

        vertex = Queue.popleft()
        print('Working with vertex %s' % vertex)

        for i in Graph[vertex]:
            if Graph[vertex][i] + VertexCost[vertex] < VertexCost[i]:
                VertexCost[i] = Graph[vertex][i] + VertexCost[vertex]
                Queue.append(i)

def rebuild_path(Queue, Graph, VertexCost, finish_at):

    Path = []

    while Queue:

        vertex = Queue.popleft()
        print('Rebuilding path. Current vertex: %s' % vertex)

#        if vertex == finish_at:
#            return Path

        for i in Graph[vertex]:
            if VertexCost[vertex] - Graph[vertex][i] == VertexCost[i]:
                Path.append(i)
                Queue.append(i)
                break

    return Path

### __main__ ###

# each edge named twice
# test graph 1
Graph = {
         'A': {'B': 2, 'C': 1},
         'B': {'A': 2, 'D': 1, 'G': 8},
         'C': {'A': 1, 'E': 2},
         'D': {'B': 1, 'F': 1, 'E': 1},
         'E': {'C': 2, 'D': 1, 'F': 5},
         'F': {'D': 1, 'E': 5, 'G': 2},
         'G': {'B': 8, 'F': 2}
        }
# test graph 2
#Graph = {
#         'A': {'B': 2, 'H': 15},
#         'B': {'A': 2, 'C': 1, 'D': 5},
#         'C': {'B': 1, 'D': 3, 'G': 1},
#         'D': {'B': 5, 'C': 3, 'F': 4, 'E': 6},
#         'E': {'D': 6, 'F': 7, 'I': 2},
#         'F': {'C': 2, 'D': 4, 'E': 7, 'G': 1, 'H': 3},
#         'G': {'C': 1, 'F': 1},
#         'H': {'A': 15, 'F': 3, 'I': 12},
#         'I': {'E': 2, 'H': 12}
#        }

Queue = collections.deque()

# Best costs for vertexes, initially "infinity", e.g. 255 :)
VertexCost = {}
for i in Graph.keys():
    VertexCost[i] = 255
Path = []

# Edges and their cost:
#for i in Graph:
#    for j in Graph[i]:
#        print(i, j, Graph[i][j])

### Part #1 - Filling VertexCost with proper values.

# The start vertex init:
VertexCost['A'] = 0
Queue.append('A')

dijkstra(Queue, VertexCost)

# The result:
print(VertexCost)

### Part #2 - Rebuilding the best path backwards:

start_vertex = 'G'
finish_at    = 'A'

Queue.append(start_vertex)
Path = rebuild_path(Queue, Graph, VertexCost, finish_at)
print(start_vertex, Path)
