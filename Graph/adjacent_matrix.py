mg = []
for i in range(6):
    temp = []
    for j in range(6):
        temp.append(0)
    mg.append(temp)

ipt = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 3], [2, 3], [2, 4], [2, 5], [3, 5]]

for u, v in ipt:
    mg[u][v] = 1
    mg[v][u] = 1

for item in mg:
    print(item)






