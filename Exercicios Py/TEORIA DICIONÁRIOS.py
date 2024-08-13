dados = {'nome':'Pedro', 'Idade': 25 } #Declaração de dicionário.
print(dados['nome'], '\n', dados['Idade'])
dados['sexo'] = 'M' #ADICIONAR VALORES (NAO PRECISA .append)
del dados['Idade'] #eliminar elementos
dados.pop('Idade')
print(dados.values()) #Pega somente os VALORES.
print(dados.keys()) #Pega somente as chaves, como se fosse os "ÍNDICES"
print(dados.items()) #Pega TODOS os valores (tanto as kyes quanto os valores)

for k,v in dados.items():       #Semelhante ao enumerante
    print(f'O {k} é {v}')  # k é a KEY // v é o  VALOR
#MOSTRAR SOMENTE AS CHAVES:
for i in dados.keys():
    print(i)
for d in dados:
    print(d)
#MOSTRAR SOMENTE OS VALORES:
for d in dados:
    print(dados[d])
print(dados.values())


