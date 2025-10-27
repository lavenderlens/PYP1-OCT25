'''
Pattern matching is the testing of a string to determine if it matches some pattern of characters
For example, an email address follows a pattern: 
n chars followed by @ followed by n chars followed by . etc.
Pattern matching is often used for validation but also for parsing data
A regular expression (regex) is a series of special characters that describes the pattern
There are many online tools to help you build patterns, e.g. regex101.com and regexr.com
The re module in the standard library may be used to do pattern matching
A bunch of signifiers are available to help construct regular expressions
They are super-specific eg.
w means ANY word series of characters
W means ANYTHING OTHER THAN a word series of characters
d means ANY digit character
D means ANYTHING OTHER THAN a digit characters
'''
file_contents = """
1234 Credit:
David Smith,500.0
2345 Debit:
Sarah Jones,-150.0
3456 Credit:
Tom Wilson,2000.0
4567 Savings:
Jane M Thompson,275.0
5678 Debit:
Simon Davis,100.0
"""
# suppose we want to parse this string data and make Python dictionaries of every 2 rows:
# re module will help us do this
# dicts are to have 3 props: number, name (SURNAME only, UPPER CASED), balance
# IGNORE credit/debit status
# IGNORE first name

# P 238 PDF

import re
accounts = {}
print(type(accounts))
pattern = '(\d{4}).+\n.+\s(.+),(.+)'
matches = re.findall(pattern, file_contents)
print(matches)#testing

for tpl in matches:
    acc_num = int(tpl[0])
    acc_name = tpl[1].upper()
    acc_balance = float(tpl[2])
    # make a dictionary for each entry
    accounts[acc_num] = {
        "number": acc_num,
        "name": acc_name,
        "balance": acc_balance,
    }
# print(accounts)
for key in accounts:
    print(key, accounts[key])