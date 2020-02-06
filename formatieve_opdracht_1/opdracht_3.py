lst = [4, 6, 6, 2, 5, 4, 7, 1, 2, 3, 9, 4, 5, 7, 4, 2, 1, 1, 1, 6, 5]
x = int(input('welk nummer: '))
def count(x, lst):
    if x in lst:
        y = (lst.count(x))
        return y
    else:
        return 0
print('Count: ' + str(count(x, lst)))

print('')
def verschil():
    x = 0
    for i in range(0, len(lst) - 1):
        if lst[i] > lst[i + 1]:
            grootste = lst[i]
            kleinste = lst[i + 1]
        else:
            grootste = lst[i + 1]
            kleinste = lst[i]

        vers = grootste - kleinste
        if vers > x:
            x = vers
    return x
print('Verschil: ' + str(verschil()))

print('')

list = [1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0]
def voldoen():
    if (count(1, list) > count(0, list)) and count(0, list) <= 12:
        return 'voldoet wel'
    else:
        return 'voldoet niet'
print(voldoen())
