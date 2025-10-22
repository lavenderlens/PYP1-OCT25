'''
a class is
a BLUEPRINT or TEMPLATE for
creating objects of a certain user-defined type
there exist many system classes such as str and list
when we create our own classes, however, we create our own types
you may choose classes over dictionaries to represent complex data
as every instance of the class will have 
the same fields (variables) and
the same methods (functions)
whereas if we used dictionaries, every usage has to be defined again
classes enforce standards applied by all objects of that class
they may also restrict direct access to state variables (data hiding/encapsulation)

also, classes may INHERIT from other classes
ensuring less code duplication
'''

class Client:
    pass

client = Client()
print(client)#<__main__.Client object at 0x100afe900> / <__main__.Client object at 0x104352900>

class Client:
    # constructor: specifies HOW to make the INITial object
    # instantiation: to make an instance of the class (an object)
    # objects, lists, sets, and dictionaries are the only MUTABLE data structures in Python
    def __init__(self):#the only dunder method we MUST implement
        self.name = "Client name"
        self.email = "Client email"
        self.dependents = []

client = Client()
print(client.name)
print(client.email)
print(client.dependents)
# setting fields
client.name = "Elon"
client.email = "musk@mars.space"
client.dependents.append("AEX11")
client.dependents.append("Grimes")
print(client.name)
print(client.email)
print(client.dependents)

for value in client.dependents:
    print(value)

clients = []#add multiple instances of clients

class Client:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.dependents = []

client1 = Client("elon", "musk@mars.space")
client2 = Client("Don", "potus@gov.mil")
client3 = Client("JD", "vance@hillbillyelegy.com")
clients.append(client1)
clients.append(client2)
clients.append(client3)
for client in clients:
    print(f"{client.name}, {client.email}")

class Client:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.dependents = []
    def add_dependent(self, name):
        if name not in self.dependents:
            self.dependents.append(name)
    def __str__(self):
        return f"{self.name}, {self.email}, {self.dependents}"
    
client1 = Client("elon", "musk@mars.space")
client1.add_dependent("AEX11")
client1.add_dependent("Grimes")
client2 = Client("Don", "potus@gov.mil")
client2.add_dependent("JD")
client2.add_dependent("Ivanka")
client2.add_dependent("Musk")
client3 = Client("JD", "vance@hillbillyelegy.com")
client3.add_dependent("Gramma")
clients = []
clients.append(client1)
clients.append(client2)
clients.append(client3)
for client in clients:
    print(f"{client.name}, {client.email}, {client.dependents}")

