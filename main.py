monsters = open('monsters.txt', 'r')
dictionary = dict()
for line in monsters:
    line = line.strip()
    split = line.split(",")
    dictionary[split[0]] = split[1]

see = 'y'
while see == 'y':
    monster_name = input('Input the name of the monster you want to learn more about (case sensitive, start with a capital letter): ')
    print("Name of monster:", monster_name)
    print("Description:", dictionary.get(monster_name, 'Monster does not exist in our database'))
    see = input('Would you like to look-up another monster? Input y or n: ')
    print('')
