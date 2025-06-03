# Create an empty dictionary. Allow 2 friends to enter their favorite language as value and use key as their names. Assume that the names are unique. 

doc = {}

name = input("Enter Friends Name: ")
lang = input("Enter Language Name: ")
doc.update({name: lang})

name = input("Enter Friends Name: ")
lang = input("Enter Language Name: ")
doc.update({name: lang})

print(doc)