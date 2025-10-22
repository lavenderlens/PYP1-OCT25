def greet9(name, **address, *languages):
    return f"My name is {name} and I train {languages}. I live in {address}."

print(greet9("Alan", "Python", "Java", "JavaScript", county="Donegal", country="Ireland"))
