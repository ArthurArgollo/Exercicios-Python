##Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo 
# que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58 
altura= float(input("Informe sua altura em metros: "))
##Para homens
peso_idealH=(72.7*altura) - 58
print("Seu peso ideal é de: ",peso_idealH)
##Para mulheres
peso_idealM=(62.1*altura) - 44.7 
print("Seu peso ideal é de: ",peso_idealM)