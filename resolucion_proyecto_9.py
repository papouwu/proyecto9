import csv
with open('ResidenciasSanitarias.csv', newline='') as csvbdd:
    lectordatos = csv.reader(csvbdd,  delimiter=' ', quotechar='|' )
    for i in lectordatos:
        print(', '.join(i))

''' inicio 

Bienvenido al programa de estadísticas de ocupación de residencias sanitarias.

Para continuar, seleccione una opción:

Opción 1: Seleccione una región para mostrar los datos respecto a ocupación de Residencias Sanitarias de los últimos 7 días.

Opción 2: Mostrar la región con mayor cantidad de residencias, mayor cantidad de cupos para
esas residencias y mayor cantidad de residentes.

Opción 3: Mostrar la región con menor cantidad de residencias, menor cantidad de cupos para
esas residencias y menor cantidad de residentes.

Opción 4: Bucar por fecha y región para mostrar residentes vs. cupos.

Opción 5: Mostrar densidad de ocupación de las residencias para las últimas 7 fechas a nivel nacional.


Ingrese su opción: _



(1)

Usted seleccionó la opción 1.
A continuación se mostrará una lista con las abreviaciones para las regiones y luego ingrese la región seleccionada.


AP - Arica y Parinacota
TA - Tarapacá
AN - Antofagasta
AT - Atacama
CO - Coquimbo
VA - Valparaíso
RM - Metropolitana
OH - O'Higgins
ML - Maule
NB - Ñuble
BI - Biobío
AR - Araucanía
LR - Los Ríos
LL - Los Lagos
AI - Aysén
MA - Magallanes


Ingrese las iniciales de la región (XX): ___

Para la región XX se registran los siguientes datos:

(Mostrar gráfico con cupos totales y con ocupación de los últimos 7 días)

Como análisis estadístico de los datos obtenidos se observa:

(Análisis)

Mostrar análisis estadísitico (Aumento en % de camas utilizadas)


(2)
Usted seleccionó la opción 2.

La región con con mayor cantidad de residencias es la región (NOMBRE DE REGIÓN) con XXX residencias, XXX cupos para esas residencias y XXXX residentes.


(3)
Usted seleccionó la opción 3.

La región con con menor cantidad de residencias es la región (NOMBRE DE REGIÓN) con XXX residencias, XXX cupos para esas residencias y XXXX residentes.


(4)
Usted seleccionó la opción 4.

A continuación se mostrará una lista con las abreviaciones para las regiones y luego ingrese la región seleccionada.

AP - Arica y Parinacota
TA - Tarapacá
AN - Antofagasta
AT - Atacama
CO - Coquimbo
VA - Valparaíso
RM - Metropolitana
OH - O'Higgins
ML - Maule
NB - Ñuble
BI - Biobío
AR - Araucanía
LR - Los Ríos
LL - Los Lagos
AI - Aysén
MA - Magallanes


Ingrese las iniciales de la región (XX): ___


Ingrese la fecha a buscar en formato DD-MM-AAAA (Sólo dígitos separados por guiones): _________


Para la region de (Nombre de la región) en la fecha (DD-MM-AAAA) se encontraron los siguientes datos:

Residentes: XX
Cupos disponibles: XX

(Mostrar gráfico)


(5)
Usted seleccionó la opción 5.

A continuación se mostrará un gráfico de la densidad de ocupación a nivel nacional de las últimas 7 fechas (% camas utilizadas vs camas totales)'''