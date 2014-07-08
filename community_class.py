'''
Sage Berg, Erica Johnson
Created 25 May 2014
'''

from sys          import argv
from queue        import PriorityQueue
from person_class import Person, print_fathers
from disasters    import *
from items        import *
from error_checking_functions import *
from death_dict   import death_dict
from government   import *

class Community(object):
    
    def __init__(self):

        #self.name              = self.name_gen()
        #self.government        = None
        #self.location          = (0, 0)
        self.person_list       = list()
        self.single_male_set   = set()
        self.single_female_set = set()
        self.economy           = dict()
        self.house_list        = list()

        self.economy[Plow]  = PriorityQueue()
        self.economy[House] = PriorityQueue()
        self.economy[Wine]  = PriorityQueue()

    def bring_out_your_dead(self):         
        '''
        removes dead people
        '''
        for person in self.person_list:
            if person.alive == False:
                self.person_list.remove(person)
                self.inheritance(person)
                person.divorce() #can't be married to the dead
                person.remove_self_from_parents_children()
#                person.home_address.occupants.remove(person)        #may cause errors
        for market in self.economy.keys():
            self.update_market(market) 

    def death(self):
        for person in self.person_list:
            person.death_chance()

    def exposure():
        for person in self.person_list:
            person.death_by_exposure_chance()

    def nutrition(self):
        for person in self.person_list:
            person.eat(self.government)
    
    def age(self):
        for person in self.person_list:
            person.get_older()
    
    def birth(self):
        for person in self.person_list:
            baby = person.give_birth_chance()
        if baby:
            self.person_list.append(baby)

    def work(self):
        for person in self.person_list:
            if person.age >= 10:
                if person.food < 1: 
                    person.job = person.change_job(self.economy)
                person.job(self.economy)

    def spend(self):
        for person in self.person_list:
            person.spend(self.economy)

    def set_prices(self):
        for person in self.person_list:
            person.set_price()
        
    def theft(self):
        for person in self.person_list:
            person.steal(self.person_list)
            
    def destruction(self): 
        '''
        decays items and removes broken items
        '''      
        for person in self.person_list: #removes items that break
            for item_list in person.owns.values():
                for item in item_list:
                    item.decay()
                    if item.durability <= 0:
                        item_list.remove(item) 
                        
    def leave_ruined_house(self):
        for person in self.person_list:
            if person.home_address != None and person.home_address.durability <= 0:
                person.home_address.occupants.remove(person)
                person.home_address = None
                
    def courtship(self):
        for person in self.person_list:
            if person.spouse == None and person.age >= 10:
                if person.gender == 'male':
                    self.single_male_set.add(person)
                else:
                    self.single_female_set.add(person)
        self.single_male_set   = \
        {male   for male   in self.single_male_set   if male.alive   and male.spouse   == None}
        self.single_female_set = \
        {female for female in self.single_female_set if female.alive and female.spouse == None}
        for male in self.single_male_set:
            male.marriage(self.single_female_set)
        self.single_male_set   = \
        {male   for male   in self.single_male_set   if male.alive   and male.spouse   == None} 
        for female in self.single_female_set:
            self.female.marriage(self.single_male_set) 

    def update_house_list(self):
        new_house_list = list()
        for person in self.person_list:
            if person.home_address != None and person.home_address not in new_house_list:
                new_house_list.append(person.home_address)
        return new_house_list

    def update_market(self, market):
        new_market = PriorityQueue()
        for i in range(economy[market].qsize()):
            listing = economy[market].get()
            seller = listing[2]
            if seller.alive:
                new_market.put(listing)
        self.economy[market] = new_market
