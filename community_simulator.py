'''
community_simulator.py
the main program

Sage Berg, Erica Johnson, Skyler Berg
Created 25 May  2014
'''

from person_class import Person, print_fathers
from disasters import *
from queue import PriorityQueue

person_list = list()
single_male_set = set()
single_female_set = set()
family = dict()
plow_market = PriorityQueue()

def main():
    for i in range(700):
        person_list.append(Person())
    for person in person_list:
        person.age = 10
        person.food = 5
    for i in range(1000):  #the number of years
        plague(person_list)
        death()
        time()
        birth()
        marriage()
        work()
        eat()
        print('year ' + str(i))
        print('there are ' + str(len(person_list)) + ' people alive')
    for person in person_list:
        if person.last_name in family:
            family[person.last_name] += 1
        else:
            family[person.last_name] = 1
        #print(person.name + '(' + str(person.age) + ') still lives.')
        #print_fathers(person)
        #print()
    for name in family:
        print(name, family[name])
    print(len(person_list))
    s = 0
    for person in person_list:
        s += person.children 
    print('average children: ' + str(round(s/(len(person_list)+1), 2)))
    farmers = 0
    plowrights = 0
    for person in person_list:
        if person.job == person.farm:
            farmers += 1
        else:
            plowrights += 1
    print('number of farmers: ' + str(farmers))
    print('number of plowrights: ' + str(plowrights))

def death():
    global plow_market
    for person in person_list:
        person.death_chance()
        if person.alive == False:
            #print(person.name + ' died at age: ' + str(person.age))
            person_list.remove(person)
    new_plow_market = PriorityQueue()
    for i in range(plow_market.qsize()):
        seller = plow_market.get()
        if seller[2].alive:
            new_plow_market.put(seller)
    plow_market = new_plow_market
        
def time():
    for person in person_list:
        person.age += 1
        
def birth():
    for person in person_list:
        baby = person.give_birth_chance(person.last_name)
        if baby:
            person_list.append(baby)
            #print(baby.name + ' was born to ' + person.name + '!')

def marriage():
    global single_male_set
    global single_female_set
    for person in person_list:
        if person.spouse == None and person.age >= 10:
            if person.gender == 'male':
                single_male_set.add(person)
            else:
                single_female_set.add(person)
    single_male_set = {male for male in single_male_set if male.alive}
    single_female_set = {female for female in single_female_set if female.alive}
    #print("          single male length: " + str(len(single_male_set)))
    for male in single_male_set:
        male.search_for_spouse(single_female_set)
        #print("               " + male.name)
    #print("          single female length: " + str(len(single_female_set)))
    for female in single_female_set:
        female.search_for_spouse(single_male_set)
        #print("               " + female.name)

def work():
    for person in person_list:
        if person.age >= 10:
            if person.job == person.farm:
                person.change_job(plow_market)
            person.job(plow_market)

def eat():
    for person in person_list:
        person.eat()
    
main()
