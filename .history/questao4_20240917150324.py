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
# Resultado: 9

# 2, 4, 8, 16, 32, 64, ____
sequencia_b = [2, 4, 8, 16, 32, 64]
proximo_b = sequencia_b[-1] * 2
print(proximo_b) 