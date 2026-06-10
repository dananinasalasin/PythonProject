import calendar
input_date = input("Enter a date (dd/mm/yyyy): ")
date_list = input_date.split("/")
day_index = calendar.weekday(int(date_list[2]), int(date_list[1]), int(date_list[0]))
print(calendar.day_name[day_index])