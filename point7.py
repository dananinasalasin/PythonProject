# 7.1.4
def squared_numbers(start, stop):
    list_squares = []
    while start <= stop:
        list_squares.append(start ** 2)
        start += 1
    return list_squares

print(squared_numbers(4, 8))

