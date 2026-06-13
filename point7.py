# 7.1.4
def squared_numbers(start, stop):
    list_squares = []
    while start <= stop:
        list_squares.append(start ** 2)
        start += 1
    return list_squares

#print(squared_numbers(4, 8))

# 7.2.1
def is_greater(my_list, n):
    list_greater = []
    for num in my_list:
        if num > n:
            list_greater.append(num)
    return list_greater

result = is_greater([1, 30, 25, 60, 27, 28], 28)
print(result)