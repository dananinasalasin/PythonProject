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

#print(sequence_del("Heeyyy   yyouuuu!!!"))

# 7.2.6
products_str = input("Please enter your products list: ")
products_list = products_str.split(",")
client_choice = int(input(
    "Please choose an option:\n"
    "1. Print the product list\n"
    "2. Print the number of products\n"
    "3. Check if a product exists in the list\n"
    "4. Count how many times a product appears\n"
    "5. Remove a product from the list\n"
    "6. Add a product to the list\n"
    "7. Print all invalid products\n"
    "8. Remove duplicate products\n"
    "9. Exit\n"
))
while client_choice != 9:
    if client_choice == 1:
        for item in products_list:
            print(item)
    elif client_choice == 2:
        print(len(products_list))
    elif client_choice == 3:
        product = input("Please enter the product name: ")
        if product in products_list: print("It appears that the product exists in the list")
        else: print("It doesn't exist in the list")
    elif client_choice == 4:
        product = input("Please enter the product name: ")
        print(products_list.count(product))
    elif client_choice == 5:
        product = input("Please enter the product name: ")
        products_list.remove(product)
    elif client_choice == 6:
        product = input("Please enter the product name: ")
        products_list.append(product)
    elif client_choice == 7:
        for item in products_list:
            if len(item) < 3 or not item.isalpha():
                print(item)
    elif client_choice == 8:
        products_list = list(set(products_list))

    client_choice = int(input(
    "Please choose an option:\n"
    "1. Print the product list\n"
    "2. Print the number of products\n"
    "3. Check if a product exists in the list\n"
    "4. Count how many times a product appears\n"
    "5. Remove a product from the list\n"
    "6. Add a product to the list\n"
    "7. Print all invalid products\n"
    "8. Remove duplicate products\n"
    "9. Exit\n"))
