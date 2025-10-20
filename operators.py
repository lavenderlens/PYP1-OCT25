# an expression involves operators (symbols that perform operations) 
# and operands (values that are transformed by the operator)
x = 1 #declares variable named x that is assigned int value of 1
x = x + 1 #re-assigns new value of itself plus one to x
# the first line initialises x with a single value, 1
# the second line assigns x the result of an expression - itself plus 1
# the expression has an operator, +
# and two operands, x (again), and 1
# single = in programming is always assignment never comparison

# arithmetic operators
# +
# -
# *     - 2 squared is 2 * 2
# **    - 2 ** 3 is 2 cubed
# /
# %     - remainder, whole number division
# //    - quotient, whole number division

print(10/2)#5.0 promoted automatically to float
print(10%2)#0
print(10%3)#1
print(10//2)#5
print(10//3)#3

print(10/3)#3.3333333333333335
# 1980s standard IEEE 754
# numpy or other math/number libs 
# for calculations where floating-point accuracy is important
# we could format our output
print(f"formatted out put for 10/3: {(10/3):.2f}")
# but the innacuracy is still there

# promotion: samller type into larger
print(10/2)#5.0 automatically
print(9 + 2)#11 (int)
print(9 + 2.0)#11.0 (float)

# non-numeric arithmetic
print("ho" * 3)#hohoho
print("*" * 50)#
# the mechanism underlying this is special method of the str class 
# that overrides the default object class behaviour of how * should behave

# assignment operators
# = is single assignment
# += is compound assignment
# note these work for strings and numbers both

my_num = 1
my_num = my_num + 1
my_num += 1
print(my_num)#3

my_string = ""
my_string += "I "
my_string += "love "
my_string += "Python. "
print(my_string)

# note this way of building strings is expensive in memory when long strings are involved
# other methods see https://www.tracedynamics.com/python-string-builder/

# walrus operator
# like a walrus lying on its side with two eyes : and two tusks =
# assigns AND returns at once
# before:
x = 1
print(x)
# print(x=1)#falls down silently at runtime #TypeError: print() got an unexpected keyword argument 'x'

# after:
print(y := 3)
# value both persisted (to y) and passed (to print())

# nested data (with respect to tuples in particular)
my_nested_dict = {
    "name":"Alan",
    "languages": ("Python", "Java", "JavaScript")
}
# tuple within dict
# tuple ELEMENTS may not be reassigned
# but the overall reference may be

# also note square brackets notation to refer to dict keys
print(my_nested_dict["languages"][2])
# my_nested_dict["languages"][2] = "React"#TypeError: 'tuple' object does not support item assignment
my_nested_dict["languages"] = ("English", "Irish", "French", "Italian")
print(my_nested_dict)

# things that are NOT very Python-esque
# increment/decrement operators ++ and --
# NOT in Python

# multiple assignment on one line
x = 1; y = 2; z = 3

# much better:
x, y, z = 4, 5, 6
# in JS: destructuring assigment

# assignment opertaor chaining (very hard to read)
x = 1
y = 1
# may be re-written as
x = y = 1

# container operators
# dict

name, languages = my_nested_dict["name"], my_nested_dict["languages"]
# we will later see that dot notation is used for objects
# dictionaries use square brackets notation to access/mutate props

# list
my_nums = [1,2,3]
first, second, third = my_nums[0], my_nums[1], my_nums[2]

# comparison operators
# <         less than
# <=        less than or equal to
# >         greater than
# >=        greater than or equal to
# 3 >= 4    #order important
# !=        not equal to
# is        tests for IDENTITY: references the same object as

my_nums = [1,2,3]
my_other_nums = [1,2,3]
my_nums_copy = my_nums
# using the is operator to check equality of reference / referential equality
print(my_nums is my_other_nums)#False
print(my_nums is my_nums_copy)#True

# the system Python uses to establish if two refs point to the same object is the builtin id() function
print(id(my_nums))          #4302110336     #4298768000
print(id(my_nums_copy))     #4302110336     #4298768000
print(id(my_other_nums))    #4301703360     #4298361024

# because my_nums and my_nums_copy both point to the same list object
# either refrence will modify the same
my_nums_copy.append(4)
my_nums.append(5)
print(my_nums)#[1, 2, 3, 4, 5]
print(my_nums_copy)#[1, 2, 3, 4, 5]

# because the copy copies the reference only, it is called referential equality // copy by reference
# the original may be mutated through the new ref
# IF we want IMMUTABLE copies taht do not cahnge the original
# python libraries to the rescue!
import copy

# using the copy module
# we may copy and effectively break all references to the original
# either at top level only
# or recursively for any number of nested levels

my_nums_shallow_copy = copy.copy(my_nums)
my_nums_shallow_copy.append(6)
print(my_nums_shallow_copy)#COPY [1, 2, 3, 4, 5, 6]
print(my_nums)#ORIGINAL [1, 2, 3, 4, 5]

my_nested_nums = [1,2,3,[4,5,6]] #list within a list: lists are mutable
my_nested_nums_shallow_copy = copy.copy(my_nested_nums)
my_nested_nums_shallow_copy[3].append(7) 
print(my_nested_nums) #[1, 2, 3, [4, 5, 6, 7]] original affected still

my_nested_nums_deep_copy = copy.deepcopy(my_nested_nums)
my_nested_nums_deep_copy[3].append(8)
print(my_nested_nums_deep_copy)#[1, 2, 3, [4, 5, 6, 7, 8]]
print(my_nested_nums)#[1, 2, 3, [4, 5, 6, 7]] original unchanged


