import re

file_contents = """
1234 Credit:
David Smith,500.0
2345 Debit:
Sarah Jones,-150.0
3456 Credit:
Tom Wilson,2000.0
4567 Savings:
Jane Thompson,275.0
5678 Debit:
Simon Davis,100.0
"""
accounts = {}
pattern = '(\d{4}).+\n.+\s(.+),(.+)'
matches = re.findall(pattern, file_contents)
for num, name, bal in matches:
    print(num, name, bal)
print(matches)#testing
for tpl in matches:
    acc_num = int(tpl[0])
    acc_name = tpl[1]
    acc_balance = float(tpl[2])
    accounts.setdefault(acc_num, {
            "number": acc_num, 
            "name": acc_name, 
            "balance": acc_balance})

# 11. refactored with automatic tuple unpacking in the for loop
# for tpl in matches:
#     accounts.setdefault(int(tpl[0]), {
#             "number": int(tpl[0]), 
#             "name": tpl[1], 
#             "balance": float(tpl[2])})

for account in accounts.values():
    print(account)
    
# print(type(matches))#testing