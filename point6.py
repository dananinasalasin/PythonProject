# 6.1.2
def shift_left(my_list):
    temp = my_list[0]
    my_list[0] = my_list[1]
    my_list[1] = my_list[2]
    my_list[2] = temp
    return my_list

#print(shift_left([0, 1, 2]))
