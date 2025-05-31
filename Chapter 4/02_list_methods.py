myList = ["Apple", "Orange", 5, 451.21, False, "Supan", "Roy"]
print(myList)

myList.append("Haris")  #Adding an element in list at the end
print(myList)

l1 = [2, 12, 25, 9, 34, 3]
l1.sort()  #Sorting a list
print(l1)
l1.reverse() #Reversing the list
print(l1)

l1.insert(3, 43) #Inserting 43 in the index 3
print(l1)

l1.pop(3) #Popping out 3th indexed value
print(l1)

l1.remove(12) #Removing element 12
print(l1)

copyList = myList.copy()  # Copying the list
print("Copied list:", copyList)

# Counting occurrences of an element
print("Count of 'Apple':", myList.count("Apple"))

# Extending list with another list
myList.extend(["New", 123])
print("After extend:", myList)

# Finding index of an element
print("Index of 'Supan':", myList.index("Supan"))