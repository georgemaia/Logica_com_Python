frase = input('Digite uma frase: ').strip().lower()

print('A letra A aparece {} vezes na frase'.format(frase.count('a')))
print('A primeira letra A aparececeu na posisão {}'.format(frase.find('a')+1))
print('A última letra A aparececeu na posisão {}'.format(frase.rfind('a')+1))