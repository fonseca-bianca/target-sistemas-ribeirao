"""
5) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada 
em salas diferentes. Você não pode ver as lâmpadas da sala em que está, mas pode 
ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir 
qual interruptor controla qual lâmpada. Como você faria para descobrir, usando 
apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada 
lâmpada? 
"""

import time

interruptores = {'A': 0, 'B': 0, 'C': 0} # interruptores vão iniciar em zero (desligado)
lâmpadas = {'A': 'desligada', 'B': 'desligada', 'C': 'desligada'}

# função pra ligar o interruptor
def ligar_interruptor(interruptor):
    interruptores[interruptor] = 1 # ligado

# função pra desligar o interruptor
def desligar_interruptor(interruptor):
    interruptores[interruptor] = 0 # desligado

# função pra verificar o estado das lâmpadas (1 ou 0)
def verificar_lâmpadas():
    for interruptor, estado in interruptores.items():
        if estado == 1:
            lâmpadas[interruptor] = "ligada"
        else:
            lâmpadas[interruptor] = "desligada"


ligar_interruptor('A')  
time.sleep(5)          # Espera por 5 seg pra ver se está ligado
desligar_interruptor('A')  
ligar_interruptor('B')  

# verificar qual o estado das lâmpadas
verificar_lâmpadas()
print("Estado das lâmpadas:")
for lâmpada, estado in lâmpadas.items():
    print(f"A lâmpada {lâmpada} está {estado}.")