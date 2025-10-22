from functions_exercise_module import (get_greeting, 
get_greeting_to,
get_product,
get_first,
get_first_with_error_handling,
get_name,
get_circumference,
get_name_refactored)


print(get_greeting())
print(get_greeting_to("Alan"))
print(get_product(1,2))
my_list = [1,2,3]
print(get_first(my_list))
# my_list = [1,2,3] #not avail;able to function above
print(get_first([1,2,3]))
# print(get_first([]))#IndexError
print(get_first_with_error_handling([]))
# test_dict = {"name":"Alan", "age": 59}
test_dict = {"fname":"Alan", "age": 59}#no name key
# print(get_name(test_dict))
print(get_name_refactored(test_dict))
print(get_circumference(10))
print(f"{get_circumference(10):.2f}")
