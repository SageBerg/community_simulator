'''
person_class.py
the core unit of the community simulator 
each person has attritutes that help them make important decisions 

Sage Berg, Erica Johnson
Creaded 25 May  2014
Edited  08 June 2014
'''

from random import *
from female_first import *
from male_first import *
from last import *

class Person():

    def __init__(self):
        self.gender = self.gender_gen()
        self.name = self.name_gen() 
        self.age = 0

        #passive traits
        #self.alive = True
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

    def death_chance(self):
        if ranint(0,29) == 0:
            return True
        return False

    def give_birth_chance(self):
        if self.gender == 'female' and self.age > 12 and self.age <= 55:
            if randint(0,4) == 0:
                return Person()

    def gender_gen(self):
        return choice(['female', 'male'])        
         
    def name_gen(self): 
        if self.gender == 'female':
           return choice(female_first_list) + " " + choice(last_list)
        return choice(male_first_list) + " " + choice(last_list)
