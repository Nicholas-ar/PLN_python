import re
import operator

# abre o arquivo, verifica se abriu corretamente, se sim, copia o valor para a var content
#filename = 'corpus-sentence-pt-br.txt'
filename = 'a.txt'
f = open(filename, 'r')
if f.mode == 'r':
    content = f.read()
f.close()

# deixa todas as palavras em caixa baixa
content = content.lower()

#separa todas as palavras e pontuação, palavras com hífen são consideradas uma única palavra
lista = re.findall(r'[\w-]+[\w]+|[.,!?;]', content)

#cria um dicionário onde a chave é a palavra, e o valor a quantidade de vezes que aparece
resultados = {}
for item in lista:
    resultados[item] = lista.count(item)
