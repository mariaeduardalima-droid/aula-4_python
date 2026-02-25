'''
3. Desenvolva um programa para calcular e escrever a área e o perímetro de um retângulo.
Exemplo: 
Base= 5
Altura = 4
Área = 20
Perímetro = 18
'''

#ENTRADA
base = float(input('informe a base do retângulo: '))
altura = float(input('informe a altura do retângulo: '))

#base, altura = map(float, input('informe a base e a altura do retângulo: '))

#Processamento
area = base * altura
perimetro = (base * 2) + (altura * 2)

#SAIDA
print('Área do retângulo:', area)
print('perimetro do retângulo:', perimetro)