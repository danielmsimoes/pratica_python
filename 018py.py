galera = list()
dados = list()
totmai = totmen = 0
for c in range(0, 3):
    dados.append(str(input('Nome:')))
    dados.append(int(input('Idade:')))
    galera.append(dados[:])
    dados.clear()
for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} maiores de idade e {totmen} menores de idade')


# galera = [['João', 28], ['Ana', 54], ['Enzo', 13], ['Maria', 73]]
# for p in galera:
#     print(f'{p[0]} tem {p[1]} anos de idade.')



# lista compostas
# pessoas = [['Pedro',25],['Gabriela',18],['João',34]]
# print(pessoas[0][0])
# print(pessoas[1][1])



# dados = list()
# pessoas = list()
# dados.append('Gabriel')
# dados.append(25)
# print(dados[0])
# print(dados[1])
# pessoas.append(dados[:])#juntando uma lista na outra