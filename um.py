import re
import operator

# abre o arquivo, verifica se abriu corretamente, se sim, copia o valor para a var conteudo
input_filename = input('Insira o nome do arquivo a ser aberto com a extensão:\n')
arquivo_entrada = open(input_filename, 'r')
if arquivo_entrada.mode == 'r':
    conteudo = arquivo_entrada.read()
arquivo_entrada.close()

# deixa todas as palavras em caixa baixa
conteudo = conteudo.lower()

# separa todas as palavras e pontuação, palavras com hífen são consideradas uma única palavra
lista = re.findall(r'[\w-]+|[\w]+|[.,!?;]', conteudo)

# cria um dicionário onde a chave é a palavra, e o valor a quantidade de vezes que aparece
resultados = {}
for item in lista:
    resultados[item] = lista.count(item)

# cria uma lista ordenada de forma decrescente de acordo com a frequência que aparece
decrescente = sorted(resultados.items(),
                     key=operator.itemgetter(1), reverse=True)

# define o arquivo para a saída
output_filename = 'saida.txt'
arquivo_saida = open(output_filename, 'w')

# percorre a lista ordenada para adicionar ao terminal e ao arquivo de saída
for item in decrescente:
    print(item[0])
    arquivo_saida.write('%s\n' % item[0])
arquivo_saida.close()
