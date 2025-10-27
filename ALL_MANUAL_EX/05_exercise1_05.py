# year_of_birth = int(input("What year were you born?"))
# OR, with pattern matching to validate input:
import re
year_of_birth = input("What year were you born? (enter numbers only in format yyyy)")
valid = re.findall("^[0-9][0-9][0-9][0-9]$", year_of_birth)
if valid:
    # could extract this to a function
    year_of_birth = int(year_of_birth)
    if year_of_birth >= 1946 and year_of_birth <= 1965:
        print("Baby Boomer!")
    elif year_of_birth >= 1966 and year_of_birth <= 1976:
        print("Gen X!")
    elif year_of_birth >= 1977 and year_of_birth <= 1994:
        print("Millenial!")
    elif year_of_birth >= 1995:
        print("Gen Z!")
else:
    print("Enter a valid year of birth in format yyyy")
