# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 19:09:32 2023

env: dardos2

Pronostica usando un modelo de Machine Learning (RandomForest)

@author: forti
"""

import pandas as pd
from darts import TimeSeries
from darts.models import RandomForest
from darts.metrics import mae, mape, rmse
import matplotlib.pyplot as plt
import streamlit as st

st.title('Pronostico del Producto (tienda 2)')
st.write('\n')
st.write('\n')
st.write('\n')
st.sidebar.title(":blue[Escribe el numero de su producto:]")
resultado = st.sidebar.text_input("Ejemplo: 116.0", key="name")
valor = st.session_state.name

#resultado = st.sidebar.button("Pronosticar")

#################### ELEGIR TIENDA ##########################

# # read new dataframe with columns representing each product-store
# df = pd.read_csv("t1_hiper-basico.csv", delimiter=",")

# read new dataframe with columns representing each product-store
df = pd.read_csv("t2_hiper-intermedio.csv", delimiter=",")

# # read new dataframe with columns representing each product-store
# df = pd.read_csv("t3_hiper-plus.csv", delimiter=",")

# # read new dataframe with columns representing each product-store
# df = pd.read_csv("t4_super-basico.csv", delimiter=",")

# # read new dataframe with columns representing each product-store
# df = pd.read_csv("t5_super-intermedio.csv", delimiter=",")

# # read new dataframe with columns representing each product-store
# df = pd.read_csv("t6_super-plus.csv", delimiter=",")

################################################################

###############  Remove products with 50% missing values ##################
max_nan_threshold = 46
for column_name in df.columns:
    missing_values_count = df[column_name].isna().sum()
    
    # Remove the column if the missing values count is below the threshold
    if missing_values_count >= max_nan_threshold:
        df = df.drop(columns=[column_name])
###########################################################################  
    
# interpolate to replace missing values between numeric values
df_2 = df.interpolate(method="linear")

# backfilling to replace missing values
df_2 = df_2.bfill()


########## Check for any NaN values left  #########################
# if df_2.isnull().values.any():
#     print("The DataFrame contains NaN values.")
# else:
#     print("The DataFrame does not contain any NaN values.")
###################################################################

######## Create a DataFrame with dates ############################

# Create the date range
new_date_range = pd.date_range(start='2021-11-01', end='2021-11-15')

# Convert the date range to a DataFrame
df_3 = pd.DataFrame({'Fecha': new_date_range})
##################################################################


number_of_columns = df_2.shape[1] - 1
if resultado:
    
    for i in range(1):
    
        # Create a TimeSeries object, specifying the time and value columns
        series = TimeSeries.from_dataframe(df_2, "id_fec_diaria", valor)
            
        
        #################### Train Forecasting Models ######################
        # # Train baseline model
        # model_1 = NaiveDrift()
        # model_1.fit(series)
        
        # Train ML model
        model_2 = RandomForest(lags=15)
        model_2.fit(series)
        ####################################################################
        
        ################## Predict with Forecasting Models #################
        # # Predict using baseline model
        # prediction_1 = model_1.predict(15)
        
        # Predict using RandomForest
        prediction_2 = model_2.predict(15)
        df_4 = pd.DataFrame(prediction_2.pd_dataframe())
        df_4 = df_4.reset_index(drop=True)
        ###################################################################
        
        ####### plot forecast from validation set ########################
        series.plot()
        figure_2 = prediction_2.plot(label="forecast", low_quantile=0.05, high_quantile=0.95)
        st.pyplot(figure_2)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        # plt.xlabel('Fecha')
        # plt.ylabel('Ventas')
        # plt.legend()
        # plt.subplots_adjust(bottom=0.2)
        # plt.savefig("producto_forecast_2.png", dpi=200)
        
        ###################################################################
        
    
        df_5 = pd.concat([df_3, df_4], axis=1)
        # Update df_3 to include the new columns from df4
        df_3 = df_5.copy()
        st.dataframe(df_3, use_container_width=True)
    
        ##############################################################################

        @st.cache_data
        def convert_df(df):
            # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')
        
        csv = convert_df(df_3)
        
        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='forecast_tienda_1.csv',
            mime='text/csv',
        )

###############################################################################
    
#################### ELEGIR TIENDA ##########################  

# # Save the DataFrame to a CSV file
# csv_filename = 't1_hiper-basico-pronostico.csv'
# df_3.to_csv(csv_filename)

# # Save the DataFrame to a CSV file
# csv_filename = 't2_hiper-intermedio-pronostico.csv'
# df_3.to_csv(csv_filename)

# # Save the DataFrame to a CSV file
# csv_filename = 't3_hiper-plus-pronostico.csv'
# df_3.to_csv(csv_filename)

# # Save the DataFrame to a CSV file
# csv_filename = 't4_super-basico-pronostico.csv'
# df_3.to_csv(csv_filename)

# # Save the DataFrame to a CSV file
# csv_filename = 't5_super-intermedio-pronostico.csv'
# df_3.to_csv(csv_filename)

# # Save the DataFrame to a CSV file
# csv_filename = 't6_super-plus-pronostico.csv'
# df_3.to_csv(csv_filename)

################################################################



