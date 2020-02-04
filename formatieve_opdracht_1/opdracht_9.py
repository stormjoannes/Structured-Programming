# ch = int(input('geef de lijst: '))
ch = '1011000'
n = int(input('geef de bitwaarde: '))

def verschuiven(ch, n):
    if n < 0:
        return ch[n:] + ch[:n]
    else:
        return ch[n:] + ch[:n]
print(verschuiven(ch, n))