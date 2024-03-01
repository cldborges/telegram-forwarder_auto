from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import random
import winsound
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import pyautogui


def ler_resultados(resultados):
    with open(f'{resultados}.txt', 'r', encoding='utf-8') as arquivo:
        lista_resultados = arquivo.readline().strip()
        lista_resultados = lista_resultados.split(', ')
        # muda a lista de string para inteiros
        lista_resultados = list(map(int, lista_resultados))
    return lista_resultados

def ler_resultados_linhas(resultados):
    with open(f'{resultados}.txt', 'r', encoding='utf-8') as arquivo:
        lista_resultados = arquivo.readlines()
        for resultados in lista_resultados:
            resultados = resultados.split(', ')
            # muda a lista de string para inteiros
            resultados = list(map(int, resultados))
        # lista_resultados = lista_resultados.split(', ')
        # muda a lista de string para inteiros
        # lista_resultados = list(map(int, lista_resultados))
    return lista_resultados


def ler_resultados2(resultados):
    lista_resultados = resultados.strip()
    lista_resultados = lista_resultados.split(', ')
    # muda a lista de string para inteiros
    lista_resultados = list(map(int, lista_resultados))
    return lista_resultados


def contar_resultados(resultados, categoria):
    contador_sequencias = {}
    sequencia_atual = 0 
    for resultado in resultados:
        if resultado not in categoria:
            sequencia_atual += 1
        else:
            if sequencia_atual > 0:
                contador_sequencias[sequencia_atual] = contador_sequencias.get(sequencia_atual, 0) + 1
                sequencia_atual = 0
    return contador_sequencias



def calcular_sequencia_atual(resultados, categoria):
    tempo_sem_numero = 0
    numeros_seguidos = 0
    for resultado in resultados:
        if resultado in categoria:
            tempo_sem_numero = 0
            numeros_seguidos +=1
        else:
            tempo_sem_numero += 1
            numeros_seguidos = 0
    return numeros_seguidos, tempo_sem_numero


def calcular_maior_sequencia(resultados, categoria):
    maior_sequencia_aparecendo = 0  # Inicializa a variável para armazenar a maior sequência
    sequencia_atual_aparecendo = 0  # Inicializa a variável para armazenar a sequência atual
    maior_sequencia_ausente = 0  # Inicializa a variável para armazenar a maior sequência
    sequencia_atual_ausente = 0  # Inicializa a variável para armazenar a sequência atual
    for resultado in resultados:
        if resultado in categoria:
            sequencia_atual_aparecendo += 1
            sequencia_atual_ausente = 0 
            if sequencia_atual_aparecendo > maior_sequencia_aparecendo:
                maior_sequencia_aparecendo = sequencia_atual_aparecendo
        else:
            sequencia_atual_ausente += 1
            sequencia_atual_aparecendo = 0 
            if sequencia_atual_ausente > maior_sequencia_ausente:
                maior_sequencia_ausente = sequencia_atual_ausente
    return maior_sequencia_aparecendo, maior_sequencia_ausente


def apostar(driver, categorias):
    if categorias == []:
        pass
    else:
        atraso_aleatorio = random.uniform(2.3, 4.8)
        time.sleep(atraso_aleatorio)
        for categoria in categorias:
            print(categoria)
            element = driver.find_element(By.CSS_SELECTOR, f'rect[data-bet-spot-id="{categoria}"]')
            # elements = driver.find_elements(By.CSS_SELECTOR, f'rect[data-bet-spot-id={categoria}]')
            # print(elements.text)
            element.click()
            numero_aleatorio = random.uniform(0.3, 1.0)
            print(numero_aleatorio)
            time.sleep(numero_aleatorio)


def apostar2(driver, apostas, estado={"ficha_anterior": None}):
    if apostas == []:
        pass
    else:
        atraso_aleatorio = random.uniform(4.4, 5.1)
        time.sleep(atraso_aleatorio)
        for aposta in apostas:
            ficha = aposta['ficha']
            if ficha != estado["ficha_anterior"]:
                numero_aleatorio = random.uniform(0.3, 0.6)
                # print(numero_aleatorio)
                time.sleep(numero_aleatorio)

                # escolher com o teclado numérico de cima
                # if ficha == 25:
                #     numero = '4'
                # elif ficha == 10:
                #     numero = '3'
                # elif ficha == 5:
                #     numero = '2'
                # else:
                #     numero = '1'
                # pyautogui.press(numero)

                # escolher ficha com o selenium
                selecionar_ficha = driver.find_element(By.CSS_SELECTOR, f'div[data-value="{ficha}"]')
                selecionar_ficha.click()

                # mesa_apostas = driver.find_element(By.CLASS_NAME, 'perspectiveContainer--87027')
                # mesa_apostas.send_keys(Keys.NUMPAD3)
                # try:
                #     selecionar_ficha.click()
                # except:
                #     numero_aleatorio = random.uniform(0.3, 0.6)
                #     print(numero_aleatorio)
                #     time.sleep(numero_aleatorio)
                #     winsound.Beep(500, 1000)
                #     selecionar_ficha = driver.find_element(By.CSS_SELECTOR, f'div[data-value="{ficha}"]')
                #     selecionar_ficha.click()
                estado["ficha_anterior"] = ficha
            for categoria in aposta['aposta']:
                numero_aleatorio = random.uniform(0.3, 0.6)
                # print(numero_aleatorio)
                time.sleep(numero_aleatorio)
                if categoria == '0':
                    forma = 'polygon'
                else:
                    forma = 'rect'
                element = driver.find_element(By.CSS_SELECTOR, f'{forma}[data-bet-spot-id="{categoria}"]')
                element.click()
        # print(ficha, aposta)


