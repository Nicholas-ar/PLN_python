unidades = ('', 'um', 'dois', 'três', 'quatro',
            'cinco', 'seis', 'sete', 'oito', 'nove')

dez = ('dez', 'onze', 'doze', 'treze', 'quatorze',
       'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove')

dezenas = ('', 'dez', 'vinte', 'trinta', 'quarenta', 'cinquenta',
           'sessenta', 'setenta', 'oitenta', 'noventa')

centenas = ('cem', 'cento', 'duzentos', 'trezentos',
            'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos', 'novecentos')


def billions(number, result):
    new_number = int(number/1000000000)
    if(new_number > 1):
        sufix = 'bilhões'
    else:
        sufix = 'bilhão'
    if(new_number > 99):
        new_number, result = hundreds(new_number, result)
    new_number, result = tens(new_number, result)
    number = number % 1000000000
    result += f' {sufix} '
    return number, result


def millions(number, result):
    new_number = int(number/1000000)
    if(new_number > 1):
        sufix = 'milhões'
    else:
        sufix = 'milhão'
    if(new_number > 99):
        new_number, result = hundreds(new_number, result)
    new_number, result = tens(new_number, result)
    number = number % 1000000
    result += f' {sufix} '
    return number, result


def thousands(number, result):
    new_number = int(number/1000)
    if(new_number > 99):
        new_number, result = hundreds(new_number, result)
    new_number, result = tens(new_number, result)
    number = number % 1000
    result += f' mil '
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


def tens(number, result):
    dezena, unidade = divmod(number, 10)
    if(dezena > 1 and unidade > 0):
        result += f'{dezenas[dezena]} e {unidades[unidade]}'
    elif(dezena > 1):
        result += f'{dezenas[dezena]} '
    elif(dezena == 1):
        result += f'{dez[unidade]}'
    else:
        result += f'{unidades[unidade]}'
    return number, result


number = int(input("Digite o número a ser escrito: "))
result = ''

if(number < 0):
    result += 'Menos '
    number = number*(-1)

if(number == 0):
    result += 'Zero '

if(number > 999999999):
    number, result = billions(number, result)

if(number > 999999):
    number, result = millions(number, result)

if(number > 999):
    number, result = thousands(number, result)

if(number > 99):
    number, result = hundreds(number, result)

number, result = tens(number, result)

result = result.capitalize()
print(result)
