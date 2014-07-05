'''
Sage Berg, Erica Johnson
Created 5 July 2014
'''


def spouse_house_check(person_list): #DEBUG function
    for person in person_list:
        if person.spouse:
            if person.spouse.home_address != person.home_address:
                print()
                print(person)
                print(person.spouse)
                raise NameError('housing mismatch')
            if person.home_address:
                if person.spouse.home_address.occupants != \
                   person.home_address.occupants:
                    print(person)
                    print(person.spouse)
                    raise NameError('housing mismatch in occupants')

def spouse_search(person_list): #DEBUG function
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

def child_search(person_list): #DEBUG function
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

def house_search(house_list, person_list): #DEBUG function
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
    
