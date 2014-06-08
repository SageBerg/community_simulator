'''
community_simulator.py
the main program

Sage Berg, Erica Johnson
Created 25 May  2014
Edited  08 June 2014
'''

from person_class import person

def main(person):
    person_list = list()
    for i in range(15):
        person_list.append(person())
    for person in person_list:
        print(person.name)

main(person)

