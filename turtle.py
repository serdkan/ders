import pywhatkit

telefon_liste = ['+905544689718','+905526643407','+905523741700','+905074825867']
kisiler = ['Serdar bey','Ömer bey','Efe bey','İdris bey']
for i in range(0,5):
    pywhatkit.sendwhatmsg(telefon_liste[i],f"Sayın ; {kisiler[i]}Dükkanı kapatıyoruz. Toptan fiyata halka!",22,5+i)

#https://web.whatsapp.com/send?phone=5545334016&text=Merhaba+bilgi+almak+istiyorum
