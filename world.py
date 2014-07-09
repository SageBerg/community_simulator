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
            for community in self.communities:
                #assertions
                spouse_house_check(community.person_list)
                house_search(community.house_list, community.person_list)
                child_search(community.person_list)
                spouse_search(community.person_list)
                
                #disasters
                plague(community.person_list)
                fire(community.house_list)
                if community.persisting_famine:
                    community.persisting_famine = end_famine_maybe(community.person_list)
                if not community.persisting_famine:
                    community.persisting_famine = famine(community.person_list)
                
                #changes in government
                if community.government == None:
                    community.insurrection()
                if community.person_list and community.government.leader:
                    community.government.collect_taxes(community.person_list)
                    community.government.succession()
                if community.government.leader == None or \
                   community.government.leader.alive == False:
                    community.government == None
             
                self.community_act(community.exposure)
                self.community_act(community.death)
                self.community_act(community.bring_out_your_dead)
                self.community_act(community.destruction)
                self.community_act(community.leave_ruined_house)
                self.community_act(community.update_house_list)
                self.community_act(community.birth)
                self.community_act(community.age)
                self.community_act(community.courtship)
                self.community_act(community.work)
                self.community_act(community.shop)
                self.community_act(community.theft)
                self.community_act(community.set_prices)     
                self.community_act(community.nutrition)

            self.year += 1

            self.print_news()

    def print_news(self):
        print()
        print('------- year ' + str(self.year) + ' -------')
        for community in self.communities:
            print(community.name.ljust(15) + ' has ' + str(len(community.person_list)) + ' residents')
   
    def print_final_summary(self):
        for community in self.communities:
            self.print_family_sizes(community)
            self.print_occupations(community)
            print()
            print('The government of ' + community.name + ' has ' + str(community.government.food) + ' food.')

    def print_family_sizes(self, community):
            print()
            family = dict()
            for person in community.person_list:
                if person.last_name in family:
                    family[person.last_name] += 1
                else:
                    family[person.last_name] = 1
            tup_list = list()
            for group in family.keys():
                tup_list.append( (family[group], group) ) 
            tup_list.sort()
            for family in tup_list:
                print( family[1].ljust(15), family[0] )

    def print_occupations(self, community):
        farmers    = 0
        vinters    = 0
        plowrights = 0
        carpenters = 0
        for person in community.person_list:
            if person.alive:
                if person.job == person.farm:
                    farmers += 1
                elif person.job == person.make_house:
                    carpenters += 1
                elif person.job == person.make_wine:
                    vinters += 1
                else:
                    plowrights += 1
        print()
        print('number of farmers: '.ljust(25)    + str(farmers))
        print('number of vinters: '.ljust(25)    + str(vinters))
        print('number of plowrights: '.ljust(25) + str(plowrights))
        print('number of carpenters: '.ljust(25) + str(carpenters))

    def print_homelessness(self, community):
   
        homeless = 0
        for person in community.person_list:
            if person.home_address == None:
                homeless += 1
        print() 
        print('number of homeless: '.ljust(25) + str(homeless))

    def community_act(self, function):     #optional argument arg?
        for community in self.communities:
            function()

def main():
    '''
    usage: $ python3 world.py 1000 200 2
    in this example: simulation starts with 1000 initial people
                     simulation runs for 200 years
                     simulation starts with 2 communities
    '''
    if len(argv) < 3:
        raise NameError('USAGE: $ python3 world.py 1000 200 2')
    world = World()
    if len(argv) > 3:
        for i in range( int(argv[3]) ):
            world.communities.append( Community() )
    for community in world.communities:
        for i in range( int(argv[1]) ):
            community.person_list.append(Person())
        for person in community.person_list:
            person.age  = 10 
            person.food = 5
            house = House()
            person.owns[House] = [ house ]
            person.move_family_into_house()
            community.house_list.append(house)
    world.time( int(argv[2]) )
    world.print_final_summary()

if __name__ == "__main__":
    main()
