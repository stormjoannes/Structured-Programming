import random
kegels = ['rood', 'blauw', 'wit', 'zwart']
code = []
while len(code) != 4:
    code.append(random.choice(kegels))

def gamemode():
    pogingen = 1
    modus = input('Wil je de Code maken of Code breken, voor de spelregels type regels: ').lower()
    if 'breken' in modus:
        code_breken(pogingen, code)
    elif 'maken' in modus:
        code_maken()
    elif 'regels' in modus:
        spelregels = 'Er zijn 4 verschillen kleuren pionnen waar je uit kunt kiezen: blauw, Wit, rood en zwart' + \
                     '\n' + \
                     'Je hebt 10 beurten om het goed te raden' + '\n'
        print(spelregels)
        gamemode()
    else:
        print('dat is geen bestaande gamemode')
        gamemode()

def code_breken(pogingen, code):
    pionnen = []
    feedback = []
    print(code)

    print('Je hebt nog ' + str(11 - pogingen) + ' pogingen over.')

    pion1 = input('welke kleur heeft pion 1: ')
    pion1 = pion1.strip()
    while pion1 not in kegels:
        print('Deze kleur pion bestaat niet, probeer het opnieuw.')
        pion1 = input('welke kleur heeft pion1: ')
    pionnen.append(pion1)

    pion2 = input('welke kleur heeft pion 2: ')
    pion2 = pion2.strip()
    while pion2 not in kegels:
        print('Deze kleur pion bestaat niet, probeer het opnieuw.')
        pion2 = input('welke kleur heeft pion2: ')
    pionnen.append(pion2)

    pion3 = input('welke kleur heeft pion 3: ')
    pion3 = pion3.strip()
    while pion3 not in kegels:
        print('Deze kleur pion bestaat niet, probeer het opnieuw.')
        pion3 = input('welke kleur heeft pion3: ')
    pionnen.append(pion3)

    pion4 = input('welke kleur heeft pion 4: ')
    pion4 = pion4.strip()
    while pion4 not in kegels:
        print('Deze kleur pion bestaat niet, probeer het opnieuw.')
        pion4 = input('welke kleur heeft pion4: ')
    pionnen.append(pion4)

    if pionnen == code:
        print('Gefeliciteerd je hebt het goed geraden')
        print('Je hebt het in ' + str(pogingen) + ' poging gehaald.')
        gamemode()
    else:
        for i in range(0, len(pionnen)):
            if pionnen[i] == code[i]:
                feedback.append('zwarte pin')
            elif pionnen[i] in code:
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
            code_breken(pogingen, code)

gamemode()