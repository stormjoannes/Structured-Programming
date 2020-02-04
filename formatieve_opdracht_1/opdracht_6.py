lst = [4, 6, 6, 2, 5, 4, 7, 1, 2, 3, 9, 4, 5, 7, 4, 2, 1, 1, 1, 6, 5]
lst1 = [3, 6, 6, 8, 7, 4, 5, 3, 1, 9, 7]
lst2 = [4, 6, 8, 2, 4, 7, 6, 5, 1, 3, 5, 4, 8, 7, 9, 4, 6]
lst3 = [6, 5, 4, 7, 8, 1, 2, 3, 4, 8, 7, 6, 6, 5, 4]
lst4 = [7, 5, 8, 4, 2, 3, 1, 2, 8, 9, 9, 3, 2, 7, 5, 8, 5]
lst5 = [4, 1, 5, 9, 7, 3, 6, 4]
lstot= [lst, lst1, lst2, lst3, lst4, lst5]
def gemiddelde(lst):
    sum = 0
    for i in lst:
        sum += i
    gem = sum / len(lst)
    gemi = sum // len(lst)

    return gem, 'afgerond ' + str(gemi)
print('gemiddelde: ' + str(gemiddelde(lst)))

def gemlst():
    for i in lstot:
        ge = gemiddelde(i)
        print('gemiddelde van ' + str(i) + ' is ' + str(ge))
gemlst()