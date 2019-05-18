unidades = ('zero', 'um', 'dois', 'tres', 'quatro',
            'cinco', 'seis', 'sete', 'oito', 'nove')

dez = ('dez', 'onze', 'doze', 'treze', 'quatorze',
       'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove')

dezenas = ('zero', 'dez', 'vinte', 'trinta', 'quarenta', 'cinquenta',
           'sessenta', 'setenta', 'oitenta', 'noventa')

centenas = ('cem', 'cento', 'duzentos', 'trezentos',
            'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos', 'novecentos')

number = int(input("Digite o número a ser escrito: "))
result = ''
prefix = ''

if(number < 0):
    prefix = 'Menos '
    number = number*(-1)
dezena, unidade = divmod(number, 10)

# definir função para lidar com number<100


if(dezena > 1):
    result = prefix + f'{dezenas[dezena]} e {unidades[unidade]}'

elif(dezena == 1):
    result = prefix + f'{dez[unidade]}'


else:
    result = prefix + f'{unidades[unidade]}'

result = result.capitalize()
print(result)


# {milhar},{centena}
