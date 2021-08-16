from urllib.request import urlopen
from bs4 import BeautifulSoup
import logging
import time

logging.basicConfig(filename='portaldelagro.log',
                    filemode='a',format='%(asctime)s : %(levelname)s : %(message)s',
                    datefmt='%d/%m/%y %H:%M:%S',
                    level=logging.INFO)
logging.info('Scraper pagina portal agro Chile')
start = time.process_time()
url_scraper = "https://www.portalagrochile.cl/"
request_pagina = urlopen(url_scraper) 
pagina_html = request_pagina.read()
request_pagina.close()

html_soup = BeautifulSoup(pagina_html, 'html.parser')
contenido_pagina = html_soup.find_all('div', class_ ='td-block-row')

filename = 'portaldelagro.csv'

f = open(filename, 'w')


f.write("Titulo;Imagen;Fecha;Hipervinculo;Autor"+"\n")  

for contenido in contenido_pagina:
    fecha = contenido.find('span', class_="td-post-date").text
    logging.info('Fecha de la noticia: '+str(fecha))
    imagen = contenido.find('img').get('src')
    titulo = contenido.find('h3', class_="entry-title").text
    logging.info('Titulo de la noticia: '+str(titulo))
    #descripcion = contenido.find('div', class_="td-excerpt").text
    hipervinculo = contenido.find('a').get('href')
    autor = contenido.find('span', class_='td-post-author-name').text  
    f.write(titulo+";"+str(imagen)+";"+fecha+";"+str(hipervinculo)+";"+autor+";""\n")

logging.warning('Cada titulo y fecha esta individualizado por cda noticia')


end = time.process_time()
logging.info('Tiempo total de ejecucion: '+str(end - start))

f.close()