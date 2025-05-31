a = (1, 3, 6, 4)
print(a)
print(type(a))

myTuple = ("Apple", "Orange", "Apple", 5, 451.21, False, "Supan", "Roy")
print("Original tuple:", myTuple)

# Counting occurrences of an element
apple_count = myTuple.count("Apple")
print("Count of 'Apple':", apple_count)

# Finding index of an element
index_supan = myTuple.index("Supan")
print("Index of 'Supan':", index_supan)

# Tuple with one item (singleton tuple)
single_item = ("Hello",)  # Note the comma!
print("Singleton tuple:", single_item)

# Tuple concatenation
newTuple = myTuple + ("New", 123)
print("After concatenation:", newTuple)

# Tuple slicing
print("Sliced tuple (1 to 4):", myTuple[1:5])

# Length of tuple
print("Length of tuple:", len(myTuple))
