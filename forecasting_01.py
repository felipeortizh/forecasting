# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 19:57:13 2023

env: dardos2

Separacion de productos por tienda

@author: forti
"""

import pandas as pd
#from darts import TimeSeries

# Read a pandas DataFrame
df = pd.read_csv("data_prueba_Forecasting.csv", delimiter=",")
#df = pd.read_csv("prueba_repetida.csv", delimiter=",")

#################### ELEGIR TIENDA ##########################

# ################  tienda_1 = Hiper-Basico #################
# df = df[(df != 'Super').all(axis=1)]
# df = df[(df != 'Intermedio').all(axis=1)]
# df = df[(df != 'Plus').all(axis=1)]
# ###########################################################

###############  tienda_2 = Hiper-Intermedio ###############
df = df[(df != 'Super').all(axis=1)]
df = df[(df != 'Basico').all(axis=1)]
df = df[(df != 'Plus').all(axis=1)]
############################################################

# ################  tienda_3 = Hiper-Plus ###################
# df = df[(df != 'Super').all(axis=1)]
# df = df[(df != 'Intermedio').all(axis=1)]
# df = df[(df != 'Basico').all(axis=1)]
# ###########################################################

# ################  tienda_4 = Super-Basico #################
# df = df[(df != 'Hiper').all(axis=1)]
# df = df[(df != 'Intermedio').all(axis=1)]
# df = df[(df != 'Plus').all(axis=1)]
# ###########################################################

# ################  tienda_5 = Super-Intermedio #############
# df = df[(df != 'Hiper').all(axis=1)]
# df = df[(df != 'Basico').all(axis=1)]
# df = df[(df != 'Plus').all(axis=1)]
# ###########################################################

# ################  tienda_6 = Super-Plus ###################
# df = df[(df != 'Hiper').all(axis=1)]
# df = df[(df != 'Intermedio').all(axis=1)]
# df = df[(df != 'Basico').all(axis=1)]
# ###########################################################

#############################################################
#convert the date column into datetime
df['id_fec_diaria'] = pd.to_datetime(df['id_fec_diaria'], yearfirst=True)


#create index with datetime values
#df.set_index('date', inplace=True)


# Define the new date range
new_date_range = pd.date_range(start='2021-08-01', end='2021-10-31')

# Create a new datetime index with the desired date range
#date_range = pd.date_range(start=df.index.min(), end=df.index.max(), freq='D')


# Group by product and apply reindex to each group

df_grouped = df.groupby('Producto')

################################################################
# Define a function to remove duplicates within each group
def remove_duplicates(group):
    return group.drop_duplicates(subset='id_fec_diaria')

# Apply the function to each group
result = df_grouped.apply(remove_duplicates)

result = result.rename(columns={'Producto': 'Product'})
df_grouped = result.groupby('Product')
################################################################

# Re-index with a new date-range for each group
df_reindexed = df_grouped.apply(lambda x: x.set_index('id_fec_diaria').reindex(new_date_range))

# Reset the index
df_reindexed = df_reindexed.reset_index(level=0, drop=True).reset_index()
df_reindexed.columns = [ 'id_fec_diaria','Unnamed: 0', 'Formato', 'Subformato', 'Tienda', 'Producto',
        'Venta', 'Precio', 'Venta_aa', 'Precio_aa']

# Fill missing sales values with 0
df_reindexed['Venta'] = df_reindexed['Venta'].fillna(0)


#################################################################

#pivot table method
pivot_table = df_reindexed.pivot_table(index='id_fec_diaria', columns='Producto', values='Venta', aggfunc='sum')




#################### ELEGIR TIENDA ##########################


# # Save the DataFrame to a CSV file
# csv_filename = 't1_hiper-basico.csv'
# pivot_table.to_csv(csv_filename)

# # Save the DataFrame to a CSV file
# csv_filename = 't2_hiper-intermedio.csv'
# pivot_table.to_csv(csv_filename)

# # Save the DataFrame to a CSV file
# csv_filename = 't3_hiper-plus.csv'
# pivot_table.to_csv(csv_filename)

# # Save the DataFrame to a CSV file
# csv_filename = 't4_super-basico.csv'
# pivot_table.to_csv(csv_filename)

# # Save the DataFrame to a CSV file
# csv_filename = 't5_super-intermedio.csv'
# pivot_table.to_csv(csv_filename)

# # Save the DataFrame to a CSV file
# csv_filename = 't6_super-plus.csv'
# pivot_table.to_csv(csv_filename)

##############################################################
