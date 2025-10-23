# execute from CMD line, ensure cursor is in this directory

# open file, same as before, but with optional 2nd arg, default is r for read, to spec MODE
file = open("data2.txt", mode="w")#mode w = write, OVERWRITE if exists, create if not exists
text = "StayAhead Training\nExplore over 200 courses with a leading UK independent IT training provider\nJoin us in the classroom or virtually"
file.write(text)
file.close()

'''
different write modes:
a = append to existing
x = creates, raises a FileExistsError is exists
w = writes but overwrites if exists
'''

