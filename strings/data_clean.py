#to clean data of empty spaces we use the "lstrip, rstrip and strip" to do that.
'''text = " Engineering".lstrip()
book = "note ".rstrip()
chapter = "   hello   ".strip()
pages = "###hello###".strip("#")

content = "  this is nice "

print(text)
print(book)
print(chapter)
print(pages)
print(len(content.strip()))
'''

#use of upper and lower, to make sure all word are the same before searching.

data = "python PROGRAMMING"
print(data.upper())
print(data.lower())

search = " email ".lower().strip()
name = "EmaiL ".lower().strip()

print( search == name)


#challenge

data = "968-Maria, ( D@t@ Engineer ) ;; 27y  "
print(data.replace("968-", "name: ").replace(",", " |").replace("(", "role:").replace(")", "|").replace(";;", "age:").replace("27y", "27").replace("@", "a").lower())