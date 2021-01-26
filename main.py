# entrada para pessoa com 18 ou + custa 30 reais
# entrada para pessoas com menos de 4 ou maior que 60 anos será gratuita
# entrada para pessoas entre 4 e 18 custará 20 reais
# estudantes e professores pagam meia


tentativas = 0
ocupação = ['estudante','professor']

while tentativas <= 2:
    digitada = input('Digite sua ocupação: ')

    if digitada == ocupação[0] or digitada == ocupação[1]:
        print('\n')
        print('a entrada será meia...')
        break

    else:
        tentativas = tentativas+1
        print('Erro durante a escrita,digite novamente (tentativa numero',tentativas,'de 3)')

    if tentativas == 3:
        print('\n')
        print('Você atingiu o limite de tentativas, reinicie por favor.')
        exit()

print('\n')


idade = int(input('Agora digite sua idade: '))

if idade < 4 or idade > 60:
    print('A entrada será gratuita')

elif idade >= 18:
    print('A entrada custará 30 reais (valor inteiro)')

elif idade >= 4 or idade <= 18:
    print('A entrada custará 20 reais (valor inteiro)')
print('\n')

if idade < 4 or idade > 60 and digitada == ocupação[0] or digitada == ocupação[1]:
    print('• Aproveite!')

elif idade >= 18 or idade == 60  and digitada == ocupação[0] or digitada == ocupação[1]:
    print('• O preço final será R$ 15.00 (por conta da meia entrada)')

elif idade >= 4 or idade <= 18 and digitada == ocupação[0] or  digitada == ocupação[1]:
    print('• O preço final será R$ 10.00 (por conta da meia entrada)')