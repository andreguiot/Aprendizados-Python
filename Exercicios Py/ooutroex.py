dic = {
    "nome": 'Andre',
    "sobrenome": 'De Martin Guiot',
    "idade": '19',
    "endereço": [
        {"rua": 'doutor jurumenha 5777', "cidade": 'São Gonçalo', "uf": 'RJ'}
    ]
}

# Imprime todos os valores do dicionário
print(dic.values())

# Itera sobre a lista de endereços e imprime cada item
for k, v in enumerate(dic["endereço"]):
    print(f'Endereço {k+1}: {v}')
    for chave, valor in v.items():
        print(f"{chave.capitalize()}: {valor}")

        