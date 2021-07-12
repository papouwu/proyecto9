#Importacion de librerias necesarias para graficar y manipulacion de datos
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np


def mostrarRegiones():#Esta funcion mostrara las regiones a escoger 
    region = 0 #Varible inicial
    print("A continuación se mostrará una lista con las abreviaciones para las regiones y " +
          " luego ingrese la región seleccionada.\n" + #Regiones que puede escoger el usuario

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

    region = int(input("Ingrese el número de la región: "))#El usuario ingresa su region en numero
    
    return region#Aqui la funcion regresa el valor que el usuario ingreso 


def continuar ():#Funcion para saber si el usuario quiere continuar en el programa
    opcion = 999#Variable inicial para entrar al ciclo
    while opcion != 1 or opcion != 9:#Verificamos que el usuario marque esas dos opciones
            opcion = int(input("Para continuar ingrese un 1 \nPara salir ingrese 9: "))#Muestra en pantalla las opciones que puede escoger
            if opcion == 1:#Esta opcion sigue el programa
                return True
            elif opcion == 9:#Esta opcion pone fin al programa
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

#Diccionario necesario para que los numeros ingresado por el usuario se convierta en su respectiva region
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
#Definir variables iniciales
opcion = 0
region = 0
nombreRegion=""
seguirPrograma = False
url = "https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto36/ResidenciasSanitarias.csv"#Dataset que se actualiza todos los dias

#Bienvenida al usuario
print("Bienvenido al programa de estadisitica de ocupacion de Residencias Sanitarias. Para continuar, selecione una opcion:\n\n")

#Entrada al ciclo de consulta al presionar un numero distinto a 9
while opcion != 9: 
    #Opciones que el usuario puede elegir
    print('''
    Opcion 1: Seleccione una región para mostrar los datos respecto a ocupación de Residencias Sanitarias de los últimos 7 días.\n
    Opcion 2: Mostrar la región con mayor cantidad de residencias, mayor cantidad de cupos para esas residencias y mayor cantidad de residentes.\n
    Opcion 3: Mostrar la región con menor cantidad de residencias, menor cantidad de cupos para esas residencias y menor cantidad de residentes.\n
    Opcion 4: Bucar por fecha y región para mostrar residentes vs. cupos.\n
    Opcion 5: Mostrar densidad de ocupación de las residencias para las últimas 7 fechas a nivel nacional.\n
    Opcion 9: Salir.''')
    
    opcion=int(input("Ingrese su opcion: "))
    
    if opcion == 1:
        print("Usted seleccionó la opción 1.")#Muestra en pantalla la opcion elegida por el usuario
        region = mostrarRegiones()#llamamos a la funcion para que nos de el numero de la region que ingreso el usuario
        
        nombreRegion = regiones.get(str(region))#Conversion en cadena de lo que ingreso el usuario en numero para su conversion en la region respecto a ese numero
        print(nombreRegion)#Muestra la region escogida por el usuario
        #Graficos
        archivo = pd.read_csv(url)#Abrimos con pandas el dataset 
        archivo = archivo.iloc[: ,np.r_[0,1,-7,-6,-5,-4,-3,-2,-1]]#Escogemos las columnas que nos sirven("Region","Categoria" y los ultimos 7 dias)
        archivo = archivo[archivo["Region"]==nombreRegion]#Filtramos la region que escoge el usuario
        archivo = archivo.iloc [: , -7:]#Esto elimina todo lo que no sea numerico para asi manejar los datos
        archivo = archivo.iloc[[0,1]]#Nos quedamos con las filas que necesitamos 
        nombres = archivo.columns.tolist()#Hacemos una lista para las ultimas 7 fechas
        cupos = archivo.iloc[0].values.tolist()#Almacenamos los valores de la primera fila de cupos en una lista
        usuarios = archivo.iloc[1].values.tolist()#Almacenamos los valores de la segunda fila de residentes en una lista
        
        fig, ax = plt.subplots()
        ancho = 0.35#Ancho de barras de grafico
        ax.bar(nombres, cupos,     ancho, label="Cupos")# los valores de cupos los ponemos en una seccion de la barra de grafico
        ax.bar(nombres, usuarios,  ancho, label="Usuarios" )# los valores de usuarios los ponemos en una seccion de la barra de grafico
        
        ax.set_ylabel("Usuarios")#Ponemos en el eje "y" los usuarios 
        ax.set_xlabel("Fechas")#Ponemos en el eje "x" las fechas
        ax.set_title("Ocupación de residencias sanitarias en los últimos 7 días para la region " + nombreRegion)#El titulo del grafico mas la region que el usuario escogio
        ax.legend()
        plt.xticks(rotation=45)#Rotamos a 45 grados las fechas para su mejor visualizacion
        plt.show()#Mostramos el grafico
        
        print("** Gráfico ploteado **")#Mensaje para que el usuario sepa que el grafico ya esta listo para que lo vea
        
        seguirPrograma = continuar()
        
        if seguirPrograma == False:
            break
        else:
            print("\n\n")
        
    elif opcion == 2:
        print("Usted seleccionó la opción 2.")#Muestra en pantalla la opcion elegida por el usuario
        
        archivo = pd.read_csv(url)#Abrimos con pandas el dataset
        archivo = archivo.iloc[: ,np.r_[0,1,-1]]#Escogemos las columnas que nos sirven("Region","Categoria" y fecha actual)
        archivo = archivo[archivo["Categoria"]=="residencias"]#Filtramos la categoria residencias
        fecha = archivo.columns.tolist()#Las columnas las pasamos a una lista
        fecha.remove("Region")#Eliminamos el item "Region"
        fecha.remove("Categoria")#Eliminamos el item "Categoria"
        
        sfecha = "".join(fecha)#Ponemos como parametro la fecha
        archivo = archivo[archivo[sfecha]==archivo[sfecha].max()].iloc[0].tolist()
        print("La región con mayor cantidad de residencias es la región de " , archivo[0] , " con " , archivo[2] , "residencias")

        region = archivo[0]  
    
        archivo = pd.read_csv(url)
     
        archivo = archivo.iloc[: ,np.r_[0,1,-1]]
      
        archivo = archivo[archivo["Region"]==region]
      
        
        cupos = archivo.iloc[0].values.tolist()
     
        usuarios = archivo.iloc[1].values.tolist()
     
        
        print("Esta region cuenta con " , cupos[2] , " cupos totales y " , usuarios[2], " usuarios en residencia.")
        
        
        
        seguirPrograma = continuar()#Llamamos a la funcion para ver si el usuario quiere seguir en el programa
        
        if seguirPrograma == False:#Si resulta que no quiere continuar se sale del ciclo
            break
        else:
            print("\n\n")

        
    elif opcion == 3:
        
        print("Usted seleccionó la opción 3.")#Muestra en pantalla la opcion elegida por el usuario

        archivo = pd.read_csv(url)#Abrimos con pandas el dataset 

        archivo = archivo.iloc[: ,np.r_[0,1,-1]]#Escogemos las columnas que nos sirven("Region","Categoria" y fecha actual)
        
        archivo = archivo[archivo["Categoria"]=="residencias"]#Filtramos la categoria residencias
        
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
               

            


    



