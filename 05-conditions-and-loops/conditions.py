'''
conditional statements are very smilar in Python to other languages,
they execute a block of code depending on whether a condition evaluates True or False
if True:
    code block, defined by indent, immediately following is executed
if False:
    #skipped
    pass

an else block has NO condition and means, really ANYTHING else

you can test multiple conditions using if elif else

following execution of a branch the interpreter steps out of the statement structure, like a break

so when using ranges of values, if..elif blocks should be arranged with care to avoid unreachable code

Since recently in Python 3.10 there is another decision control statement
Called Structural Pattern Matching or match case
This mimicks the behaviour of switch in Java and JS, which traditionally has had no equivalent in Python
The match statement tests a single variable or expression for equality
There may be performance improvements depending on your data. 

'''
# single branch IF
if True:
    pass
    #pass is a keyword used when unit testing code
    # it enables us to run code with no errors, but doesn't add anything
    # we can fill in the code later
    # even comments should also be indented to the block they refer to

if True:
# print("true path executed")#IndentationError: expected an indented block after 'if' statement on line 32
    print("true path executed")
    #  print("true path executed")##IndentationError:
    # WITHIN a block, indents must be consistent
    # best practice: consistent throughout all code

# 2 branch - IF ELSE
if False:
    print("true path executed")
else:
    print("else executed")

# 3 or more branch - IF ELIF ELSE
# there is no practical limit to the number of ELIF statements
# but match case may be more performant for large numbers
if False:
    print("true path executed")
elif True:
    print("elif block executed")
else:
    print("else executed")

# IF ELSE on one line - this is Python equivalent of ternary operator in other languages

temperature = "cold"
temperature = "scorcio"

clothing = "jumper" if temperature == "cold" else "T-shirt"
print(clothing)
print(clothing := "jumper" if temperature == "cold" else "T-shirt")