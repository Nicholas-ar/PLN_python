unidades = ('', 'um', 'dois', 'três', 'quatro',
            'cinco', 'seis', 'sete', 'oito', 'nove')

dez = ('dez', 'onze', 'doze', 'treze', 'quatorze',
       'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove')

dezenas = ('', 'dez', 'vinte', 'trinta', 'quarenta', 'cinquenta',
           'sessenta', 'setenta', 'oitenta', 'noventa')

centenas = ('cem', 'cento', 'duzentos', 'trezentos',
            'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos', 'novecentos')


def thousands(number, result):
    if(number > 99999):
        cent_milhar = int(number/100000)
        number = number-cent_milhar*100000
        if(number > 999):
            result += f'{centenas[cent_milhar]} e '
        elif(cent_milhar == 1):
            result += f'{centenas[0]} '
        else:
            result += f'{centenas[cent_milhar]} '

    if(number > 9999):
        dez_milhar = int(number/10000)
        number = number-dez_milhar*10000
        if(dez_milhar > 1):
            if(number > 999):
                result += f'{dezenas[dez_milhar]} e '
            else:
                result += f'{dezenas[dez_milhar]} '
        else:
            milhar = int(number/1000)
            number = number - milhar * 1000
            if(number > 999):
                result += f'{dez[milhar]} e '
            else:
                result += f'{dez[milhar]} '

    if(number > 999):
        milhar = int(number/1000)
        number = number-milhar*1000
        print(milhar)
        result += f'{unidades[milhar]} '
    result += f'mil '
    return number, result


def hundreds(number, result):
    centena = int(number/100)
    number = number-centena*100
    if(number != 0):
        result += f'{centenas[centena]} e '
    elif(centena == 1):
        result += f'{centenas[0]}'
    else:
        result += f'{centenas[centena]}'
    return number, result


number = int(input("Digite o número a ser escrito: "))
result = ''

if(number < 0):
    result += 'Menos '
    number = number*(-1)

if(number > 999):
    number, result = thousands(number, result)


if(number > 99):
    number, result = hundreds(number, result)

dezena, unidade = divmod(number, 10)

if(dezena > 1):
    result += f'{dezenas[dezena]} e {unidades[unidade]}'

elif(dezena == 1):
    result += f'{dez[unidade]}'

else:
    result += f'{unidades[unidade]}'

result = result.capitalize()
print(result)
