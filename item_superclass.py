'''
item_superclass.py

Sage Berg, Erica Johnson
Created 26 June 2014
'''

from random import *

class Item(object):
    
    def __init__(self):
        self.durability = 100
        
    def decay(self):           #override and pass for wine?
        self.durability -= randint(0,5)