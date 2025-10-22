'''
scope defines the visibility and lifespan of a variable
WHERE and WHEN it is seen / available
local scope:
-   declared within a function
-   visible only within the function or its blocks
-   lives and dies with the function execution
global scope:
-   declared outside of any functions
-   visible to all functions in the script
-   functions can see the scope chain "up and out" 
-   but not down and in
-   global scope lives whilst the whole script is executing
-   pure functions: accept copies of data, 
-   ALWAYS return the same thing EVERY time, for given same input
-   impure functions: have global dependencies on OTHER functions/variables,
-   do not always return same result for same given input
-   because their dependencies may change
-   impure functions are VERY hard to test
lexical scope:
-   defined as local function scope, lexical scope includes a "memory" of its parent function scope
-   this is achieved when a function is returned from the parent function with the local variable
-   that local variable becomes EFFECTIVELY GLOBAL for the function returned
-   lexical scope means functions can have memory and state persists between function calls

'''

# pure vs impure functions
next_num = 1#global variable

# impure function
def get_next_num():
    return next_num + 1

print(get_next_num())
print(get_next_num())

next_num = 99

print(get_next_num())
print(get_next_num())
# LOOKS LIKE the ouput will be the same each call
# but the global dependency can change and affect the output

# how to make this function pure:

def get_next_num_pure(next_num):#passes in a COPY of data
    return next_num + 1#next_num HERE is ANY num passed in the params

print(get_next_num_pure(next_num))
print(get_next_num_pure(next_num))
print(get_next_num_pure(next_num))

next_num = 499
print(get_next_num_pure(next_num))
print(get_next_num_pure(next_num))
print(get_next_num_pure(next_num))

# global dependency STILL APPERAS to change output
# but the value of the arg copied into the pure function ALSO changes
# so the function is pure, NO global dependency as it passes by copy

# what if we wished to update global state in our function?
# we have to TWO-WAY BIND function code to global state
# we use the keyword global
# print(next_num)#499

# impure function again
def get_and_mutate_next_num():
    global next_num #declaration of a local variable BOUND to the global of the same name
    next_num += 1
    return next_num

print(get_and_mutate_next_num())
print(next_num)
print(get_and_mutate_next_num())
print(next_num)

# what if we were to bind to LOCAL function scope and not to global?
# local function scope is EFFECTIVELY global to functions returned from a function
# this enables state to persist between function calls

# a variable declared inside a function is said to have LOCAL scope
# it remains completely separate from a global variable EVEN of the same name:

def get_next_local_num():
    next_num = 1001
    next_num += 1
    return next_num

print(get_next_local_num())
print(get_next_local_num())#always 1002

# what if we were to bind to the local variable in a similar way we bound to the global
# and return ANOTHER, INNER function which has the is local variable as the next level up in its scope chain?

# we can do the following because:
# functions themselves are higher order objects (HOC/HOF) in Python
# this means they can be passed to and returned from other functions
# if we have an inner function, its effectively global scope
# is the parent, or outer functions's scope
# this scope level, to an inner function, is called LEXICAL scope
# it measn: the outer function scope
# EFFECTIVELY global,
# to an inner function returned

def get_next_lexical_num():
    next_num = 3001#lexically-scoped
    def get_next_num():
        nonlocal next_num
        next_num += 1
        return next_num
    return get_next_num

# inner function, when invocated as part of a function expression,
# is said to create a CLOSURE around the lexically-scoped variable
# it not only remembers the value of its lexically-scoped environment at closure creation time
# it also persists this value IN BETWEEN function calls

my_closure = get_next_lexical_num()
print(my_closure())
print(my_closure())
print(my_closure())
# reset by making a new fresh closure
my_closure = get_next_lexical_num()
print(my_closure())
print(my_closure())
print(my_closure())

# in summary
# global scope: shared by any function
# local scope: local to a particular function
# lexical scope: effectively global to an inner function returned
# if a value for a variable is not found in the immediate scope, 
# Python will look in the next scope level up (immediate parent) and so on
# ALL 3 may use the same variable name with no conflict
# but it's probably not a good idea to do this!