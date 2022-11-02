# Define function to convert Fahrenheit to Celsius
def ConvertFtoC(F):
# Convert the Fahrenheit into Celsius
    C = (5 / 9) * (F - 32)
    # Return the conversion value
    return C
# Take the Fahrenheit value from the user
F = float(input("Enter the temperature in Fahrenheit: "))
# Print the Fahrenheit value
print("Temperature in Fahrenheit = {:.2f}".format(F))
# Print the Celsius value
print("Temperature in Celsius = {:.2f}".format(ConvertFtoC(F)))
