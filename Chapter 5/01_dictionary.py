marks = {
        "Supan": 86,
        "Raju": 81,
        "Jenny": 68,
        75: "Rohan"
}

print(marks, type(marks))
print(marks["Supan"])
print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"Raju": 82, "Shanzid": 74})
print(marks["Raju"])
print(marks.values())

print(marks.get("Joy")) # Prints None
print(marks["Unknown"]) # Returns an Error