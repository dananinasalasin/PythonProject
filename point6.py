# 6.1.2
def shift_left(my_list):
    temp = my_list[0]
    my_list[0] = my_list[1]
    my_list[1] = my_list[2]
    my_list[2] = temp
    return my_list

#print(shift_left([0, 1, 2]))

# 6.2.3
def format_list(my_list):
    return ", ".join(my_list[:-1:2]) + ", and " + my_list[-1]

my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
print(format_list(my_list))