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

class community(object):
    
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

    def bring_out_your_dead(self):
        for person in person_list:
            if person.alive == False:
                self.person_list.remove(person)
                self.inheritance(person)
                person.divorce() #can't be married to the dead

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
