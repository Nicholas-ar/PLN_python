import re

#função recursiva que imprime todas as combinações possíveis de quebra de uma frase
#cada combinação é delimitada por colchetes: []
def recursao(frase, index, saida):
    if(len(frase) == index):
        saida = saida[:-1]
        saida+=']'
        print(saida)
    
    j = len(frase)-1

    while(j >= index):
        temp = index
        outra_palavra = "'"
        while(temp <= j):
            outra_palavra += f'{frase[temp]} '
            temp += 1
        outra_palavra = outra_palavra[:-1]
        outra_palavra += "',"
        recursao(frase, j+1, f"{saida}{outra_palavra}")
        j -= 1


frase = input("Insira uma frase a ser analisada:\n")

# separa todas as palavras e pontuação, palavras com hífen são consideradas uma única palavra
lista = re.findall(r'[\w-]+|[\w]+|[.,!?;]', frase)

print('As combinações possíveis com essa frase são:\n')
    
recursao(lista, 0, '[')