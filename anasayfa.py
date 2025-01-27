import pyautogui as pg

# Ekranın genişliği ve yüksekliğini alıyoruz    
x = pg.size()
print(x)
# mouse 0,0 konumuna gidiyor
pg.moveTo(565,870)
# mouse sol butonuna basıyor
pg.click()
#klavyeden yazı yazdırma
pg.write("chrome")
# enter tuşuna basıyor 2 saniye bekleme süresi
pg.press("enter",interval=2)

pg.write("https://www.sahibinden.com",interval=0.25)

pg.press("enter",interval=2)

# alt + space + x tuşlarına basıyor
pg.hotkey("alt","space","x",interval=2)