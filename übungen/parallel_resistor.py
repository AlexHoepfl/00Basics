resistor_1 = float(input("Widerstand R1: "))
resistor_2 = float(input("Widerstand R2: "))

total_resistance = (resistor_1 * resistor_2) / (resistor_1 + resistor_2)

print("Gesamtwiederstand: ", total_resistance, " Ohm")
