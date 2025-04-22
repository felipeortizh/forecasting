# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 23:21:39 2023

t1_hiper-basico = En 1206 (1022, 1248) de los 1668 productos el error MAE (MAPE,RMSE)
                  es menor con el modelo 2:RandomForest
                  
t2_hiper-intermedio = En 923 (769, 958) de los 1261 productos el error MAE (MAPE,RMSE)
                  es menor con el modelo 2: RandomForest
                  
t3_hiper-plus = En 569 (495, 583) de los 754 productos el error MAE (MAPE,RMSE)
                  es menor con el modelo 2: RandomForest
                  
t4_super-basico = En 189 (146, 201) de los 277 productos el error MAE (MAPE,RMSE)
                  es menor con el modelo 2:RandomForest
                  
t5_super-intermedio = En 357 (307, 360) de los 491 productos el error MAE (MAPE,RMSE)
                  es menor con el modelo 2:RandomForest

t6_super-plus = En 299 (255, 306) de los 390 productos el error MAE (MAPE,RMSE)
                  es menor con el modelo 2: RandomForest


Checa para cuantos productos el error MAE es menor con el modelo 2 (RandomForest)
@author: forti
"""

import pandas as pd


#################### ELEGIR TIENDA ##########################

# # read new dataframe with columns representing each product-store
# df = pd.read_csv("t1_hiper-basico-metricas.csv", delimiter=",")
# df = df.drop(columns='Unnamed: 0')

# read new dataframe with columns representing each product-store
df = pd.read_csv("t2_hiper-intermedio-metricas.csv", delimiter=",")
df = df.drop(columns='Unnamed: 0')

# # read new dataframe with columns representing each product-store
# df = pd.read_csv("t3_hiper-plus-metricas.csv", delimiter=",")
# df = df.drop(columns='Unnamed: 0')

# # read new dataframe with columns representing each product-store
# df = pd.read_csv("t4_super-basico-metricas.csv", delimiter=",")
# df = df.drop(columns='Unnamed: 0')

# # read new dataframe with columns representing each product-store
# df = pd.read_csv("t5_super-intermedio-metricas.csv", delimiter=",")
# df = df.drop(columns='Unnamed: 0')

# # read new dataframe with columns representing each product-store
# df = pd.read_csv("t6_super-plus-metricas.csv", delimiter=",")
# df = df.drop(columns='Unnamed: 0')

################################################################

number_of_columns = df.shape[1] - 1
cont = 0
for i in range(0,number_of_columns,2):
    if df.loc[0,df.columns[i+1]] > df.loc[0,df.columns[i+2]]:
        cont = cont + 1


print("Numero de productos con MAE_2 (modelo 2) menor que MAE_1 (modelo 1) = ", cont)



cont = 0
for i in range(0,number_of_columns,2):
    if df.loc[1,df.columns[i+1]] > df.loc[1,df.columns[i+2]]:
        cont = cont + 1


print("Numero de productos con MAPE_2 (modelo 2) menor que MAPE_1 (modelo 1) = ", cont)


cont = 0
for i in range(0,number_of_columns,2):
    if df.loc[2,df.columns[i+1]] > df.loc[2,df.columns[i+2]]:
        cont = cont + 1


print("Numero de productos con MAPE_2 (modelo 2) menor que MAPE_1 (modelo 1) = ", cont)




