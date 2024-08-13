def voto(vt):
    from datetime import date
    atual = date.today().year
    idad3 = atual - vt
    if idad3 >= 18 and idad3 < 65:
        r = str(f'Com {idad3} : VOTO OBRIGATÓRIO')
        return r
    if idad3 < 18 and idad3 > 16 or idad3 >= 65:
        r = str(f'Com {idad3} : VOTO OPCIONAL')
        return r
    else:
        r = str(f'Com {idad3} : NÃO VOTA')
        return r




print('-' * 20)
ano = int(input('Em que ano você nasceu? '))
r = voto(ano)
print(r)