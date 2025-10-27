# SEE MANUAL PAGE 207
# the exercise converts each line of a string into separate dictionaries
# NOTE this exercise solution uses the setdefault() method of dict in part 6-v.
# a_dictionary.setdefault(newkey, newvalue)
# same as a_dictionary["newkey"] = "newvalue" - use this if you prefer

file_contents = """\
1234,smith     ,500.0
2345,jones     ,-150.0
3456,wilson    ,2000.0
4567,thompson  ,275.0
5678,davis     ,100
"""

accounts = {}

lines = file_contents.split("\n")
# print(lines)#testing
for line in lines:
    if line != "":
        parts = line.split(",")
        acc_num = int(parts[0])
        acc_name = parts[1].strip().title()
        acc_balance = float(parts[2])
        # accounts.setdefault(acc_num, {
        #     "number": acc_num, 
        #     "name": acc_name, 
        #     "balance": acc_balance})
        accounts[acc_num] = {
            "number": acc_num, 
            "name": acc_name, 
            "balance": acc_balance}
# print(accounts)#testing
for account in accounts.values():
    print(account)