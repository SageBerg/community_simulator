last_name_set = set()

last_name_file = open('last.txt')

for name in last_name_file:
    last_name_set.add(name.strip())

last_list = list(last_name_set)
