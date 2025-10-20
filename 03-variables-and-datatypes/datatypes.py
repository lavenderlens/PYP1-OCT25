# the standard, built-in datatypes
# literals, or single values, OR expressions that evaluate to them
# IMMUTABLE by default
# this means that a value IS a value and will always be
# we may go off and reference ANOTHER value
# but the original one doesn't change, it is merely de-referenced

my_int = 1#no keyword for a new variable
my_int = 2
# also
my_int = "3"

# datatypes can and do change - dynamic typing
# also Python infers the datatype of the variable on the LHS
# from the datatype of the expression on the RHS

# variables must be initialised:
my_bool = True #declaration and assignment at once
# in all but two edge cases global and nonlocal - see Functions
# because there is NO KEYWORD to denote a variable declared for the first time
# we must always (almost always) assign an initial value which determines a variable's type as well

# int. or integer/whole number value
# values: whole numbers, negative or positive, OR an expression that evaluates to a whole number
# immutable type (values cannot be changed, just de-referenced / re-referenced)

# float. or floating-point/decimal number value
# values: fractional numbers, negative or positive, with the dot character OR an expression that evaluates to a number
# immutable type (values cannot be changed, just re-referenced)

my_float = 1.0#initialised
my_float = 1.5#re-assigned

# str (strings)
# values: any characters of zero or more
# immutable type
# single, double OR triple-quoted
# zero indexed (from first character)
# have a length property, obtained by using len()

my_str = "Hello"
first_character = my_str[0]
print(first_character)
print(len(my_str))
# print(my_str[5])#IndexError: string index out of range

# container types for multiple values

# LIST list() OR [] INSTANTIATED
# holds multiple values
# values may be of same type but strictly do not have to be
# mutable by default
# commonly used for items of same type
# ordered, permits duplicates

my_list = [0, True, "Hello"]#permissible but not beneficial

my_list = ["bat", "ball", "gloves"]

# copying (reference only)
my_list_reference_copy = my_list#clue is: no extra or new []
# if there are no new [] (and list() hasn't been used)
# ####then there is no new list####
# so both references point to the same list
# a change in one mutates the same list in place
# and must be reflected when accessing that list
# from the other variable

my_list_reference_copy[0] = "cricket bat"
print(my_list_reference_copy)
print(my_list)#original mutated

my_list_reference_copy.append("whites")#append adds to end of list
print(my_list_reference_copy)#same
print(my_list)#same

# TUPLE tuple() OR () INSTANTIATED
# holds multiple values
# values may be of same type but strictly do not have to be
# IMMUTABLE by default:
# does not permit ITEM re-assignment
# commonly used for items of differing type
# ordered, permits duplicates

my_tuple = ("bat", "ball", "gloves")
# my_tuple[0] = "cricket bat" #TypeError: 'tuple' object does not support item assignment
# does support overall reassignment
my_tuple = ("ball", "shin pads", "goal")

# tuples commonly used to store data of different types eg
# mapping columns from a database
my_restaurant = ("at the end of the universe", 42, True)

# sets
# values: the elements can be of any type
# not ordered
# may not contain duplicates
# set methods for data analytics - see later
my_set = {1,2,2,3,4,4,5}#set holds single values
print(my_set)#{1, 2, 3, 4, 5}

my_other_set = {"one", "two", "two", "forty_four", "ninety-one", "a-one"} 
print(my_other_set)#{'one', 'ninety-one', 'a-one', 'two', 'forty_four'}
# {'two', 'forty_four', 'a-one', 'one', 'ninety-one'} 2nd time

# DICTIONARIES
# values: key: value, pairs, comma-separated
# keys: may be of any type but are commonly strings
# keys must be unique
# values: may be of any type and may be duplicated
# mutable

my_dict = {"name": "Fred", "age": 21, "employed": True}
print(my_dict)

#None 
# the value None is a type itself
print(my_dict)
my_dict = None
print(my_dict)#None
print(type(my_dict))#<class 'NoneType'>