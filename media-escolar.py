ficha = list()
while True:
  nome = str(input('Nome: '))
  nota1 = float(input('Nota 1: '))
  nota2 = float(input('Nota 2: '))
  media = (nota1 + nota2) / 2
  ficha.append([nome, [nota1, nota2], media])
  resp = str(input('Quer continuar? S/N?'))
  if resp in 'Nn':
    break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>9}')
print('-'*26)
for i, a in enumerate(ficha):
  print(f'i{i:<3}{a[0]:<10}{a[2]:>8.1f}')