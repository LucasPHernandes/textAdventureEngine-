# RELAÇÃO é determinada de 0 a 10, sendo que 10 sendo uma ótima relação de confiança/amizade dando mais escolhas ao personagem

import os


import decor as dec  # Relacionado a aparência do texto
from personas import persona as personas

def cls():
    os.system('cls')

# TESTEee

# Capitulo 1: Mais um dia normal
## CASA
def cap1Acordando():
    cls()
    print(dec.reset + "Você olha pela pequena janela adjunta ao seu colchão que corta metade da visão dessa janela, ainda está escuro lá fora, mas já se pode perceber um enorme movimento nas ruas e a fumaça já começam a tomar conta da cidade" + dec.italic + " -- se é que algum dia ela deixou de existir..." + dec.reset)
    input(dec.italic + "O que fazer: ")

def iniciacao():
    cls()
    print("beep! beep!")
    print("Você é acordado mais uma vez com uma ligação de " + dec.bold + personas.claudia.name + dec.reset)
    input(dec.italic + "Enter para continuar: ")
    cap1Acordando()

if __name__ == "__main__":
    while True:
        cls()
        print("Neste mundo você possui a liberdade para fazer diversas coisas como: Andar, Olhar, Pegar e outras ações que seram apresentadas ao longo dessa aventura!")
        op = input("Digite 1 para começarmos!")
        if op:
            iniciacao()

# class op:
#     option,
#     validade,
#     parse,
#     object
#
# class room:
#     nameRoom,
#     description,
#     objects/things,
#     directions(up/down, left/right, front/rear)   -> Criado com base nos nomes das salas
