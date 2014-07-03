'''
community_simulator.py
the main program

Sage Berg, Erica Johnson, Skyler Berg
Created 25 May  2014
'''

from queue        import PriorityQueue
from person_class import Person, print_fathers
from disasters    import *
from items        import *

person_list = list()
single_male_set   = set()
single_female_set = set()
family = dict()

economy = dict()
economy[Plow]  = PriorityQueue()
economy[House] = PriorityQueue()

print()
print(economy)
print(economy[House].qsize())

house_list = list()

def main():
    global house_list

    for i in range(1000): #number of people
        person_list.append(Person())
    for person in person_list:
        person.age  = 10
        person.food = 5
        house = House()
        person.owns['house'] = [ house ]
        person.home_address = person.owns['house'][0]
        house.occupants.append(person)
        house_list.append(house)

    famine_flag = False
    for i in range(201):  #number of years
        print()
        print('----- year ' + str(i) + ' -----') 
        print('there are ' + str(len(person_list)) + ' people alive')
        print('there are ' + str(len(house_list))  + ' houses standing') 
        print()
        plague(person_list)
        if famine_flag == False:
            famine_flag = famine(person_list)
#        global_decay()
        death()             #kills and removes people from lists
        destruction()       #decays and removes items
        house_list = update_house_list() #adds new houses
        age()               #increments everyone's age
        birth()
        search_for_spouse()
        work()
        spouse_house_check()
        spend(i) 

        house_search()
        child_search()
        spouse_search()

        set_prices()     #prices change based on demand

        eat()

        if famine_flag: 
            famine_flag = end_famine_maybe(person_list)
    
    for person in person_list:
        if person.last_name in family:
            family[person.last_name] += 1
        else:
            family[person.last_name] = 1
        #print(person.name + '(' + str(person.age) + ') still lives.')
        #print_fathers(person)
        #print()
    print()
    for name in family:
        print(name, family[name])
    s = 0
    for person in person_list:
        s += len(person.children)
    print('average children per family: ' + str(round(s/(len(person_list)//2 +1), 2)))
    #+1 to the divisor to avoid division by 0

    farmers = 0
    plowrights = 0
    carpenters = 0
    for person in person_list:
        if person.job == person.farm:
            farmers += 1
        elif person.job == person.make_house:
            carpenters += 1
        else:
            plowrights += 1
    print('number of farmers: '    + str(farmers))
    print('number of plowrights: ' + str(plowrights))
    print('number of carpenters: ' + str(carpenters))
   
    homeless = 0
    for person in person_list:
        if person.home_address == None:
            homeless += 1
    print('number of homeless: ' + str(homeless))

    #for house in house_list:
    #    print("~~~~~~~~~~~~~~~~~~~~~~~ house occupants:")
    #    for person in house.occupants:
    #        print(person.name + ' age: ' + str(person.age), end=', ')
    #        #print("MORALITY: " + str(person.morality))
    #        print()

def spouse_house_check(): #DEBUG function
    for person in person_list:
        if person.spouse:
            if person.spouse.home_address != person.home_address:
                print()
                print(person)
                print(person.spouse)
                raise NameError('housing mismatch')
            if person.home_address:
                if person.spouse.home_address.occupants != person.home_address.occupants:
                    print(person)
                    print(person.spouse)
                    raise NameError('housing mismatch in occupants')

def spouse_search(): #DEBUG function
    for person in person_list:
        if person.spouse != None and person.spouse.spouse != person:
            print()
            print('person: ' + person.name, str(person.alive))
            print('spouse: ' + person.spouse.name, str(person.spouse.alive))
            print('spouse of spouse: ' + person.spouse.spouse.name, str(person.spouse.spouse.alive))
            raise NameError(person.name + ' has marraige problems')
        elif person.spouse != None:
            #print(person.name + ' and ' + person.spouse.name + ' have a fine marriage')
            pass

def child_search(): #DEBUG function
    for person in person_list:
        try:
            if person not in person.mother.children:
                raise NameError(person.name + ' Age: (' + str(person.age) + \
                ') is not in mother children list')
            if person not in person.father.children:
                raise NameError(person.name + ' Age: (' + str(person.age) + \
                ') is not in father children list')
        except:
            pass
            #initial people do not have parents 

def house_search(): #DEBUG function
    for house in house_list:
        #print(house, 'Durability:', house.durability)
        for occupant in house.occupants:
            if occupant.home_address != house:
                print()
                print('HOUSE ERROR')
                print(occupant.home_address, 'Durability:', occupant.home_address.durability)
                print(house, 'Durability:', house.durability)
                print(occupant.name + ' is an occupant of ' + str(occupant.home_address))
                if occupant.spouse:
                    print(occupant.spouse.name + ' is an occupant of ' + str(occupant.spouse.home_address))
                raise NameError(occupant.name + ' (' + str(occupant.age) + \
                ') has address ' + str(occupant.home_address)) 
    for person in person_list:
        if person.home_address != None and person not in person.home_address.occupants:
            print()
            print("OCCUPANTS: ")
            print(person)
            raise NameError(person.name + ' Age: (' + str(person.age) + \
            ') is not in occupants list')
    
def decay(item):
    item.durability -= randint(0,5)

def destruction():
    for person in person_list: #people leave destroyed homes
        if person.home_address != None and person.home_address.durability <= 0:
            person.home_address.occupants.remove(person)
            person.home_address = None
        
    item_set = set()
    for person in person_list: #removes items that break
        for item_list in person.owns.values():
            for item in item_list:
                if item in item_set:
                    print(str(item) + ' is shared by ' + person.name)
                    raise NameError('two people own the same item')
                item_set.add(item)
                decay(item)
                if item.durability <= 0:
            	    item_list.remove(item) 
            	    #print(person.name + '\'s ' + str(type(item)) + ' broke')

def update_house_list():
    new_house_list = list()
    for person in person_list:
        if person.home_address != None and person.home_address not in new_house_list:
            new_house_list.append(person.home_address)
    return new_house_list

def update_market(market):
    new_market = PriorityQueue()
    for i in range(economy[market].qsize()):
        listing = economy[market].get()
        seller = listing[2]
        if seller.alive:
            new_market.put(listing)
    economy[market] = new_market

def death():
    global house_list
    global economy
    for person in person_list:
        person.death_chance()
        if person.alive == False:

            person_list.remove(person)

            if person.spouse != None:
                for key in person.owns.keys():
                    if key not in person.spouse.owns:
                        person.spouse.owns[key] = person.owns[key]
                    else:
                        person.spouse.owns[key] += person.owns[key]
                #if person.gender == 'female':
                #    print(person.name + ' died and left her items to her husband ' + person.spouse.name)
                #else:
                #    print(person.name + ' died and left his items to his wife ' + person.spouse.name)
            elif len(person.children) > 0:
                for key in person.owns.keys():
                    if key not in person.children[0].owns:
                        person.children[0].owns[key] = person.owns[key]
                    else:
                        person.children[0].owns[key] += person.owns[key]
                    #print(person.children[0].name + ' inherited ' + str(len(person.owns[key])) + ' ' + key + 's')
                    #print(person.owns)
                    #print(person.children[0].owns)
                #raise NameError('child inherited stuff')
            else:
                pass
                #print('no one was alive to inhereit ' + person.name + '\'s items')
            try:
                person.mother.children.remove(person)
                person.father.children.remove(person)
            except:
                #print('initial people don\'t have parents') 
                pass
            #print(person.name + ' died at age: ' + str(person.age))

            if person.spouse:
                person.spouse.spouse = None #people can't be married to dead people
            person.spouse = None  
            
    update_market(Plow)
    update_market(House)

    for house in house_list: #remove dead people from houses
        #print(house.occupants)
        for person in house.occupants:
            if person.alive == False: #causing errors I don't fully understand
                #person.home_address = None 
                #house.occupants.remove(person)
                pass 
def age():
    for person in person_list:
        person.age += 1
        
def birth():
    for person in person_list:
        baby = person.give_birth_chance()
        if baby:
            person_list.append(baby)

def search_for_spouse():
    global single_male_set
    global single_female_set
    for person in person_list:
        if person.spouse == None and person.age >= 10:
            if person.gender == 'male':
                single_male_set.add(person)
            else:
                single_female_set.add(person)
                #print(person.name + ' ' + str( person.age ) + ' is looking for a husband!!!')
    single_male_set   = {male   for male   in single_male_set   if male.alive   and male.spouse   == None}
    single_female_set = {female for female in single_female_set if female.alive and female.spouse == None}
    #print("          single male length: " + str(len(single_male_set)))
    for male in single_male_set:
        male.marriage(single_female_set)
        #print("               " + male.name)
    #print("          single female length: " + str(len(single_female_set)))
    #for female in single_female_set:
    #    female.marraige(single_male_set) #weird error female has no attribute marriage
        #print("               " + female.name)

def work():
    for person in person_list:
        if person.age >= 10:
            if person.food < 1: #people change jobs if their work doesn't get them by
                person.job = person.change_job(economy)
            person.job(economy)

def eat():
    for person in person_list:
        person.eat()

def spend(year):
    for person in person_list:
        person.spend(economy)

def set_prices():
    for person in person_list:
        person.set_price()
    
main()
