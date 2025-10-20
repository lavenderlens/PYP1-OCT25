# the input() function takes keyboard input from the user
# there are of course IRL many more forms of input device
# in development and testing we tend to stick with keyboard in: terminal out

# prompt the user:
print("enter your name:")
name = input()
print("You entered",name)
print(type(name))#<class 'str'>

# the input() function ALWAYS returns a str
# for numbers and other types we must perform a conversion

# print("enter your age")#saves a line
age = input("enter your age")
# print("age next birthday:", age + 1)#TypeError: can only concatenate str (not "int") to str
print("Carrying on regardless...")#unreachable code if program crashes
print("age next birthday:", age + str(1))#age next birthday: 211
print("age next birthday:", int(age) + 1)#age next birthday: 22

# we may be tempted to collapse lines further if all we want is a number form input()
age = int(input("Already wrapped and coerced to int"))
# not a good pattern for error handling
age = input("enter age")#this line will always work
age = int(age)#this line will sometimes work
