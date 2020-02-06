ch = '1011000'
n = int(input('geef de bitwaarde: '))
def verschuiven(ch, n):
    return ch[n:] + ch[:n]
print(verschuiven(ch, n))