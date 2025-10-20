# 1. Create a script named exercise1_console_io.py.
# 2. Prompt the user to input his/her name and capture it in variable named name.
# 3. Prompt the user to input his/her age and capture it in a variable named age.
# 4. Print the user's name and age to the console. You might try doing this with one
# invocation of the built-in print function.
# 6. Optionally, try adding 1 to the age and display it as age next birthday.

# 7. Modify your script so that the variable for age has its
# datatype changed after it is taken in from the user and before it is used in an expression.

print("Enter your name:")
name = input()
print("you entered", name)
print("Enter your age:")
age = input()
age = int(age)
print("you entered " + str(age))#coerces int to str

print(f"age next birthday: \n{age + 1}")#since Python 3.7>
# and also - multi-line strings
print(f"""
age next birthday: 
{age + 1}""")
# above looks odd but works in context of triple-quoted strings