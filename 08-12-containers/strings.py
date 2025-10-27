# raw strings
# sometimes escape characters need to be printed literally, eg. in a file path 
# C:\users\alan
# print(file_path := "C:\users\alan")#SyntaxError: (unicode error) 'unicodeescape' 
# codec can't decode bytes in position 2-3: truncated \uXXXX escape

print(file_path := r"C:\users\alan")#OK

print(registered_symbol := '\u00ae')

print(waving_hand := '\U0001F44B')

print(dog_face := '\U0001F436')

'''
strings are immutable, ordered containers of characters, 
they may contain duplicate characters
string methods return a new string
the original is unaffected but the same reference may be updated 
to point to the new string
'''

s1 = "hello"
s2 = "hello"
print(s1, id(s1))#hello 4340196720
print(s2, id(s2))#hello 4340196720
# strings are immutable

lst1 = ["hello"]
lst2 = ["hello"]
print(lst1, id(lst1))#['hello'] 4376466688
print(lst2, id(lst2))#['hello'] 4376566464
# lists are mutable