'''
community_simulator.py
the main program

Sage Berg, Erica Johnson
Created 25 May  2014
Edited  08 June 2014
'''

from person_class import Person

def main():
    person_list = list()
    for i in range(15):
        person_list.append(Person())
    for person in person_list:
        print(person.name)
        
def time():
    for person in person_list:
        if Person.death_chance() == True:
            person_list.remove(person)
        person.age += 1


main(person)

