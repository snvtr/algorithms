#!/usr/bin/python3

### __subs__ ###

def dfs(vertex, G, Used):
    """ depth-first search """
    Used.add(vertex)
    print('got new vertex %s' % vertex)
    for neighbour in G[vertex]:
        if neighbour not in Used:
            dfs(neighbour, G, Used)

### __main__ ###
 
G = {
     'A': ['C','D'],
     'B': ['C'],
     'C': ['D'],
     'D': [],
     'E': ['F'],
     'F': []
     }

Used = set()

for vrtx in G.keys():
    if vrtx not in Used:
        dfs(vrtx, G, Used)
