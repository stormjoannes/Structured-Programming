x = input('zin 1: ')
y = input ('zin 2: ')

def verschil(x, y):
    if len(x) > len(y):
        l = len(y)
    else:
        l = len(x)

    for i in range (0, l - 1):
        if x[i] != y[i]:
            print(i)
            break

verschil(x, y)