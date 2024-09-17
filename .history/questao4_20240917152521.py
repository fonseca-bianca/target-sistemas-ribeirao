"""
4) Descubra a lógica e complete o próximo elemento:
a) 1, 3, 5, 7, ___
b) 2, 4, 8, 16, 32, 64, ____
c) 0, 1, 4, 9, 16, 25, 36, ____
d) 4, 16, 36, 64, ____
e) 1, 1, 2, 3, 5, 8, ____
f) 2,10, 12, 16, 17, 18, 19, ____
"""

# a) 1, 3, 5, 7, ___
sequencia_a = [1, 3, 5, 7]
proximo_a = sequencia_a[-1] + 2
if proximo_a % 2 != 0:  # número ímpar tem resto 1 na divisão por 2
    print(proximo_a)  
else:
    print("Erro: o próximo número não é ímpar.")
# Próximo elemento: 9

# b) 2, 4, 8, 16, 32, 64, ____
sequencia_b = [2, 4, 8, 16, 32, 64]
proximo_b = sequencia_b[-1] * 2 # -1: acessa o último elemento da lista e multiplica ele por 2
print(proximo_b) 
# Próximo elemento: 128

# c) 0, 1, 4, 9, 16, 25, 36, ____
sequencia_c = [0, 1, 4, 9, 16, 25, 36]
proximo_c = (len(sequencia_c)) ** 2 # o quadrado de cada número
print(proximo_c) 
# Próximo elemento: 49

# d) 4, 16, 36, 64, ____
sequencia_d = [4, 16, 36, 64]
proximo_d = (len(sequencia_d) * 2 +2 ) ** 2 # o último elemento será 10 (8 + 2) * ele mesmo (10) = 100
print(proximo_d)
# Proximo elemento:	100

# g) 1, 1, 2, 3, 5, 8, ____
sequencia_e = [1, 1, 2, 3, 5, 8]
proximo_e = sequencia_e[-1] + sequencia_e[-2] # acessa último elemento da lista e soma com o penúltimo elemento
print(proximo_e)
# Próximo elemento: 13

# f) 2,10, 12, 16, 17, 18, 19, ____
sequencia_f = [2, 10, 12, 16, 17, 18, 19]
proximo_f = sequencia_f[-1] + 1
print(proximo_f)
