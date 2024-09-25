import json

# Carrega o arquivo JSON com os dados de faturamento
with open('arquivo.json', 'r') as arquivo:
    dados = json.load(arquivo)

# Filtra os dias com faturamento maior que 0
faturamentos = [dia['faturamento'] for dia in dados if dia['faturamento'] > 0]

# Calcula menor e maior faturamento
menor_faturamento = min(faturamentos)
maior_faturamento = max(faturamentos)

# Calcula a média de faturamento
media_faturamento = sum(faturamentos) / len(faturamentos)

# Conta quantos dias o faturamento foi maior que a média
dias_acima_media = sum(1 for faturamento in faturamentos if faturamento > media_faturamento)

# Exibe os resultados
print(f"Menor faturamento: {menor_faturamento}")
print(f"Maior faturamento: {maior_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
