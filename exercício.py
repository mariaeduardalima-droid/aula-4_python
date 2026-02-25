'''
1. Crie um programa que leia o salário de um funcionário e mostra na tela o seu salário anual.
Exemplo: 
salario_mensal = R$ 2000,00
salario_anual = R$ 24000,00
'''

#ENTRADA
#Capturando o salario e convertendo para float
salario_mensal = float(input('informe o seu salário mensal'))

#PROCESSAMENTO
salario_anual = salario_mensal * 12

#SAIDA
print('salario anual: R$', salario_anual)