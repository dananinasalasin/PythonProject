# 5.3.4
def last_early(my_str):
    my_str = my_str.lower()
    last_char = my_str[-1]
    return last_char in my_str[:-1]

str = input("Please enter a string: ")
print(last_early(str))