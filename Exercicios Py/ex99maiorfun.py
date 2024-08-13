def maior(* num):
    x = len(num)
    print('\n', ('-=' * 20))
    print(f'Foram informados {x} valores ao todo.')
    maiorvalor = menorvalor = 0
    for i, v in enumerate(num):
        if i == 0:
            maiorvalor = menorvalor = v
        else:
            if maiorvalor < v:
                maiorvalor = v
            if menorvalor > v:
                menorvalor = v
    print(f'O maior valor infomado é {maiorvalor}\n O menor valor informado é {menorvalor}')
    print('\n', ('-=' * 20))


maior(2, 9, 4, 5, 7, 1)
maior(2, 4, 6, 8)
