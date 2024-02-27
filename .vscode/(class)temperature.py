#creation of class
class Temperature:
    def __init__(self, celsius, fahrenheit):
        self.celsius = celsius
        self.fahrenheit = fahrenheit
#methods for converting celcius to fahrnheit
    def to_fahrenheit(self):
        fahrenheit = (self.celsius * 1.8) + 32
        print(f"The Fahrenheit temperature is {fahrenheit:.2f}°F")
#methods to convert fahrnheit
    def to_celsius(self):
        celsius = (self.fahrenheit - 32) / 1.8
        print(f"The Celsius temperature is {celsius:.2f}°C")

temperature = Temperature(70, 60)
temperature.to_fahrenheit()
temperature.to_celsius()






     



