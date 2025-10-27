'''
a list is a mutable, indexed/ordered container
permits duplicates
commonly used to store elements of the same type (any)
but need not be
'''

# creation
nums = []
nums = list()#empty list
nums = [1,2,3]

# element referencing
print(third_element := nums[2])

# element reassigning
nums[2] = 4

# adding elements
nums.append(5) # to the end
nums.insert(3, 4)

# print(nums)#[1, 2, 3, 4, 5]

# slicing: the creation of a new list from all or some parts of the original
# slice syntax:
# [startIdx, endIdx, step]
# note endIdx is EXclusive (one beyond what you need)
fib = [0,1,1,2,3,5,8,13,21,34]
print(len(fib))

# give me the last 5 values
print(fib[5:])
# the first 5
print(fib[0:5])
# the last element
print(fib[9:])
print(fib[9:10])
# print(fib[10])#IndexError: list index out of range

# the 3rg arg: step
# give me every second value
print(fib[::2])
# every second value missing out 1
print(fib[2::2])
print(fib[1::2])

# reverse step
print(fib[9::-1])
print(fib)#original unchanged

# an even more powerful tool for working with lists is
# list comprehensions
# a comprehension passes in a function
# to be performed on every element of the original list

# note that our list slicing example above relies on INDEX
# list comprehensions rely on the ELEMENTS themselves

# get the actual even number values
print(even_values := [element for element in fib if element %2 == 0])
print(odd_values := [element for element in fib if element %2 != 0])
print(under_10_values := [element for element in fib if element < 10])
print(over_10_values := [element for element in fib if element > 10])
# akin to a filter operation
# filter returns some elements that pass a test (predicate function)
# whereas a map returns a list with ALL element transformed by a function
print(elements_scaled_by_2 := [element * 2 for element in fib])

# builtin list methods
print(f"num elements: {len(fib)}")
print(f"sum elements: {sum(fib)}")
print(f"min elements: {min(fib)}")
print(f"max elements: {max(fib)}")

# add lists
print(added_list := fib + [55,89])

# multiply lists
print(multiplied_by_2 := fib * 2)

# what if we wanted to multiply individual values:
# use a list comprehension to transform each value in turn
print(fib_scaled_by_2 := [element * 2 for element in fib]) # akin to a map operation
# map returns all elements after a transformation of each has been applied

# inserting after an index
names = ["Attila", "Vishnu", "John", "Marc", "alan", "tim", "Horatio"]
names.insert(5, "Bertrand")
print(names)

del names[6]
print(names)#time, at index 6, is gone

# if we did not know where the index of an element was
del names[names.index("alan")]
print(names)

# if we wish to remove last element
names.pop()
print(names)
# when supplied with an arg pop removes and returns element at that index
names.insert(3, "Ludwig")
print(names)
names.pop(names.index("Ludwig"))
print(names)

print("Ludwig" in names)
print("Attila" in names)

names.sort()
print(names)
names.sort(reverse=True)
print(names)
names.sort(key=len)
print(names)

print(elements_scaled := [element * 2 for element in fib])
