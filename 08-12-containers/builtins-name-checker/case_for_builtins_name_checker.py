# monkey-patching: the assigning of reserved system words to new values
str = "str" #the system reserved word str is now monkey-patched to a different meaning
my_str = str(1)#this line will fail
