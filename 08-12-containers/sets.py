'''
sets are mutable, unordered containers that do not permit duplicates
as such, they are often used for converting lists with duplicates into lists with unique values
moreover, they have utility methods for comparing between sets, useful for data science
'''

# creation
unique_nums = {44,55,66,44,55,66}
print(unique_nums)#{66, 44, 55}
# unique_nums2 = set(44,55,66,44,55,66)#TypeError: set expected at most 1 argument, got 6
unique_nums2 = set({44,55,66,44,55,66})#works: one arg is a set
unique_nums3 = set([44,55,66,44,55,66])#works: one arg is a set
unique_nums4 = set((44,55,66,44,55,66))#works: one arg is a set
# sets do NOT convert from dicts

# most common-useful use case: convert from list and back again to remove duplicates in a list
nums = [44,55,66,44,55,66]
unique_nums5 = set(nums)
unique_nums5_as_list = list(unique_nums5)

# comparing sets (very powerful in data sci)
unique_nums6 = {55,66,33,22,11}
print(common_values := unique_nums.intersection(unique_nums6))#reflexive {66, 55}
print(different_values := unique_nums.difference(unique_nums6))#non-reflexive {44}
print(different_values := unique_nums6.difference(unique_nums))#non-reflexive {33, 11, 22}
print(different_values := unique_nums.symmetric_difference(unique_nums6))# reflexive {33, 22, 11, 44}
print(different_values := unique_nums6.symmetric_difference(unique_nums))#{33, 11, 44, 22}
