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

    def action(self, fuction):
        for person in self.person_list:
            person.function()

    def bring_out_your_dead(self):         #not done
        '''
        removes dead people
        '''
        for person in person_list:
            if person.alive == False:
                self.person_list.remove(person)
                self.inheritance(person)
                person.divorce() #can't be married to the dead
                person.remove_self_from_parents_children()
#                 person.home_address.occupants.remove(person)        #may cause errors
        for market in self.economy.keys():
            self.update_market(market)           #update_market not written yet
                
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
                
    def search_for_spouse(self):
        for person in self.person_list:
            if person.spouse == None and person.age >= 10:
                if person.gender == 'male':
                    self.single_male_set.add(person)
                else:
                    self.single_female_set.add(person)
        self.single_male_set   = {male   for male   in single_male_set   if male.alive   and male.spouse   == None}
        self.single_female_set = {female for female in single_female_set if female.alive and female.spouse == None}
        for male in self.single_male_set:
            male.marriage(self.single_female_set)
        self.single_male_set   = {male   for male   in single_male_set   if male.alive   and male.spouse 
        for female in self.single_female_set:
            female.marriage(single_male_set) #weird error female has no attribute marriage
        

def main(initial_population_size, years):
    com = Community()
    for i in range(initial_population_size):
        com.person_list.append(Person())
    for person in com.person_list:
        person.age  = 10 
        person.food = 5
        house = House()
        person.owns[House] = [ house ]
        person.move_family_into_house()
        house_list.append(house)
    for 
