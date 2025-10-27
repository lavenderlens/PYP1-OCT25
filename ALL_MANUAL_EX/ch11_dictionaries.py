# SEE MANUAL PAGE 186
# NOTE this exercise requires the get() method of dict
# where passing a key will return a value

accounts = {
    1234: {
        #inner indent doesn't seem to matter
        "number": 1234,
        "name": "Smith",
        "balance": 500.0
    },
    2345: {
        "number": 2345,
        "name": "Jones",
        "balance": -150.0
    },
    3456: {
        "number": 3456,
        "name": "Wilson",
        "balance": 2000.0
    },
    4567: {
        "number": 4567,
        "name": "Thompson",
        "balance": 275.0
    },
    5678: {
        "number": 5678,
        "name": "Davis",
        "balance": 100.0
    }
}
# print(accounts) #check indents

while True:
    acc_num = int(input("Enter an account number"))
    acc = accounts.get(acc_num) #OR
    # acc = accounts[acc_num] 
    if acc is not None:
        # YOU ABSOLUTELY CANNOT DO THIS:
        # print(f'{acc.number}: balance €{acc.balance}')
        print(f'{acc["number"]}: balance €{acc["balance"]}')
    else:
        print('Account not found')
    # print(accounts[acc_num]) #testing
    # print(acc) #testing
    more = input("Enter y to search another account, n to stop")
    if more.casefold() == 'n':
        break

# sorted_accounts = sorted(accounts, key=lambda a : a["name"])
# sorted_accounts = sorted(accounts, reverse=True)# gives list of ints not objects
# sorted_accounts = sorted(accounts.values(), key=lambda account: account["name"])
sorted_accounts = sorted(accounts.values(), key=lambda account: account["number"], reverse=True)#phew!
# print(sorted_accounts)#testing
# for accountNum in sorted_accounts:
#     print(f'{accounts[accountNum]["number"]}, {accounts[accountNum]["name"]}, €{accounts[accountNum]["balance"]}')
for account in sorted_accounts:
    print(account)
# testing
# print(accounts[1234]["name"])#Smith