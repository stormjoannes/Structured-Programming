import random

x = random.randrange(1, 11)
z = 0
y = 0
try:
    while y != x:
        y = int(input('Gok een getal van 1 tot en met 10: '))
        z += 1
        print('Probeer opnieuw, het is niet ' + str(y))
    print('Gefeliciteerd! Je hebt er ' + str(z) + ' pogingen over gedaan')
except ValueError:
    print('vul een getal in!')
