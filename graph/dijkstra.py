#!/usr/bin/python3

### __subs__ ###

def dijkstra(start, end, prev, total_best):
    
    best    = None

    print('Working with vertex %s' % start)

    for i in Graph[start]:
        if i in Used:
            print('Used vertex %s. Skipped' % i)
            continue
        if Graph[start][i] < VertexCost[i]:
            VertexCost[i] = Graph[start][i]
            best = i

    if best is not None:
        print('The best vertex: %s' % best)
        Used.append(start)
        total_best += Graph[start][best]
        VertexCost[best] = total_best
#        if best == end:
#            return
#        else:
        dijkstra(best, end, start, total_best)
    else:
        return

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

VertexCost = {'A': 255, 'B': 255, 'C': 255, 'D': 255, 'E': 255, 'F': 255, 'G': 255} # Best cost of the route to the vertex
Used = []
Path = []

# Edges and their cost:
#for i in Graph:
#    for j in Graph[i]:
#        print(i, j, Graph[i][j])

VertexCost['A'] = 0
Used.append('A')

dijkstra('A', 'G', '', 0)

print(VertexCost)