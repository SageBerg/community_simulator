'''
person_class.py
the core unit of the community simulator 
each person has attritutes that help them make important decisions 

Sage Berg, Erica Johnson
Created 25 May  2014
Edited  09 June 2014
'''

from random import *
from female_first import *
from male_first import *
from last import *
from death_dict import *

class Person():

    @staticmethod
    def last_name_gen():
        return choice(last_list)

    def __init__(self, last_name=None):
        self.gender = self.gender_gen()
        self.first_name = self.first_name_gen() 
        if last_name == None:
            self.last_name = Person.last_name_gen() 
        else:
            self.last_name = last_name
        self.name = self.first_name + ' ' + self.last_name
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
        self.spouse = None
        #self.children
        #self.mother
        #self.father

    def death_chance(self):
        if randint(0,100) <= death_dict[self.age]*100:
            return True
        return False

    def give_birth_chance(self, last_name):
        if self.gender == 'female' and self.age > 12 and self.age <= 55 and self.spouse and self.spouse.alive:
            if randint(0,2) == 0:
                return Person(last_name)
    
    def search_for_spouse(self, singles):
        for potential_mate in (singles):
            #print(self.name + ' is looking for love')
            #print(len(singles))
            if potential_mate.last_name != self.last_name:
                if potential_mate.gender == 'female':
                    bride = potential_mate
                    groom = self
                else:
                    bride = self
                    groom = potential_mate
                print(bride.name + ' married ' + groom.name + '!!!')
                bride.spouse = groom
                groom.spouse = bride
                bride.last_name = groom.last_name
                bride.name = bride.first_name + ' ' + bride.last_name
                singles.remove(potential_mate)
                return

    def gender_gen(self):
        return choice(['female', 'male'])        
         
    def first_name_gen(self): 
        if self.gender == 'female':
           return choice(female_first_list)
        return choice(male_first_list)

