# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 21:38:48 2021

@author: Vir
"""


# Importamos las librerías Python que utilizaremos:
import requests
from bs4 import BeautifulSoup
import csv


# Indicamos la ruta de la web que deseamos acceder:
url_page = 'https://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000'

#Hacemos el request a esa ruta y procesamos el HTML (la convierte en texto)
#mediante un objeto de tipo BeautifulSoap:
page = requests.get(url_page).text #la convierte en texto
soup = BeautifulSoup(page, "lxml") #de HTML  a xml

# Obtenemos la tabla por un ID específico y de ahi vamos a acceder a sus celdas.
tabla = soup.find('table', attrs={'id': 'ctl00_Contenido_tblAcciones'})
tabla

#Dentro de la tabla y siendo que en este caso no tenemos un acceso directo a las celdas por ids únicos, sólo nos queda iterar
#Entonces, accederemos a la primer fila y obtendremos de las celdas el nombre del índice y su valor:

nombre=""
ultimo=0
dif=0
maximo = 0
minimo =0
fecha = ""

# DEFINO ARRAY DONDE GUARDAR LOS DATOS DE CADA ITERACION
array=[]


nroFila=0 # Flag se utiliza Para tener visibilidad de las iteraciones.
for fila in tabla.find_all('tr'):
    
    nroCelda=0
    for celda in fila.find_all('td'):
        if nroCelda==0:
            nombre=celda.text
          
        if nroCelda==1:
            ultimo=celda.text
            
        if nroCelda==2:
            dif=celda.text
          
        if nroCelda==3:
            maximo=celda.text
          
        if nroCelda==4:
            minimo=celda.text
          
        if nroCelda==7:
            fecha=celda.text
        
        nroCelda=nroCelda+1 # FLAG que incrementa la celda
    nroFila=nroFila+1 # Flag que incrementa la fila 
    
    # AGREGO/GUARDO LOS DATOS EN FORMATO DICCIONARIO EN EL ARRAY.
    array.append({"nombre": nombre, "ultimo": ultimo, "dif":dif, "maximo":maximo, "minimo":minimo, "fecha":fecha})

#EMPIEZO A CREAR EL CSV con la libreria CSV.
# Abrimos el csv con open para que pueda agregar contenidos al final del archivo.
# Abro/Creo archivo CSV al que llamare csv_file dentro de python. https://www.w3schools.com/python/ref_func_open.asp
# Agrego el parametro newline="" para que no haga un salto de linea.
with open('bolsa_de_madrid.csv', 'a', newline="") as csv_file: 
    writer = csv.writer(csv_file) # Determino que voy a escribir el archivo
    writer.writerow(["nombre", "ultimo" , "dif", "maximo", "minimo","fecha"]) #Header de la tabla.
    for row in array : # Recorro el diccionario linea por linea.
             
        #if(row['nombre'] != ""): # Como el primer registro es null y no quiero que se escriba en el CSV con IF salteo ese registro
            writer.writerow([row["nombre"], row["ultimo"], row["dif"], row["maximo"], row["minimo"], row["fecha"]])


# Importar libreria de panda para trabajar con datos tabulados
import pandas as pd
# Esta libreria la utilizo para acomodar el decodificado de caracteres.
import codecs 

# Esta linea decodifica el archivo CSV para que quede en UTF-8
#C:\xampp\htdocs\pp12021grupo4_a1-pp12021grupo4_a1\
with codecs.open(r"bolsa_de_madrid.csv", 'r', encoding='utf-8', errors='ignore') as fdata:
# instancio pandas y llamo a la funcion read_csv el cual lee el archivo CSV y lo convierte en tabla
    df = pd.read_csv(fdata)
    df
print(" ################################ \n FINALIZO CSV \n ######################## \n")

# Convertir el valor de STRING a FLOAT
df['ultimo'] = df['ultimo'].apply(lambda x: x.replace(',','.'))
# Convierte los datos a tipo float
df['ultimo'] = df['ultimo'].astype(float)

#Ordeno el df de menor a mayor segun la columna ultimo.
print(df.sort_values(by=['ultimo']), "\n")



print("OBJETIVO 2 : Cotizacion de Mayor ganancia y Mayor perdida")
# Obtengo los VALORES MAXIMOS Y MINIMOS del df
#Valor Maximo
max_valor = df.ultimo.max()
print(max_valor)
#Valor Minimo
min_valor = df.ultimo.min()
print(min_valor)
# Los 2 maximos
# Ordeno de Menor a Mayor por la columna Ultimo
m_mayores = df.sort_values('ultimo').tail(2)
m_menores = df.sort_values('ultimo').head(2)
print(m_mayores)
print(m_menores)



