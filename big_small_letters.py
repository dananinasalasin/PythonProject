input_str = input("Please enter a string: ")
print(input_str[:len(input_str)//2].lower() + input_str[len(input_str)//2:].upper())