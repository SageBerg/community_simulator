'''
community_simulator.py
the main program

Sage Berg, Erica Johnson, Skyler Berg
Created 25 May  2014
'''

from person_class import Person, print_fathers
from disasters import *
from queue import PriorityQueue
from items import *

person_list = list()
single_male_set = set()
single_female_set = set()
family = dict()
plow_market = PriorityQueue()
house_list = list()

def main():
    for i in range(1000):
        person_list.append(Person())
    for person in person_list:
        person.age = 10
        person.food = 5
        house = House()
        person.owns['house'] = [ house ]
        person.home_address = person.owns['house'][0]
        house.occupants.append(person)
        house_list.append(house)

    famine_flag = False
    for i in range(200):  #the number of years
        plague(person_list)
        if famine_flag == False:
            famine_flag = famine(person_list)
        global_decay()
        destruction()
        death()
        age()
        birth()
        marriage()
        work()
        eat()
        if famine_flag: 
            famine_flag = end_famine_maybe(person_list)
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
        s += len(person.children)
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
  #   for house in house_list:
#         print("~~~~~~~~~~~~~~~~~~~~~~~ house occupants:")
#         for person in house.occupants:
#             print(person.name + ' age: ' + str(person.age))
#             print("MORALITY: " + str(person.morality))

def decay(item):
    item.durability -= randint(0,5)

def global_decay(): #calls decay on lists of items
    global house_list
    for house in house_list:
        decay(house)

def destruction():
    global house_list
    for house in house_list:
        if house.durability <= 0:
            house_list.remove(house)
            #print('a house fell victim to time and neglect')
            for person in house.occupants:
                print(person.name)
    for person in person_list:
        for item_list in person.owns.values():
            for item in item_list:
            	if item.durability <= 0:
            	    item_list.remove(item) 
            	    #print(person.name + '\'s house blew up!!!!!!!!!!!!!')
            
def death():
    global house_list
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
    for house in house_list: #remove dead people from houses
        for person in house.occupants:
            if person.alive == False:
                house.occupants.remove(person)
        
def age():
    for person in person_list:
        person.age += 1
        
def birth():
    for person in person_list:
        baby = person.give_birth_chance()
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
