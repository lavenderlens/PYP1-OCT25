from calculator_procedural import add, sub, mul, div, equals
# from calculator_oo import Calculator
from calculator_oo_refactored import Calculator

add(5)
sub(2)
mul(3)
div(9)
#expect 1.0
print(equals())#1.0

c = Calculator()
c.add(5)
c.sub(2)
c.mul(3)
c.div(9)
print(c.equals())

d = Calculator()
d.add(15)
d.sub(12)
d.mul(13)
d.div(19)
print(d.equals())