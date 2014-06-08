'''
community_simulator.py
the main program

Sage Berg, Erica Johnson
Created 25 May  2014
Edited  08 June 2014
'''

from person_class import Person

person_list = list()

def main():
    for i in range(100):
        person_list.append(Person())
    for person in person_list:
        print(person.name)
    for i in range(1000):
        time()
    for person in person_list:
        print(person.name + '(' + str(person.age) + ') still lives.')
    print(len(person_list))

def time():
    for person in person_list:
        if person.death_chance() == True:
            print(person.name + ' died at age: ' + str(person.age))
            person_list.remove(person)
        person.age += 1
        baby = person.give_birth_chance(person.last_name)
        if baby:
            person_list.append(baby)
            print(baby.name + ' was born to ' + person.name + '!')
main()
