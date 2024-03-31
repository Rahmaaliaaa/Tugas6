rows = 5

for i in range(rows, 0, -1):
    for j in range(1, i):
        print("_", end= " ")
    for k in range(i, rows + 1):
        print(k, end=" ")
    print()        