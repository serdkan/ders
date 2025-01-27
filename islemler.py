import pyautogui as pg
#not defteri açan kodlar scope
def notdefteriac(x="serdar",y="hoş"):
    pg.press("win")
    pg.write("notepad",interval=0.25)
    pg.press("enter")
    pg.hotkey("alt","shift")
    pg.write(f"{x} geldi hoş geldi, {y} geldi keyif geldi",interval=0.25)
    pg.sleep(1)

def notdefterikapat():
    #confirm dialog
    z = pg.confirm('Kapansın mı?', title='Emin misin?', buttons=['Evet', 'Hayır'])
    if z == "Evet":
        pg.hotkey("alt","f4")
def topla(a,b):
    return a+b

