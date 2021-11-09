salario = float(input("digite o salário:"))

if salario >= 1000:
    salario = salario * 1.1
    print('O salario atual é R$ 1{:.2f}'.format(salario))
else:
    salario = salario * 1.15
    print('O salario atual é R$ {:.2f}'.format(salario))

#teste = 7.98562434234
#print('O valor de teste formatado é {:.4f}'.format(teste))