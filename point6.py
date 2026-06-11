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
#print(format_list(my_list))

# 6.2.4
def extend_list_x(list_x, list_y):
    list_x[:0] = list_y
    return list_x

x = [4, 5, 6]
y = [1, 2, 3]
#print(extend_list_x(x, y))

# 6.3.1
def are_lists_equal(list1, list2):
    return sorted(list1) == sorted(list2)

list1 = [0.6, 1, 2, 3]
list2 = [3, 2, 0.6, 1]
list3 = [9, 0, 5, 10.5]
#print(are_lists_equal(list1, list2))

# 6.3.2
def longest(my_list):
    longest_mem = max(my_list, key=len)
    return longest_mem

list1 = ["111", "234", "2000", "goru", "birthday", "09"]
print(longest(list1))
