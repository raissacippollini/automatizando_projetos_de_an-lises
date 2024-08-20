import pyperclip
import pyautogui
import webbrowser
import time
import yfinance

ticker = input("Digite o código da ação desejada: ")

dados = yfinance.Ticker(ticker).history(start="2020-01-01" , end="2020-12-31")
fechamento = dados.Close

maxima = round(fechamento.max(), 2)
minima = round(fechamento.min(), 2)
valor_medio = round(fechamento.mean(), 2)

destinatario = "__________@hotmail.com"
assunto = "Análises do projeto 2020"

mensagem = f"""
Prezado gestor,
    
Seguem as análises solicitadas da ação {ticker}:

cotação máxima: R${maxima}
cotação minima: R${minima}
valor médio: R${valor_medio}

Qualquer dúvida, estou á disposição!

Atte.
"""

#abrir o navegador e ir para o hotmail
webbrowser.open("https://outlook.live.com/")
time.sleep(3)

# configurando uma pausa de 3 segundos
pyautogui.PAUSE = 3

# clicar no botão Novo email
pyautogui.click(x=212, y=225)

# digitar o email do destinatário e teclar TAB
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl" , "v")
pyautogui.hotkey("tab")

# digitar o assunto do email
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl" , "v")
pyautogui.hotkey("tab")

# digitar a mensagem
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl" , "v")

# clicar no botão enviar
pyautogui.click(x=450, y=312)

# fechar o hotmail
pyautogui.click("ctrl", "f4")

print("Email enviado com sucesso!")
