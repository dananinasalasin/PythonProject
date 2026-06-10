temp = input("Insert the temperature you would like to convert: ")
type_temp = temp[-1].lower()
float_temp = float(temp[:len(temp)-1])
if type_temp == "c":
    new_temp = (5*float_temp - 160)/9
    print(str(new_temp) + "F")
else:
    new_temp = (float_temp-32)*5/9
    print(str(new_temp) + "C")


