rows = 5
start_col = 1
increment = 2
for i in range(1, rows + 1):
    col = start_col
    for j in range(1, rows + 1):
        print(col, end= " ")
        col += increment
    start_col += 1
    print()    