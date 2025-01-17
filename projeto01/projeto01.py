import pyautogui
import pandas as pd
import keyboard  # Biblioteca para detectar teclas pressionadas
from time import sleep

# Abrir o navegador e acessar o site
pyautogui.press('win')
pyautogui.write('chrome')
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.moveTo(x=787, y=596)
pyautogui.click()
sleep(1)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
sleep(1)
pyautogui.moveTo(x=735, y=375)
pyautogui.click()
pyautogui.write('kauadev720@gmail.com')
pyautogui.press('tab')
pyautogui.write('qwe123')
pyautogui.press('tab')
pyautogui.press('enter')

# Ler a tabela de produtos
tabela = pd.read_csv('produtos.csv')
sleep(1)

# Loop para iterar pelas linhas da tabela
for linha in tabela.index:
    # Verificar se a tecla 'ESC' foi pressionada
    if keyboard.is_pressed('esc'):
        print("Execução interrompida pelo usuário.")
        break

    # Interagir com o sistema
    pyautogui.moveTo(x=797, y=258)
    pyautogui.doubleClick()

    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(str(codigo))
    pyautogui.press('tab')
    
    marca = tabela.loc[linha, 'marca']
    pyautogui.write(str(marca))
    pyautogui.press('tab')

    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(str(tipo))
    pyautogui.press('tab')

    categoria = tabela.loc[linha, 'categoria']
    pyautogui.write(str(categoria))
    pyautogui.press('tab')

    preco_unitario = tabela.loc[linha, 'preco_unitario']
    pyautogui.write(str(preco_unitario))
    pyautogui.press('tab')

    custo = tabela.loc[linha, 'custo']
    pyautogui.write(str(custo))
    pyautogui.press('tab')

    obs = tabela.loc[linha, 'obs']
    pyautogui.write(str(obs))
    pyautogui.press('tab')
    pyautogui.moveTo(x=830, y=929)
    pyautogui.click()
    pyautogui.press('enter')


print("Finalizado.")
