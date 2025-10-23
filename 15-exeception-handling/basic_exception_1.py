"""
   from a user POV, exception handling enables the code to recover
   and carry on from a catastrophic event
   from a dev POV, it enables us to create and raise Errors 
   (objects with information about the problem)
   according to business logic 
   exceptions should be seen as creating opportunities
   (for our system to intervene)
   not so much as presenting difficulties
"""
num1 = input("enter a number")
num2 = input("enter another number")
try:
    num1 = int(num1)#exception likely to occur
    num2 = int(num2)#exception likely to occur ValueError: invalid literal for int() with base 10
    print(result := num1 / num2)
except ValueError:
    print("wrong input, try again")
except ZeroDivisionError:
    print("you cannot divide by zero")
    # the order of except blocks matters

print("Carrying on as usual...")
# stuff occurs, you do not know until runtime what that will be
# these are the types of Error that should be handled

# where an error could be prevented by better programming
# we can, but should not, handle it with error handling code
try:
    nums = [1,2,3]
    print(nums[3])#IndexError: list index out of range
except IndexError:
    print("index out of range")
print("carrying on as usual...")
