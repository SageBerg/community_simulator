'''
person_class.py
the core unit of the community simulator 
each person has attributes that help them make important decisions 

Sage Berg, Erica Johnson, Skyler Berg
Created 25 May  2014
Edited  12 June 2014
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

    def __init__(self, last_name=None, mother=None, father=None):
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
        self.job #= function 
        #self.persuasion
        self.farm_skill = 5
        #self.parenting
        #self.fight
       
        #OWNERSHIP
        self.food = 0
        #self.home_address 
        #self.wealth = 0
        self.owns = dict() 

        #RELATIONS
        #self.relation_to_authority
        #self.relations
        #self.boss
        #self.servants
        self.spouse = None
        #self.children =
        self.mother = mother
        self.father = father

    def death_chance(self): #death from old age and sickness
        if randint(0,100) <= death_dict[self.age]*100:
            self.alive = False

    def give_birth_chance(self, last_name):
        if self.gender == 'female' and self.age > 12 and self.age <= 55 and self.spouse and self.spouse.alive:
            if randint(0,100) < 33:
                baby = Person(last_name, mother=self, father=self.spouse)
                return baby
    
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
                #print(bride.name + ' married ' + groom.name + '!!!')
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

    def farm(self):
        production = self.farm_skill
        if 'plow' in self.owns:
            production += 2
        self.food += randint(0, production)

    def eat(self):
        if self.age < 10:
            if self.father.food > 0:
                self.father.food -= 1
            elif self.mother.food > 0:
                self.mother.food -= 1
            else:
                self.alive = False
                print('baby ' + self.name + ' starved to death at age ' + str(self.age))
        else:
            if self.food > 0:
                self.food -= 1
            elif self.food == 0 and self.spouse != None and self.spouse.food > 1:
                self.spouse.food -= 1
            else: 
                self.alive = False
                print(self.name + ' starved to death 0X')
    
    def buy_plow(self):
        if self.food > 14 and 'plow' not in self.owns:
            self.food -= 15
            self.owns['plow'] = 1
            #print(self.name + ' bought a plow!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            
    def make_plow(self):
        self.owns['plow'] = randint(1, 2)
        
    def change_job(self):
        

def print_fathers(person):
    while person:
        print(person.name)
        person = person.father