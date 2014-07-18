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
                
    def war(self, winner, loser):
        for i in range(len(winner.military)):
            winner.military[i].alive = False
            winner.food += loser.food
        for community in loser.communities:
            print(community.name + ' was taken in war')
            winner.communities.append(community)
            community.government = winner
        for soldier in loser.military:
            soldier.alive = False
        return loser

    def declare_war(self, governments_list):
        rival = choice(governments_list)
        while rival == self:
            rival = choice(governments_list)
        print(self.leader.title + ' ' + self.leader.name + ' has declared war on ' + \
              rival.leader.title + ' ' + rival.leader.name + '!')
        if len(self.military) >= len(rival.military):
            loser = self.war(self, rival)
            print(self.leader.title + ' ' + self.leader.name + ' won the war!')
        else:
            loser = self.war(rival, self)
            print(rival.leader.title + ' ' + rival.leader.name + ' won the war!')
        return loser
            
    def hire_workers(self):
        pass 

    def pay_workers(self):
        for soldier in self.military:
            if self.food >= 10:
                soldier.food += 10
                self.food -= 10

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
        
    def conscript_soldiers(self, desired_military_size):
        for community in self.communities:
            for person in community.person_list:
                if person.gender == 'male' and person.age > 14 and person.age < 36 \
                and len(self.military) < desired_military_size and person.job != person.soldier:
                    person.job = person.soldier
                    self.military.append(person)

    def move_soldiers(self):
        '''
        a government can move soldiers to another location

        it will move them toward enemies if it can see them
        but it will also make intelligent retreats
        '''
        pass


        
