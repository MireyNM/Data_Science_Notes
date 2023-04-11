from item import Item

item1 = Item("MyItem", 750)

# Setting an Attribute
item1.name = "OtherItem"
item1.__price= 900
# Getting an Attribute
print(item1.name)
print(item1.price)

item1.apply_increment(0.2)
print(item1.price)

item1.apply_discount()
print(item1.price)

# Abstraction = Acess calling methods (connect, prepare body..) from the instance 
# item1.send_email()

# Child Class Phone (Inheritance)
from phone import Phone 
item2 = Phone('jscPhone', 1000,3)
item2.apply_increment(0.2)
print(item2.price)

from keyboard import Keyboard 
item3 = Keyboard('iphone', 1000,2)
item3.apply_discount()
print(item3.price)

