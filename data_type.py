'''a = 10 #integer
b = 3.5 # float
c = "hello" #string
d = "123" # string
e = True False #boolean
f = None # this is none waiting for input.

#function and Methods
function.name( ) #syntax
name.upper() #method
# most method will work for specific data types.
'''

name = "Timothy"
age = 36

print(type(name))
print(f'your name is {name} and you are {age} yrs old')

password = input("what is your password? ")
length_of_password = len(password)
#print(length_of_password)

if length_of_password < 8:
    print(f"password is {length_of_password} which is short")
else:
    print(f"the length of your password is {length_of_password} you have been given access!")