# def apostar2(driver, apostas, estado={"ficha_anterior": None}):
#     if apostas == []:
#         pass
#     else:
#         atraso_aleatorio = random.uniform(4.4, 5.1)
#         time.sleep(atraso_aleatorio)
#         for aposta in apostas:
#             ficha = aposta['ficha']
#             if ficha != estado["ficha_anterior"]:
#                 numero_aleatorio = random.uniform(0.3, 0.6)
#                 print(numero_aleatorio)
#                 time.sleep(numero_aleatorio)
#                 if ficha == 25:
#                     numero = '4'
#                 elif ficha == 10:
#                     numero = '3'
#                 elif ficha == 5:
#                     numero = '2'
#                 else:
#                     numero = '1'
#                 # selecionar_ficha = driver.find_element(By.CSS_SELECTOR, f'div[data-value="{ficha}"]')
#                 pyautogui.press(numero)
#                 # mesa_apostas = driver.find_element(By.CLASS_NAME, 'perspectiveContainer--87027')
#                 # mesa_apostas.send_keys(Keys.NUMPAD3)
#                 # try:
#                 #     selecionar_ficha.click()
#                 # except:
#                 #     numero_aleatorio = random.uniform(0.3, 0.6)
#                 #     print(numero_aleatorio)
#                 #     time.sleep(numero_aleatorio)
#                 #     winsound.Beep(500, 1000)
#                 #     selecionar_ficha = driver.find_element(By.CSS_SELECTOR, f'div[data-value="{ficha}"]')
#                 #     selecionar_ficha.click()
#                 estado["ficha_anterior"] = ficha
#             for categoria in aposta['aposta']:
#                 numero_aleatorio = random.uniform(0.3, 0.6)
#                 # print(numero_aleatorio)
#                 time.sleep(numero_aleatorio)
#                 if categoria == '0':
#                     forma = 'polygon'
#                 else:
#                     forma = 'rect'
#                 element = driver.find_element(By.CSS_SELECTOR, f'{forma}[data-bet-spot-id="{categoria}"]')
#                 element.click()
#         print(ficha, aposta)


def apostar3(driver, apostas, estado={"ficha_anterior": None}):
    if apostas == []:
        pass
    else:
        atraso_aleatorio = random.uniform(4.4, 5.1)
        time.sleep(atraso_aleatorio)
        for aposta in apostas:
            ficha = aposta['ficha']
            if ficha != estado["ficha_anterior"]:
                numero_aleatorio = random.uniform(0.3, 0.6)
                print(numero_aleatorio)
                time.sleep(numero_aleatorio)
                # if ficha == 25:
                #     numero = '4'
                # elif ficha == 10:
                #     numero = '3'
                # elif ficha == 5:
                #     numero = '2'
                # else:
                #     numero = '1'
                selecionar_ficha = driver.find_element(By.CSS_SELECTOR, f'div[data-value="{ficha}"]')
                # pyautogui.press(numero)
                mesa_apostas = driver.find_element(By.CLASS_NAME, 'expandedChipStack--0a379')
                # mesa_apostas = driver.find_element(By.CLASS_NAME, 'perspectiveContainer--87027')
                mesa_apostas.send_keys('1')
                try:
                    selecionar_ficha.click()
                except:
                    numero_aleatorio = random.uniform(0.3, 0.6)
                    print(numero_aleatorio)
                    time.sleep(numero_aleatorio)
                    winsound.Beep(500, 1000)
                    selecionar_ficha = driver.find_element(By.CSS_SELECTOR, f'div[data-value="{ficha}"]')
                    selecionar_ficha.click()
                estado["ficha_anterior"] = ficha
            for categoria in aposta['aposta']:
                numero_aleatorio = random.uniform(0.3, 0.6)
                # print(numero_aleatorio)
                time.sleep(numero_aleatorio)
                if categoria == '0':
                    forma = 'polygon'
                else:
                    forma = 'rect'
                element = driver.find_element(By.CSS_SELECTOR, f'{forma}[data-bet-spot-id="{categoria}"]')
                element.click()
        print(ficha, aposta)
                

