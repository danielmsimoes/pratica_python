import time

boletim = []
while True:
    nome = (str(input('Nome:'))).capitalize()
    nt1 = (float(input('Nota 1:')))
    nt2 = (float(input('Nota 2:')))
    media = (nt1 + nt2) / 2
    boletim.append([nome, [nt1, nt2], media])
    continuar = (input('Quer continuar [S/N]')).capitalize()
    if continuar == 'N':
        break
final = len(boletim)
print('-='*30)
print(f'{"No.":<}{"NOME":<10}{"MÉDIA":>8}')
print('-'*30)
for i, v in enumerate(boletim):
    print(f'{i:<4}{v[0]:<10}{v[2]:>8.1f}')
print('-'*30)
while True:
    interrompe = int(input('Mostrar notas de qual aluno? (999 interrompe)'))
    if interrompe == 999:
        print('Finalizando...')
        time.sleep(1.5)
        break
    if interrompe <= len(boletim) - 1:
            print(f'Notas de {boletim[interrompe][0]} são {boletim[interrompe][1]}')
            print('-'*30)
print('<<<VOLTE SEMPRE>>>')

