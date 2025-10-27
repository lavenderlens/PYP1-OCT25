'''
a tuple is an IMMUTABLE, idexed (ordered) container
permits duplicates
commonly used to store different types of data together
such as that returned from a function
ensures that data cannot be modified
'''

my_tuple = ("alan", 21, ["walking", "photgraphy"], True)
my_emptyTuple = ()
my_emptyTuple = tuple()
fib = (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144)

# tuple methods
print(fib.count(1))
print(fib.index(144))

# we can slice tuples as we would lists
# returns another tuple
print("low numbers and high numbers slices:")
print(low_numbers := fib[:6])#endIdx(0, 1, 1, 2, 3, 5)
print(high_numbers := fib[6:])#startIdx(8, 13, 21, 34, 55, 89, 144)

# we can iterate tuples
for el in fib:
    print(el)

# we can enumerate them as well
for index, element in enumerate(fib):
    print(index, element)

# tuple arithmetic
print(fib + (233, 377))
print(fib * 2)
print(fib)# original unaffected

# it looks here that the original is mutated when reassigned
fib = fib + (233,377)
print(fib)

# item reassignment is the immutable bit
print(len(fib))
print(fib[14])
# if we attempt to re-assign an item:
# fib[14] = 0#TypeError: 'tuple' object does not support item assignment

# it would be better to say a tuples elements are immutable