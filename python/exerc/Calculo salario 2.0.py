##Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são 
# descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

##salário bruto
hora_Ganha=float(input("Informe seu salario ganho por hora: "))
Horas= float(input("Quantas horas voce trabalha: "))
salario = (hora_Ganha*Horas)*25
print("Você recebe",salario,"R$")

#Quanto pagou ao INSS
Inss= 0.08*salario
print("Voce pagou ao inss: ",Inss)

#quanto pagou ao sindicato.
Sindicato = 0.05 * salario
print("Voce pagou ao sindicato: ",Sindicato)

#Imposto de Renda
Ir= 0.11*salario
#o salário líquido
salario_liquido = salario - (Ir+ Sindicato+Inss)
print("O valor do salario liquido é de: ",salario_liquido)