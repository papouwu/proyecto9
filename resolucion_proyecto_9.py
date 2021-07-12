#Importacion de librerias necesarias para graficar y manipulacion de datos
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np


def mostrarRegiones():
    region = 0 
    print("A continuación se mostrará una lista con las abreviaciones para las regiones y " +
          " luego ingrese la región seleccionada.\n" + 

            "1 - Arica y Parinacota\n"
            "2 - Tarapacá\n"
            "3 - Antofagasta\n"
            "4 - Atacama\n"
            "5 - Coquimbo\n"
            "6 - Valparaíso\n"
            "7 - Metropolitana\n"
            "8 - O’Higgins\n"
            "9 - Maule\n"
            "10 - Ñuble\n"
            "11 - Biobío\n"
            "12 - Araucanía\n"
            "13 - Los Ríos\n"
            "14 - Los Lagos\n"
            "15 - Aysén\n"
            "16 - Magallanes\n")

    region = int(input("Ingrese el número de la región: "))
    
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
    fechaValida = False
    lsFechasArchivo = getFechasArchivo()
    while fechaValida == False:
        fecha = input("Ingrese la fecha a buscar en formato AAAA-MM-DD (Sólo dígitos separados por guiones): ")
        if fecha in lsFechasArchivo:
            fechaValida = True
        else:
            print("Fecha no válida. Intentelo de nuevo. Fechas válidas entre " , lsFechasArchivo[0] , " y " , lsFechasArchivo[len(lsFechasArchivo) - 1])
    return fecha

def getFechasArchivo():
    url = "https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto36/ResidenciasSanitarias.csv"
    lsFechasArchivo = pd.read_csv(url, index_col=0, nrows=0).columns.tolist()
    lsFechasArchivo.remove("Categoria")
    return lsFechasArchivo


def leerArchivo():
    url = "https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto36/ResidenciasSanitarias.csv"
    c = pd.read_csv(url)
    return c
    
#Inicio de programa

regiones={  "1"  :"Arica y Parinacota",
            "2"  :"Tarapacá",
            "3"  :"Antofagasta",
            "4"  :"Atacama",
            "5"  :"Coquimbo",
            "6"  :"Valparaíso",
            "7"  :"Metropolitana",
            "8"  :"O’Higgins",
            "9"  :"Maule",
            "10" :"Ñuble",
            "11" :"Biobío",
            "12" :"Araucanía",
            "13" :"Los Ríos",
            "14" :"Los Lagos",
            "15" : "Aysén",
            "16" :"Magallanes"}

opcion = 0
region = 0
nombreRegion=""
seguirPrograma = False
url = "https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto36/ResidenciasSanitarias.csv"


print("Bienvenido al programa de estadisitica de ocupacion de Residencias Sanitarias. Para continuar, selecione una opcion:\n\n")


