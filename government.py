'''
Sage Berg, Erica Johnson
Created 5 July 2014
'''

class government(object):
    
    def __init__(self):
        self.leader     = None
        #self.location   = (0, 0)
        self.military   = list()
        self.communitie = list()
        self.tax        = 0 #amount of food taken per year
        self.owns       = dict()
        self.in_hiding  = False

    def declare_war(self, governments_list):
        pass

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


        
