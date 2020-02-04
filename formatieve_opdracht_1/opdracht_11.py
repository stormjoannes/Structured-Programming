alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
x = input('geef een tekst: ')
y = int(input('geef een rotatie'))
for i in x:
    for z in range(0, len(alfabet) - 1):
        if alfabet[z] == i:
            