# Função para inverter uma string
def inverter_string(s):
    string_invertida = ""
    
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    return string_invertida

# Entrada do usuário ou string pré-definida
entrada = input("Digite uma string para inverter: ")

# Chama a função e exibe o resultado
resultado = inverter_string(entrada)
print(f"String invertida: {resultado}")
