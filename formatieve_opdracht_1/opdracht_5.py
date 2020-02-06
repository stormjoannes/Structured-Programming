lst = [4, 6, 6, 2, 5, 4, 7, 1, 2, 3, 9, 4, 5, 7, 4, 2, 1, 1, 1, 6, 5]
#bij deze opdracht heb ik twee methodes gebruikt. Eentjes met swappen die we bij een ander vak al hadden gemaakt, en eentje waarbij je een nieuwe lijst creëert en met minimaal werkt.
def sort(lst):
    lengte = len(lst)
    for i in range(lengte):
        for x in range(lengte - i - 1):
            if lst[x] > lst[x + 1]:
                lst[x], lst[x + 1] = lst[x + 1], lst[x]
    return lst
print(sort(lst))

def asort(lst):
    nlst = []
    while (len(lst) != 0):
        for i in range(0, len(lst)):
            if i == 0:
                min = lst[i]
            else:
                if lst[i] < min:
                    min = lst[i]
        nlst.append(min)
        lst.remove(min)
    return nlst
print(asort(lst))
