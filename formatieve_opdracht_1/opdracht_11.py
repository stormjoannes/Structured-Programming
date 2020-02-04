alfabet = 'abcdefghijklmnopqrstuvwxyz'
x = input('geef een tekst: ')
y = int(input('geef een rotatie: '))
s = ''
for i in x:
    if i not in alfabet:
        s += i
    else:
        for z in range(0, len(alfabet)):
            if alfabet[z] == i:
                samen = z + y
                if samen > len(alfabet) - 1:
                    over = samen - len(alfabet)
                    s += alfabet[over]
                else:
                    s += alfabet[samen]
print(s)

