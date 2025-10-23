num1 = input("enter a number")
num2 = input("enter another number")
try:
    num1 = int(num1)#exception likely to occur
    num2 = int(num2)#exception likely to occur ValueError: invalid literal for int() with base 10
    print(result := num1 / num2)
# except:#catches any error
#     print("enter only digits 0-9")
except ValueError:
    print("wrong input, try again")
except ZeroDivisionError:
    print("you cannot divide by zero")
finally:
    print("all done")