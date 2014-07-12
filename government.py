'''
Sage Berg, Erica Johnson
Created 5 July 2014
'''

from random import *

class Government(object):
    
    def __init__(self):
        self.leader      = None
        #self.location   = (0, 0)
        self.military    = list()
        self.communities = list()
        self.tax         = randint(1, 3) #amount of food taken per year
        self.owns        = dict()
        self.in_hiding   = False
        self.food        = 0
        
    def coronation(self):
        if self.leader.gender == 'female':
            self.leader.title = 'Queen'
        else:
            self.leader.title = 'King'
        
    def succession(self):
        if self.leader.alive == False:
            #print(self.leader.title + ' ' + self.leader.name + ' has died.')
            if self.leader.children:
                heir = self.leader.children[0]
                self.leader = heir
                self.coronation()
            elif self.leader.spouse:
                heir = self.leader.spouse
                self.leader = heir
                self.coronation()
            else:
                self.leader = None
                #print('...and there is no heir')
                
    def collect_taxes(self, person_list):
        for person in person_list:
            if person.food > self.tax + len(person.children):
                person.food -= self.tax   
                self.food += self.tax 

    def declare_war(self, governments_list):
        rival = choice(governments_list)
        while rival == self:
            rival = choice(governments_list)
        print(self.leader.title + ' ' + self.leader.name + ' has declared war on ' + \
              rival.leader.title + ' ' + rival.leader.name + '!')
            

    def hire_workers(self):
        pass 

    def pay_workers(self):
        pass

    def fire_workers(self):
        pass

    def buy(self):
        pass 

    def go_into_hiding(self):
        ''' 
        a government can hide in forests and mountains 
        in this case it's more like a group of rebels
        and doesn't have the ability to tax or enforce policy
        '''
        pass

    def hire_mercenaries(self):
        '''
        a government can hire another government to 
        help it fight
        '''
        pass

    def move_soldiers(self):
        '''
        a government can move soldiers to another location

        it will move them toward enemies if it can see them
        but it will also make intelligent retreats
        '''
        pass


        
