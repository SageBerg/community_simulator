'''
disasters.py
This file defines disaster functions that might befall the community
intended to be imported by community_simulator.py

Sage Berg, Erica Johnson, Skyler Berg
Created 12 June 2014
'''

from random import *

def plague(person_list):
    if randint(0, 100) == 0:
        death_threshold = randint(1, 50)
        for person in person_list:
            if randint(0, 100) < death_threshold:
                print(person.name + ' died of plague 0X 0X 0X 0X 0X.')
                person.alive = False

def famine(person_list):
    if randint(0,100) == 0:
        print('A FAMINE HAS STRUCK THE LAND............................')
        for person in person_list:
            person.farm_skill -= 5
        return True #used by famine flag
    return False # if there isn't a famine

def end_famine_maybe(person_list):
    if randint(0,2) == 1:
        print('THE FAMINE HAS ENDED')
        for person in person_list:
            person.farm_skill += 5
        return False
    return True

