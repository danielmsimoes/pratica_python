kg = float (input('Qual é o seu peso ? (kg)'))
alt = float (input('Qual é a sua altura ? (m)'))
q = alt * alt
imc = kg / q
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
# Abaixo do peso
if imc < 18.5:
    print('Você está ABAIXO DO PESO, cuidado!')

# Peso ideal
elif 18.5 <= imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL')
# Sobrepeso
elif 25 <= imc < 30:
    print('Você está em SOBREPESO')
# Obesidade
elif 30 <= imc < 40:
    print('Você está em OBESIDADE!')

# Obesidade Mórbida
else:
    print ('Você está em OBESIDADE MÓRBIDA, cuidado!')