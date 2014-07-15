'''
person_class.py
the core unit of the community simulator 
each person has attributes that help them make important decisions 

Sage Berg, Erica Johnson, Skyler Berg
Created 25 May 2014
'''

from random       import *
from female_first import *
from male_first   import *
from last         import *
from death_dict   import *
from items        import *

class Person(object):

    @staticmethod
    def last_name_gen():
        return choice(last_list)
        
    def __init__(self):
        self.gender     = self.gender_gen()
        self.first_name = self.first_name_gen() 
        self.last_name  = Person.last_name_gen() 
        self.name       = self.first_name + ' ' + self.last_name
        self.title      = None
        self.age        = 0
        
        #RELATIONS
        #self.relation_to_authority
        #self.relations
        #self.boss
        #self.servants
        self.mother   = None
        self.father   = None
        self.spouse   = None
        self.children = list()

        #passive traits
        self.alive = True

        self.pride        = None
        self.morality     = None
        self.intelligence = None
        self.thriftiness  = None
        self.creativity   = None
        self.vigilance    = None
        self.pride        = self.attribute_gen(self.pride)
        self.morality     = self.attribute_gen(self.morality)
        self.intelligence = self.attribute_gen(self.intelligence)
        self.thriftiness  = self.attribute_gen(self.thriftiness)
        self.creativity   = self.attribute_gen(self.creativity)
        self.vigilance    = self.attribute_gen(self.vigilance)

        #skills
        self.job   = self.farm #self.job = function
        self.price = randint(5,9) 
        self.strength   = 1 - 10*death_dict[self.age] #make better scale for strength later
        self.farm_skill = 5 #do not change without changing the famine function in disasters.py
        #self.fight = 
        #self.persuasion
        #self.parenting
       
        #OWNERSHIP
        self.food         = 0 #food is used as currency for now
        self.home_address = None
        self.owns         = dict() 
        self.listings     = dict() 
        #self.wealth      = 0

    def __str__(self):
        string = self.name  + ' (' + str(self.age) + ')\n' 
        if self.home_address:
            string += 'of ' + str(self.home_address) + '\n'
        if self.spouse:
            string += 'married to ' + self.spouse.name + ' (' + str(self.spouse.age) + ')\n' 
        if self.alive == False:
            string += 'IS DEAD'
        return string  
        
    def gender_gen(self):
        return choice(['female', 'male'])        
         
    def first_name_gen(self): 
        if self.gender == 'female':
           return choice(female_first_list)
        return choice(male_first_list)

    def attribute_gen(self, attribute):
        stat = 0
        if self.mother != None:
            stat += round((self.mother.attribute + self.father.attribute) / 2, 0)
        for i in range(10):
            stat += randint(-10, 10)
        return stat

    def set_price(self):
        job_market_dict = {
        self.make_plow:  Plow, 
        self.make_house: House,
        self.make_wine:  Wine,
        }

        if self.job == self.soldier:
            return
        if self.job != self.farm and \
        job_market_dict[self.job] in self.listings and \
        self.listings[job_market_dict[self.job]] == 0:
            self.price += 1
        elif self.job != self.farm and \
        job_market_dict[self.job] in self.listings and \
        self.listings[job_market_dict[self.job]] > 0:
            self.price -= 1
        if self.price < len(self.children) + 1:
            self.price = len(self.children) + 1

    def get_older(self):
        self.age += 1
        self.strength = 1 - death_dict[self.age]

    def death_chance(self): #death from old age, sickness, and accidents
        if randint(0,100) <= death_dict[self.age]*100: 
            self.alive = False
            #return 'age/sickness'

    def death_by_exposure_chance(self):
        if self.home_address == None and randint(0,9) == 0:
            self.alive = False
            #print(str(self.name) + ' died of exposure **************************')
            #return 'exposure'

    def inheritance(self):
            #TO DO: add have listings be inheritable as well
        if self.spouse:
            self.bequeath(self.spouse)

        elif len(self.children) > 0:
            self.bequeath(self.children[0])

        elif self.mother and self.mother.alive:
            self.bequeath(self.mother)

        elif self.father and self.father.alive:
            self.bequeath(self.father)

        else:
            pass
            #later government inherits items

    def bequeath(self, recipient):
        for key in self.owns.keys():
            if key not in recipient.owns:
                recipient.owns[key] =  self.owns[key]
            else:
                recipient.owns[key] += self.owns[key]
        recipient.food += self.food

    def remove_self_from_parents_children(self):
        try:
            self.mother.children.remove(self)
            self.father.children.remove(self)
        except:
            #print('initial people don\'t have parents')
            pass
    
    def give_birth_chance(self):
        if self.gender == 'female' and self.age > 15 and self.age <= 55 and self.spouse and self.spouse.alive:
            if randint(-60, 60) > self.age:
                baby = Person()
                self.children.append(baby)
                self.spouse.children.append(baby)
                baby.mother = self
                baby.father = self.spouse
                baby.last_name = self.last_name
                baby.name = baby.first_name + ' ' + baby.last_name
                baby.home_address = self.home_address
                if self.home_address != None:
                    self.home_address.occupants.append(baby)
                #print(baby.name + " was born to " + self.name + " and " + self.spouse.name)
                
                if self.home_address:
                    if self.home_address.occupants != self.spouse.home_address.occupants:
                        raise NameError('parents not living in same house')
                    if self.home_address.occupants != baby.home_address.occupants:
                        raise NameError('baby didn\'t come home')

                return baby
    
    def marriage(self, prospect_set):
        for potential_mate in prospect_set:
            if potential_mate not in self.children and \
               (potential_mate.mother != self.mother or \
                self.father == None) and \
               (potential_mate.father != self.father or \
                self.mother == None) and \
               potential_mate != self.mother and \
               potential_mate != self.father:
                if potential_mate.gender == 'female':
                    bride = potential_mate
                    groom = self
                else:
                    bride = self
                    groom = potential_mate
                #print(bride.name + ' (' + str(bride.age) + ') married ' + \
                #      groom.name + ' (' + str(groom.age) + ')!!!')
                bride.spouse = groom
                groom.spouse = bride
                bride.last_name = groom.last_name
                bride.name = bride.first_name + ' ' + bride.last_name
                groom.move_family_into_house()
                bride.move_family_into_house()

                assert (groom.alive and bride.alive)
                
                if groom.home_address != bride.home_address:
                    raise NameError('bride and groom didn\'t go home to the same house')
                if groom.home_address:
                    if groom.home_address.occupants != bride.home_address.occupants:
                        raise NameError('occupants list not equal after wedding')

                prospect_set.remove(potential_mate)
                break

    def divorce(self):
        if self.spouse:
            self.spouse.spouse = None
        self.spouse = None

    def farm(self, economy):
        production = self.farm_skill
        if Plow in self.owns and len(self.owns[Plow]) > 0:
            production += randint(0, 2)
        self.food += randint(0, production)
        
    def soldier(self, economy):
        pass

    def make_plow(self, economy):
        for i in range( randint(1, 2) ):
            self.produce(Plow, economy)

    def make_house(self, economy):
        for i in range(randint(1,1)):
            self.produce(House, economy)
   
    def make_wine(self, economy):
        for i in range(randint(0,5)):
            self.produce(Wine, economy)
    
    def produce(self, item, economy):
        economy[item].put( (self.price, id(self), self) )
        if item not in self.listings:
            self.listings[item] = 1
        else:
            self.listings[item] += 1

    def change_job(self, economy):
        '''economy is a dictionary mapping "market" strings to priority queues
           returns a self.job function which is assigned to self in community_simulator.py
        '''
        market_job_dict = {
        Plow:  self.make_plow,
        House: self.make_house,
        Wine:  self.make_wine,
        }
       
        rand_job_list = list()
        for market in economy.keys():
            rand_job_list.append(market) 
        shuffle(rand_job_list)
        for market in rand_job_list:
            if economy[market].empty():
            #at least one person will always try each job
                #print(self.name + ' started a ' + str(market) + '. Price: ' + str(self.price))
                return market_job_dict[market]
            elif economy[market].queue[0][0] > self.price:
                #print(self.name + ' joined the ' + str(market) + ' market')
                return market_job_dict[market]
        #print(self.name + ' BECAME a farmer')
        return self.farm #people farm if they don't have other good options

    def spend(self, economy):
        if self.home_address == None or len(self.home_address.occupants) > 15:
            self.buy(House, economy)
            self.move_family_into_house()

        if self.job == self.farm:
            self.buy(Plow, economy)
        while self.job != self.make_wine and economy[Wine].qsize() > 0 and self.food > max(self.thriftiness, economy[Wine].queue[0][0]) :
            self.buy(Wine, economy) 

    def buy(self, item, economy):
        if economy[item].qsize() > 0 and \
           self.food > economy[item].queue[0][0]:
            #print(self.name, self.food)
            listing = economy[item].get()
            #print(listing)
            price   = listing[0]
            seller  = listing[2]
            self.food   -= price
            seller.food += price 
            if item not in self.owns:
                self.owns[item] = [ item() ]
            else:
                self.owns[item].append( item() )
            seller.listings[item] -= 1
            #print(self.name + ' bought a(n) ' + str(item) + ' from ' + seller.name + '. Price: ' + str(price))

    def move_family_into_house(self):
        '''
        should be the only code that gets people into houses
        this way occupancy rules are all in one place
        NOTE: self.owns[House] should only ever map to one House object
        '''
        if House in self.owns and len(self.owns[House]) > 0 and self.home_address == None:
            self.home_address = self.owns[House][0]
            self.home_address.occupants.append(self) 
        if self.spouse and self.spouse.home_address != self.home_address: 
            if self.spouse.home_address != None:
                self.spouse.home_address.occupants.remove(self.spouse)
            self.move(self.spouse)
        for child in self.children:
            if child.home_address == None:
                self.move(child)
                child.move_family_into_house()
        for parent in [ self.mother, self.father ]:
            if parent != None and parent.alive and parent.home_address == None:
                self.move(parent)
                if parent.spouse:
                    self.move(parent.spouse)

    def move(self, person):
        person.home_address = self.home_address 
        if self.home_address:
            self.home_address.occupants.append(person) 
            #print(person.name + ' moved into ' + self.name + '\'s house')
    
    def eat(self, government):
        if self.age < 10:
            if self.father.food > 0:
                self.father.food -= 1
            elif self.mother.food > 0:
                self.mother.food -= 1
            elif government.food > 0:
                government.food -= 1
            else:
                self.alive = False
                return 'child starvation' 
#                print('little ' + self.name + ' starved to death at age ' + str(self.age))
        else:
            if self.food > 0:
                self.food -= 1
            elif self.food == 0 and self.spouse != None and self.spouse.food > 1:
                self.spouse.food -= 1
            elif government.food > 0:
                government.food -= 1
            else: 
                self.alive = False
                return 'starvation' 
                #print(self.name + ' starved to death 0X')
                
    def steal(self, person_list):
        if self.food + self.morality < 0 and len(person_list) > 1:
            victim = choice(person_list)
            if victim.food > self.morality:
                if victim.vigilance > self.vigilance:
                    if victim.morality < 0:
                        if randint(0, 9) == 0:
                            #print('fight')
                            pass
                victim.food -= 1
                self.food += 1
                #print(self.name + ' stole from ' + victim.name)

def print_fathers(person):
    while person:
        print(person.name)
        person = person.father
