ch = '1011000'
n = int(input('geef een bitwaarde: '))
def verschuiven(ch, n):
    return ch[n:] + ch[:n]
print(verschuiven(ch, n))