openfile = open('best1.txt', 'r')
user = openfile.readlines()

file = open("nieuw_bestand.txt", 'w')
for i in user:
    if i != '\n':
        file.write((i.strip() + '\n'))
