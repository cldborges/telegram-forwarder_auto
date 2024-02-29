# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
import colorama
from colorama import Fore
import winsound
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time
from funcoes import *
# from bs4 import BeautifulSoup


categorias = (
    # {'nome':'linha de cima (3, 6, 9, 12, ...)', 'atributo': ('top2to1', ''), 'grupo': 'linhas', 'numeros': list(set(range(3, 36 + 1, 3)))},
    # {'nome':'linha do meio (2, 5, 8, 11, ...)', 'atributo': ('middle2to1', ''), 'grupo': 'linhas', 'numeros': list(set(range(2, 36 + 1, 3)))},
    # # {'nome':'linha de baixo (1, 4, 7, 10, ...)', 'atributo': ('bottom2to1', ''), 'grupo': 'linhas', 'numeros': list(set(range(1, 36 + 1, 3)))}, 
    {'nome':'linhas cima e meio', 'atributo': ('top2to1', 'middle2to1'), 'contrario': ('bottom2to1', ''), 'grupo': 'linhas 2to1', 'numeros': list(set(list(range(3, 36 + 1, 3)) + list(range(2, 36 + 1, 3))))},
    {'nome':'linhas cima e baixo', 'atributo': ('top2to1', 'bottom2to1'), 'contrario': ('middle2to1', ''), 'grupo': 'linhas 2to1', 'numeros': list(set(list(range(3, 36 + 1, 3)) + list(range(1, 36 + 1, 3))))},
    {'nome':'linhas meio e baixo', 'atributo': ('middle2to1', 'bottom2to1'), 'contrario': ('top2to1', ''), 'grupo': 'linhas 2to1', 'numeros': list(set(list(range(2, 36 + 1, 3)) + list(range(1, 36 + 1, 3))))},
    # {'nome':'1a dúzia', 'atributo': ('1st12', ''), 'grupo': 'duzias', 'numeros': list(set(range(1, 12 + 1)))}, 
    # {'nome':'2a dúzia', 'atributo': ('2nd12', ''), 'grupo': 'duzias', 'numeros': list(set(range(13, 24 + 1)))},
    # {'nome':'3a dúzia', 'atributo': ('3rd12', ''), 'grupo': 'duzias', 'numeros': list(set(range(25, 36 + 1)))},
    {'nome':'zero', 'atributo': ('0', ''), 'grupo': 'zero', 'numeros': [0]}, 
    {'nome':'1a e 2a dúzias', 'atributo': ('1st12', '2nd12'), 'contrario': ('3rd12', ''), 'grupo': 'duzias 2to1', 'numeros': list(set(range(1, 24 + 1)))},
    {'nome':'1a e 3a dúzias', 'atributo': ('1st12', '3rd12'), 'contrario': ('2nd12', ''), 'grupo': 'duzias 2to1', 'numeros': list(set(list(range(1, 12 + 1)) + list(range(25, 36 + 1))))},
    {'nome':'2a e 3a dúzias', 'atributo': ('2nd12', '3rd12'), 'contrario': ('1st12', ''), 'grupo': 'duzias 2to1', 'numeros': list(set(range(13, 36 + 1)))},
    # {'nome':'1a metade', 'atributo': ('from1to18', ''), 'grupo': 'metades', 'numeros': list(set(range(1, 18 + 1)))},
    # {'nome':'2a metade', 'atributo': ('from19to36', ''), 'grupo': 'metades', 'numeros': list(set(range(19, 36 + 1)))},
    # {'nome':'pretos', 'atributo': ('black', ''), 'grupo': 'cores', 'numeros': [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]},
    # {'nome':'vermelhos', 'atributo': ('red', ''), 'grupo': 'cores', 'numeros': [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]},
    # {'nome':'even (par)', 'atributo': ('even', ''), 'grupo': 'multiplos', 'numeros': list(set(range(2, 36 + 1, 2)))},
    # {'nome':'odd (ímpar)', 'atributo': ('odd', ''), 'grupo': 'multiplos', 'numeros': list(set(range(1, 36 + 1, 2)))}
)
# for categoria in categorias:
#     print(len(categoria['atributo']) if isinstance(categoria['atributo'], tuple) else 1)
ficha = 1
foco = False
teto_manual = True
tempo_limite = 1200
tempo_inicio = time.time()
# gale_ativacao = 3
# numeros = []

