dados_times_brasileirao = (
    ("Fortaleza", 48, 14, 3),
    ("Botafogo", 47, 14, 5),
    ("Palmeiras", 44, 14, 5),
    ("Flamengo", 44, 13, 5),
    ("São Paulo", 41, 12, 5)
)

for time in dados_times_brasileirao:
    print(f"Time: {time[0]}, Pontos: {time[1]}, Vitórias: {time[2]}, Derrotas: {time[3]}")

#  desempenho_times_brasileirao = [
#     ("Fortaleza", 48, 14, 3),
#     ("Botafogo", 47, 14, 5),
#     ("Palmeiras", 44, 14, 5),
#     ("Flamengo", 44, 13, 5),
#     ("São Paulo", 41, 12, 5)
# ]

# taxa_pontos = []
# for time, pontos, vitorias, derrotas in desempenho_times_brasileirao:
#     taxa = pontos / (pontos + derrotas)
#     taxa_pontos.append((time, taxa))
# taxa_derrotas = []
# for time, pontos, vitoria, derrotas in desempenho_times_brasileirao:
#     taxas = derrotas/ (derrotas + pontos)
#     taxa_derrotas.append((time,taxas))

# maior_taxa = taxa_pontos[0]
# menor_taxa = taxa_pontos[0]

# print("Taxa de pontos por equipe:")
# for time, taxa in taxa_pontos:
#     print(f"{time}: {taxa:.2f}")

# maior_taxa = taxa_pontos[0]
# menor_taxa = taxa_pontos[0]

# for time, taxa in taxa_pontos:
#     if taxa > maior_taxa[1]:
#         maior_taxa = (time, taxa)
#     if taxa < menor_taxa[1]:
#         menor_taxa = (time, taxa)

# maior_taxa_derrota = taxa_derrotas[0]
# menor_taxa_derrota = taxa_derrotas[0]
# for time, taxa in taxa_derrotas:
#     if taxa > maior_taxa_derrota[1]:
#         maior_taxa_derrota = (time, taxa)
#     if taxa < menor_taxa_derrota[1]:
#         menor_taxa_derrota = (time, taxa)


# print(f"O time com a maior taxa é o: {maior_taxa[0]} com taxa {maior_taxa[1]:.2f}")
# print(f"O time com a menor taxa é o: {menor_taxa[0]} com taxa {menor_taxa[1]:.2f}")

# print(f"O time com a maior taxa de derrota é o: {maior_taxa_derrota[0]} com taxa {maior_taxa_derrota[1]:.2f}")
# print(f"O time com a menor taxa de derrota é o: {menor_taxa_derrota[0]} com taxa {menor_taxa_derrota[1]:.2f}")