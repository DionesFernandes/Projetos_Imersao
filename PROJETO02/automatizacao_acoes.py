###################### PROJETO 02 ##############################

#         PASSO A PASSO DO PROBLEMA
# - Buscar as informações da ação automaticamente
# - Criar as análises solicitadas
#       * Cotação máxima
#       * Cotação minima
#       * valor médio
# - Enviar um e-mail automaticamente para o gestor
#
#      --------- Bibliotecas usadas ---------
#
#     - yfinance  - matplotlib

import yfinance

# - Buscar as informações da ação automaticamente

codigo_acao = input('Digite o código da ação desejada: ')
dados = yfinance.Ticker(codigo_acao).history(start='2023-01-01', end='2023-12-31')
fechamento = dados.Close 

# fechamento.plot() # função plot mostra em grafico
# linha 19 - armazenando e definindo data de inicio e fim da ação
# linha 20 - armazenando a coluna close "fechamento" da ação
# linha 32 - função round defini em quantas casas decimais vc quer

# - Criar as análises solicitadas
#       * Cotação máxima
#       * Cotação minima
#       * valor médio

maxima = round(fechamento.max(), 2) 
minima = round(fechamento.min(), 2)
valor_medio = round(fechamento.mean(), 2)

# - Enviar um e-mail automaticamente para o gestor

#     * Abrir o navegador e ir para o gmail
#     * Clicar no botão Escrever
#     * Digitar o email do destinatário e teclar TAB
#     * Digitar o assunto e teclar Tab
#     * Digitar a mensagem
#     * Clicar no botão Enviar

# --------- Bibliotecas usadas ---------

#     - pyautogui - pyperclip - ( webbrowser - ja é instalada com a pyautogui )

import pyautogui
import pyperclip
import webbrowser
import time

destinatario = 'dionesfernandes7@yahoo.com.br'
assunto = 'analise do mercado financeiro de ações'
mensagem = f"""
Prezado gestor,

seguem as análises solicitadas da ação {codigo_acao}:

Cotação máxima: R${maxima}
Cotação minima: R${minima}
Valor médio: R${valor_medio}

Qualquer dúvida, estou à disposição!

Att.
"""

#     * Abrir o navegador e ir para o gmail
webbrowser.open('www.gmail.com')
time.sleep(5)

# configurando uma pausa de 3 segundos
pyautogui.PAUSE = 3

#     * Clicar no botão Escrever
pyautogui.click(x=1460, y=218)
time.sleep(4)

#pyautogui.position()         - funçaõ para identificar a posição
# print(pyautogui.position()) - printar a posição x=, y=

#     * Digitar o email do destinatário e teclar TAB
pyperclip.copy(destinatario)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('tab')

#     * Digitar o assunto e teclar Tab
pyperclip.copy(assunto)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('tab')


#     * Digitar a mensagem
pyperclip.copy(mensagem)
pyautogui.hotkey('ctrl', 'v')

#     * Clicar no botão Enviar
pyautogui.click(x=2204, y=685)

#     * Fechar o gmail
pyautogui.hotkey('ctrl', 'w')

print('Email enviado com sucesso')
