from item import Item

item1 = Item("MyItem", 750)

# Setting an Attribute
item1.name = "OtherItem"
item1.__price= 900
# Getting an Attribute
print(item1.name)
print(item1.__price)
