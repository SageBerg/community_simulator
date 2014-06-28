'''
house_class.py

Sage Berg, Erica Johnson
Created 23 June 2014
'''

class House(object):
    
    def __init__(self, creator='Johnson-Berg', year_sold=0):
        self.durability = 100
        self.occupants = list()

    def __str__(self):
        return creator.name + ' ' + str(year_sold)
        
