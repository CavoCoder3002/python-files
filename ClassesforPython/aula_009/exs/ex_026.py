print('')
print('')
fr = (str(input('Digite aqui uma frase: ')).strip()).upper()
print('')
na = (fr.count('A'))
a1 = (fr.find('A'))
print('A frase possui {} letras "a".'.format(na))
print('')
print('A primeira letra "a" aparece na posição {}, sendo que se for -1 não possui "a".'.format(a1))
print('')
ulta = (fr.rfind('A'))
print('E por fim, o último "a" aparece na posição {}'.format(ulta))