def get_next_lexical_num():
    next_num = 3001#lexically-scoped
    def get_next_num():
        nonlocal next_num
        next_num += 1
        return next_num
    return get_next_num
my_closure = get_next_lexical_num()
print(my_closure())
print(my_closure())
print(my_closure())
my_closure = get_next_lexical_num()
print(my_closure())
print(my_closure())
print(my_closure())
