
'''
# CODIGO QUE DEVUELVE UN DF POR CADA MONEDA
#pip install yfinance
import yfinance as yf

if __name__ == '__main__':
        # Mostrar datos en tabla 

        # Datos del día "BBVA"
        print("---------Tabla de precios Banco BBVA----------\n")
        BBVA_precios = yf.download("BBVA", period='1d')
        print (BBVA_precios)
        print("\n")

        # Datos del día "Banco Santander"
        print("---------Tabla de precios Banco Santander----------\n")
        SAN_precios= yf.download("SAN", period= '1d')
        print(SAN_precios)
        print("\n")

        # Datos del día "Telefónica"
        print("---------Tabla de precios Telefónica----------\n")
        TEF_precios= yf.download("TEF", period= '1d')
        print(TEF_precios)
        print("\n")

        # Datos del día "Arcelormittal"
        print("---------Tabla de precios Arcelomittal----------\n")
        MT_precios= yf.download("MT", period= '1d')
        print(MT_precios)
        print("\n")

'''

'''
#CODIGO DEVUELVE 1ROW x 24 COLUMNAS

import pandas as pd
from datetime import date, timedelta

start_date = date.today() - timedelta(days=1)
enddate = date.today()

array_monedas =["BBVA","SAN","TEF","MT"]
array=[]

df_final = yf.download(
    tickers = array_monedas,
    start = start_date,
    end= enddate,
    group_by='ticker',
    threads = True    
    )
df_final.tail()
  
'''
# 1 normalizar los datos (la informacion no esta almacenada en ningun csv, y deben estar en un unico archivo)
# El script busca las monedas y las carga todas juntas en un unico DF para su analisis
import pandas as pd
import yfinance as yf
# ARRAY DE MONEDAS A BUSCAR


def df_monedas(array_monedas):
    array_monedas = array_monedas # tiene las monedas que yo quiero buscar["BBVA","SAN","TEF","MT"]
#Creo los headers del data frame final (COLUMNAS DEL DATA FRAME FINAL)
#Aca voy a ir guardando lo que me devuelve la consulta y que va a ser mi tabla final.
    df_final= pd.DataFrame(columns = ['Data','Moneda','Open','Low','High','Volumne'])
    
    # RECORRO ARRAY DE MONEDAS Y CREO EL ARRAY FINAL
    for moneda in array_monedas :
        # Instancio un Ticker le paso la moneda que quiero buscar y el periodo.
        #Busca los datos de la moneda que le pido. 
        df = yf.Ticker(moneda).history(period="1d")
        # Elimino las columnas del dataframe que envia yfinance
        df.drop(["Dividends","Stock Splits"], axis=1, inplace=True)
        # Agrego la columna MONEDA para identificar el registro
        df["Moneda"]=moneda
        # Agreg
        df_final=df_final.append(df)
        
    return df_final


array_monedas =["BBVA","SAN","TEF","MT"]
d = df_monedas(array_monedas)
print(d,"\n")

#Creo el CSV desde un panda data frame
csvstring = d.to_csv('Tabla Yfinance.csv')
print(csvstring)


print("OBJETIVO 2 : Cotizacion de Mayor ganancia y Mayor perdida")
# VALORES MAXIMOS Y MINIMOS
#Valor Maximo
max_valor = d.Close.max()
print(max_valor)
#Valor Minimo
min_valor = d.Close.min()
print(min_valor)
# Los 2 maximos
# Ordeno de Menor a Mayor por la columna Close
m_mayores = d.sort_values('Close').tail(2)
m_menores = d.sort_values('Close').head(2)
print(m_mayores)
print(m_menores)




    
      





