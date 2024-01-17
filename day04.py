squares = list()
for i in range(1,6):
    squares.append(i*i)
print(squares)

squares_list = [i*i for i in range(1,6)]
print(squares_list)

even_list = [i for i in range(1,6) if i % 2 == 0]
print(even_list)

