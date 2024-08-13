valores = []

while True:
    n = int(input('Digite um valor : ')) #Outra variável 'n' para que ela seja analisada no próximo 'if'

    if n not in valores:    #if para analisar se há algum valor igual na lista e que já tenha sido digitado.
        valores.append(n)   #Adiciona o valor digitado (n) na lista "valores".
    else:
        print('Erro! Valor Duplicado.')
    continuar = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if continuar == 'N':
        break
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Opção inválida. Deseja continuar? [S/N] : ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'Os valores digitados foram {sorted(valores)}')