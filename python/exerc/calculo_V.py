salario=float(input("Adicione o salario: "))
Fgts=0.08 * salario
Inss= 0.09 * salario
salario_liquido = salario - (Fgts+Inss)
print("Fgts:",Fgts)
print("Inss:",Inss)
print("Salario liquido:",salario_liquido)
