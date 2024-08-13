def criar_multiplicador(multiplicador):
  def multiplicar(numero):
    return numero * multiplicador
  return multiplicar


duplicador = criar_multiplicador(2)
triplicador = criar_multiplicador(3)
quadruplicador = criar_multiplicador(4)

print(duplicador(2))
print(triplicador(3))
print(quadruplicador(4))