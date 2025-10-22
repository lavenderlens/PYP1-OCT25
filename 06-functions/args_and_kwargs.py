def greet7(name, languages):
    return f"My name is {name} and I train {languages}"

print(greet7("Alan", ("Python", "Java", "JavaScript")))#a single arg as second positional arg

def greet8(name, *languages):
    return f"My name is {name} and I train {languages}"#zero, one or many individual args packed into a tuple

print(greet8("Alan", "Python", "Java", "JavaScript"))

# *args
# the * is mandatory, the args is not
# none, one, or many args are packed into a tuple
# the *args parameter must come after any others

def greet9(name, *languages, **address):
    return f"My name is {name} and I train {languages}. I live in {address}."

print(greet9("Alan", "Python", "Java", "JavaScript", county="Donegal", country="Ireland"))

# **kwargs
# the ** is mandatory, the kwargs is not
# none, one, or many keyword args are packed into a dictionary
# the **kwargs parameter must come after any others INCLUDING *ARGS IF PRESENT

# print(greet9("Alan", county="Donegal", country="Ireland", "Python", "Java", "JavaScript"))#SyntaxError: positional argument follows keyword argument