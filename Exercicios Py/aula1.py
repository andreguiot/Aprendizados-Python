fg = input("Escreva abaixo uma das seguintes figuras geométricas para calcular a área : Círculo, Retângulo , Triângulo  ")
if fg == 'Círculo': 
    raio = float(input("Agora Informe o tamanho do raio do seu círculo : "))
    a = (raio * raio) * 3.1415
    print("A área do círculo é de {}" .format(a))
elif fg == 'Retângulo':
    base = float(input("Agora informe o tamanho da base do retângulo : "))
    altura = float(input("Agora informe o tamanho da altura do retângulo : "))
    a = base * altura
    print("A área do retângulo é de {}" .format(a))
elif fg == 'Triângulo':
    base = float(input("Agora informe o tamanho da base do triângulo : "))
    altura = float(input("Agora informe o tamanho da altura do triângulo : "))
    a = (base * altura)/2
    print("A área do triângulo é de {}" .format(a))
else: 
    print("Não digite algo diferente do que está exatamente escrito nas opções anteriores.")

    
