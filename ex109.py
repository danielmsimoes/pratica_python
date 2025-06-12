from ex111.utilidadescev import moeda
n = float(input('Digite o preço: R$'))
print(f'A metade de R${moeda.moeda(n)} é R${moeda.metade(n, True)}')
print(f'O dobro de R${moeda.moeda(n)} é R${moeda.dobro(n, True)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(n, 10, True)}')
print(f'Reduzindo 10%, temos R${moeda.diminuir(n, 10, True)}')