# 8.2.1
data = ("self", "py", 1.543)
format_string = "Hello %s.%s learner, you have only %.1f units left before you master the course!"
print(format_string % data)

# 8.2.2
def sort_prices(list_of_tuples):
    return sorted(list_of_tuples, key=lambda item: float(item[1]), reverse=True)

products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
print(sort_prices(products))
