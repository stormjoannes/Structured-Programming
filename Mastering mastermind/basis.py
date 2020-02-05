import random
spelregels = 'Er zijn 4 verschillen kleuren pionnen waar je uit kunt kiezen: blauw, Wit, rood en zwart' + \
             '\n' + \
             'Je hebt 10 beurten om het goed te raden'

def gamemode():
    pogingen = 1
    gamemode = input('Wil je de Code maken of Code breken, voor de spelregels type regels:').lower()
    if 'breken' in gamemode:
        code_breken(pogingen)
    elif 'maken' in gamemode:
        code_maken()
    elif 'regels' in gamemode:
        print(spelregels)
    else:
        print('dat is geen bestaande gamemode')

def code_breken(pogingen):
    kegels = ['rood', 'blauw', 'wit', 'zwart']
    code = []
    pionnen = []
    feedback = []

    while len(code) != 4:
        code.append(random.choice(kegels))

    pion1 = input('welke kleur heeft pion1: ')
    while pion1 not in kegels:
        print('Deze kleur pion bestaat niet, probeer het opnieuw.')
        pion1 = input('welke kleur heeft pion1: ')
    pionnen.append(pion1)

    pion2 = input('welke kleur heeft pion2: ')
    while pion2 not in kegels:
        print('Deze kleur pion bestaat niet, probeer het opnieuw.')
        pion2 = input('welke kleur heeft pion2: ')
    pionnen.append(pion2)

    pion3 = input('welke kleur heeft pion3: ')
    while pion3 not in kegels:
        print('Deze kleur pion bestaat niet, probeer het opnieuw.')
        pion3 = input('welke kleur heeft pion3: ')
    pionnen.append(pion3)

    pion4 = input('welke kleur heeft pion4: ')
    while pion4 not in kegels:
        print('Deze kleur pion bestaat niet, probeer het opnieuw.')
        pion4 = input('welke kleur heeft pion4: ')
    pionnen.append(pion4)

    if pionnen == code:
        print('Gefeliciteerd je hebt het goed geraden')
        print(pogingen)
    else:
        for i in range(0, len(pionnen)):
            if pionnen[i] == code[i]:
                feedback.append('zwarte pin')
            elif pionnen[i] in code:
                feedback.append('witte pin')
        random.shuffle(feedback)
        print(feedback)
        code_breken(pogingen += 1)

gamemode()