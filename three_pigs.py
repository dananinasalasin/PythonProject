three_digit_number = int(input("Enter three digits (each digit for one pig): "))
sum_three_digits = three_digit_number % 10 + (three_digit_number // 10) % 10 + (three_digit_number // 10) // 10
print(sum_three_digits)
print(sum_three_digits // 3)
print(sum_three_digits % 3)
print(sum_three_digits % 3 == 0)