#rounding numbers and removing +ve or -ve signs

print(abs(2 - 10)) #abs removes the -ve result.

#round(),floor() , ceil() are used to round numbers up or down. you have to import the floor and ceil

import math
price = 35.6743556
print(math.floor(price))
print(math.ceil(price))
print(round(price))
print(round((price, 2)))