# Neste deasafio, devemos implementar uma lógica que filtre as transações bancárias que ultrapassam um 
# determinado limite informado pelo usuário. A entrada é composta por uma lista de transações e um valor 
# de limite. A saída deve ser uma lista com as transações que ultrapassam o limite.

def filtrar_transacoes(transacoes, limite):
    transacoes_filtradas = []

    # TODO: Itere sobre cada transação na lista:
    for valor in transacoes:
      valor_abs = abs(valor)
      if valor_abs > limite:
        transacoes_filtradas.append("valor")
    
      
        # TODO: Verifique se o valor absoluto da transação é maior que o limite:
        
            # TODO: Adicione a transação à lista filtrada:
            

    # Retorna a lista de transações filtradas
    return transacoes_filtradas


entrada = input()

entrada_transacoes, limite = entrada.split("],")
entrada_transacoes = entrada_transacoes.strip("[]").replace(" ", "") 
limite = float(limite.strip())  # Converte o limite para float


transacoes = [int(valor) for valor in entrada_transacoes.split(",")]

# TODO: Filtre as transações que ultrapassam o limite:
resultado = filtrar_transacoes(transacoes, limite)

print(f"Transações: {resultado}") 