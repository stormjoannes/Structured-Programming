def feedback(code, poging):
    temp = []
    feedback = []
    for i in range(0, len(poging)):
        if poging[i] == code[i]:
            e = str(poging[i]) + ':' + 'zwart'
            temp.append(e)
            feedback.append('zwart')
    for i in range(0, len(poging)):
        if poging[i] in code:
            d = str(poging[i]) + ':' + 'wit'
            print(temp.count(str(poging[i]) + ':' + 'zwart') < code.count(poging[i]))
            if d not in temp and temp.count(str(poging[i]) + ':' + 'zwart') < code.count(poging[i]) and temp.count(str(poging[i]) + ':' + 'zwart') < poging.count(poging[i]):
                print(temp)
                temp.append(d)
                feedback.append('wit')
    print(temp)
    return str(feedback.count('zwart')) + ', ' + str(feedback.count('wit'))

print(feedback('3432', '3624'))