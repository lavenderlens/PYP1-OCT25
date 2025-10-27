names = ["Ellis", "Brad", "Katy", "Becca", "Shaun", "Chris", "Owen", "Mike", "Bertrand", "Immanuel", "Ludwig", "Alan", "Zak"]

# using list comprehensions,
# tell me

# 1. the names of less than 5 characters length
for name in names:
    if len(name) < 5:
        print(name)#output is print only, nothing is persisted

shorter_names = [name for name in names if len(name) < 5]
print(shorter_names)

# 2. the names of greater than 5 characters length
print(long_names := [name for name in names if len(name) > 5])

# 3. the names with even numbers of characters
print(names_with_even_num_of_chars := [name for name in names if len(name) % 2 == 0])

# 4. the names beginning with "B" - case-insensitive, use startswith() method of str()
print(names_starting_with_b := [name for name in names if name.startswith(("b","B"))])
print(names_starting_with_b := [name.title() for name in names if name.startswith(("B"))])

# 5. all the names, upper-cased
print(all_names_upper := [name.upper() for name in names])#no condition, but a transformation
# for name in names:
#     #if [name for name in names if name % 2 == 0]
#     if [name[names.index()] % 2 == 0]
#         print(name)

new_list = [name for name in names if len(name) %2 == 0]
print(new_list)