'''
death_dict.py

Sage Berg, Erica Johnson
Created 9 June 2014
'''

death_dict = dict()
x = 0.05

for i in range(200):
    if i < 10:
          x *= 0.85
          death_dict[i] = x
    elif i < 40:
        x *= 1.01
        death_dict[i] = x
    else:
        x *= (1.02 + i/2000)
        death_dict[i] = x

print(death_dict)
