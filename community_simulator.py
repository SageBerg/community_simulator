'''
community_simulator.py
the main program

Sage Berg
Created 25 May 2014
'''

from person_class import person

def main(person):
    person_list = list()
    for i in range(10):
        person_list.append(person())
    for person in person_list:
        print(person.name)

main(person)

