lst = [4, 6, 6, 2, 5, 4, 7, 1, 2, 3, 9, 4, 5, 7, 4, 2, 1, 1, 1, 6, 5]
def sort(lst):
    lengte = len(lst)
    for i in range(lengte):
        for x in range(lengte - i - 1):
            if lst[x] > lst[x + 1]:
                lst[x], lst[x + 1] = lst[x + 1], lst[x]
    return lst
print(sort(lst))