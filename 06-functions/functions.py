radius = 10
print(area := 3.14 * radius ** 2)
# min LOC for a function: 1
def calcAreaOfCircle(radius):
    return 3.14 * radius ** 2 #HOW to do it

print(calcAreaOfCircle(10))#WHAT to do
print(calcAreaOfCircle(20))
print(calcAreaOfCircle(5))

'''
functions, as in any other language, wrap one or more LOC in a function name
to be called zero, one, or many times at some time in the future
functions are commonly defined in a script ON THEIR OWN, with no runtime code
the script with the runtime code in it, that USES the functions,
is separate, and IMPORTS them from the first script
the first script is called a module

how short can a function be?
1 LOC
why? to make code more declarative
the function name may be more descriptive than its workings
how long can a function be?
Not too long.
As a rule of thumb I would be wary of functions over 50-100 LOC
It is very likely they will have dependencies on other code.
If that other code were to break, so would your function.
You may never know this while unit testing
if a function consistently produces the same result for the same given input
it is said to be pure, or idempotent 
pure functions are much easier to test in an automated test environment
we do not have to mock dependencies that may change independently of the function
'''

# functions have input, output, both, or neither
# a print statement is NOT considered output
# a return statement is
# this output may be persisted in a variable
# or passed as INPUT to ANOTHER function
# input is taken in via parameter brackets ()
# even if there is no input the brackets must be there 
# both at function definition time and at runtime
# inside the brackets data is referred to as 
# PARAMETERS at function definition time
# ARGUMENTS (args) at runtime
# the only situation where the invocating brackets () may be omitted
# is if the function code is passed to another function as a callback

# WAY 1, no input, no output
def greet1():
    print("Hello")
    print("from greet1")
    print("how are you today?")

greet1()
greeting1 = greet1()
print(greeting1)#None 

# WAY 2, no input, output
def greet2():
    return "Hello \nfrom greet2 \nhow are you today?"

greet2()#NO VISIBLE OUTPUT
print(greet2())#output from greet2 as input to print
greeting2 = greet2()
print(greeting2)
# output is persisted to the rest of the system,
# either as a variable
# or as input to another function (in this case print())

# WAY 3, input and output
def greet3(name):
    return "Hello " + name + "\nfrom greet3 \nhow are you today?"
# print(greeting3 := greet3())#TypeError: greet3() missing 1 required positional argument: 'name'
print(greeting3 := greet3("Alan"))#

# WAY 4, input, no output
def greet4(name):
    print("Hello " + name)
    print("from greet4")
    print("how are you today?")
greet4("Vishnu")
print(greeting4 := greet4("Marc"))#None - no return

# positional vs named args
# consider a function that accepts two positional args:
def greet5(name, age):
    return f"Hello {name}\nfrom greet5\nyou are {age} today"

print(greeting5 := greet5("John", 21))
print(greeting5 := greet5(21, "John"))

def greet6(name="friend", age = 21):
    return f"Hello {name}\nfrom greet6\nyou are {age} today"
print(greeting6 := greet6(name="Attila", age=21))
print(greeting6 := greet6(age=21, name="Attila"))#with args named, position doesn't matter
print(greeting6 := greet6())#even with no args, there is no error, just default values swapped in

# default, named args
# 1. supply a value if not supplied at runtime
# 2. order of args and even missing args is no problem

