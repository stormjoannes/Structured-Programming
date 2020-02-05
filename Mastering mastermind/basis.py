import random

kegels = ['rood', 'blauw', 'wit', 'zwart']
code = []


def gamemode():
    pogingen = 1
    gespeeld = input('Heb je dit spel aal een keer gespeeld [Y/N]: ').lower()
    if 'n' in gespeeld:
        spelregels = 'Er zijn 4 verschillen kleuren pionnen waar je uit kunt kiezen: blauw, Wit, rood en zwart' + \
                     '\n' + \
                     'Je hebt 10 beurten om het goed te raden' + '\n'
        print(spelregels)
    modus = input('Wil je de Code maken of breken: ').lower()
    if 'breken' in modus:
        code_breken(pogingen, code)
    elif 'maken' in modus:
        code_maken()
    else:
        print('dat is geen bestaande gamemode')
        gamemode()


def code_breken(pogingen, codes):
    pionnen = []
    feedback = []
    while len(codes) != 4:
        codes.append(random.choice(kegels))
    print(codes)

    print('Je hebt nog ' + str(11 - pogingen) + ' pogingen over.')

    pion1 = input('welke kleur heeft pion 1: ')
    pion1 = pion1.strip()
    while pion1 not in kegels:
        print('Deze kleur pion bestaat niet, probeer het opnieuw.')
        pion1 = input('welke kleur heeft pion 1: ')
    pionnen.append(pion1)

    pion2 = input('welke kleur heeft pion 2: ')
    pion2 = pion2.strip()
    while pion2 not in kegels:
        print('Deze kleur pion bestaat niet, probeer het opnieuw.')
        pion2 = input('welke kleur heeft pion 2: ')
    pionnen.append(pion2)

    pion3 = input('welke kleur heeft pion 3: ')
    pion3 = pion3.strip()
    while pion3 not in kegels:
        print('Deze kleur pion bestaat niet, probeer het opnieuw.')
        pion3 = input('welke kleur heeft pion 3: ')
    pionnen.append(pion3)

    pion4 = input('welke kleur heeft pion 4: ')
    pion4 = pion4.strip()
    while pion4 not in kegels:
        print('Deze kleur pion bestaat niet, probeer het opnieuw.')
        pion4 = input('welke kleur heeft pion 4: ')
    pionnen.append(pion4)

    if pionnen == codes:
        print('Gefeliciteerd je hebt het goed geraden')
        print('Je hebt het in ' + str(pogingen) + ' poging gehaald.' + '\n')
        gamemode()
    else:
        for i in range(0, len(pionnen)):
            if pionnen[i] == codes[i]:
                feedback.append('zwarte pin')
            elif pionnen[i] in codes:
                feedback.append('witte pin')
            else:
                feedback.append('geen kegel')
        random.shuffle(feedback)
        print(feedback)
        pogingen += 1
        if pogingen == 11:
            print('Helaas je hebt de code niet kunnen kraken in 10 pogingen' + '\n')
            gamemode()
        else:
            code_breken(pogingen, codes)


def code_maken():
    eigencode = []
    randcode = []
    pion1 = input('kies een kleur voor pion 1: ')
    pion1 = pion1.strip()
    while pion1 not in kegels:
        print('Deze kleur pion bestaat niet, probeer het opnieuw.')
        pion1 = input('kies een kleur voor pion 1: ')
    eigencode.append(pion1)

    pion2 = input('kies een kleur voor pion 2: ')
    pion2 = pion2.strip()
    while pion2 not in kegels:
        print('Deze kleur pion bestaat niet, probeer het opnieuw.')
        pion2 = input('kies een kleur voor pion 2: ')
    eigencode.append(pion2)

    pion3 = input('kies een kleur voor pion 3: ')
    pion3 = pion3.strip()
    while pion3 not in kegels:
        print('Deze kleur pion bestaat niet, probeer het opnieuw.')
        pion3 = input('kies een kleur voor pion 2: ')
    eigencode.append(pion3)

    pion4 = input('kies een kleur voor pion 2: ')
    pion4 = pion4.strip()
    while pion4 not in kegels:
        print('Deze kleur pion bestaat niet, probeer het opnieuw.')
        pion4 = input('kies een kleur voor pion 2: ')
    eigencode.append(pion4)
    print(eigencode)
    while len(randcode) != 4:
        randcode.append(random.choice(kegels))
    print(randcode)


gamemode()
