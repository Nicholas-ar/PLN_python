unidades = ('zero', 'um', 'dois', 'tres', 'quatro',
            'cinco', 'seis', 'sete', 'oito', 'nove')

dez = ('dez', 'onze', 'doze', 'treze', 'quatorze',
       'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove')

dezenas = ('zero', 'dez', 'vinte', 'trinta', 'quarenta', 'cinquenta',
           'sessenta', 'setenta', 'oitenta', 'noventa')

centenas = ('cem', 'cento', 'duzentos', 'trezentos',
            'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos', 'novecentos')

number = 209
result = ''
prefix = ''
if(number < 0):
    prefix = 'Menos'
    number = number*(-1)
dezena, unidade = divmod(number, 10)

# definir função para lidar com number<100

""" result = result.capitalize()
print(f'{result}') """

if(dezena > 1):
    print(f'{dezenas[dezena]} e {unidades[unidade]}')
elif(dezena == 1):
    print(f'{dez[unidade]}')
else:
    print(f'{unidades[unidade]}')

# {milhar},{centena}
