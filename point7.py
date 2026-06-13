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
#print(result)

# 7.2.2
def numbers_letters_count(my_str):
    num_lett_count = [0,0]
    for lett in my_str:
        if lett.isdigit(): num_lett_count[0] += 1
        else: num_lett_count[1] += 1
    return num_lett_count

#print(numbers_letters_count("Python 3.6.3"))

# 7.2.4
def seven_boom(end_number):
    numbers_list = []
    for i in range (end_number + 1):
        if i % 7 == 0 or str(7) in str(i):
            numbers_list.append("BOOM")
        else:
            numbers_list.append(i)
    return numbers_list

#print(seven_boom(17))

# 7.2.5
def sequence_del(my_str):
    original_str = ""
    for i in range(len(my_str)):
        if my_str[i] != my_str[i-1]:
            original_str += my_str[i]
    return original_str

print(sequence_del("Heeyyy   yyouuuu!!!"))