def extrair_resultados(driver):
    numeros = []
    html = driver.page_source

    # Parseie o HTML usando BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Encontre todos os elementos <div> com a classe "single-number--43778" (que contêm os números)
    number_divs = soup.find_all('div', class_='single-number--43778')

    # Itere sobre os elementos e extraia os números
    for div in number_divs:
        # Obtenha o número dentro do elemento <span>
        number = int(div.find('span', class_='value--877c6').text)
        numeros.append(number)
    numeros = numeros[13:]
    return numeros


def login(roleta):
    driver = webdriver.Chrome()
    options = webdriver.ChromeOptions()
    options.add_argument(r'--user-data-dir=C:/Temp/Sessoes/UserData/') #caso dê erros com o caminho, principalmente quando termina com \, alterar as barras para /
    driver = webdriver.Chrome(options=options)
    driver.get(f'https://blaze-7.com/pt/games/{roleta}')
    # driver.get('https://blaze-1.com/pt/games/vip-roulette')

    # time.sleep(45)
    # driver.maximize_window()
    time.sleep(5)
    driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="game_wrapper"]/iframe'))
    time.sleep(1)
    driver.switch_to.frame(driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/iframe'))
    # botão estatística
    #root > div > div > div.content--82383 > div:nth-child(10) > div.bottom-right--235ec > div > div > button
    
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[9]/div[4]/div/div/button').click()
    # driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div[2]/div[10]/div[4]/div/div/button').click()

    time.sleep(1)
                                #    //*[@id="root"]/div[2]/div/div[2]/div[12]/div[1]/div/div/div[2]/div/div/div/div/ul/li[3]/button/span[1]
    # driver.find_element(By.LINK_TEXT, 'ÚLTIMOS 500').click()
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[12]/div[1]/div/div/div[2]/div/div/div/div/ul/li[3]/button/span[1]').click()

    # driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div[2]/div[12]/div[1]/div/div/div[2]/div/div/div/div/ul/li[3]/button/span[1]').click()
    return driver


def criar_aposta(categoria, ficha, apostas_permitidas):
    aposta = []
    # ficha = 2.5
    if categoria['nome'] in apostas_permitidas:
        for atributo in categoria['atributo']:
        # for atributo in categoria['contrario']:
            if atributo != '':
                aposta.append(atributo)
    return {'ficha': ficha, 'aposta': aposta}


def limpar_apostas_duplicadas(apostas):

    # Lista para armazenar as apostas que já foram vistas
    apostas_vistas = set()

    # Lista para armazenar os dicionários finais
    dicionarios_finais = []

    # Iterar sobre a lista de dicionários
    for dicionario in apostas:
        apostas_comuns = set(dicionario['aposta']) & apostas_vistas
        # Se não houver apostas comuns, adicione este dicionário às apostas vistas e à lista final
        if not apostas_comuns:
            apostas_vistas.update(dicionario['aposta'])
            dicionarios_finais.append(dicionario)
        else:
            # Se houver apostas comuns, encontre o dicionário existente com a ficha mais alta
            for dic in dicionarios_finais:
                if any(aposta in dic['aposta'] for aposta in apostas_comuns) and dic['ficha'] < dicionario['ficha']:
                    # Substitua o dicionário existente se a ficha for mais alta
                    dicionarios_finais.remove(dic)
                    apostas_vistas.difference_update(dic['aposta'])
                    apostas_vistas.update(dicionario['aposta'])
                    dicionarios_finais.append(dicionario)
                    break
    print(dicionarios_finais)
    return dicionarios_finais


def limpar_apostas_duplicadas2(apostas):

    # Lista para armazenar as apostas que já foram vistas
    apostas_vistas = set()

    # Lista para armazenar os dicionários finais
    dicionarios_finais = []

    # Iterar sobre a lista de dicionários
    for dicionario in apostas:
        apostas_comuns = set(dicionario['aposta']) & apostas_vistas
        # Se não houver apostas comuns, adicione este dicionário às apostas vistas e à lista final
        if not apostas_comuns:
            apostas_vistas.update(dicionario['aposta'])
            dicionarios_finais.append(dicionario)
        else:
            # Se houver apostas comuns, encontre o dicionário existente com a ficha mais alta
            for dic in dicionarios_finais:
                if any(aposta in dic['aposta'] for aposta in apostas_comuns) and dic['rodadas_liberadas'] < dicionario['rodadas_liberadas']:
                    # Substitua o dicionário existente se a ficha for mais alta
                    dicionarios_finais.remove(dic)
                    apostas_vistas.difference_update(dic['aposta'])
                    apostas_vistas.update(dicionario['aposta'])
                    dicionarios_finais.append(dicionario)
                    break
    print(dicionarios_finais)
    return dicionarios_finais



def ultima_aparicao(resultados):

    from collections import defaultdict

    # Sequência de resultados da roleta
    resultados_roleta = resultados
    resultados_roleta.reverse()
    # Dicionário para armazenar o número e em qual rodada ele foi visto pela última vez
    ultima_aparicao = defaultdict(int)

    # Itera sobre os resultados da roleta e atualiza a última aparição de cada número
    for rodada, numero in enumerate(resultados_roleta):
        ultima_aparicao[numero] = rodada

    # Ordena o dicionário com base no número de rodadas sem aparecer
    ultima_aparicao_ordenada = sorted(ultima_aparicao.items(), key=lambda x: x[1])

    # Imprime os resultados
    # for numero, rodada in ultima_aparicao_ordenada:
    #     rodadas_sem_aparecer = len(resultados_roleta) - rodada - 1
    #     print(f"Número {numero} não apareceu há {rodadas_sem_aparecer} rodadas.")
    return ultima_aparicao_ordenada


def penultima_aparicao(resultados):

    from collections import defaultdict

    # Sequência de resultados da roleta
    resultados_roleta = resultados
    resultados_roleta.reverse()
    # Dicionário para armazenar o número e em qual penúltima rodada ele foi visto pela última vez
    penultima_aparicao = defaultdict(lambda: [-2, -1])  # Valor inicial é -2 para indicar que o número ainda não apareceu

    # Itera sobre os resultados da roleta e atualiza a penúltima aparição de cada número
    for rodada, numero in enumerate(resultados_roleta):
        penultima_aparicao[numero][0], penultima_aparicao[numero][1] = penultima_aparicao[numero][1], rodada

    # Filtra os números que apareceram pelo menos duas vezes
    numeros_filtrados = {numero: penultima_aparicao[numero][0] for numero in penultima_aparicao if penultima_aparicao[numero][0] >= 0}

    # Ordena o dicionário com base no número de rodadas sem aparecer
    numeros_filtrados_ordenados = sorted(numeros_filtrados.items(), key=lambda x: x[1], reverse=True)

    # Imprime os resultados
    # for numero, penultima_rodada in numeros_filtrados_ordenados:
    #     rodadas_sem_aparecer = len(resultados_roleta) - penultima_rodada - 1
    #     print(f"Número {numero} não apareceu há {rodadas_sem_aparecer} rodadas.")
    return numeros_filtrados_ordenados


def aparicoes(resutados):

    from collections import defaultdict

    # Sequência de resultados da roleta
    resultados_roleta = resutados
    resultados_roleta.reverse()
    # Dicionário para armazenar a penúltima e última aparição de cada número
    aparicoes = defaultdict(lambda: [-2, -1])  # Valor inicial é -2 para indicar que o número ainda não apareceu

    # Itera sobre os resultados da roleta e atualiza a penúltima e última aparição de cada número
    for rodada, numero in enumerate(resultados_roleta):
        aparicoes[numero][0], aparicoes[numero][1] = aparicoes[numero][1], rodada

    # Filtra os números que apareceram pelo menos duas vezes
    numeros_filtrados = {numero: (aparicoes[numero][1] - aparicoes[numero][0]) for numero in aparicoes if aparicoes[numero][0] >= 0}

    # Ordena o dicionário com base na diferença entre a última e a penúltima aparição
    numeros_filtrados_ordenados = sorted(numeros_filtrados.items(), key=lambda x: x[1], reverse=True)

    # Imprime os resultados
    # for numero, diferenca_aparicoes in numeros_filtrados_ordenados:
    #     print(f"Número {numero} não apareceu há {diferenca_aparicoes} rodadas entre sua penúltima e última aparição.")
    return numeros_filtrados_ordenados


def contar_ausencia(resultados, numeros):
    contador_ausencia = {}  # Dicionário para armazenar o número de ocorrências de ausência de sequências
    sequencia_atual = 0 
    resultados.reverse()
    for numero in resultados:
        if numero not in numeros:
            sequencia_atual += 1
        else:
            if sequencia_atual > 0:
                contador_ausencia[sequencia_atual] = contador_ausencia.get(sequencia_atual, 0) + 1
                sequencia_atual = 0
    if sequencia_atual > 0:
        contador_ausencia[sequencia_atual] = contador_ausencia.get(sequencia_atual, 0) + 1
    return contador_ausencia


def gravar_resultados(roleta, resultados):
    with open(f'{roleta}.txt', 'a') as arquivo:
        linha = ', '.join(map(str, resultados)) + '\n'
        # Escreva a linha no arquivo
        arquivo.write(linha)