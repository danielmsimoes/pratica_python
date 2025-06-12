s = str(input('Informe seu sexo: [M/F]')).capitalize()

while s not in 'MF':
    s = str(input('Dados inválidos. Por favor, informe seu sexo: ')).capitalize()
    if s == 'M':
        print('Sexo Masculino registrado com sucesso')

    elif s == 'F':
        print('Sexo Feminino registrado com sucesso')