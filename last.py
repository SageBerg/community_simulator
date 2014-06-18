last_name_set = set()

last_name_file = open('last.txt')

for name in last_name_file:
    last_name_set.add(name.strip())

<<<<<<< HEAD
last_list = list(last_name_set)
=======
last_list = list(last_name_set)
>>>>>>> 6684b2d852b2fbafcdfc78c3e93bb6136801472a
