rows = 4
chars = ["A", "B"]

for i in range(rows):
    start_char = chars[i % 2]
    for j in range(rows + 1):
        print(start_char, end= " ")
        start_char = chars[(chars.index(start_char) + 1) %2]
    print()