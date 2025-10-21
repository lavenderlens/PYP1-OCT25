# WAY 1
import functions_module
functions_module.greet1()
print(functions_module.greet2())
# the trouble with this way is having to use the module name repeatedly in the runtime code

# WAY 2 the wildcard
from functions_module import *
print(greet3("Alan"))
greet4("Margaret")
# the trouble with THIS is that the NEXT person
# doesn't know whether these are functions declared here or in the module

# WAY 3 (the best IMHO)
from functions_module import greet5, greet6

print(greet5("Alan", 59))
print(greet6("Margaret", 60))