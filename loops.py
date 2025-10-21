'''
Loops come in two sorts: the while loop and the for loop
# while loops are commonly used for console IO
# there may be no obvious end to the process
# for loops are commonly used to iterate over containers
# the length of the container is known in advance
The for loop in Python is syntactic sugar for a while loop, 
usually when the number of iterations is known in advance.
There are no for loops at runtime, only while loops that the code is compiled into.
While loops in source code are useful when the number of iterations is not known in advance.

In Python, an optional else clause may be added to the end of both types of loop, for and while.
It is executed if the loop completes and doesn't hit a break statement.
In other words, if the loop completes normally.
To make this clearly readable, add a comment "# no break" next to the else clause.
'''
names = ['Michael Jackson', 'David Bowie', 'Janet Jackson', 'James Brown',
         'Gordon Brown', 'David Hume', 'Michael Jackson']
print(names)

# names is a container with a length prop
print(len(names))#7

# so we may use a for loop
for name in names:
    print(name)

# name is an arbitary variable - it just stands for each element
# names is a real name of a container

# while loop with counter
counter = 0
while counter < len(names):
    print(names[counter])
    counter += 1#important: omitting this gives you an infinite loop
    # the condition never becomes False so the loop carries on
    # and on

# while loop without a counter or a collection
# much more typical
while True:
    birth_year = input("Enter the year you were born, or zero to quit:")#an error will never occur here
    birth_year = int(birth_year)#an error could occur here
    if birth_year == 0:
        break
    if birth_year in range(1946, 1966):
        print(f"Born in: {birth_year}: baby boomer!")
    elif birth_year in range(1966, 1976):
        print(f"Born in: {birth_year}: Gen X!")
    elif birth_year in range(1977, 1994):
        print(f"Born in: {birth_year}: Millenial!")
    else:
        print(f"Born in: {birth_year}: Gen Z!")

# using break and continue with else
print("using break and continue, with else")
for name in names:
    if name == "Janet Jackson":
        break#breaks out of loop, else does not execute
        # continue#breaks out of one iteration only, loop completes, else executed
    print(name)
# no break
else:
    print("end of names list")

guest_list = []
while True:
    print("Enter a name for the guest list, or type \"exit\" to quit")
    name = input()
    if name == "exit":
        break
    guest_list.append(name)

print(guest_list)

# the do-while loop does not exist in Python