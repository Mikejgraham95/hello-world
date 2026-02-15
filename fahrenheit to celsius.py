#Michael Graham
#02/08/2026
#This program will convert Fahrenheit to celsius
#function to convert fahrenheit to celsius
def convert_f_to_c(temp_in_fahrenheit):
    return (temp_in_fahrenheit - 32) * 5 / 9
#ask for temp in fahrenheit
tempf = float(input('What is the temperature in Fahrenheit? '))
tempc = convert_f_to_c(tempf)
#output is degrees celsius
print(f'Converted, it is {tempc:.1f} degrees Celsius')
