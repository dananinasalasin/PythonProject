# 8.2.1
data = ("self", "py", 1.543)
format_string = "Hello %s.%s learner, you have only %.1f units left before you master the course!"
#print(format_string % data)

# 8.2.2
def sort_prices(list_of_tuples):
    return sorted(list_of_tuples, key=lambda item: float(item[1]), reverse=True)

products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
#print(sort_prices(products))

# 8.2.3
def mult_tuple(tuple1, tuple2):
    result = []
    for item1 in tuple1:
        for item2 in tuple2:
            result.append((item1, item2))
            result.append((item2, item1))
    return tuple(result)

first_tuple = (1, 2)
second_tuple = (4, 5)
#print(mult_tuple(first_tuple, second_tuple))

# 8.2.4
def sort_anagrams(list_of_strings):
    result = []
    for word in list_of_strings:
        sorted_word = sorted(word)
        found_group = False
        for group in result:
            if sorted(group[0]) == sorted_word:
                group.append(word)
                found_group = True
                break
        if not found_group:
            result.append([word])
    return result

list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters', 'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']
#print(sort_anagrams(list_of_words))