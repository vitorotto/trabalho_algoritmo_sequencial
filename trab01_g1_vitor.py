# Vitor Hugo Otto

"""
Escrever um programa em Python que converta uma temperatura informada
pelo usuário em Fahrenheit (°F) para Celsius (°C).
A temperatura em graus Celcius deve ser exibida com uma casa decimal.
"""

# tf = Temperatura em Fahrenheit
# tc = Temperatura em Celcius

tf = float(input("Forneça a temperatura em graus Fahrenheit (°F): "))

tc = (tf - 32) / 9 * 5

print("A temperatura em Celsius (°C) é %.1f" %tc)