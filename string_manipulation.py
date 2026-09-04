''' we are learning the replace, split, cat methods.'''

price = "34,56"

new_price = price.replace(",", ".")

print(new_price)

price = "34,56"

phone = "+49 (176) 123-4567" #replace this number tp show 00491761234567

answer = print(phone.replace("+", "00").replace("(", "").replace(")", "").replace("-", "").replace(" ", ""))
#cat

name = "kalu"
first_name = "Timothy"
surname = "Mang"
full_name = name + first_name + surname

print(full_name)
print(surname + " " + first_name)
