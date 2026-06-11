# 5.3.4
def last_early(my_str):
    my_str = my_str.lower()
    last_char = my_str[-1]
    return last_char in my_str[:-1]

#str = input("Please enter a string: ")
#print(last_early(str))

# 5.3.5
def distance(num1, num2, num3):
    if abs(num1 - num2) == 1 or abs(num1 - num3) == 1:
        if (abs(num1 - num2) >= 2 and abs(num3 - num2) >= 2) or (abs(num1 - num3) >= 2 and abs(num2 - num3) >= 2):
            return True
    return False

#print(distance(4, 5, 3))

# 5.3.6
def fix_age(age):
    if age >= 13 and age <= 19:
        if age != 15 and age != 16:
            return 0
    return age

def filter_teens(a = 13, b = 13, c = 13):
    return fix_age(a) + fix_age(b) + fix_age(c)

print(filter_teens(2, 1, 15))


