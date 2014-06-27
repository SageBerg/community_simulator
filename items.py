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
    def __init__(self):
        Item.__init__(self)
        self.occupants = list()