import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Ubicacion de archivos
document = "C:/Users/Lenovo/OneDrive/Escritorio/Analisis de datos"
data_energy_plant_1 = document + "/data_plantas_1.xlsx"
data_energy_plant_2 = document + "/data_plantas_2.xlsx"

# Data Frame
df_plant_1 = pd.read_excel(data_energy_plant_1)
df_plant_2 = pd.read_excel(data_energy_plant_2)
df_all_plant = pd.concat([df_plant_1, df_plant_2])

#Suma de active power diario plantas 1,2 y ambas plantas
all_power_plant_1 = df_plant_1['active_power_im'].sum()
all_power_plant_2 = df_plant_2['active_power_im'].sum()
all_power_plants = df_all_plant['active_power_im'].sum()
print("Produccion planta solar uno: ",all_power_plant_1)
print("Produccion planta solar dos: ",all_power_plant_2)
print("Produccion total ambas plantas: ",all_power_plants)

# Energia de activacion minima y maxima planta 1
energy_max_plant_1 = df_plant_1["active_energy_im"].max()
energy_min_plant_1 = df_plant_1["active_energy_im"].min()
print("Energia activacion minima planta 1: ", energy_min_plant_1,"\nEnergia activacion maxima planta 1: ",energy_max_plant_1)

# Energia de activacion minima y maxima planta 2
energy_max_plant_2 = df_plant_2["active_energy_im"].max()
energy_min_plant_2 = df_plant_2["active_energy_im"].min()
print("Energia activacion minima planta 2: ", energy_min_plant_2,"\nEnergia activacion maxima planta 2: ",energy_max_plant_2)

# Grafico Planta Solar Uno
def graph_1():
    df_plant_1.plot(x="fecha_im", y="active_power_im", rot=30, figsize=(8,7))
    plt.style.use('ggplot')
    plt.xlabel("Date")
    plt.ylabel("Active Power")
    plt.title("Energy Solar Plant 1")
    plt.savefig("Grafico 1.jpg")
    plt.show()
    print("imagen guarda"+os.getcwd())

graph_1()

# Grafico Planta Solar Dos
def graph_2():
    df_plant_2.plot(x="fecha_im", y="active_power_im", rot=30, figsize=(8,7))
    plt.style.use('ggplot')
    plt.xlabel("Date")
    plt.ylabel("Active Power")
    plt.title("Energy Solar Plant 2")
    plt.savefig("Grafico 2.jpg")
    plt.show()
    print("imagen guarda"+os.getcwd())
    
graph_2()

# Archivo de almacenamiento de datos
def archivo():
    a, b, c = all_power_plant_1, all_power_plant_2, all_power_plants
    max_plant_1, min_plant_1 = energy_max_plant_1, energy_min_plant_1
    max_plant_2, min_plant_2 = energy_max_plant_2, energy_min_plant_2
    ubicacion = os.getcwd()
    archivo = open("archivo.txt", "w")
    archivo.write("Suma de active power segun planta solar\n")
    archivo.write("Suma planta solar uno: "+str(a)+"\n")
    archivo.write("Suma planta solar dos: "+str(b)+"\n")
    archivo.write("Suma ambas plantas solares: "+str(c)+"\n")
    archivo.write("Valores maximos y minimo de active energy en las plantas \n")
    archivo.write("planta 1 \nminimo: "+str(min_plant_1) +" maximo: "+str(max_plant_1)+"\n")
    archivo.write("planta 2 \nminimo: "+str(min_plant_2) +" maximo: "+str(max_plant_2)+"\n")
    archivo.write("Archivo guardados en: " + str(ubicacion))
    print("datos almacenados")

archivo()
