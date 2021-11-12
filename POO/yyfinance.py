import pandas as pd
import yfinance as yf

class Yfinance:
    def __init__(self,array_monedas,ruta_descarga):
        self.array_monedas =  array_monedas
        self.ruta_descarga =  ruta_descarga
        self.df ={}

    def df_monedas(self):
            array_monedas = self.array_monedas #["BBVA","SAN","TEF","MT"]
            #COLUMNAS DEL DATA FRAME FINAL
            df_final= pd.DataFrame(columns = ['Data','Moneda','Open','Low','High','Volumne'])
            
            # RECORRO ARRAY DE MONEDAS Y CREO EL ARRAY FINAL
            for moneda in array_monedas :
                # Instancio un Ticker (info, moneda) y el historico de precio en dias
                df = yf.Ticker(moneda).history(period="1d")
                # Elimino las columnas del dataframe que envia yfinance
                df.drop(["Dividends","Stock Splits"], axis=1, inplace=True)
                # Agrego la columna MONEDA para identificar el registro
                df["Moneda"]=moneda
                # Agrego df al df final
                df_final=df_final.append(df)
            self.df = df_final
            return self.df

    def guardar_csv(self):
        #Creo el CSV desde un panda data frame
        self.df.to_csv(r""+self.ruta_descarga+"Tabla Yfinance.csv")
        return True
    def max_valor(self):
        return self.df.Close.max()
    def min_valor(self):
        return self.df.Close.min()
    def to_max_valor(self):
        return self.df.sort_values('Close').tail(2)
    def to_min_valor(self):
        return self.df.sort_values('Close').head(2)
    

