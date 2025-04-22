Ejecutar en orden:


a) forecasting_01.py: Programa que genera ( para la tienda deseada) una matriz
de datos ("t6_super-plus.csv")donde cada columna representa un producto y sus respectivas ventas.

b) forecasting_02_e.py: Programa elimina productos con el 50% de valores faltantes, interpola y calcula el error MAE,MAPE y RMSE para cada producto usando dos modelos predictivos (Naive Forecast y Random Forest). Los datos se guardan en el archivo "t6_super-plus-metricas.csv".

c) forecasting_03_c.py:  Programa que elimina productos con el 50% de valores faltantes, interpola y calcula el pronostico del 1 de noviembre al 15 de noviembre del 2021. Los datos se guardan en el archivo "t6_super-plus-pronostico.csv"

d) forecasting_04_b.py: Programa que calcula el numero de productos en la cual el error MAE, MAPE Y RMSE es menor con el modelo 2 (Random Forest).

e) forecasting_03_c_deploy.py: Web-app que entrena el modelo 2 y grafica las ventas y pronostico del producto deseado. 

Para ver en linea esta web-app ir a la siguiente liga: 

https://atrenux-enki-demo.hf.space



NOTA: Ejecutar para cada tienda. Elegir tienda al principio y al final de cada programa