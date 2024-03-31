rows = 5
col = 9

for i in range(rows):
    for j in range(i+1):
        print(col, end=" ")
        col-= 1
    print()
    col +=i    