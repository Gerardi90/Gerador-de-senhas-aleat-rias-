#importando bibliotecas 
import time
import secrets
import string 
from random import *
print("GERADOR DE SENHAS ALEATÓRIAS - GERA QUARENTA SENHAS")
print("      ")
senha_chave = input("Deseja acrescentar uma palavra chave na senha? (s/n): ")
if senha_chave == "s":
    varnome = input("Escreva a palvra chave: ")
    for cod in range (0,40):
      tamanho_da_senha = randint(8,10)
      caracteres =  string.ascii_letters + string.digits + string.punctuation
      senha = ''.join(secrets.choice(caracteres) for i in range (tamanho_da_senha))
      print(varnome+senha)
      time.sleep(0.5)
elif senha_chave == "n": 
    print("Certo! Veja as senhas a seguir: ")
    for cod1 in range (0,40):
      tamanho_da_senha = randint(10,14)
      caracteres =  string.ascii_letters + string.digits + string.punctuation
      senha = ''.join(secrets.choice(caracteres) for i in range (tamanho_da_senha))
      print(senha)
      time.sleep(0.5)
else:
    print("Algo deu errado, reinicie o código :(")
