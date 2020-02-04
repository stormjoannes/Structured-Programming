lst = [4, 6, 6, 2, 5, 4, 7, 1, 2, 3, 9, 4, 5, 7, 4, 2, 1, 1, 1, 6, 5]
def gemiddelde(lst):
    sum = 0
    for i in lst:
        sum += i
    gem = sum / len(lst)
    gemi = sum // len(lst)
    return gem, gemi
print('gemiddelde: ' + str(gemiddelde(lst)))