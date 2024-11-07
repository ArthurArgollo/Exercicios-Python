def calculo ():
    print("Calculadora basica 0.1")
    numero_1=float(input("Informe um número: "))
    numero_2=float(input("Informe um número: "))
    operação = input (
    '''
    Selecione qual operaçâo você deseja
    + (soma)
    - (subtração)
    * (multiplicação)
    / (divisão)
    '''
    )
    if operação== "+":
        resultado = numero_1+numero_2
        print("A soma = {:.2f}".format (resultado))
    elif operação== "-":
        resultado = numero_1-numero_2
        print("A subtração = {:.2f}".format (resultado))
    elif operação== "*":
        resultado = numero_1*numero_2
        print("A multiplicação = {:.2f}".format (resultado))
    elif operação== "/":
        resultado = numero_1/numero_2
        print("A divisão = {:.2f}".format (resultado))
    else:
        print("refaça")
calculo()