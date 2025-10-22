# procedural
# just functions, and a global variable to hold a running total

total = 0

def add(num):
    global total
    total += num

def sub(num):
    global total
    total -= num

def mul(num):
    global total
    total *= num

def div(num):
    global total
    if num != 0:
        total /= num

def equals():
    global total
    #take a snapshot of current total
    #reset total to zero
    #return snapshot
    snapshot_total = total
    total = 0
    return snapshot_total

# add(2) #unit test
# print(total)#expected: 2 got: 2
# div(0)#ZeroDivisionError: division by zero
# print(total)
add(2)
mul(2)
print(equals())

add(2)
print(equals())