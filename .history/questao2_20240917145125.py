"""
2) Escreva um programa que verifique, em uma string, a existência da letra 'a', 
seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela 
ocorre.

IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência 
ou pode ser previamente definida no código;
"""


palavra_entrada = input("Escreva uma palavra: ")
 
i = 0
qtd_vezes_a = 0
letra_mais_vezes = " "

for letra in palavra_entrada:
    if letra.lower() == "a":
        qtd_vezes_a += 1
    
    
if qtd_vezes_a > 0:
    print(f"A letra 'a' apareceu {qtd_vezes_a} vezes.")
else:
    print("A letra 'a' não foi encontrada na palavra digitada.")

    