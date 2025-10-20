# Python is dynamically-typed
# this means that datatypes can change during an application
# this type coercion or conversion happens implicitly in Python
# but may be called explicitly as well, on purpose
# each data type has its wrapper function of the same name

# conversion to boolean (bool)
# every datatype has its truthy and falsey values (convert to True or False)
# easier to remember the Falsey values - most values are truthy
# falsey values:
# Zero numbers 0 and 0.0
# empty collections/containers
# including str which is a collection or container (of single characters)
# note empty collections in JS, by contrast, are truthy!
# None
# in Python, an empty container is False and BECOMESTRUE when leemnt(s) added

print("using the bool() wrapper function")
print("numbers: ")
print(bool(1))
print(bool(-99))
print(bool(0))
print(bool(0.0))

print("containers: list")
print(bool([1,2,3]))
print(bool(["name"]))
print(bool([]))

print("containers: dictionary")
print(bool({"name": "Alan", "age": 21}))
print(bool({2: 22, 1: 33}))
print(bool({}))#actually an empty set
print(type({}))
# trying to assign and return in same statement impossible
# print(empty_dict = bool(dict()))#TypeError: print() got an unexpected keyword argument 'empty_dict'
# ÷OR, using Walrus
print(empty_dict := dict())#TypeError: print() got an unexpected keyword argument 'empty_dict'
print(empty_dict)#{}
print("empty dictionary:", type(empty_dict))#<class 'dict'>

print(type(dict))#class type
print(type(list))#class type
print(type(int))#class type

print("type coercion using the str() wrapper function")
print(str(True))
print(str(False))
# but words True and False both evaluate to True as booleans
if str(True):
    print("value True:", str(True))

# if str(False):
if bool(""):
    print("value False:", str(False))

# this is because both False AND True are both non-empty string values
# the only falsey string value is empty string

print("type coercion using the int() wrapper function")
print(int(True))#1
print(int(False))#0
# print(int("a non-empty string"))#cannot convert str to int
print(bool("a non-empty string"))#True
print(bool(""))#False

print("float to int")
print(int(1.0))#1
print(int(1.9))#1 (truncated, NOT rounded)

print("int to float")
print(3/4)#0.75 - IMPLICIT coercion
print(float(1))#1.0 - EXPLICIT coercion