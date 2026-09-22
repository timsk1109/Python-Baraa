'''# for loop is used to iterate items in a list.
fruits = ["mango", "orange", "paw-paw", "banana", "carrots"]

for i in fruits:
    if i == "banana":
        print("i love banana")
    print(fruits[3: ])
#you can iterate through list[], Tuple(), string"timothy", range(1, 100) and dictionary{}. The "item" in the "items" can be missed with different data types.

lists = [1, 2, 3, 4, 5]
tuples = (6, 7, 8, 9, 10)
dictionarys = {11, 12, 13, 14, 15}
strings = "Timothy"


total = 0

for list in lists:
    total += list
    print("current total is:", str(total))
print(total)
'''

#challenge- print the 7 times table form 1 - 10.
total = 7
for seven in range(1, 11):
    print(f"7 x {seven} = ", total * seven)
#print(7*2)