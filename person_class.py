'''
person_class.py
the core unit of the community simulator 
each person has attributes that help them make important decisions 

Sage Berg, Erica Johnson, Skyler Berg
Created 25 May 2014
'''

from random import *
from female_first import *
from male_first import *
from last import *
from death_dict import *
from items import *

class Person(object):

    @staticmethod
    def last_name_gen():
        return choice(last_list)

    def __init__(self):
        self.gender = self.gender_gen()
        self.first_name = self.first_name_gen() 
        self.last_name = Person.last_name_gen() 
        self.name = self.first_name + ' ' + self.last_name
        self.age = 0
        
        #RELATIONS
        #self.relation_to_authority
        #self.relations
        #self.boss
        #self.servants
        self.spouse = None
        self.children = list()
        self.mother = None
        self.father = None

        #passive traits
        self.alive = True
        self.pride = None
        self.morality = None
        self.intelligence = None
        self.extravagance = None
        self.creativity = None
        self.pride = self.attribute_gen(self.pride)
        self.morality = self.attribute_gen(self.morality)
        self.intelligence = self.attribute_gen(self.intelligence)
        self.extravagance = self.attribute_gen(self.extravagance)
        self.creativity = self.attribute_gen(self.creativity)

        #skills
        self.job = self.farm #self.job = function
        self.price = self.set_price() 
        #self.persuasion
        self.farm_skill = 5 
        #self.parenting
        #self.fight
       
        #OWNERSHIP
        self.food = 0
        self.home_address = None
        #self.wealth = 0
        self.owns = dict() 
        

    def death_chance(self): #death from old age and sickness
        if randint(0,100) <= death_dict[self.age]*100:
            if len(self.children) > 0:
                for key in self.owns.keys():
                    if key not in self.children[0].owns:
                        self.children[0].owns[key] = self.owns[key]
                    else:
                        self.children[0].owns[key] += self.owns[key]
#                     if self.job == self.make_plow:
#                         try:
#                             print('plowright ' + self.name + ' died and left ' + \
#                             str(len(self.owns['plow'])) + ' plow(s) to the heir ' + self.children[0].name)
#                         except:
#                             print('plowright died with no plows')
#                     print(self.children[0].name + ' inherited ' + str(len(self.owns[key])) + ' ' + key + 's')
            try:
                self.mother.children.remove(self)
                self.father.children.remove(self)
            except:
                #print('initial people don\'t have parents') 
                pass
            self.alive = False

    def give_birth_chance(self):
        if self.gender == 'female' and self.age > 12 and self.age <= 55 and self.spouse and self.spouse.alive:
            if randint(0,100) < 33:
                baby = Person()
                self.children.append(baby)
                self.spouse.children.append(baby)
                baby.mother = self
                baby.father = self.spouse
                baby.last_name = self.last_name
                baby.name = baby.first_name + ' ' + baby.last_name
                baby.home_address = self.home_address
                self.home_address.occupants.append(baby)
                #print(baby.name + " was born to " + self.name + " and " + self.spouse.name)
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
#                 print('bride home_address occupants: ' + str(bride.home_address.occupants))
#                 for person in bride.home
                bride.home_address.occupants.remove(bride)
                bride.home_address = groom.home_address
                groom.home_address.occupants.append(bride)
                singles.remove(potential_mate)
                return

    def gender_gen(self):
        return choice(['female', 'male'])        
         
    def first_name_gen(self): 
        if self.gender == 'female':
           return choice(female_first_list)
        return choice(male_first_list)

    def farm(self, market):
        production = self.farm_skill
        if 'plow' in self.owns:
            production += 2
        self.food += randint(0, production)
        self.buy_plow(market)

    def eat(self):
        if self.age < 10:
            if self.father.food > 0:
                self.father.food -= 1
            elif self.mother.food > 0:
                self.mother.food -= 1
            else:
                self.alive = False
#                 print('baby ' + self.name + ' starved to death at age ' + str(self.age))
        else:
            if self.food > 0:
                self.food -= 1
            elif self.food == 0 and self.spouse != None and self.spouse.food > 1:
                self.spouse.food -= 1
            else: 
                self.alive = False
#                 print(self.name + ' starved to death 0X')
    
    def buy_plow(self, market):
        if self.food > market.queue[0][0] and 'plow' not in self.owns:
            seller = market.get()
            self.food -= seller[0] #the price 
            seller[2].food += seller[0] #give seller food payment
            if 'plow' in self.owns:
                self.owns['plow'].append( Plow() )
            else:
                self.owns['plow'] = [ Plow() ]
           # print(self.name + ' bought a plow!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            
    def make_plow(self, market):
        for i in range( randint(1, 2) ):
            market.put( (self.price, id(self), self) )
        
    def change_job(self, market):
        if market.empty():
            self.job = self.make_plow
#             print(self.name + ' was first to join the plow market. Price: ' + str(self.price))
        elif market.queue[0][0] > 5:
            self.job = self.make_plow
#             print(self.name + ' joined the plow market.')
    
    def set_price(self):
        return randint(3,10)
        
    def attribute_gen(self, attribute):
        stat = 0
        if self.mother != None:
            stat += round((self.mother.attribute + self.father.attribute) / 2, 0)
        for i in range(10):
            stat += randint(-10, 10)
        return stat
        

def print_fathers(person):
    while person:
        print(person.name)
        person = person.father
