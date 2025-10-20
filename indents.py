#  print("I am not indented in a block")#IndentationError: unexpected indent
print("I am not indented in a block")
    # print("I am indented in a block")#IndentationError: unexpected indent

if False:
    print("I am indented in a block")
    print("I am indented in a block")
    print("I am indented in a block")
print("I am now back on the LH margin")