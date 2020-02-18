import random

st = ''
set = []
for i in range(1111, 6667):
    st = str(i)
    if '0' not in st and '7' not in st and '8' not in st and '9' not in st:
        set.append(st)
code = []
hat = []
voorkomen = {}

def spelregels():
    gespeeld = input('Heb je dit spel al een keer gespeeld [Y/N]: ').lower()
    if 'n' == gespeeld:
        regels = '---SPELREGELS---' + \
                     '\n' + \
                     'Er zijn 6 verschillen getallen waar je uit kunt kiezen, 1 t/m 6.' + \
                     '\n' + \
                     'Je hebt 10 beurten om het goed te raden, haal je ndit niet heb je verloren.' + \
                     '\n' + \
                     'Zodra een getal op de goede plek staat en het goede getal is komt er een zwart pinnetje te staan.' + \
                     '\n' + \
                     'Zodra een getal niet op de goede plek staat, maar als het getal wel in de code voorkomt ' + \
                     'krijg je een wit pinnetje erbij.' + \
                     '\n' + \
                     'Als je de code hebt geraden heb je gewonnen.' + \
                     '\n' + \
                     'Hoe minder pogingen je er over doet, hoe beter je bent.' + \
                     '\n' + \
                     'Van de feedback is het eerste getal de zwarte pion en het tweede getal de witte pion. ' + \
                     '\n' + \
                     'Bijv: 1, 2. Dit betekent 1 zwarte pion en 2 witte pionnen.' + \
                     '\n'
        print(regels)
        gamemode()
    elif 'y' == gespeeld:
        print('\n')
        gamemode()
    else:
        print('Dit is geen geldige optie, probeer het opnieuw.' + '\n')
        spelregels()


def gamemode():
    pogingen = 0
    modus = input('Wil je de code maken of breken: ').lower()
    if 'breken' in modus:
        print('De te raden getallen zijn: ' + '1 t/m 6. ')
        code = []
        code_breken(pogingen, code)
    elif 'maken' in modus:
        pc_raden(pogingen, set)
    else:
        print('dat is geen bestaande gamemode, probeer het opnieuw')
        gamemode()

def inp():
    poging = ''
    while poging not in set:
        poging = input('Wat is de code:  ')
        poging = poging.strip()
        if poging not in set:
            print('Deze codecombinatie bestaat niet, probeer het opnieuw.')
    return poging


def code_breken(pogingen, codes):
    if len(codes) < 4:
        codes = random.choice(set)
    print('Je hebt nog ' + str(10 - pogingen) + ' pogingen over.')
    pogingen += 1

    poging = inp()

    if poging == codes:
        print('Gefeliciteerd je hebt het goed geraden')
        print('Je hebt het in ' + str(pogingen) + ' poging gehaald.' + '\n')
        gamemode()
    else:
        terugslag = feedback(codes, poging)
        print('Feedback: ' + str(terugslag))

        if pogingen == 10:
            print('Helaas je hebt de code niet kunnen kraken in 10 pogingen')
            print('De code was ' + str(codes) + '\n')
            gamemode()
        else:
            code_breken(pogingen, codes)


def pc_raden(pogingen, set):
    index = 0
    eigencode = inp()

    randcode = []
    lst = []
    while index <= 5 and sum(voorkomen.values()) < 4:
        for i in range(1, 7):
            while len(randcode) < 4:
                randcode.append(str(i))

            index += 1
            pogingen += 1
            print('Gok ' + str(pogingen) + ': ' + str(''.join(randcode)))
            if randcode == eigencode:
                print('Helaas, de computer heeft het goed geraden in ' + str(pogingen) + ' pogingen.' + '\n')
                gamemode()

            rand_2 = ''.join(randcode)
            reflectie = feedback(eigencode, str(rand_2))
            hat.append(rand_2)
            if reflectie != '0, 0':
                voorkomen[i] = int(reflectie[0])
            randcode.clear()

    lst_2 = ''
    lst = []
    while lst_2 != eigencode:
        lst.clear()
        for h in voorkomen:
            for a in range(0, voorkomen[h]):
                lst.append(str(h))
        random.shuffle(lst)
        lst_2 = ''.join(lst)
        while lst_2 in hat:
            random.shuffle(lst)
            lst_2 = ''.join(lst)
        pogingen += 1
        hat.append(lst_2)
        print('Gok ' + str(pogingen) + ': ' + str(lst_2))
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
spelregels()