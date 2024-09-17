"""
5) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada 
em salas diferentes. Você não pode ver as lâmpadas da sala em que está, mas pode 
ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir 
qual interruptor controla qual lâmpada. Como você faria para descobrir, usando 
apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada 
lâmpada? 
"""

import time # biblioteca importa pra poder usar o sleep()

interruptores = {'A': 0, 'B': 0, 'C': 0} # interruptores vão iniciar em zero (desligado)
lampadas = {'A': 'desligada', 'B': 'desligada', 'C': 'desligada'}

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
            lampadas[interruptor] = "ligada"
        else:
            lampadas[interruptor] = "desligada"


ligar_interruptor('A')  
time.sleep(5)          # Espera por 5 seg pra ver se está ligado
desligar_interruptor('A')  
ligar_interruptor('B')  
desligar_interruptor('B') 

# verificar qual o estado das lâmpadas
verificar_lâmpadas()
print("Estado das lâmpadas:")
for lampada, estado in lampadas.items():
    print(f"A lâmpada {lampada} está {estado}.")
    
"""
Retorno código:
Estado das lâmpadas:
A lâmpada A está desligada.
A lâmpada B está ligada.
A lâmpada C está desligada.
"""