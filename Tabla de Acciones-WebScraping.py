
# import libraries
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
# importar libreria de panda para trabajar con datos tabulados
import pandas as pd
import codecs # Esta libreria la utilizo para acomodar el decodificado de caracteres


url_page = 'http://www.bolsamadrid.es/esp/aspx/Indices/Resumen.aspx'
page = requests.get(url_page).text 
soup = BeautifulSoup(page, "lxml")

# Obtenemos la tabla por un ID específico
tabla = soup.find('table', attrs={'id': 'ctl00_Contenido_tblÍndices'})

#Extrayendo datos de la tabla
name=""
price=""
nroFila=0 # Flag se utiliza lara tener visibilidad de las iteraciones
# DEFINO ARRAY DONDE GUARDAR LOS DATOS DE CADA ITERACION
array=[]

for fila in tabla.find_all('tr'):
    # for row in  tabla.find_all("td")::
    nroCelda=0
    for celda in fila.find_all('td'):
        if nroCelda==0:
            name=celda.text
            print("Indice:", name)
        if nroCelda==2:
            price=celda.text
            print("Valor:", price)
        nroCelda=nroCelda+1 # FLAG que incrementa la celda
    nroFila=nroFila+1 # Flag que incrementa la fila 
    # AGREGO/GUARDO LOS DATOS EN FORMATO DICCIONARIO EN EL ARRAY.
    array.append({"name": name, "price": price})


# Abrimos el csv con open para que pueda agregar contenidos al final del archivo
# agrego el parametro newline="" para que no haga un salto de linea 
with open('bolsa_ibex35.csv', 'a', newline="") as csv_file: # Abro/Creo archivo CSV al que llamare csv_file dentro de python
    writer = csv.writer(csv_file) # Determino que voy a escribir el archivo
    for row in array : # Recorro el diccionario linea por linea.
        #print(row['name'])
        
        if(row['name'] != ""): # Como el primer registro es null y no quiero que se escriba en el CSV con IF salteo ese registro
            writer.writerow([row['name'], row['price'], datetime.now()])

# importar libreria de panda para trabajar con datos tabulados
import pandas as pd
import codecs # Esta libreria la utilizo para acomodar el decodificado de caracteres.

# Esta linea decodifica el archivo CSV para que quede en UTF-8
with codecs.open(r"C:\repo_Git\bolsa_ibex35.csv", 'r', encoding='utf-8',
                 errors='ignore') as fdata:
# instancio pandas  (con pd) y llamo a la funcion read_csv el cual lee el archivo CSV y lo convierte en tabla
    df = pd.read_csv(fdata)

print (df)
