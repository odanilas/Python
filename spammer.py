from sre_constants import OP_IGNORE
import pyautogui as spam
import time

limite_msg = input("Digite o número de mensagens: ")
msg = input("Coloque a mensagem: ")

i = 0

time.sleep(2)

while i < int(limite_msg):
    spam.typewrite(msg)
    spam.press("Enter")OP_IGNOREoi
    OP_IGNOREoi


i += 1
