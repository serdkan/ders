import subprocess
import pyautogui as pg
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
subprocess.Popen([chrome_path])
pg.sleep(1)
pg.write("https://web.whatsapp.com/send?phone=5523741700&text=efe+örnek+için",interval=0.02)
pg.sleep(2)
pg.press("enter")
pg.sleep(3)
pg.press("enter")