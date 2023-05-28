
from datetime import datetime
import random 

#Módulo 1
print('-----Oá! Seja bem vindo a empresa.-----')

nome_user = (input('Nome: ').capitalize())
idade = int(input('Digite sua idade: '))
data_cadastro = datetime.now()
data_aniversario = datetime.strptime(input('Digite sua data de aniversario no formato dd/mm/aa: '), '%d/%m/%y')

cartoes = ['R$50,00','R$250,00','R$120,00']
cartao_sorteado = random.choice(cartoes)

#Módulo 2
print(f"Olá {nome_user}, seu registro foi concluído com sucesso no dia {data_cadastro.day}/{data_cadastro.month}/{data_cadastro.year}.\nParabéns, houve um sorteio e você ganhou um cartão de compras no valor de {cartao_sorteado}.")