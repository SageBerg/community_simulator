'''
community_simulator.py
the main program

Sage Berg, Erica Johnson
Created 25 May  2014
Edited  08 June 2014
'''

from person_class import Person

person_list = list()
single_male_set = set()
single_female_set = set()

def main():
    for i in range(10):
        person_list.append(Person())
#     for person in person_list:
#         print(person.name)
    for i in range(100):
        death()
        time()
        birth()
        marriage()
        print('year ' + str(i))
    for person in person_list:
        print(person.name + '(' + str(person.age) + ') still lives.')
    print(len(person_list))

def death():
    print('there are ' + str(len(person_list)) + ' people alive')
    for person in person_list:
        if person.death_chance() == True:
            print(person.name + ' died at age: ' + str(person.age))
            person.alive = False
            person_list.remove(person)
        
def time():
    for person in person_list:
        person.age += 1
        
def birth():
    for person in person_list:
        baby = person.give_birth_chance(person.last_name)
        if baby:
            person_list.append(baby)
            print(baby.name + ' was born to ' + person.name + '!')

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
    print("          single male length: " + str(len(single_male_set)))
    for male in single_male_set:
        print("               " + male.name)
    print("          single female length: " + str(len(single_female_set)))
    for female in single_female_set:
        print("               " + female.name)
#     for male in single_male_set:
#         male.search_for_spouse(single_female_set)
#     male_still_single = list()
#     female_still_single = list()
#     for i in range(len(single_male_set)):
#         if male.spouse == None:
#             male_still_single.append(male)
#     for female in single_female_set:
#         if female.spouse == None:
#             female_still_single.append(female)
#     single_male_set.clear()
#     single_female_set.clear()
#     for male in male_still_single:
#         single_male_set.add(male)
#     for female in female_still_single:
#         single_female_set.add(female)
#     print(len(single_male_set))
#     print(len(male_still_single))
    
main()