driver = login('roleta-ao-vivo')  # 'vip-roulette' / 'roleta-relampago / 'roleta-ao-vivo'

# time.sleep(50)

ultimos_5_numeros_anterior = []
iniciar = True
# n_jogo_anterior =''
while True:
        # numeros = []
        # time.sleep(1)
        numeros = extrair_resultados(driver)
        ultimo_numero = numeros[0]
        ultimos_5_numeros = numeros[0:5]
        if ultimos_5_numeros_anterior != ultimos_5_numeros:
        # if ultimos_5_numeros_anterior != ultimos_5_numeros and ultimo_numero != 0:
            nova_rodada = True
            # winsound.Beep(500, 1000)
            print('Nova rodada!')
            cor = Fore.CYAN
        # else:
        #     cor = Fore.WHITE
            ultimos_5_numeros_anterior = ultimos_5_numeros
            # print(ultimos_5_numeros)
            # numeros = numeros[13:]
            numeros.reverse()
            # print(numeros)
            colorama.init(autoreset=True)
            print(cor + f'Número sorteado: {ultimo_numero}')
            colorama.deinit()
            apostas = []
            for categoria in categorias:
                categoria['numeros'].sort()
                numeros_seguidos, tempo_sem_numero = calcular_sequencia_atual(numeros, categoria['numeros'])
                maior_sequencia_aparecendo, maior_sequencia_ausente = calcular_maior_sequencia(numeros, categoria['numeros'])
                grupo = categoria['grupo']
                soma_grupo = sum(1 for categoria in categorias if categoria['grupo'] == grupo)
                soma_atributo = len(categoria['atributo']) if isinstance(categoria['atributo'], tuple) else 1
                # print(soma_grupo)
                if teto_manual == True:
                    if soma_grupo == 3:
                        if soma_atributo == 2:
                            maior_sequencia_ausente = 5
                    #     if soma_atributo == 1:
                    #         maior_sequencia_ausente = 12
                    if soma_grupo == 2:
                    #     if soma_atributo == 1:
                    #         maior_sequencia_ausente = 6
                        if soma_atributo == 2:
                            maior_sequencia_ausente = 11
                if tempo_sem_numero == 0 and foco == True:
                    pass
                else:
                    # n_jogo = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div[2]/div[9]/div[2]/div/div/div[2]/div[2]/div').text
                    if maior_sequencia_ausente - tempo_sem_numero == 0:
                        cor = Fore.RED
                        winsound.Beep(500, 1000)
                        # iniciar = True
                        # # # if n_jogo != n_jogo_anterior:
                        # if nova_rodada == True:
                        # # if ultimos_5_numeros_anterior != ultimos_5_numeros:
                        #     # print('Jogo mudou ', n_jogo, n_jogo_anterior)
                        #     # time.sleep(5)
                        #     aposta = []
                        #     ficha = 10
                        #     for atributo in categoria['atributo']:
                        #     # for atributo in categoria['contrario']:
                        #         if atributo != '':
                        #             aposta.append(atributo)
                        #     apostas.append({'ficha': ficha, 'aposta': aposta})

                    elif maior_sequencia_ausente - tempo_sem_numero == 1:
                        cor = Fore.YELLOW
                        winsound.Beep(500, 1000)
                        # winsound.Beep(500, 1000)
                        # if n_jogo != n_jogo_anterior:
                        if nova_rodada == True:
                        # if ultimos_5_numeros_anterior != ultimos_5_numeros:
                            # print('Jogo mudou ', n_jogo, n_jogo_anterior)
                            # time.sleep(5)
                            aposta = []
                            ficha = 10
                            for atributo in categoria['atributo']:
                            # for atributo in categoria['contrario']:
                                if atributo != '':
                                    aposta.append(atributo)
                            apostas.append({'ficha': ficha, 'aposta': aposta})
                    elif maior_sequencia_ausente - tempo_sem_numero == 2:
                        # aposta = []
                        cor = Fore.GREEN 
                        winsound.Beep(500, 1000)               
                        # if n_jogo != n_jogo_anterior:
                        if nova_rodada == True:
                        # if ultimos_5_numeros_anterior != ultimos_5_numeros:
                            # print('Jogo mudou ', n_jogo, n_jogo_anterior)
                            # time.sleep(5)
                            aposta = []
                            ficha = 2.5
                            # for atributo in categoria['contrario']:
                            for atributo in categoria['atributo']:
                                if atributo != '':
                                    aposta.append(atributo)
                            apostas.append({'ficha': ficha, 'aposta': aposta})

                    elif maior_sequencia_ausente - tempo_sem_numero == 3:
                        cor = Fore.BLUE
                        # if n_jogo != n_jogo_anterior:
                        # if soma_grupo == 2:
                            # if nova_rodada == True:
                            # # if ultimos_5_numeros_anterior != ultimos_5_numeros:
                            #     # print('Jogo mudou ', n_jogo, n_jogo_anterior)
                            #     # time.sleep(5)
                            #     aposta = []
                            #     ficha = 2.5
                            #     for atributo in categoria['atributo']:
                            #     # for atributo in categoria['contrario']:
                            #         if atributo != '':
                            #             aposta.append(atributo)
                            #     apostas.append({'ficha': ficha, 'aposta': aposta})
                    elif maior_sequencia_ausente - tempo_sem_numero == 4:
                        cor = Fore.CYAN
                    # #     # if n_jogo != n_jogo_anterior:
                    #     if soma_grupo == 2:
                    #         if nova_rodada == True:
                    #         # if ultimos_5_numeros_anterior != ultimos_5_numeros:
                    #             # print('Jogo mudou ', n_jogo, n_jogo_anterior)
                    #             # time.sleep(5)
                    #             aposta = []
                    #             ficha = 2.5
                    #             for atributo in categoria['atributo']:
                    #             # for atributo in categoria['contrario']:
                    #                 if atributo != '':
                    #                     aposta.append(atributo)
                    #             apostas.append({'ficha': ficha, 'aposta': aposta})
                    else:
                        cor = Fore.WHITE
                    colorama.init(autoreset=True)
                    print(cor + categoria['nome'])
                    print(f'Sequência atual: Aparecendo: {numeros_seguidos}, Ausente:'  , cor + str(tempo_sem_numero))
                    print(f'Maior sequência: Aparecendo: {maior_sequencia_aparecendo}, Ausente:' , cor + str(maior_sequencia_ausente))
                    # print('---------------------------')
                    colorama.deinit()
            # n_jogo_anterior = n_jogo
            # print(apostas)
            if nova_rodada == True:
                apostas_filtradas = limpar_apostas_duplicadas(apostas)
                if apostas_filtradas != []:
                    apostas_filtradas.append({'ficha': 1, 'aposta': ['0']})
                if iniciar == True:
                    apostar2(driver, apostas_filtradas)
                    tempo_inicio = time.time()
                else:
                    tempo_atual = time.time()
                    tempo_decorrido = tempo_atual - tempo_inicio
                    if tempo_decorrido >= tempo_limite:
                        # 20 minutos se passaram sem a ação ser concluída
                        driver.refresh()
                        # Reinicia o tempo de contagem para a próxima verificação
                        tempo_inicio = time.time()                    
                nova_rodada = False

        else:
            # print('...')
            time.sleep(1)
