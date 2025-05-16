name = input("Enter your name: ")

print(f"Greetings, {name}")

letter = '''Dear <|Name|>,
Welcome to HIT!
<|Date|>'''

print(letter.replace("<|Name|>", "Roy").replace("<|Date|>", "16 May, 2025"))