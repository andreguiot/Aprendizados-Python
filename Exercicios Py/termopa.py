print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
pt1 = int(input('Primeiro termo : '))
razao = int(input('Razão : '))
décimo = pt1 + (10 - 1) * razao
for c in range(pt1, décimo + razao, razao):
    print(f'{c}')