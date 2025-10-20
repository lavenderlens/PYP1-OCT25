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
