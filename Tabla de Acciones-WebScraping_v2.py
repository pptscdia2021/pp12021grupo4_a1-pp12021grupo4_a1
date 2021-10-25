# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 21:38:48 2021

@author: Vir
"""


# import libraries
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# indicar la ruta
url_page = 'https://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000'
# tarda 480 milisegundos
page = requests.get(url_page).text 
soup = BeautifulSoup(page, "lxml")
# Obtenemos la tabla por un ID específico
tabla = soup.find('table', attrs={'id': 'ctl00_Contenido_tblAcciones'})
tabla

nombre=""
util=0
dif=0
maximo = 0
minimo =0
fecha = ""

nroFila=0 # Flag se utiliza lara tener visibilidad de las iteraciones
# DEFINO ARRAY DONDE GUARDAR LOS DATOS DE CADA ITERACION
array=[]

for fila in tabla.find_all('tr'):
    # for row in  tabla.find_all("td")::
    nroCelda=0
    for celda in fila.find_all('td'):
        if nroCelda==0:
            nombre=celda.text
            print("nombre:", nombre)
        if nroCelda==1:
            util=celda.text
            print("util:", util)    
        if nroCelda==2:
            dif=celda.text
            print("dif:", dif)
        if nroCelda==3:
            maximo=celda.text
            print("maximo:", maximo)
        if nroCelda==4:
            minimo=celda.text
            print("minimo:", minimo)
        if nroCelda==7:
            fecha=celda.text
            print("fecha:", fecha)
        nroCelda=nroCelda+1 # FLAG que incrementa la celda
    nroFila=nroFila+1 # Flag que incrementa la fila 
    # AGREGO/GUARDO LOS DATOS EN FORMATO DICCIONARIO EN EL ARRAY.
    array.append({"nombre": nombre, "util": util, "dif":dif, "maximo":maximo, "minimo":minimo, "fecha":fecha})

# Abrimos el csv con open para que pueda agregar contenidos al final del archivo
# agrego el parametro newline="" para que no haga un salto de linea 
with open('bolsa_de_madrid.csv', 'a', newline="") as csv_file: # Abro/Creo archivo CSV al que llamare csv_file dentro de python
    writer = csv.writer(csv_file) # Determino que voy a escribir el archivo
    writer.writerow(["nombre", "util" , "dif", "maximo", "minimo","fecha"])
    for row in array : # Recorro el diccionario linea por linea.
        #print(row['name'])
        
        #if(row['name'] != ""): # Como el primer registro es null y no quiero que se escriba en el CSV con IF salteo ese registro
            writer.writerow([row["nombre"], row["util"], row["dif"], row["maximo"], row["minimo"], row["fecha"]])

# importar libreria de panda para trabajar con datos tabulados
import pandas as pd
import codecs # Esta libreria la utilizo para acomodar el decodificado de caracteres.

# Esta linea decodifica el archivo CSV para que quede en UTF-8
with codecs.open(r"C:\xampp\htdocs\pp12021grupo4_a1-pp12021grupo4_a1\bolsa_de_madrid.csv", 'r', encoding='utf-8', errors='ignore') as fdata:
# instancio pandas  (con pd) y llamo a la funcion read_csv el cual lee el archivo CSV y lo convierte en tabla
    df = pd.read_csv(fdata)
    
print(" ################################ \n FINALIZO \n ######################## \n")

# Convertir el valor de STRING a FLOAT
df['util'] = df['util'].apply(lambda x: x.replace(',','.'))
# Convierte los datos a tipo float
df['util'] = df['util'].astype(float)

print(df.sort_values(by=['util']))


# VALORES MAXIMOS Y MINIMOS
#Valor Maximo
max_valor = df.util.max()
print(max_valor)
#Valor Minimo
min_valor = df.util.min()
print(min_valor)
# Los 2 maximos
# Ordeno de Menor a Mayor por la columna Close
m_mayores = df.sort_values('util').tail(2)
m_menores = df.sort_values('util').head(2)
print(m_mayores)
print(m_menores)

#df['util'] = df['util'].astype(float)

