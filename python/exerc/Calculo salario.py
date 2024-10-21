##Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.
hora_Ganha=float(input("Informe seu salario ganho por hora: "))
Horas= float(input("Quantas horas voce trabalha: "))
salario = (hora_Ganha*Horas)*25
print("Você recebe",salario,"R$")