'''
1. Check if a user's name is not empty and the age is greater than or equal to 18.
2. Check if the password is at least 8 characters long and does not contain spaces.
3. check if a user's email is not empty, contains '@' and ends with '.com'
4. Check if a username is a string, is not None, and is longer than 5 characters
5. check if a username is either an admin or a moderator, and either they're not banned or thy've verified their email
'''
print("Answer 1.")
username = "Ann"
age = 20
print(username != "" and age >= 18)

print("Answer 2.")
password = "qwerty1234"

print(len(password) >= 8 and " " not in password)

print("Answer 3.")

email = "timo@gmail.com"
print((email is not " " and "@" in email) and email.endswith(".com"))

print("Answer 4.")

username = "Timothy"

print(type(username), username is not None and len(username) > 5)