n = int(input('wat is n: '))
x = [0, 1]

def fibonaci(n):
    if n == 1:
        print(x[1])
        return
    som = sum(x)
    x[0] = x[1]
    x[1] = som
    fibonaci(n - 1)
fibonaci(n)