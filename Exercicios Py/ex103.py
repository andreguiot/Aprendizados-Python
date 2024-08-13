def ficha(nome= '<desconhecido>', gols = '0'):
    if nome.strip() == "":
        print(f'O jogador {nome} fez {gols} no campeonato')
    else:
        print(f'O jogador {nome} fez {gols} gols no campeonato')




nm = str(input('Nome do Jogador : '))
gols = str(input('Número de gols : '))
ficha(nm, gols)