print('')
print('')
n = (str(input('Digite aqui um número de 0 ate 9999: ')).strip()).zfill(4)
print('')
print('O número possui {} unidades;'.format(n[3:4]))
print('O número possui {} dezenas;'.format(n[2:3]))
print('O número possui {} centenas;'.format(n[1:2]))
print('O número possui {} milhares;'.format(n[0:1]))
