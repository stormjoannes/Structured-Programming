import random

kegels = ['rood', 'blauw', 'wit', 'zwart', 'geel', 'groen']
random.shuffle(kegels)
code = []
set = []
gespeeld = input('Heb je dit spel al een keer gespeeld [Y/N]: ').lower()
index = 0
hvl = 0
voorkomen = {}

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
    voorkomen.clear()
    pogingen = 1
    modus = input('Wil je de Code maken of breken: ').lower()
    if 'breken' in modus:
        code_breken(pogingen, code)
    elif 'maken' in modus:
        code_maken(pogingen, set)
    else:
        print('dat is geen bestaande gamemode, probeer het opnieuw')
        gamemode()


def code_breken(pogingen, codes):
    print('De te raden kleuren zijn: ' + '\n' + str(kegels))
    pionnen = []
    feedback = []
    while len(codes) != 4:
        codes.append(random.choice(kegels))

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
            print('De code was ' + str(code))
            gamemode()
        else:
            set.append(pionnen)
            code_breken(pogingen, codes)



def code_maken(pogingen, set):
    set.clear()
    eigencode = []
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
        pion3 = input('kies een kleur voor pion 3: ')
    eigencode.append(pion3)

    pion4 = input('kies een kleur voor pion 4: ')
    pion4 = pion4.strip()
    while pion4 not in kegels:
        print('Deze kleur pion bestaat niet, probeer het opnieuw.')
        pion4 = input('kies een kleur voor pion 4: ')
    eigencode.append(pion4)
    pc_raden(pogingen, eigencode, index, hvl, set, voorkomen)


def pc_raden(pogingen, eigencode, index, hvl, set, voorkomen):
    randcode = []
    terug = []

    if hvl <= 5 and sum(voorkomen.values()) < 4:
        print(index)
        while len(randcode) != 4:
            randcode.append(kegels[index])

        if randcode == eigencode:
            print('Helaas, de computer heeft het goed geraden in ' + str(pogingen) + ' pogingen.')
            gamemode()

        for i in range(0, len(randcode)):
            if randcode[i] == eigencode[i]:
                terug.append('zwarte pin')
            elif randcode[i] in eigencode:
                terug.append('witte pin')
            else:
                terug.append('geen kegel')
        random.shuffle(terug)
        set.append(randcode)
        hvl += 1
        if terug.count('geen kegel') == 4:
            index += 1
            pogingen += 1
            pc_raden(pogingen, eigencode, index, hvl, set, voorkomen)
        else:
            voorkomen[kegels[index]] = terug.count('zwarte pin')
            index += 1
            pogingen += 1
            pc_raden(pogingen, eigencode, index, hvl, set, voorkomen)
    else:
        lager(eigencode, pogingen, set, voorkomen)


def lager(eigencode, pogingen, set, voorkomen):
    lst = []
    for i in voorkomen:
        for a in range(0, voorkomen[i]):
            lst.append(i)
    print(lst)
    print(set)
    random.shuffle(lst)
    if lst in set:
        lager(eigencode, pogingen, set, voorkomen)
    else:
        print(lst)
        set.append(lst)
        if lst == eigencode:
            print('helaas het is geraden in ' + str(pogingen) + ' pogingen' + '\n')
            gamemode()
        else:
            pogingen += 1
            lager(eigencode, pogingen, set, voorkomen)
gamemode()