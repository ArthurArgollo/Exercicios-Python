##Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da 
# área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a 
# tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de 
# tinta a serem compradas e o preço total. 

area=float(input("Informe o tamanho da area em metro quadrados: "))
preço = 80
cobertura_tinta = 54
if area <= 54:
    print("Você deve comprar 1 lata de tinta e isso vai te custar 80 reais")
else:
    quantidade = int(area/cobertura_tinta)
    preço_total=preço*quantidade
    print("Você deve comprar",quantidade," latas de tintas e isso vai te custar",preço_total)
