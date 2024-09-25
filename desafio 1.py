# Variáveis utilizadas
indice = 13
soma = 0
k = 0

# Função para realiza a soma
def soma_total():
    global k
    global soma

    k = k + 1
    soma = soma + k
    return

# Loop para garantir a execução do software até a contagem necessária
while k < indice:
    soma_total()

print(soma)