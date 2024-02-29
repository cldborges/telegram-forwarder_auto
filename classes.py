import re

class Sinal:
    def __init__(self, sinal):
        self.estrategia = re.search(r"\*\*(.*?)\*\*", sinal.splitlines()[0]).group(1)
        self.campeonato = re.search(r"\[(.*?)\]", sinal.splitlines()[1]).group(1)
        self.hora = re.search(r'\d{2}', sinal.splitlines()[3]).group()
        self.minutos = sinal.splitlines()[4][2:].split(sep=' ')
        self.mercado = sinal.splitlines()[6].split(sep='** ')[1]


    def print_atributos(self):
        print('-------------------------------------------------------')
        print(self.estrategia)
        print(self.campeonato)
        print(self.hora)
        print(self.minutos)
        print(self.mercado)
        print('-------------------------------------------------------')


# teste = sinal.splitlines()[6].split(sep='** ')[1]

# print(teste)


# sinal = """⚽️ **RDtips ultra02** ⚽️
# 🏆 [SUPER](https://www.bet365.com/#/AVR/B146/R%5E1/) 🏆

# ⏰ H: 18
# ➡ 58 01 04 07

# ✔ **Entrada:** Ambas Sim

# 🔗 [ACESSE AQUI](https://www.bet365.com/#/AVR/B146/R%5E1/)

# Gerada à partir de: https://bbtips.com.br
# **1 Greens Seguidos! ** 🤑

# ✅42➖➖➖✖4➖➖➖A: 0
# SG: 19➖➖➖G1: 19➖➖➖G2: 4➖➖➖G3: 0

# ➡️ 91,30% de Acerto"""

# sinal1 = Sinal(sinal)
# sinal1.print_atributos()