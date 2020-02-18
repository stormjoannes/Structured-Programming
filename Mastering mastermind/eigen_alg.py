import random

st = ''
set = []
for i in range(1111, 6667):
    st = str(i)
    if '0' not in st and '7' not in st and '8' not in st and '9' not in st:
        set.append(st)
code = []
hat = []
index = 0
voorkomen = {}

gespeeld = input('Heb je dit spel al een keer gespeeld [Y/N]: ').lower()
if 'n' == gespeeld:
    spelregels = '---SPELREGELS---' + \
                 '\n' + \
                 'Er zijn 6 verschillen kleuren pionnen waar je uit kunt kiezen: blauw, Wit, rood en zwart.' + \
                 '\n' + \
                 'Je hebt 10 beurten om het goed te raden, haal je ndit niet heb je verloren.' + \
                 '\n' + \
                 'Zodra een pion op de goede plek staat en de goede kleur is komt er een zwart pinnetje te staan.' + \
                 '\n' + \
                 'Zodra een pion niet op de goede plek staat, maar de kleur wel in de code voorkomt.' + \
                 'Krijg je een wit pinnejte erbij.' + \
                 '\n' + \
                 'Als je de code hebt geraden heb je gewonnen.' + \
                 '\n' + \
                 'Hoe minder pogingen je er over doet, hoe beter je bent.' + \
                 '\n'
    print(spelregels)
elif 'y' == gespeeld:
    print('\n')


def gamemode():
    pogingen = 0
    modus = input('Wil je de Code maken of breken: ').lower()
    if 'breken' in modus:
        print('De te raden getallen zijn: ' + '1 t/m 6. ')
        code = []
        code_breken(pogingen, code)
    elif 'maken' in modus:
        eigencode = ''
        pc_raden(pogingen, set, eigencode)
    else:
        print('dat is geen bestaande gamemode, probeer het opnieuw')
        gamemode()


def code_breken(pogingen, codes):
    if len(codes) < 4:
        codes = random.choice(set)
    print('Je hebt nog ' + str(11 - pogingen) + ' pogingen over.')

    poging = ''
    while poging not in set:
        poging = input('Wat is de code:  ')
        poging = poging.strip()
        if poging not in set:
            print('Deze kleur codecombinatie bestaat niet, probeer het opnieuw.')

    if poging == codes:
        print('Gefeliciteerd je hebt het goed geraden')
        print('Je hebt het in ' + str(pogingen) + ' poging gehaald.' + '\n')
        gamemode()
    else:
        terugslag = feedback(codes, poging)
        print(terugslag)
        pogingen += 1

        if pogingen == 11:
            print('Helaas je hebt de code niet kunnen kraken in 10 pogingen' + '\n')
            print('De code was ' + str(codes))
            gamemode()
        else:
            code_breken(pogingen, codes)


def pc_raden(pogingen, set, eigencode):
    while eigencode not in set:
        eigencode = input('Wat is de code:  ')
        eigencode = eigencode.strip()
        if eigencode not in set:
            print('Deze codecombinatie bestaat niet, probeer het opnieuw.')

    randcode = []
    lst = []
    while index <= 5 and sum(voorkomen.values()) < 4:
        for i in range(1, 7):
            print(randcode, 'randcodeeeeeeeee')
            while len(randcode) < 4:
                randcode.append(str(i))

            pogingen += 1
            if randcode == eigencode:
                print('Helaas, de computer heeft het goed geraden in ' + str(pogingen) + ' pogingen.' + '\n')
                gamemode()

            rand_2 = ''.join(randcode)
            reflectie = feedback(eigencode, str(rand_2))
            print(reflectie)
            hat.append(rand_2)

            print(reflectie, 'reflectieeeeeee')
            if reflectie != '0, 0':
                print('dagggggggggggggggg')
                voorkomen[i] = int(reflectie[0])
                print(voorkomen)
            randcode.clear()

    lst_2 = ''
    lst = []
    while lst_2 != eigencode:
        lst.clear()
        print(lst_2)
        for h in voorkomen:
            for a in range(0, voorkomen[h]):
                lst.append(str(h))
        random.shuffle(lst)
        lst_2 = ''.join(lst)
        while lst_2 in hat:
            print(lst_2, 'whileeeeeeeeeee')
            random.shuffle(lst)
            lst_2 = ''.join(lst)
        pogingen += 1
        hat.append(lst_2)
        if lst_2 == eigencode:
            if pogingen >= 11:
                print('gefeliciteerd, de computer heeft je code niet in 10 pogingen kunnen raden.')
                print('De computer deed er ' + str(pogingen) + ' pogingen over.' + '\n')
            else:
                print('Helaas, de computer heeft het goed geraden in ' + str(pogingen) + ' pogingen.' + '\n')
            gamemode()






    gamemode()


def feedback(code, poging):
    temp = []
    feedback = []
    for i in range(0, len(poging)):
        print(poging[i])
        if poging[i] == code[i]:
            e = str(poging[i]) + ':' + 'zwart'
            temp.append(e)
            feedback.append('zwart')
    for i in range(0, len(poging)):
        if poging[i] in code:
            d = str(poging[i]) + ':' + 'wit'
            if d not in temp and temp.count(str(poging[i]) + ':' + 'zwart') < code.count(poging[i]) and temp.count(str(poging[i]) + ':' + 'zwart') < poging.count(poging[i]):
                temp.append(d)
                feedback.append('wit')
    return str(feedback.count('zwart')) + ', ' + str(feedback.count('wit'))

gamemode()