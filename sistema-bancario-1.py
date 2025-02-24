menu = """
================= BANCO DEVPRO =================
Selecione uma opção:
[1] Depositar
[3] Sacar
[5] Extrato
[0] Sair
================================================
=> """

saldo = 0 #Saldo inicial da conta
limite = 500 #Limite de saque
extrato = "" 
numero_saques = 0 #número inicial de saques diários realizados
LIMITE_SAQUES = 3 #Limite de saques diários

while True: #Loop infinito até que o usuário escolha a opção de sair

    opcao = input(menu)

    if opcao == "1": #Depositar
        try:
            valor = float(input("Digite o valor do depósito: "))
            if valor <= 0:
                print("O valor precisa ser maior que zero. Tente novamente.")
                continue
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado.")
            continue
        
        except ValueError:
            print("\n***Entrada inválida! Digite apenas números.***\n***Tente novamente.***")
            continue

    elif opcao == "3": #Sacar
        if numero_saques >= LIMITE_SAQUES: #Verifica se o número de saques diários é maior ou igual ao limite de saques diários
            print("Não é possível realizar essa operação. Limite de saques diários atingido.")
            continue
        valor = float(input("Digite o valor do saque: "))
        if valor <= 0: #Verifica se o valor é negativo ou zero
            print("O valor precisa ser maior que zero. Tente novamente.")
            continue
        if valor > limite: #Verifica se o valor do saque é maior que o limite de saque
            print("Erro. Valor maior que o limite de saque. Tente novamente.")
            continue
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado.")
    
    elif opcao == "5": #Extrato
        print("\n========Extrato========")
        if extrato == "":
            print("\n**Nenhuma operação realizada ainda.**\n")
            print("=====Fim do extrato=====\n")
            continue
        print(f"Saldo: R$ {saldo:.2f}")
        print(extrato)

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
