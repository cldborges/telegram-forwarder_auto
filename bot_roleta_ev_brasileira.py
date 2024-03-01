#    Copyright (c) 2021 Ayush
#    
#    This program is free software: you can redistribute it and/or modify  
#    it under the terms of the GNU General Public License as published by  
#    the Free Software Foundation, version 3.
# 
#    This program is distributed in the hope that it will be useful, but 
#    WITHOUT ANY WARRANTY; without even the implied warranty of 
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
#    General Public License for more details.
# 
#    License can be found in < https://github.com/Ayush7445/telegram-auto_forwarder/blob/main/License > .

from telethon import TelegramClient, events
from decouple import config
import logging
from telethon.sessions import StringSession
# import easygui
import re
# from classes import Sinal

# from selenium import webdriver
# import time
from funcoes import *
# from variaveis import *

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

print("Starting...")

# Basics
APP_ID = config("APP_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
SESSION = config("SESSION")
FROM_ = config("FROM_CHANNEL")
TO_ = config("TO_CHANNEL")

FROM = [int(i) for i in FROM_.split()]
TO = [int(i) for i in TO_.split()]

try:
    BotzHubUser = TelegramClient(StringSession(SESSION), APP_ID, API_HASH)
    BotzHubUser.start()
except Exception as ap:
    print(f"ERROR - {ap}")
    exit(1)

driver = login('roleta-ao-vivo')
apostas_filtradas = []
ficha_zero = 1
ficha = 2.5

@BotzHubUser.on(events.NewMessage(incoming=True, chats=FROM))
async def sender_bH(event):
    for i in TO:
        try:
            await BotzHubUser.send_message(
                i,
                event.message
            )
        except Exception as e:
            print(e)
    texto_mensagem = event.message.text
    print(texto_mensagem)
    if 'ENTRADA CONFIRMADA' in texto_mensagem:
        apostas_filtradas = []
        coluna1, coluna2 = re.findall(r'(\d)', texto_mensagem.splitlines()[5])
        for coluna in coluna1, coluna2:
            if coluna == '1':
                coluna_tag = 'bottom2to1'
            elif coluna == '2':
                coluna_tag = 'middle2to1'
            elif coluna == '3':
                coluna_tag = 'top2to1'
            apostas_filtradas.append({'ficha': ficha, 'aposta': [coluna_tag]})
        print(coluna1, coluna2)
        apostas_filtradas.append({'ficha': ficha_zero, 'aposta': ['0']})
        print(apostas_filtradas)
        apostar2(driver, apostas_filtradas)
    # sinal1 = Sinal(texto_mensagem)
    # sinal1.print_atributos()

@BotzHubUser.on(events.MessageEdited(incoming=True, chats=FROM))
async def sender_bH(event):
    for i in TO:
        try:
            await BotzHubUser.send_message(
                i,
                event.message
            )
        except Exception as e:
            print(e)
    # print(event.message.text)
    # if '✖✖✖✖✖✖✖✖✖✖' in event.message.text:
    #     easygui.msgbox('Loss identificado')
    #     print('Deu ruim')
    # if 'GREEN NO' in event.message.text:
    #     print('deu bom')

print("Bot has started.")
BotzHubUser.run_until_disconnected()
