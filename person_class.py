'''
person_class.py
the core unit of the economy simulator 
each person has attritutes that help them make important decisions 

Sage Berg
Creaded 25 May 2014
'''

from random import *
from female_first import *
from male_first import *
from last import *

class person():

    def __init__(self):
        #self.gender = self.gender_gen()
        self.name = self.name_gen() 
        self.age = 0

        #passive traits
        self.alive = True
        #self.pride
        #self.morality
        #self.intelligence
        #self.extravagance
        #self.creativity

        #skills
        #self.persuation
        #self.farming
        #self.parenting
        #self.fight
       
        #OWNERSHIP
        #self.home_address 
        #self.wealth = 0
        #self.owns = dict() 

        #RELATIONS
        #self.relation_to_authority
        #self.relations
        #self.boss
        #self.servants
        #self.spouse
        #self.children
        #self.mother
        #self.father
         
    def name_gen(self): 
        return choice(female_first_list) 
