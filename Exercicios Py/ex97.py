def escreva(* txt):
    x = 0
    lis = []
    for i , p in enumerate(txt):
        for k in p:
            lis.append(k)
        x = len(lis)
        print('~' * x)
        for v in lis:
            print(v, end = '')
        print()
        print('~' * x)

escreva('Flamengo maior do mundo')
escreva('Vasco vice')
escreva('oi')

