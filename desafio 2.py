def pertence_fibonacci(n):
    # Inicializa os primeiros números da sequência de Fibonacci
    a, b = 0, 1
    
    # Verifica se o número já é 0 ou 1, que pertencem à sequência
    if n == 0 or n == 1:
        return True
    
    # Gera a sequência até encontrar ou ultrapassar o número informado
    while b <= n:
        if b == n:
            return True
        a, b = b, a + b
    
    return False

# Aqui você pode definir o número manualmente ou usar uma entrada do usuário
numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

# Verifica e exibe a mensagem correspondente
if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")
