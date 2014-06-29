'''
items.py

Sage Berg, Erica Johnson
Created 26 June 2014
'''

from item_superclass import Item

class Plow(Item):
    def __init__(self):
        Item.__init__(self)

class House(Item):
    def __init__(self, creator='Johnson-Berg', year=0):
        Item.__init__(self)
        self.occupants = list()
        self.creator = creator #person.name
        self.year = year

    def __str__(self):
        return 'House created by: ' + self.creator + \
        ' in year: ' + str(self.year) + \
        ' Durability: ' + str(self.durability) + \
        ' Occupants: ' + str(len(self.occupants))
