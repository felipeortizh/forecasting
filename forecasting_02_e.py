# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 19:09:32 2023

env: dardos2

Calcula las metricas usando un modelo baseline y otro de Machine Learning

@author: forti
"""

import pandas as pd
from darts import TimeSeries
from darts.models import NaiveDrift
from darts.models import RandomForest
from darts.metrics import mae, mape, rmse
import matplotlib.pyplot as plt


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

######## Create a DataFrame with metric values ####################
metrics = {
    'Metric': ['MAE', 'MAPE', 'RMSE'],
}

df_3 = pd.DataFrame(metrics)
##################################################################

j=0
number_of_columns = df_2.shape[1] - 1

for i in range(number_of_columns):

    # Create a TimeSeries object, specifying the time and value columns
    series = TimeSeries.from_dataframe(df_2, "id_fec_diaria", df_2.columns[i+1])
    
    # Set aside the last 16 days as a validation series
    train, val = series[:-17], series[-17:]
    
    
    #################### Train Forecasting Models ######################
    # Train baseline model
    model_1 = NaiveDrift()
    model_1.fit(train)
    
    # Train ML model
    model_2 = RandomForest(lags=15)
    model_2.fit(train)
    ####################################################################
    
    ################## Predict with Forecasting Models #################
    # Predict using baseline model
    prediction_1 = model_1.predict(len(val))
    
    # Predict using RandomForest
    prediction_2 = model_2.predict(len(val))
    #df_4 = pd.DataFrame(prediction_2.pd_dataframe())
    ###################################################################
    
    ####################### metrics #######################
    # Calculate MAE
    mae_1 = mae(val, prediction_1)
    mape_1 = mape(val, prediction_1)
    rmse_1 = rmse(val, prediction_1)
    
    mae_2 = mae(val, prediction_2)
    mape_2 = mape(val, prediction_2)
    rmse_2 = rmse(val, prediction_2)
    ###################################################################
    
    ######## plot forecast from validation set ########################
    # series.plot()
    # prediction_1.plot(label="forecast", low_quantile=0.05, high_quantile=0.95)
    # plt.legend()
    ###################################################################
    
    
    metric_1 = [mae_1, mape_1, rmse_1]
    metric_2 = [mae_2, mape_2, rmse_2]
    position = j+1
    df_3.insert(position, df_2.columns[i+1] + ' (modelo 1)', metric_1)
    df_3.insert(position + 1, df_2.columns[i+1] + ' (modelo 2)', metric_2)
    j=j+2
    
    
#################### ELEGIR TIENDA ##########################

# # Save the DataFrame to a CSV file
# csv_filename = 't1_hiper-basico-metricas.csv'
# df_3.to_csv(csv_filename)

# Save the DataFrame to a CSV file
csv_filename = 't2_hiper-intermedio-metricas.csv'
df_3.to_csv(csv_filename)

# # Save the DataFrame to a CSV file
# csv_filename = 't3_hiper-plus-metricas.csv'
# df_3.to_csv(csv_filename)

# # Save the DataFrame to a CSV file
# csv_filename = 't4_super-basico-metricas.csv'
# df_3.to_csv(csv_filename)

# # Save the DataFrame to a CSV file
# csv_filename = 't5_super-intermedio-metricas.csv'
# df_3.to_csv(csv_filename)

# # Save the DataFrame to a CSV file
# csv_filename = 't6_super-plus-metricas.csv'
# df_3.to_csv(csv_filename)

##############################################################















