import math

x_1 = float(input("x1: "))
y_1 = float(input("y1: "))
x_2 = float(input("x2: "))
y_2 = float(input("y2: "))

distance = math.sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)

print("Abstand: ", distance)