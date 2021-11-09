numero = int(input("digite um numero:"))

for i in range(1, 11):
    print(numero, 'X', i, '=', (numero * i))
    i +=1

i = 1
print('\n')
while i <= 10:
    print(numero, 'X', i, '=', (i * numero))
    i +=1