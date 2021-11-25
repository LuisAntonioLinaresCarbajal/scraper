from selenium import webdriver #paqueteria selenium y webdriver para lograr el scriping
import time #paqueteria para obtener la fecha del servidor
from urllib.request import urlopen

#obtener los datos con: (Python and Selenium)
PATH = "C:\Program Files (x86)\chromedriver.exe"  
driver = webdriver.Chrome(PATH) 
driver.get("http://notificacion.pjedomex.gob.mx/notificacion/vista/php/consultaServiciosBoletin.php#") #link de la pagina de la que se extraeran los datos
time.sleep(5) #tiempo de ejecucion
Data = driver.find_element_by_xpath('//*[@id="tblResultados_wrapper"]') #etiqueta Xpath de la que obtendremos los datos 
print('Dictionary: '+ Data)
driver.quit()

#informacion relativa de la pagina
pagina = urlopen("http://notificacion.pjedomex.gob.mx/notificacion/vista/php/consultaServiciosBoletin.php#")
headers = pagina.info()
print('FECHA :', headers['date'])
print('HEADERS:,')
print('------------------------')
print(headers)

#fecha del servidor donde esta alojada la pagina
data = pagina.read().decode('utf-8')
print('LENGTH:', len(data))
print('DATA :')
print('------------------------')
print(data)