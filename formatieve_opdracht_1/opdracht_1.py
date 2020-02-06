k = int(input('hoe groot:'))
for i in range (1, k + 1):
    print(i * '*')

for x in range (1, k):
    print((k - x) * '*')

print ('')

ka = 0
while ka != 5:
    ka += 1
    print(ka * '*')

j = k
while j != 0:
    j -= 1
    print(j * '*')

ko = 0
b = k
while b != 0:
    ko += 1
    b -= 1
    print(b * ' ' + (ko * '*'))

ha = k
while ha != 0:
    ha -= 1
    print((k - ha) * ' ' + (ha * '*'))


for i in range(1, k + 1):
    print((k - i) * ' ' + (i * '*'))

haak = k
for x in range(k):
    haak -= 1
    print((k - haak) * ' ' + (haak * '*'))