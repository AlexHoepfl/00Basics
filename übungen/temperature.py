temperature_celsius = float(input("Temperatur in °C: "))
CONVERSION_FACTOR = 1.8
OFFSET = 32

temperature_fahrenheit = temperature_celsius * CONVERSION_FACTOR + OFFSET

print("Temperatur in °F:", temperature_fahrenheit)

