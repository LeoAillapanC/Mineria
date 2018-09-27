#Se importan la librerias a utilizar
import pandas as pd
import numpy as np
import quandl
import pandas_datareader.data as web
import datetime

#quandl.ApiConfig.api_key = "xcNBNsZfuA-jrf9K4N9z"
########## PREPARAR LA DATA ##########
#Se define el periodo periodo de tiempo a utilizar
#start = datetime.datetime(2010, 1, 1)
#end = datetime.date.today()
#start = pd.to_datetime("2010-01-01")
#end = pd.to_datetime("2018-09-18")

#Esta será la variable que se cambiará para colocar la acción que se quiera evaluar
#predict_stock = 'NFLX'

#Se obtiene la data de la página de morningstar
#df = web.DataReader(predict_stock, "morningstar", start, end)
#df = web.DataReader(predict_stock, "quandl", start, end)
#df = quandl.get("EOD/AMD",start_date=start,end_date=end)

#Se guarda la data en un archivo .csv
#df.to_csv('predict_stockAMD.csv')

#Lectura del archivo .csv para manipular la data
df = pd.read_csv('predict_stockAPPLE.csv', parse_dates = True, index_col = 1)  #analiza la columna 1 como fechas

#Calculo el porcentaje del promedio de cambios durante el día
df['Promedio_HL'] = (df['High'] - df['Low']) / df['Low'] * 100.0
df['Promedio_Cambios_Dia'] = (df['Close'] - df['Open']) / df['Open'] * 100.0

#Selecciono solo los datos que voy a utilizar en el análisis
df = df[['Close', 'Promedio_HL', 'Promedio_Cambios_Dia', 'Volume']]

#En caso que alguna data no se encuentre NAN se rellena con el valor 99999
df.fillna(value=-99999, inplace=True)
