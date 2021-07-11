import csv
import matplotlib.pyplot as plt      #intilar con: pip install matplotlib 

import pandas as pd
import numpy as np



def mostrarRegiones():
    region = 0

    print("A continuacion se mostrara una lista con las abreviaciones para las regiones y "+
            "luego ingrese la region seleccionada\n"+
            
            
            
            "1 - Arica y Parinacota\n"
            "2 - Tarapacá\n"
            "3 - Antofagasta\n"
            "4 - Atacama\n"
            "5 - Coquimbo\n"
            "6 - Valparaíso\n"
            "7 - Metropolitana\n"
            "8 - O'Higgins\n"
            "9 - Maule\n"
            "10 - Ñuble\n"
            "11 - Biobío\n"
            "12 - Araucanía\n"
            "13 - Los Ríos\n"
            "14 - Los Lagos\n"
            "15 - Aysén\n"
            "16 - Magallanes\n")


    region = int(input("Ingrese el numero de la region: "))

    return region            




def continuar ():
    opcion = 999
    while opcion != 1 or opcion != 9:
            opcion = int(input("Para continuar ingrese un 1 \nPara salir ingrese 9: "))
            if opcion == 1:
                return True
            elif opcion == 9:
                return False




def recibirFecha():
    fecha = ""
    fecha = input("Ingrese la fecha a buscar en forma DD-MM-AAAA(solo digitos separados por guiones):")
    return fecha




def leerArchivo():
    c = pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto36/ResidenciasSanitarias.csv")
    print(c)


regiones ={ "1"  :"Arica y Parinacota",
            "2"  :"Tarapacá",
            "3"  :"Antofagasta",
            "4"  :"Atacama",
            "5"  :"Coquimbo",
            "6"  :"Valparaíso",
            "7"  :"Metropolitana",
            "8"  :"O'Higgins",
            "9"  :"Maule",
            "10" :"Ñuble",
            "11" :"Biobío",
            "12" :"Araucanía",
            "13" :"Los Ríos",
            "14" :"Los Lagos",
            "15" : "Aysén",
            "16" :"Magallanes"}










'''regiones=['1 - Arica y Parinacota', '2 - Tarapacá','3 - Antofagasta','4 - Atacama','5 - Coquimbo','6 - Valparaíso','7 - Metropolitana','8 - OHiggins','9 - Maule',
'10 - Ñuble','11 - Biobío','12 - Araucanía','13 - Los Ríos','14 - Los Lagos','15 - Aysén','16 - Magallanes']
                        
with open('ResidenciasSanitarias.csv', newline='') as csvbdd:
    lectordatos = csv.reader(csvbdd,  delimiter=' ', quotechar='|' )
    for i in lectordatos:'''
    

while True: 
    print("bienvenido al programa de estadisitica de ocupacion de Residencias Sanitarias. Para continuar, selecione una opcion:")
    print('''
    opcion 1: Seleccione una región para mostrar los datos respecto a ocupación de Residencias Sanitarias de los últimos 7 días.
    opcion 2: Mostrar la región con mayor cantidad de residencias, mayor cantidad de cupos para esas residencias y mayor cantidad de residentes.
    opcion 3: Mostrar la región con menor cantidad de residencias, menor cantidad de cupos para esas residencias y menor cantidad de residentes.
    opcion 4: Bucar por fecha y región para mostrar residentes vs. cupos.
    opcion 5: Mostrar densidad de ocupación de las residencias para las últimas 7 fechas a nivel nacional.''')
    
    opcion=int(input("ingrese su opcion:"))
    if opcion == 1:
        regiones=[]
        sigla=input("ingrese el numero de la region deseada:")
    
    '''elif opcion == 2:

    elif opcion == 3:

    elif opcion == 4:

    elif opcion == 5:'''
