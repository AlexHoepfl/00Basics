first_number = float(input("Erste Zahl: "))
second_number = float(input("Zweite Zahl: "))

temp = first_number
first_number = second_number
second_number = temp
#first_number, second_number = second_number, first_number

print("Erste Zahl: ", first_number)
print("Zweite Zahl: ", second_number)