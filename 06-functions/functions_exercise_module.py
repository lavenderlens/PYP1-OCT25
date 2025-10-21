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

# get_name that accepts a dict and returns the value assoc. with the name key
# def get_name(supporters,club):
#         return {supporters}, {club}
# def get_name(supporters):
#         list_of_tuples = []
#         for key, value in supporters.items():
#             list_of_tuples.append((supporters[key]))    
#         return (footy)
 
# print(get_name({"Katy":"WHUFC","Ellis":"MUFC","Chris":"AVFC"}))
supprters = {"Katy":"WHUFC","Ellis":"MUFC","Chris":"AVFC"}
def get_names_and_teams(supporters):
    list_of_tuples = []
    for key, value in supporters.items():
        list_of_tuples.append((key, value))
    return list_of_tuples

print(get_names_and_teams(supprters))