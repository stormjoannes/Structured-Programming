import random

st = ''
set = []
for i in range(1111, 6667):
    st = str(i)
    if '0' not in st and '7' not in st and '8' not in st and '9' not in st:
        set.append(st)

def spelregels():
    "'Deze functie heb ik om het wat meer op een spel te laten lijken, hierin kun je de spelregels krijgen als je het spel nog nooit hebt gespeeld.'"
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
    "'In deze functie kies ik of ik de code wil raden of de computer de code wil laten raden.'"
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
    "'In deze functie voer ik in wat mijn gok is of wat de code moet zijn.'"
    poging = ''
    while poging not in set:
        poging = input('Wat is de code:  ')
        poging = poging.strip()
        if poging not in set:
            print('Deze codecombinatie bestaat niet, probeer het opnieuw.')
    return poging


def code_breken(pogingen, codes):
    "'In deze functie raad ik zelf de code.'"
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

#bron: 'YET ANOTHER MASTERMIND STRATEGY from Barteld Kooi, Department of Philosophy, University of Groningen, The Netherlands
def pc_raden(pogingen, set):
    "'In deze functie staat het simple strategy algorithme.'"
    eigencode = inp()


    while len(set) > 0:
        guess = set[0]
        pogingen += 1
        print('gok ' + str(pogingen) + ': ' + str(guess))
        if guess == eigencode:
            break
        reflectie = feedback(eigencode, guess)

        memorie = []
        for i in set:
            if feedback(guess, i) == reflectie:
                memorie.append(i)
        set = memorie
    if pogingen > 10:
        print('Gefeliciteerd de computer heeft het niet binnen 10 pogingen geraden!')

        print('De computer heeft er ' + str(pogingen) + ' pogingen over gedaan' + '\n')
    else:
        print('Helaas, de computer heeft het in ' + str(pogingen) + ' pogingen geraden!' + '\n')
    gamemode()

#Deze functie is deels in samenwerking met Brandon Betz
def feedback(code, poging):
    "'In deze functie geef ik hoeveel zwarte pionnen en hoeveel witte pionnen er terugkomen bij de vergelijking van de 2 parameters.'"
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