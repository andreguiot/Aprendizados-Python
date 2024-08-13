# Declara a matriz 3x3 com valores inicializados como zero
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = somacoluna = maiorvalor = 0
# Preenche a matriz com valores do usuário
for i in range(0,3):
    for j in range(0,3):
        matriz[i][j] = int(input(f'Digite um valor para [{i},{j}] : '))
        if matriz[i][j] % 2 == 0:
            soma += matriz[i][j]
        if j == 2:
            somacoluna += matriz[i][j]
    if i == 1 and maiorvalor < matriz[i][j]:
        maiorvalor = matriz[i][j]

# Exibe a matriz na tela
print('-=' * 30)
print("Matriz 3x3:")
for linha in matriz:
    print(linha)
print('-=' * 30)
print(f'A soma dos números pares da matriz é {soma}')
print(f'A soma dos valores da terceira coluna é {somacoluna}')
print(f'O maior valor da segunda linha é {maiorvalor}')