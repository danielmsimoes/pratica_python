estado = dict()
brasil = list()
for c in range (0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)
# brasil = []
# estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
# brasil.append(estado1)
# brasil.append(estado2)
# print(brasil[0]['sigla'])





# pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
# pessoas['peso'] = 98.5
# del pessoas['sexo']
# for k, v in pessoas.items():
#     print(f'{k} = {v}')

# print(pessoas.keys())
# print(pessoas.items())
# print(pessoas.values())
# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')