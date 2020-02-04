#ik zag het nut van opdr 4 om een built in function te gebruiken niet in maar ik dacht ik gebruik reverse wel op een rare manier.
def palindroome():
    x = input('geef een woord: ')
    lst = []
    for i in x:
        lst.append(i)
    lst.reverse()
    lstheel = []
    for i in x:
        lstheel.append(i)
    if lst == lstheel:
        return 'Wel een palindroom'
    else:
        return 'Niet een palindroom'
print(palindroome())

print('')

def palindroom():
    x = input('geef een woord: ')
    a = x[::-1]
    if a == x:
        return 'Wel een palindroom'
    else:
        return 'Niet een palindroom'
print(palindroom())
