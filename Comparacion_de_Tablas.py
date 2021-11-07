'''
Leer los dos archivos csv 
Buscar el dato que se puede comparar (vincular los datos)--> Columna Ultimo
Vincular los datos de una tabla con otra
Hacer un reporte de resultados.

Data	Moneda
BBVA	BBVA
B.SANTANDER	SAN
TELEFONICA	TEF
ARCELORMIT.	MT

'''
import pandas as pd
import codecs 
import matplotlib.pyplot as plt

   
# Esta linea decodifica el archivo CSV para que quede en UTF-8
with codecs.open(r"bolsa_de_madrid.csv", 'r', encoding='utf-8', errors='ignore') as fdata:
# instancio pandas  (con pd) y llamo a la funcion read_csv el cual lee el archivo CSV y lo convierte en tabla
    dfbm = pd.read_csv(fdata)
    dfbm
   
# Esta linea decodifica el archivo CSV para que quede en UTF-8
with codecs.open(r"Tabla Yfinance.csv", 'r', encoding='utf-8', errors='ignore') as fdata:
# instancio pandas  (con pd) y llamo a la funcion read_csv el cual lee el archivo CSV y lo convierte en tabla
    dfyf = pd.read_csv(fdata)
    dfyf

# FILTRO EL DF y creo un nuevo DF con los registro que quiero comparar
df_empresas_bm = dfbm[dfbm.nombre.isin(["B.SANTANDER","BBVA","TELEFONICA","ARCELORMIT."])]

df_empresas_bm

# Creo un array con los valores de la nueva columna para relacionar con el otro dataframe
# link ref: https://www.analyticslane.com/2019/05/10/operaciones-de-filtrado-de-dataframe-con-pandas-en-base-a-los-valores-de-las-columnas/
# link ref: https://www.delftstack.com/es/howto/python-pandas/how-to-add-a-new-column-to-existing-dataframe-with-default-value-in-pandas/
# EL ORDEN DEBE SER CALIBRADO CON EL DATA FRAME
print(dfyf)
short_name=["MT", "SAN","BBVA","TEF"]
# Agrego columna al DF con sus datos (short_name)
             # insert(posicion, "nombre_columna", valores,duplicados)
df_empresas_bm.insert(1, "short_name", short_name, allow_duplicates=False)
df_empresas_bm

# Unir 2 data frames
# Link ref: https://www.analyticslane.com/2018/09/10/unir-y-combinar-dataframes-con-pandas-en-python/
df_conjunto = pd.merge(df_empresas_bm, dfyf, left_on='short_name', right_on='Moneda', suffixes=('B_MADRID', 'YFINANCE'))
df_conjunto
# Creo un nuevo data frame para comparar precios 
df_final = df_conjunto[["nombre","short_name", "ultimo","Close","fecha"]]

df_final

# Convertir el valor de STRING a FLOAT
df_final['ultimo'] = df_final['ultimo'].apply(lambda x: x.replace(',','.'))
# Convierte los datos a tipo float
df_final['ultimo'] = df_final['ultimo'].astype(float)


# Recorro el DF y defino nueva columna
# link ref: https://www.delftstack.com/es/howto/python-pandas/how-to-iterate-through-rows-of-a-dataframe-in-pandas/

resultados =[] #creo el array que almacena el resultado para cada fila

for valor in df_final.index :
    print(valor)
    ultimo = float(df_final['ultimo'][valor])
    close = float(df_final['Close'][valor])
    if ultimo > close:
        resultados.append('MADRID')
    else:
        resultados.append('YFINANCE')
    

# Inserto la columna con los datos correspondiente a cada fila        
df_final.insert(4, "MAYOR", resultados, allow_duplicates=False)

df_final
# USO MATPLOTLIB PARA GRAFICAR
# Link ref: https://aprendeconalf.es/docencia/python/manual/matplotlib/

fig, ax = plt.subplots() #defino variables
monedas = df_final.short_name #defino de mi data frame que columa usare en el eje X
ax.scatter(monedas, df_final['ultimo'], color = 'tab:red', label = 'Bolsa Madrid') #defino estilo y columna del DF que voy a graficar
ax.scatter(monedas, df_final['Close'], color = 'tab:blue', label = 'YFinance') #defino estilo y columna del DF que voy a graficar
ax.set_ylabel("VALOR ACCION") #Titulo del eje y
ax.set_xlabel("ACCION") # Titulo del eje x
ax.legend(loc = 'upper right') # leyenda y posicion
ax.grid(axis = 'y', color = 'gray', linestyle = 'dashed') #grilla
plt.show() #dibujo

print("Resultado de comparar las 2 fuentes de datos \n" , df_final)





