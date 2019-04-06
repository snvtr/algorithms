#!C:/Python37/python3.exe

N = 5  # количество предметов
M = 15 # емкость рюкзака в кг

F = [[0] * (N + 1) for i in range(M + 1)]

# массы предметов
m = [2, 4, 3, 5, 6, 7]

#стоимости предметов
v = [1, 2, 4, 3, 3, 4]

for i in range(1, N+1):
    for k in range(1, M+1):
        if m[i] <= k:
            F[k][i] = max(F[k][i-1], v[i] + F[k-m[i]][i-1]) 
        else:
            F[k][i] = F[k][i-1]

for i in range(len(F)):
    print(F[i])