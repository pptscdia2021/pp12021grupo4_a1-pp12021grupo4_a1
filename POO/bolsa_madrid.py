# import libraries
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import pandas as pd
import codecs # Esta libreria la utilizo para acomodar el decodificado de caracteres.

class Bolsa_madrid:
    def __init__(self, url, ruta_descarga):
        self.url = url
        self.ruta_descarga = ruta_descarga
        self.df = {}

    
    def buscar_datos(self):
        # tarda 480 milisegundos
        page = requests.get(self.url).text 
        soup = BeautifulSoup(page, "lxml")
        # Obtenemos la tabla por un ID específico
        tabla = soup.find('table', attrs={'id': 'ctl00_Contenido_tblAcciones'})
        nombre=""
        ultimo=0
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
                # print("nombre:", nombre)
                if nroCelda==1:
                    ultimo=celda.text
                # print("ultimo:", ultimo)    
                if nroCelda==2:
                    dif=celda.text
                # print("dif:", dif)
                if nroCelda==3:
                    maximo=celda.text
                # print("maximo:", maximo)
                if nroCelda==4:
                    minimo=celda.text
                # print("minimo:", minimo)
                if nroCelda==7:
                    fecha=celda.text
                #  print("fecha:", fecha)
                nroCelda=nroCelda+1 # FLAG que incrementa la celda
            nroFila=nroFila+1 # Flag que incrementa la fila 
            # AGREGO/GUARDO LOS DATOS EN FORMATO DICCIONARIO EN EL ARRAY.
            array.append({"nombre": nombre, "ultimo": ultimo, "dif":dif, "maximo":maximo, "minimo":minimo, "fecha":fecha})
        return array
    
    def crear_csv(self,array):
        # Abrimos el csv con open para que pueda agregar contenidos al final del archivo
        # agrego el parametro newline="" para que no haga un salto de linea 
        with open(r""+self.ruta_descarga+'bolsa_de_madrid.csv', 'a', newline="") as csv_file: # Abro/Creo archivo CSV al que llamare csv_file dentro de python
            writer = csv.writer(csv_file) # Determino que voy a escribir el archivo
            writer.writerow(["nombre", "ultimo" , "dif", "maximo", "minimo","fecha"])
            for row in array : # Recorro el diccionario linea por linea.
                #print(row['name'])
                
                #if(row['name'] != ""): # Como el primer registro es null y no quiero que se escriba en el CSV con IF salteo ese registro
                    writer.writerow([row["nombre"], row["ultimo"], row["dif"], row["maximo"], row["minimo"], row["fecha"]])
        return True
    
    def lee_csv(self):
        # Esta linea decodifica el archivo CSV para que quede en UTF-8
        with codecs.open(r""+self.ruta_descarga+"bolsa_de_madrid.csv", 'r', encoding='utf-8', errors='ignore') as fdata:
        # instancio pandas  (con pd) y llamo a la funcion read_csv el cual lee el archivo CSV y lo convierte en tabla
            df = pd.read_csv(fdata)
        # Convertir el valor de STRING a FLOAT
        df['ultimo'] = df['ultimo'].apply(lambda x: x.replace(',','.'))
        # Convierte los datos a tipo float
        df['ultimo'] = df['ultimo'].astype(float)
        self.df = df.sort_values(by=['ultimo'])

        return self.df
    def max_valor(self):
        return self.df.ultimo.max()
    def min_valor(self):
        return self.df.ultimo.min()
    def to_max_valor(self):
        return self.df.sort_values('ultimo').tail(2)
    def to_min_valor(self):
        return self.df.sort_values('ultimo').head(2)



        
