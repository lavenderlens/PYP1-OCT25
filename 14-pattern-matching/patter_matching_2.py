'''
let's try matching valid NINO numbers
these are a lot more uniform and predictable than email addresses, postodes etc

a NINO has three parts
TWO uppercase letters
SIX digits
ONE uppercase letter

eg.
AB123456C
'''
import re

nino_pattern = '([A-Z]{2})([0-9]{6})([A-Z]{1})'

while True:
    nino = input("Enter a candidate NINO to test, or 0 to quit")
    if nino == "0":
        break
    matches = re.findall(nino_pattern, nino)
    if matches:
        print(matches)
    else:
        print("not valid")
