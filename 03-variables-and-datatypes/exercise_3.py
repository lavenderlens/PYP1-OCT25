# Built-in data types
# In this exercise you will create a script comprising airline passenger information. You
# must choose the most appropriate data type for each item of data. In practice, it is
# unlikely that you will hard-code data into a script in this manner, but the purpose of the
# exercise is to make you familiar with the built-in data types at your disposal. Don't forget
# about Python's naming conventions.
# 1. Create a script named ch3_data_types.py.
# 2. Declare and assign one variable for each of the items of data tabled below.

# Description             Value
# ID                      1234
# First name              John
# Last name               Doe
# Checked bags            False
# Visited countries       Latvia, Guyana, Yemen, Uzbekistan
# Flight                  LGW to CDG
# Flight time             1 hour 15 minutes

id = 1234
first_name = "John"
last_name = "Doe"
checked_bags = False
visited_countries = "Latvia, Guyana, Yemen, Uzbekistan"
visited_countries = ["Latvia", "Guyana", "Yemen", "Uzbekistan"]
no_of_visited_countries = len(visited_countries)
visited_countries.append("USA")
flight = {"dep": "LGW", "arr": "CDG"}
flight_time = 75
flight_time = 1.25
flight_time = {"hours": 1, "mins": 15}

# why not relate ALL pax info in one dictionary?
passenger1 = {
    "id":1234,
    "first_name":"John",
    "last_name":"Doe",
    "checked_bags":False,
    "visited_countries":["Latvia", "Guyana", "Yemen", "Uzbekistan"],
    "flight":{"dep": "LGW", "arr": "CDG"},
    "flight_time":{"hours": 1, "mins": 15}
}
print(passenger1)
