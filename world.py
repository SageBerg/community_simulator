'''
Sage Berg, Erica Johnson
Created 5 July 2014
'''

from tkinter import *

class World(object):
    
    def __init__(self):
        self.year        = 0
        self.hexgrid     = list() 
        self.governments = list()
        self.communities = list()

#         self.root = Tk()
#         self.canvas = Canvas(self.root, height=1000, width=1800, bd=0, bg='white')
#         self.canvas.pack()
#         x = 0
#         y = 0 
#         offset_flag = True 
#         #for i in range(6):
#         #    self.canvas.creat_polygon( 
#         for i in range(1000): 
#             self.canvas.create_polygon(x-43, y-25, 
#                                        x   , y-50, 
#                                        x+43, y-25, 
#                                        x+43, y+25, 
#                                        x   , y+50, 
#                                        x-43, y+25, fill='#3cb371', outline='black', width=1)
#             x += 86
#             if x > 1900:
#                 if offset_flag:
#                     x = 43
#                     offset_flag = False
#                 else:
#                     x = 0
#                     offset_flag = True
#                 y += 75 
#         #self.canvas.create_polygon(200, 200, 200, 250, 243, 275, 286, 250, 286, 200, 243, 175, fill='#30AA50',
#         #                           outline='black', width = 1)
#         #self.canvas.create_line(243, 0, 243, 400)
#         #self.canvas.create_line(0, 225, 400, 225)
#         self.root.mainloop()

    #def draw_hex_block(self):

World()
