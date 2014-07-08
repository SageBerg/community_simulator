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
                community.bring_out_your_dead
            for community in self.communities:
                community.courtship
            self.year += 1

    def print_news(self):
        print()
        print('------- year ' + str(self.year) + ' -------')

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