while opcion != 9: 
    
    print('''
    Opcion 1: Seleccione una región para mostrar los datos respecto a ocupación de Residencias Sanitarias de los últimos 7 días.\n
    Opcion 2: Mostrar la región con mayor cantidad de residencias, mayor cantidad de cupos para esas residencias y mayor cantidad de residentes.\n
    Opcion 3: Mostrar la región con menor cantidad de residencias, menor cantidad de cupos para esas residencias y menor cantidad de residentes.\n
    Opcion 4: Bucar por fecha y región para mostrar residentes vs. cupos.\n
    Opcion 5: Mostrar densidad de ocupación de las residencias para las últimas 7 fechas a nivel nacional.\n
    Opcion 9: Salir.''')

    opcion=int(input("Ingrese su opcion: "))
    
    if opcion == 1:
        print("Usted seleccionó la opción 1.")
        region = mostrarRegiones()
        
        nombreRegion = regiones.get(str(region))
        print(nombreRegion)
        
        archivo = pd.read_csv(url)
        archivo = archivo.iloc[: ,np.r_[0,1,-7,-6,-5,-4,-3,-2,-1]]
        archivo = archivo[archivo["Region"]==nombreRegion]
        archivo = archivo.iloc [: , -7:]
        archivo = archivo.iloc[[0,1]]
        nombres = archivo.columns.tolist()
        cupos = archivo.iloc[0].values.tolist()
        usuarios = archivo.iloc[1].values.tolist()
        
        fig, ax = plt.subplots()
        ancho = 0.35
        ax.bar(nombres, cupos,     ancho, label="Cupos")
        ax.bar(nombres, usuarios,  ancho, label="Usuarios" )
        
        ax.set_ylabel("Usuarios")
        ax.set_xlabel("Fechas")
        ax.set_title("Ocupación de residencias sanitarias en los últimos 7 días para la region " + nombreRegion)
        ax.legend()
        plt.xticks(rotation=45)
        plt.show()
        
        print("** Gráfico ploteado **")
        
        seguirPrograma = continuar()
        
        if seguirPrograma == False:
            break
        else:
            print("\n\n")
        
    elif opcion == 2:
        print("Usted seleccionó la opción 2.")
        
        archivo = pd.read_csv(url)
        archivo = archivo.iloc[: ,np.r_[0,1,-1]]
        archivo = archivo[archivo["Categoria"]=="residencias"]
        fecha = archivo.columns.tolist()
        fecha.remove("Region")
        fecha.remove("Categoria")
        
        sfecha = "".join(fecha)
        archivo = archivo[archivo[sfecha]==archivo[sfecha].max()].iloc[0].tolist()
        print("La región con mayor cantidad de residencias es la región de " , archivo[0] , " con " , archivo[2] , "residencias")

        region = archivo[0]  
    
        archivo = pd.read_csv(url)
     
        archivo = archivo.iloc[: ,np.r_[0,1,-1]]
      
        archivo = archivo[archivo["Region"]==region]
      
        
        cupos = archivo.iloc[0].values.tolist()
     
        usuarios = archivo.iloc[1].values.tolist()
     
        
        print("Esta region cuenta con " , cupos[2] , " cupos totales y " , usuarios[2], " usuarios en residencia.")
        
        
        
        seguirPrograma = continuar()
        
        if seguirPrograma == False:
            break
        else:
            print("\n\n")

        
    elif opcion == 3:
        
        print("Usted seleccionó la opción 3.")

        archivo = pd.read_csv(url)

        archivo = archivo.iloc[: ,np.r_[0,1,-1]]
        
        archivo = archivo[archivo["Categoria"]=="residencias"]
        
        fecha = archivo.columns.tolist()
        fecha.remove("Region")
        fecha.remove("Categoria")
        
        sfecha = "".join(fecha)
        
        archivo = archivo[archivo[sfecha]==archivo[sfecha].min()].iloc[0].tolist()
        
        print("La región con menor cantidad de residencias es la región de " , archivo[0] , " con " , archivo[2] , "residencias")
        
        region = archivo[0]  
        
        archivo = pd.read_csv(url)
        archivo = archivo.iloc[: ,np.r_[0,1,-1]]
        archivo = archivo[archivo["Region"]==region]
        
        cupos = archivo.iloc[0].values.tolist()
        usuarios = archivo.iloc[1].values.tolist()
        
        print("Esta region cuenta con " , cupos[2] , " cupos totales y " , usuarios[2], " usuarios en residencia.")
              
        seguirPrograma = continuar()
        
        if seguirPrograma == False:
            break
        else:
            print("\n\n")


            
    elif opcion == 4:
        print("Usted seleccionó la opción 4.")
        
        region = mostrarRegiones()
        
        nombreRegion = regiones.get(str(region))
        print(nombreRegion)
        
        fecha = recibirFecha()
        
        archivo = pd.read_csv(url)

        archivo = archivo.filter(items=["Region" , "Categoria" , fecha])

        archivo = archivo[archivo["Region"]==nombreRegion]

        archivo = archivo[archivo["Categoria"]=="cupos totales"]


        cupos = int(archivo[fecha])
        
        archivo = pd.read_csv(url)
        archivo = archivo.filter(items=["Region" , "Categoria" , fecha])
        archivo = archivo[archivo["Region"]==nombreRegion]
        archivo = archivo[archivo["Categoria"]=="usuarios en residencia"]
        residentes = int(archivo[fecha])
       
        print("Para la region de " , nombreRegion , " en la fecha ", fecha , " se encontraron los siguientes datos:")
        print("Residentes: " , residentes)
        print("Cupos disponibles: " , cupos)
        
        seguirPrograma = continuar()
        
        if seguirPrograma == False:
            break
        else:
            print("\n\n")
     
    
    
    elif opcion == 5:
        print("Usted seleccionó la opción 5.")
        
        print("A continuación se mostrará un gráfico de la densidad de ocupación a nivel nacional de las últimas 7 fechas (cupos en residencia utilizados vs cupos totales)")
        
        archivo = pd.read_csv(url)

        archivo = archivo.iloc[: ,np.r_[1,-7,-6,-5,-4,-3,-2,-1]]
        
        archivo = archivo.groupby(["Categoria"]).sum()
        
        archivo = archivo.iloc[[0,2], :]
        
        nombres = archivo.columns.tolist()
        
        cupos = archivo.iloc[0].values.tolist()
        
        usuarios = archivo.iloc[1].values.tolist()
        
        fig, ax = plt.subplots()
        
        ancho = 0.35
        
        ax.bar(nombres, cupos,     ancho, label="Cupos")
        ax.bar(nombres, usuarios,  ancho, label="Usuarios" )
        ax.set_ylabel("Usuarios")
        ax.set_title("Densidad de ocupación de residencias sanitarias a nivel nacional")
        ax.legend()
        plt.xticks(rotation=45)
        plt.show()
        
        print("** Gráfico ploteado **")
        
        seguirPrograma = continuar()
        
        if seguirPrograma == False:
            break
        else:
            print("\n\n")
     elif opcion == 9:
        break

print("\n\n**Fin del programa**")      
               

            


    



