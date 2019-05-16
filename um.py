import re

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
