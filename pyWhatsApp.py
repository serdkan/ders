import subprocess
import pyautogui as pg

def whatsAppMesajGonder (cepNo,mesaj):
    x = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    subprocess.Popen([x])
    pg.sleep(3)
    pg.write(F"https://web.whatsapp.com/send?phone={cepNo}&text={mesaj}",interval=0.01)
    pg.press("enter")
    pg.sleep(3)
    pg.press("enter")
    pg.sleep(3)
    pg.press("enter")