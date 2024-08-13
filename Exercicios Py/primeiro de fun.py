def soma(a, b):             #para definir uma função
    s = a + b
    print(f'A soma é {s}')


soma(0 , 1)
soma(2 , 3)
soma(5,9)


def contador(* n):        #utilizado para passar n parâmetros
    print(n)


contador(1 , 2, 4)
contador(7, 1 )