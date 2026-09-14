#boolean expressions can return True or False values.
#all and any in an expression requires some conditions to be met.
 #"all" requires all condition to be met to return "True"
 #while "any" requires one condition to be met to return "True"
 
email = "timothymang@gmail.com"
id = 70989
height = 5.10
age = ""

print(all([email, id, height, age]))
print(any([email, id, height, age]))

# > greater than, < less than can be used as operands.

age = 36

print(18 < age >= 36)

# using "and" and "or" in expression.
