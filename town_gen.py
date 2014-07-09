'''
Sage Berg
Created: 24 September 2013
'''

from random import choice

def get_pref_suff():
    pre = open("town_prefix.txt")
    suf = open("town_suffix.txt")
    p_list = []
    s_list = []
    for i in pre:
        p_list.append(i.strip("\n").capitalize())
    for i in suf:
        s_list.append(i.strip("\n"))
    pre.close()
    suf.close()
    return p_list, s_list

def gen_town_name():
    prefix_list, suffix_list = get_pref_suff()
    return choice(prefix_list) + choice(suffix_list)
