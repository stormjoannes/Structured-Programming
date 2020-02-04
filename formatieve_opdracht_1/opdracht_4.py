# def palindroome():
#     x = input('geef een woord: ')
#     a = x.reverse()
#     if a == x:
#         return 'Wel een palindroom'
#     else:
#         return 'Niet een palindroom'
# print(palindroome())

print('')

def palindroom():
    x = input('geef een woord: ')
    a = x[::-1]
    if a == x:
        return 'Wel een palindroom'
    else:
        return 'Niet een palindroom'
print(palindroom())
