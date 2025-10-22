'''
Create a file named functions_exercise_module.py and another named functions_exercise_runtime.py.

Code and test simple functions as follows:

get_greeting that returns a greeting, e.g. G'day

get_greeting_to that accepts a name and returns G'day [name]

get_product that accepts two numbers and returns the product of those numbers

get_first that accepts a list and returns the first element

get_name that accepts a dict and returns the value assoc. with the name key

get_circumference that accepts a radius and returns the circumference (2 * Pi * radius)
For Pi just use 3.14

time permitting, pick 3 of these functions and convert them into functions without a return statement, called print....

get_name >>> print_name
'''

def get_greeting():
    return "Hello! "
def get_greeting_to(name):
    return "Hello, " + name
def get_product(num1,num2):
    """return: product of numbers:
        args: num1: int | float, num2: int | float"""
    return(num1+num2)
def get_first(items):
    return items[0]
def get_first_with_error_handling(items):
    if len(items) > 0:
        return items[0]
    return None
def get_name(dict):
    return f"Hello {dict["name"]}\nYou are {dict["age"]} years old"
def get_name_refactored(dict):
    return dict.get("name", "no name prop")
def get_circumference(radius):
    PI=3.14
    return 2 * PI * radius #returns number with inaccuracy
    # return f"{2 * PI * radius:.2f}" #returns STRING, formatted to two dec places
    # separation of concerns:
    # PRESENTation from CALCULation

# print("functions_exercise_module")#runtime code in the module

# show runtime code hiding in module

# conditional with dunder properties
# dunder: DoubleUNDERscore
if __name__ == "__main__": #only if we are running this module
    print("functions_exercise_module")#runtime code in the module
    supprters = {"Katy":"WHUFC","Ellis":"MUFC","Chris":"AVFC"}
    def get_names_and_teams(supporters):
        list_of_tuples = []
        for key, value in supporters.items():
            list_of_tuples.append((key, value))
        return list_of_tuples
    print(get_names_and_teams(supprters))

# break
# show type hinting

def type_hinting(name: str, number: int | float)-> str:
    return f"{name}, {number}"

# show docstrings
def type_hinting_with_docstring(name: str, number: int | float)-> str:
    """this is a test function that accepts two args and returns them in a string

    Args:
        name (str): a name
        number (int | float): a number

    Returns:
        str: formatted string containing the name and number
    """
    return f"{name}, {number}"


# // extension
# supprters = {"Katy":"WHUFC","Ellis":"MUFC","Chris":"AVFC"}
# def get_names_and_teams(supporters):
#     list_of_tuples = []
#     for key, value in supporters.items():
#         list_of_tuples.append((key, value))
#     return list_of_tuples

# print(get_names_and_teams(supprters))