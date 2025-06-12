import time
n1 = int(input('Primeiro valor:'))
n2 = int(input('Segundo valor:'))
escolha = 0
while escolha != 5:
    print("""
        [ 1 ] somar
        [ 2 ] multiplicar 
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa""")
    escolha = (int(input('>>>>> Qual é a sua opção ?')))

    if escolha == 1:
        soma = n1 + n2
        print (f'A soma entre {n1} + {n2} é {soma}')
    elif escolha == 2:
        multiplicacao = n1 * n2
        print (f'O resultado entre {n1} x {n2} é {multiplicacao}')
    elif escolha == 3:
        if n1 > n2:
            maior = n1
        elif n1 < n2:
            maior = n2
        print(f'Entre {n1} e {n2} o maior é {maior}')

    elif escolha == 4:
        print('Informe os números novamente')
        n1 = int(input('Primeiro valor:'))
        n2 = int(input('Segundo valor:'))
    elif escolha == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('-==-' * 10)
    time.sleep(2) #se aplica a tudo no while acima
    
print('Fim do programa! Volte sempre!')
exit()
