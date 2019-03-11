#!C:/Python37/python3

# практически построение треугольника ѕаскал€. ¬ычисление количества возможных путей добратьс€ до клетки.

Board = [ [1, 1, 1, 1, 1],
          [1, 0, 0, 0, 0],
          [1, 0, 0, 0, 0],
          [1, 0, 0, 0, 0],
          [1, 0, 0, 0, 0]
        ]

print(Board)

for i in range(1,len(Board)):
    for j in range(1, len(Board[0])):
        Board[i][j] = Board[i-1][j] + Board[i][j-1]
        print("Element(%d,%d) = %d, Element(%d,%d) = %d, Element(%d,%d) = %d" % (i-1,j,Board[i-1][j],i,j-1,Board[i][j-1],i,j,Board[i][j]))
#        print("Element(%d,%d) = Element(%d,%d) + Element(%d,%d). Equals %d" % (i,j,i-1,j,i,j-1,Board[i][j]))

print(Board)

