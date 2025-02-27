#Neste desafio, devemos implementar uma lógica que calcule o saldo de uma conta bancária com base em uma 
# lista de transações informadas pelo usuário. O saldo inicial da conta é zero. As transações podem ser 
# depósitos ou saques. O saldo deve ser calculado somando os valores das transações. A saída deve ser o saldo 
# formatado em moeda brasileira com duas casas decimais.

def calcular_saldo(transacoes):
    saldo = 0
    
    for valor in transacoes:
      saldo += valor
    return f"Saldo: R$ {saldo:.2f}"
    
    
    # TODO: Itere sobre cada transação na lista:
    
        # TODO: Adicione o valor da transação ao saldo
        

    # TODO: Retorne o saldo formatado em moeda brasileira com duas casas decimais:
    

entrada_usuario = "[100,-50,200]"

entrada_usuario = entrada_usuario.strip("[]").replace(" ", "")

transacoes = [float(valor) for valor in entrada_usuario.split(",")]

# TODO: Calcule o saldo com base nas transações informadas:
resultado = calcular_saldo(transacoes)

print(resultado)