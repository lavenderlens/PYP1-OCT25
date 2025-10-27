'''
a dict is a mutable, unordered container of key: value pairs
keys must be unique, and, ideally, immutable (numbers or strings)
values may be duplicated
dicts are commonly used to represent complex data
and to facilitate sharing between different languages in any stack
eg. JavaScript > json > Python > json > Java

use a class where you want a uniform list of props and functions that modify those props
use a dict where you have a one-off scenario or props/data shape change
'''

# creation
book = {}
print(type(book))#class dict, amazingly!
book_as_set = {"book1", "book2"}
print(type(book_as_set))#class set!
book = dict()

# adding props after instantiation
book["title"] = "Scary Smart"
book["author"] = "Mo Gawdat"
book["published"] = 2019
print(book)

# other dict methods include
print(published_year := book.pop("published"))#mutates original, returns popped key
print(book)#{'title': 'Scary Smart', 'author': 'Mo Gawdat'}

# iterating
# keys (in the absence of any other method, a loop will access keys)
for key in book:
    print(key)

# values
for value in book.values():
    print(value)

# keys and values
for key, value in book.items():
    print(datatype := (key, value))#tuple
    print(type(datatype))
    
# using keys to access values
for key in book:
    print(f"{key}: {book[key]}")