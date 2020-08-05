
def main():
    celsius=float(input("Please enter temperature in celsius: "))
    fahrenheit=celsius_to_fahrenheit(celsius)
    print("Tempreture in fahrenheit is ", fahrenheit)

def celsius_to_fahrenheit(celsius):
    return celsius*1.8+32.0

main()

