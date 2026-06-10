input_str = input("Please enter a string: ")
new_str = input_str[0] + input_str[1:].replace(input_str[0], "e")
print(new_str)