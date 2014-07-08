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
from error_checking_functions import *
from death_dict   import death_dict
from government   import *

person_list       = list()
single_male_set   = set()
single_female_set = set()
family            = dict()
government_list   = list()
ruler_list        = list()

cause_of_death_dict = dict()
cause_of_death_dict['age/sickness'] = 0
cause_of_death_dict['plague']       = 0
cause_of_death_dict['starvation']   = 0
cause_of_death_dict['exposure']     = 0
cause_of_death_dict['child starvation']     = 0

economy = dict()
economy[Plow]  = PriorityQueue()
economy[House] = PriorityQueue()
economy[Wine]  = PriorityQueue()

house_list = list()

def main():
    global house_list

    for i in range(1000): #number of people
        person_list.append(Person())
    for person in person_list:
        person.age  = 10
        person.food = 5
        house = House()
        person.owns[House] = [ house ]
        person.home_address = person.owns[House][0]
        house.occupants.append(person)
        house_list.append(house)

    famine_flag = False
    for i in range(201):  #number of years
        print()
        print('----- year ' + str(i) + ' -----') 
        print('there are ' + str(len(person_list)) + ' people alive')
        print('there are ' + str(len(house_list))  + ' houses standing') 
        print()
        plague_death_count = plague(person_list)
        if plague_death_count:
            cause_of_death_dict['plague'] += plague_death_count
        fire(house_list)
        if famine_flag == False:
            famine_flag = famine(person_list)
#        global_decay()
        exposure()
        death()             #kills and removes people from lists
        destruction()       #decays and removes items
        house_list = update_house_list() #adds new houses
        age()               #increments everyone's age
        birth()
        search_for_spouse()
        work()

        #debugging functions (imported from error_checking_functions.py)
        spouse_house_check(person_list)
        house_search(house_list, person_list)
        child_search(person_list)
        spouse_search(person_list)

        spend() 
        set_prices()     #prices change based on demand
        
        if not government_list:
            insurrection()
        if person_list:
            if government_list[0].leader not in ruler_list:
                ruler_list.append(government_list[0].leader)
            government_list[0].collect_taxes(person_list)
            government_list[0].succession()
            if government_list[0].leader == None:
                insurrection()

        theft()
        nutrition()

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

    farmers    = 0
    vinters    = 0
    plowrights = 0
    carpenters = 0
    for person in person_list:
        if person.job == person.farm:
            farmers += 1
        elif person.job == person.make_house:
            carpenters += 1
        elif person.job == person.make_wine:
            vinters += 1
        else:
            plowrights += 1
    print('number of farmers: '.ljust(25)    + str(farmers))
    print('number of vinters: '.ljust(25)    + str(vinters))
    print('number of plowrights: '.ljust(25) + str(plowrights))
    print('number of carpenters: '.ljust(25) + str(carpenters))
   
    homeless = 0
    for person in person_list:
        if person.home_address == None:
            homeless += 1
    print('number of homeless: '.ljust(25) + str(homeless))

    #for house in house_list:
    #    print("~~~~~~~~~~~~~~~~~~~~~~~ house occupants:")
    #    for person in house.occupants:
    #        print(person.name + ' age: ' + str(person.age), end=', ')
    #        #print("MORALITY: " + str(person.morality))
    #        print()
    
    print()
    for key, value in cause_of_death_dict.items():
        print(key.ljust(20), value)
    
    print()
    print('Rulers:')
    for ruler in ruler_list:
        print('    ' + ruler.name.ljust(24) + 'pride: ' + str(ruler.pride))
        
    print()
    print('Government food: ' + str(government_list[0].food))

def decay(item):               #Now in item_superclass as decay()
    item.durability -= randint(0,5)

def destruction():             #Now in community_class as destruction()
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
    #                print(person.name + '\'s ' + str(type(person.owns[House])) + ' broke')

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
        key = person.death_chance()
        if key:
            cause_of_death_dict[key] += 1
        if person.alive == False:
            person_list.remove(person)
            person.inheritance()
            person.remove_self_from_parents_children()
            person.divorce() 

    for market in economy.keys():
        update_market(market)

    for house in house_list: #remove dead people from houses
        #print(house.occupants)
        for person in house.occupants:
            if person.alive == False: #causing errors I don't fully understand
                #person.home_address = None 
                #house.occupants.remove(person)
                pass 
                
def exposure():
    for person in person_list:
        key = person.death_by_exposure_chance()
        if key:
            cause_of_death_dict[key] += 1

def age():
    for person in person_list:
        person.get_older()
        
def birth():
    for person in person_list:
        baby = person.give_birth_chance()
        if baby:
            person_list.append(baby)

def search_for_spouse():          #Now in community_class as search_for_spouse()
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
    for male in single_male_set:
        male.marriage(single_female_set)
    single_male_set   = {male   for male   in single_male_set   if male.alive   and male.spouse   == None}
    for female in single_female_set:
        female.marriage(single_male_set) #might cause error
    

def work():
    for person in person_list:
        if person.age >= 10:
            if person.food < 1: #people change jobs if their work doesn't get them by
                person.job = person.change_job(economy)
            person.job(economy)

def nutrition():
    for person in person_list:
        key = person.eat(government_list[0])
        if key:
            cause_of_death_dict[key] += 1

def spend():
    for person in person_list:
        person.spend(economy)

def set_prices():
    for person in person_list:
        person.set_price()
    
def theft():
    for person in person_list:
        person.steal(person_list)
        
def insurrection():
    if person_list:
        most_proud = None
        for person in person_list:
            if  most_proud == None or person.pride > most_proud.pride:
                most_proud = person
        if not government_list:
            new_government = Government()
            new_government.leader = most_proud
            government_list.append(new_government)
            print("A NEW GOVERNMENT WAS MADE BY " + most_proud.name)
        else:
            government_list[0].leader = most_proud
    
    
    
main()
