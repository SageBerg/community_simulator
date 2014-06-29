'''
person_class.py
the core unit of the community simulator 
each person has attributes that help them make important decisions 

Sage Berg, Erica Johnson, Skyler Berg
Created 25 May 2014
'''

from random       import *
from female_first import *
from male_first   import *
from last         import *
from death_dict   import *
from items        import *

class Person(object):

    @staticmethod
    def last_name_gen():
        return choice(last_list)
        
    def __init__(self):
        self.gender     = self.gender_gen()
        self.first_name = self.first_name_gen() 
        self.last_name  = Person.last_name_gen() 
        self.name       = self.first_name + ' ' + self.last_name
        self.age        = 0
        
        #RELATIONS
        #self.relation_to_authority
        #self.relations
        #self.boss
        #self.servants
        self.mother   = None
        self.father   = None
        self.spouse   = None
        self.children = list()

        #passive traits
        self.alive = True

        self.pride        = None
        self.morality     = None
        self.intelligence = None
        self.extravagance = None
        self.creativity   = None
        self.pride        = self.attribute_gen(self.pride)
        self.morality     = self.attribute_gen(self.morality)
        self.intelligence = self.attribute_gen(self.intelligence)
        self.extravagance = self.attribute_gen(self.extravagance)
        self.creativity   = self.attribute_gen(self.creativity)

        #skills
        self.job = self.farm #self.job = function
        self.price = randint(5,9) 
        self.farm_skill = 5 
        #self.fight
        #self.persuasion
        #self.parenting
       
        #OWNERSHIP
        self.food = 0 #food is used as currency for now
        self.home_address = None
        self.owns = dict() 
        self.plow_listings  = 0
        self.house_listings = 0
        #self.wealth = 0

    def __str__(self):
        string = self.name  + ' (' + str(self.age) + ')\n' 
        if self.home_address:
            string += 'of ' + str(self.home_address) + '\n'
        if self.spouse:
            string += 'married to ' + self.spouse.name + ' (' + str(self.spouse.age) + ')\n' 
        if self.alive == False:
            string += 'IS DEAD'
        return string  
        
    def gender_gen(self):
        return choice(['female', 'male'])        
         
    def first_name_gen(self): 
        if self.gender == 'female':
           return choice(female_first_list)
        return choice(male_first_list)

    def attribute_gen(self, attribute):
        stat = 0
        if self.mother != None:
            stat += round((self.mother.attribute + self.father.attribute) / 2, 0)
        for i in range(10):
            stat += randint(-10, 10)
        return stat

    def set_price(self):
        if self.job == self.make_plow and self.plow_listings == 0:
            self.price += 1
        elif self.job == self.make_plow and self.plow_listings > 0:
            self.price -= 1
        if self.job == self.make_house and self.house_listings == 0:
            self.price += 1
        elif self.job == self.make_house and self.house_listings > 0:
            self.price -= 1
        if self.price < len(self.children) + 1:
            self.price = len(self.children) + 1

    def death_chance(self): #death from old age, sickness, and accidents
        if randint(0,100) <= death_dict[self.age]*100: 
            self.alive = False
        if self.home_address == None and randint(0,9):
            self.alive = False
            #print(str(self) + 'died of exposure')

    def give_birth_chance(self):
        if self.gender == 'female' and self.age > 15 and self.age <= 55 and self.spouse and self.spouse.alive:
            if randint(-60, 60) > self.age:
                baby = Person()
                self.children.append(baby)
                self.spouse.children.append(baby)
                baby.mother = self
                baby.father = self.spouse
                baby.last_name = self.last_name
                baby.name = baby.first_name + ' ' + baby.last_name
                baby.home_address = self.home_address
                if self.home_address != None:
                    self.home_address.occupants.append(baby)
                #print(baby.name + " was born to " + self.name + " and " + self.spouse.name)
                
                if self.home_address:
                    if self.home_address.occupants != self.spouse.home_address.occupants:
                        raise NameError('parents not living in same house')
                    if self.home_address.occupants != baby.home_address.occupants:
                        raise NameError('baby didn\'t come home')

                return baby
    
    def marriage(self, singles):
        for potential_mate in singles:
            if potential_mate.last_name != self.last_name:
                if potential_mate.gender == 'female':
                    bride = potential_mate
                    groom = self
                else:
                    bride = self
                    groom = potential_mate
                #print(bride.name + ' (' + str(bride.age) + ') married ' + \
                #      groom.name + ' (' + str(groom.age) + ')!!!')
                bride.spouse = groom
                groom.spouse = bride
                bride.last_name = groom.last_name
                bride.name = bride.first_name + ' ' + bride.last_name
                #print('bride home_address occupants: ' + str(bride.home_address.occupants))
                if groom.home_address != None and bride.home_address != None:
                    bride.home_address.occupants.remove(bride)
                    bride.home_address = groom.home_address
                    groom.home_address.occupants.append(bride)
                    #print(bride.name + ' (' + str(bride.age) + ') married ' + \
                    #      groom.name + ' (' + str(groom.age) + ') and she moved to his house')
                    #print()
                elif groom.home_address != None and bride.home_address == None:
                    bride.home_address = groom.home_address
                    groom.home_address.occupants.append(bride)
                    #print(bride.name + ' (' + str(bride.age) + ') married ' + \
                    #      groom.name + ' (' + str(groom.age) + ') and she moved off the streets')
                    #print()
                elif groom.home_address == None and bride.home_address != None:
                    groom.home_address = bride.home_address
                    bride.home_address.occupants.append(groom)
                    #print(bride.name + ' (' + str(bride.age) + ') married ' + \
                    #      groom.name + ' (' + str(groom.age) + ') and he moved off the streets')
                    #print()
                else:
                    #print(bride.name + ' ' + groom.name + ' got married in the streets')
                    pass

                if groom.home_address != bride.home_address:
                    raise NameError('bride and groom didn\'t go home to the same house')
                if groom.home_address:
                    if groom.home_address.occupants != bride.home_address.occupants:
                        raise NameError('occupants list not equal after wedding')

                singles.remove(potential_mate)
                break

    def farm(self, economy):
        production = self.farm_skill
        if 'plow' in self.owns:
            production += randint(0, 2)
        self.food += randint(0, production)

    def make_plow(self, economy):
        for i in range( randint(1, 2) ):
            economy['plow_market'].put( (self.price, id(self), self) ) #make listing
            self.plow_listings += 1

    def make_house(self, economy):
        #TO DO: have carpenters and their families move into the first house they make
        for i in range(randint(1,1)):
            economy['house_market'].put( (self.price, id(self), self) ) #make listing
            self.house_listings += 1
            
    def change_job(self, economy):
        '''economy is a dictionary mapping "market" strings to priority queues
           returns a self.job function which is assigned to self in community_simulator.py
        '''
        market_job_dict = {
        'plow_market':  self.make_plow,
        'house_market': self.make_house,
        }
       
        rand_job_list = list()
        for market in economy.keys():
            rand_job_list.append(market) 
        shuffle(rand_job_list)
        for market in rand_job_list:
            if economy[market].empty(): #at least one person will always try each job
                #print(self.name + ' started a ' + market + '. Price: ' + str(self.price))
                return market_job_dict[market]
            elif economy[market].queue[0][0] > self.price:
                #print(self.name + ' joined the ' + market)
                return market_job_dict[market]
        #print(self.name + ' BECAME a farmer')
        return self.farm #people farm if they don't have other good options

    def spend(self, economy, year):
        if self.home_address == None:
            if self.spouse:
                if self.spouse.home_address:
                    print()
                    print('the offender is:')
                    print(self)
                    raise NameError('the spouse (' + self.spouse.name + ') had a house and wasn\'t sharing')
            self.buy_house(economy, year)
        if self.job == self.farm:
            self.buy_plow(economy)
            
    def buy_house(self, economy, year):
        if economy['house_market'].qsize() > 0 and \
        self.food > economy['house_market'].queue[0][0]:
            listing = economy['house_market'].get()
            price = listing[0]
            seller = listing[2] 
            self.food -= price 
            seller.food += price #give seller food payment
            seller.house_listings -= 1
            house = House(seller.name, year) 
            self.owns['house'] = [ house ]
            #print(self.name + ' bought a house from ' + seller.name + ' %%% %%%')
            self.home_address = house
            self.home_address.occupants.append(self)

            if self.spouse:
                self.spouse.home_address = house
                house.occupants.append(self.spouse)

                if self.home_address != self.spouse.home_address:
                    raise NameError('they didn\'t move in together')

            #for child in self.children:
            #    child.home_address = house
            #    house.occupants.append(child)
    
    def buy_plow(self, economy):
        if 'plow' not in self.owns and \
        economy['plow_market'].qsize() > 0 and \
        self.food > economy['plow_market'].queue[0][0] and \
        economy['plow_market'].queue[0][2].plow_listings > 0:
            listing = economy['plow_market'].get()
            price  = listing[0]
            seller = listing[2]
            self.food -= price 
            seller.food += price 
            seller.house_listings -= 1
            self.owns['plow'] = [ Plow() ] #uncommon index error to FIX
            #seller.owns['plow'].remove(seller.owns['plow'][-1])
            #print(self.name + ' bought a plow!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            
    def eat(self):
        if self.age < 10:
            if self.father.food > 0:
                self.father.food -= 1
            elif self.mother.food > 0:
                self.mother.food -= 1
            else:
                self.alive = False
#                print('baby ' + self.name + ' starved to death at age ' + str(self.age))
        else:
            if self.food > 0:
                self.food -= 1
            elif self.food == 0 and self.spouse != None and self.spouse.food > 1:
                self.spouse.food -= 1
            else: 
                self.alive = False
                #print(self.name + ' starved to death 0X')

def print_fathers(person):
    while person:
        print(person.name)
        person = person.father
