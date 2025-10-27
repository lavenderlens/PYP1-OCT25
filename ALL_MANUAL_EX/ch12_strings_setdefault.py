# SEE STRINGS CH11 MANUAL EXERCISE

a_dict = {"key1": 1, "key2": 2}
a_dict.setdefault("key4", {"number": 1, "name": "alan"})
# same as
a_dict["key5"] = {"number": 2, "name": "fred"}
print(a_dict)