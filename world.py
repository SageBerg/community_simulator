'''
Sage Berg, Erica Johnson
Created 5 July 2014
'''

from sys     import argv
from tkinter import *
from items   import *
from person_class    import *
from community_class import *
from government      import *
from disasters       import *

class World(object):
    
    def __init__(self):
        self.year        = 0
        self.hexgrid     = list() 
        self.governments = list()
        self.communities = list()

    def time(self, years):
        for year in range(years):
            self.print_news()
            for community in self.communities:
                plague(community.person_list)
            for community in self.communities:
                fire(community.house_list)
            for community in self.communities:
                if community.persisting_famine == True:
                    community.persisting_famine = famine(community.person_list)
            self.community_act(community.exposure)
            for community in self.communities:
                community.death()
            for community in self.communities:
                community.bring_out_your_dead()
            for community in self.communities:
                community.destruction()
            for community in self.communities:
                community.leave_ruined_house
            for community in self.communities:
                community.update_house_list
            for community in self.communities:
                community.courtship()
            self.year += 1
            
#         plague_death_count = plague(person_list)
#         if plague_death_count:
#             cause_of_death_dict['plague'] += plague_death_count
#         fire(house_list)
#         if famine_flag == False:
#             famine_flag = famine(person_list)
# #        global_decay()
#         exposure()
#         death()             #kills and removes people from lists
#         destruction()       #decays and removes items
#         house_list = update_house_list() #adds new houses
#         age()               #increments everyone's age
#         birth()
#         search_for_spouse()
#         work()

    def print_news(self):
        print()
        print('------- year ' + str(self.year) + ' -------')
        
    def community_act(self, function):     #optional argument arg?
        for community in self.communities:
            function()

def main():
    '''
    usage: $ python3 world.py 1000 200
    in this example: simulation starts with 1000 initial people
    in this example: simulation runs for 200 years
    '''
    if len(argv) < 3:
        raise NameError('USAGE: $ python3 world.py 1000 200')
    world = World()
    world.communities.append( Community() )
    for i in range( int(argv[1]) ):
        world.communities[0].person_list.append(Person())
    for person in world.communities[0].person_list:
        person.age  = 10 
        person.food = 5
        house = House()
        person.owns[House] = [ house ]
        person.move_family_into_house()
        world.communities[0].house_list.append(house)
    world.time( int(argv[2]) )

if __name__ == "__main__":
    main()
