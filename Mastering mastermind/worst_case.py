import random

st = ''
set = []
for i in range(1111, 6667):
    st = str(i)
    if '0' not in st and '7' not in st and '8' not in st and '9' not in st:
        set.append(st)
copy = set

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
    pogingen = 1
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
    if len(eigencode) < 4:
        while eigencode not in set:
            eigencode = input('Wat is de code:  ')
            eigencode = eigencode.strip()
            if eigencode not in set:
                print('Deze kleur codecombinatie bestaat niet, probeer het opnieuw.')
    guess = random.choice(set)
    print(guess)
    print(len(set))
    print(set)
    pogingen += 1
    if guess == eigencode:
        print('Helaas, de computer heeft het in ' + str(pogingen) + ' pogingen geraden!')
        set = copy
        gamemode()
    reflectie = feedback(eigencode, guess)
    print(reflectie)
    print('guess: ', guess)
    for i in set:
        print('i ', i)
        if feedback(guess, i) != reflectie:
            set.remove(i)

    pc_raden(pogingen, set, eigencode)


def feedback(code, poging):
    feedback = {'zwart': 0, 'wit': 0}
    for i in range(0, len(poging)):
        if code[i] == poging[i]:
            feedback['zwart'] = + 1
        elif code[i] in poging:
            feedback['wit'] = + 1
    return feedback

gamemode()