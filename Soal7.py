rows = 5
chars = ["S", "o"]

for i in range(rows):
    start_char = chars[i % 2]
    for j in range(rows - i):
        print(start_char, end= " ")
        start_char = chars[(chars.index(start_char) + 1) % 2]
    print()    