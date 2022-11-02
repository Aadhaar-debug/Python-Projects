
# Define function to convert Celsius into Fahrenheit
def ConvertCtoF(C):
# Convert the Celsius into Fahrenheit
    F = (C * 1.8) + 32
    # Return the conversion value
    return F
# Take the Fahrenheit value from the user
F = float(input("Enter the temperature in Celsius: "))
# Print the Celsius value
print("Temperature in Celsius = {:.2f}".format(C))
# Print the Fahrenheit value
print("Temperature in Fahrenheit = {:.2f}".format(ConvertFtoC(C)))
