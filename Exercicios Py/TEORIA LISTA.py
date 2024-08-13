lista = [0, 2, 4, 7]
lista.append(3) #para adicionar números (apenas na última posição)
lista.insert(5, 5) #para inserir e ADICIONAR números em QUALQUER posição
                                  #OBS : VÁLIDO APENAS PARA INDEX.

lista[2] = 4 #SUBSTITUI o valor naquela posição por outro.

if 0 in lista:          #If para verificar se há algum número na lista e removê-lo.
    lista.remove(0)
    print(f'\n\nA lista sem o valor 0 fica {lista}')
    print(f'Modificando o total de posições para {len(lista)} posições.')
else:
    print(f'\n\nNão encontrei o valor 0 em sua lista')

print(lista)
print(f'a sua lista tem {len(lista)} elementos') # len(x) - PARA INFORMAR QUANTOS/AS POSIÇÕES, INDEX, EXISTEM NA LISTA.

print(f'Os valores presentes na sua lista são : ')
for v in lista:    # for para escrever de maneira "limpa" somente os valores da lista, através da variável de controle "v".
    print(f'{v}', end =' ')
print('\n\n')

del lista #apaga todos os valores da lista.
lista = []
for cont in range(0,5):     #FOR para o usuário ler valores e armazenar-los dentro da lista.
    lista.append(int(input('Digite um valor : ')))
#AGORA
#PARA INFORMAR O ÍNDICE E O VALOR DA LISTA, É NECESSÁRIO UM "FOR" COM DUAS VARIÁVEIS DE CONTROLE
#EX :
for i, v in enumerate(lista):   #Destaque para a importância do "enumerate()", uma vez que ele pega tanto a posição (a chave) quanto o valor.
                                # Primeira variável i para índice // Segunda variável v para demonstrar o valor.
    print(f'O valor correspondente na posição {i} é o elemento {v}')
print(f'Havendo assim o total de {len(lista)} posições.\n\n')

#LIGAÇÃO entre listas
a = [2, 3, 4 , 7]
b = a
print(f'Ligação\na lista b : {b} \na lista a : {a} \n\n')

#CÓPIA de uma lista
a = [2, 3, 4 , 7]
b = a[:]    #Técnica de fatiamento para pegar somente os valores da lista "a" e jogar-los para lista "b".
b[2] = 0
print(f'Cópia\nlista b : {b} \nlista a : {a}')








