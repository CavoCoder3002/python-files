print('')
print('')
name = (str(input('Digite aqui seu nome completo: ')).strip()).split()
print('')
print('Seu primeiro nome é: {}'.format(name[0]))
print('Seu último sobrenome é: {}'.format(name[len(name)-1]))