##Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.

int1=int(input("Informe um numero inteiro: "))
int2=int(input("Informe outro numero inteiro: "))
real=float(input("informe um numero real: "))

## O produto do dobro do primeiro com metade do segundo.
dobro = int1*2
metade = int2/2
print("O produto do dobro do primeiro é:",dobro,"e a metade do segundo é: ",metade)
#a soma do triplo do primeiro com o terceiro.
triplo= int1*3
soma= triplo + real
print("A soma do triplo do primeiro com o terceiro é: ",soma)
#o terceiro elevado ao cubo
cubo= real**3
print("O terceiro elevado ao cubo é: ",cubo)
