# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 17:00:41 2021

@author: Vir
"""

from bolsa_madrid import * 
from yyfinance import *

if __name__ == "__main__":
  url = "https://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000"
  ruta_descarga = " "
  
  # Instancio la clase BOLSA_MAD
  bm = Bolsa_madrid(url,ruta_descarga)
  result = bm.buscar_datos() # devuelve un aarray
  print(result)
  bm.crear_csv(result) # Crea el CSV
  df = bm.lee_csv() # lee el csv. Crea y Devuelve un DF
  print(df)
  print(bm.max_valor())
  print(bm.min_valor())
  print(bm.to_max_valor())
  print(bm.to_min_valor())
  
  # Y FINANCE
  array=["BBVA","SAN","TEF","MT"] #defino el array de las monedas que voy a utilizar.
  yaf = Yfinance(array,ruta_descarga) # instancio la clase
  df = yaf.df_monedas() # busca los tikets del array y arma un DF
  print(df)
  yaf.guardar_csv() # crea y guarda en un CSV
  print(yaf.max_valor())
  print(yaf.min_valor())
  print(yaf.to_max_valor())
  print(yaf.to_min_valor())
  
  
  
  
  