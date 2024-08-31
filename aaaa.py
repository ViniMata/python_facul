dados_times_brasileirao = (
    ("Fortaleza", 48, 14, 3),
    ("Botafogo", 47, 14, 5),
    ("Palmeiras", 44, 14, 5),
    ("Flamengo", 44, 13, 5),
    ("São Paulo", 41, 12, 5)
)

dados_2_times_brasileirao = (
    ("Fluminense", 24, 6, 6),
    ("Vitória", 22, 6, 4),
    ("Corinthians", 22, 4, 10),
    ("Cuiabá", 18, 4, 6),
    ("Atlético-GO", 18, 4, 6)
)

dados_novos = dados_times_brasileirao + dados_2_times_brasileirao

dados_novos

lista_dados = [list(item) for item in dados_novos]


lista_dados[5][1] = 28
lista_dados[5][2] = 7
lista_dados[5][3] = 7

print(lista_dados)

soma_pontos = 0
soma_vitorias = 0
soma_derrotas = 0

for i in dados_novos:
    time, pontos, vitorias, derrotas = i
    soma_pontos += pontos
    soma_vitorias += vitorias
    soma_derrotas += derrotas

print(soma_pontos)
print(soma_vitorias)
print(soma_derrotas)