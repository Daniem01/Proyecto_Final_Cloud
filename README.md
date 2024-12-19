# Proyecto_Final_Cloud

Realizado por Álvaro Domínguez Sánchez y Daniel Martín del Castillo
 
En este repositorio esta:

    -MEMORIA BIG DATA: Memoria del proyecto.
    -prueba_normal y prueba_top: 2 outputs distintos de nuestra practica.
    -accidentes.py: Codigo que hemos creado.

Por separado se ha entregado el .csv con los datos que hemos analizado
debido a que por su tamaño no entra en el repositorio.

# MEMORIA DEL PROYECTO: ACCIDENTES EN ESTADOS UNIDOS


<img width="650" alt="image" src="https://github.com/user-attachments/assets/5a64a28b-1d11-48a7-a1cb-e93822c2cf2c" />

# Descripción del problema

Los accidentes de tráfico son una de las principales causas de mortalidad y lesiones graves en todo el mundo, especialmente en países como Estados Unidos, donde la red de carreteras y autopistas es extensa y variada. Comprender los factores asociados con los accidentes, como la severidad de los mismos y las condiciones climáticas en las que ocurren, es esencial para mejorar la seguridad vial, optimizar los recursos de emergencia y diseñar políticas preventivas más efectivas.

El análisis de los accidentes de tráfico en Estados Unidos desde 2016 hasta marzo de 2023 tiene como objetivo identificar patrones relevantes entre la severidad de los accidentes, las condiciones climáticas y las ubicaciones geográficas (por estado). Con este análisis se busca responder preguntas clave como:

- ¿Qué estados presentan mayores promedios de severidad en condiciones climáticas específicas?
- ¿Qué factores climáticos están más correlacionados con accidentes graves?
- ¿Cómo varía el comportamiento del tráfico en función de la ubicación y el clima?

Estos datos pueden proporcionar información valiosa para agencias gubernamentales, compañías de seguros, investigadores de seguridad vial y ciudadanos interesados en mejorar la seguridad vial. Para abordar esta problemática, se utilizará un enfoque de Big Data que permita procesar y analizar un volumen significativo de datos históricos de accidentes de tráfico de forma eficiente y escalable.

La solución desarrollada se centra en aprovechar Apache Spark, una plataforma de procesamiento distribuido, para realizar tareas de filtrado, agregación y análisis avanzado. Este sistema permite extraer estadísticas clave que ayudan a caracterizar el impacto de las condiciones climáticas en la severidad de los accidentes por estado, con un énfasis en identificar áreas de alto riesgo y tendencias peligrosas a lo largo de los años analizados.
# Necesidad de Big Data y la Nube

## Big Data
- El conjunto de datos ocupa aproximadamente 3 GB de almacenamiento, lo que representa un volumen de datos muy grande, además de una complejidad muy alta para utilizar un sistema tradicional de análisis, sobre todo por la dificultad de la lectura y análisis de los datos.  
- Los datos requieren técnicas avanzadas de procesamiento y almacenamiento.

## Cloud
- La infraestructura de la nube permite la escalabilidad necesaria para analizar estos datos de manera eficiente.  
- En nuestro caso, contamos con herramientas instaladas en Google Cloud (como Apache Spark) que permiten realizar tareas y cálculos en paralelo, reduciendo significativamente el tiempo necesario para procesar los datos.
# Descripción de los datos

El conjunto de datos incluye información detallada sobre accidentes de tráfico ocurridos en Estados Unidos desde 2016 hasta marzo de 2023. Los atributos más relevantes para el análisis son:

- **Severidad del accidente**: Representada por una escala numérica (1 a 4), donde los valores más altos indican mayor gravedad.  
- **Ubicación geográfica**: Información precisa del lugar del accidente, como estado, ciudad y coordenadas geográficas (latitud y longitud). Esto permite estudiar patrones espaciales.  
- **Condiciones climáticas**: Variables como temperatura, visibilidad, precipitación, velocidad del viento y una descripción de las condiciones generales (e.g., lluvia ligera, despejado) en el momento del accidente.  
- **Factores temporales**: Fechas y horas de inicio y fin del accidente, lo que ayuda a identificar tendencias según franjas horarias o estaciones del año.  
- **Factores de infraestructura vial**: Indicadores sobre la presencia de semáforos, cruces, rotondas y otras características de la carretera que podrían influir en la ocurrencia de los accidentes.  

Este conjunto de datos se proporciona en formato **CSV** (Comma-Separated Values), lo que facilita su procesamiento y análisis. El tamaño del conjunto de datos es de **2.9 GB**. 

Ha sido obtenido de **Kaggle**, una plataforma en línea que ofrece conjuntos de datos públicos para análisis y competencias de ciencia de datos. Lo hemos elegido debido a su amplitud y relevancia, ya que permite analizar patrones en accidentes de tráfico en función de variables como la severidad, las condiciones climáticas y la ubicación, lo cual es crucial para mejorar la seguridad vial.
# Descripción de la aplicación, modelos de programación, plataforma e infraestructura

## Aplicación
La aplicación es un sistema de análisis de Big Data diseñado para analizar una base de datos de accidentes en Estados Unidos.

### Objetivo principal
Relacionar las condiciones climatológicas con la gravedad de los accidentes.

### Funcionalidades principales
- Relacionar condiciones climatológicas y severidad de accidentes.  
- Clasificar accidentes por estado.  
- Calcular el promedio de severidad de los accidentes por estado.  
- Obtener el top 5 de combinaciones de estado y clima con los promedios de severidad más altos.  

## Modelo de programación
La aplicación utiliza el modelo de programación basado en **Resilient Distributed Datasets (RDDs)**.

### Operaciones principales

#### Transformaciones
- **filter**: Filtra datos relevantes.  
- **map**: Transforma líneas de texto en pares clave-valor.  
- **reduceByKey**: Agrega datos por clave, sumando valores asociados.  
- **sortBy**: Ordena los resultados.  

#### Acciones
- **takeOrdered**: Obtiene los registros con mayor severidad promedio.  
- **saveAsTextFile**: Escribe los resultados en el sistema de archivos.  

### Ventajas de RDDs en esta aplicación
- Distribución automática de datos entre nodos del clúster, acelerando el procesamiento.  
- Tolerancia a fallos de Spark, garantizando la confiabilidad del análisis.  

## Plataforma
La aplicación está diseñada para ejecutarse en **Apache Spark**, aprovechando sus características clave:
- **Compatibilidad con múltiples lenguajes**: Usamos Python con PySpark.  
- **Distribución automática de datos y tareas**: Spark distribuye de forma eficiente entre los nodos del clúster, mejorando rapidez y eficiencia.  

## Infraestructura

### Hardware
- Clúster de Dataproc de Google Cloud con múltiples nodos:
  - **Master Node**: Coordina el clúster.  
  - **Worker Nodes**: Ejecutan las diferentes tareas.  

### Software
- **Apache Spark**: Instalado en el clúster.  
- **Python (PySpark)**: Lenguaje principal de implementación.  

### Almacenamiento
- **Bucket de Google Cloud**:  
  - Entrada: Archivo `.csv` con los datos.  
  - Salida: Resultados del análisis.
# Diseño del software

El uso de este análisis de accidentes de tráfico se centra en identificar patrones entre la severidad de los accidentes, las condiciones climáticas y la ubicación geográfica. A continuación se describen los pasos clave del proceso, desde la carga del dataset hasta la obtención de los resultados:

## Pasos clave

### 1. Carga de Datos
- Se carga el archivo **CSV** que contiene los datos de los accidentes.  
- Este archivo es procesado por **Apache Spark**, lo que permite manejar grandes volúmenes de datos de forma eficiente.

 ![Captura de pantalla 2024-12-07 204005](https://github.com/user-attachments/assets/cc48a9f9-3171-4dff-8914-78edbcf14198)


### 2. Filtrado de Datos
- Se eliminan las líneas que contienen información incompleta o no válida (e.g., registros con valores nulos o encabezados de columnas).
  
![Captura de pantalla 2024-12-07 204630](https://github.com/user-attachments/assets/2bbcd546-ac6d-402a-bbf7-d5a20b70787f)

### 3. Transformación de Datos
- Se extraen los datos relevantes, como el estado, las condiciones climáticas y la severidad.  
- Los datos se transforman en pares clave-valor para facilitar su agregación.

![Captura de pantalla 2024-12-07 204736](https://github.com/user-attachments/assets/07f3496d-5033-4aff-9018-6eb99e32a476)

### 4. Agregación de Datos
- Los datos se agrupan por estado y condición climática.  
- Se suman los valores de severidad y el conteo de accidentes para cada grupo.

![Captura de pantalla 2024-12-07 204937](https://github.com/user-attachments/assets/5fbd44dd-24a1-4e69-8a54-e0334c13fc5b)

### 5. Cálculo del Promedio de Severidad
- Se calcula el promedio de severidad por estado y condición climática dividiendo la suma de severidad por el número de accidentes registrados.

![Captura de pantalla 2024-12-07 205150](https://github.com/user-attachments/assets/36e84040-21d9-4bc2-ae93-f850a140d8cf)

### 6. Ordenación de Resultados
- Los resultados se ordenan primero por estado y luego por el promedio de severidad (de mayor a menor).

![Captura de pantalla 2024-12-07 205317](https://github.com/user-attachments/assets/07cb53ab-6e54-4832-af4a-2e10babc3df9)

### 7. Visualización de Resultados
- Los resultados se guardan en archivos de salida.

![Captura de pantalla 2024-12-07 205500](https://github.com/user-attachments/assets/7c805958-d9b3-426f-94b1-c9ba86a67e97)

### 8. Obtención del Top 5
- Se obtiene el **Top 5** de los estados con la mayor severidad promedio para condiciones climáticas específicas.

![Captura de pantalla 2024-12-07 205645](https://github.com/user-attachments/assets/865e5536-6ad5-4e09-9cbe-cf1e1092628d)

### 9. Visualización de Resultados del Top 5
- Los resultados del Top 5 se guardan en un archivo de salida adicional.  
- El archivo contiene:  
  - **Estado**  
  - **Condición climática**  
  - **Promedio de severidad**  
  - **Número de accidentes**
  
![Captura de pantalla 2024-12-07 205835](https://github.com/user-attachments/assets/6bde11da-41ef-415d-abaa-94dd1d848094)

# USO

Para realizar todas las pruebas y generar los outputs (resultados), hemos llevado a cabo los siguientes pasos, basándonos en el laboratorio 4 de Spark:

## Configuración del clúster:
Una vez creado el fichero anterior, procedimos a configurar un clúster mediante el siguiente comando:

```bash
gcloud dataproc clusters create mycluster --region=europe-southwest1 \
--master-machine-type=e2-standard-4 --master-boot-disk-size=50 \
--worker-machine-type=e2-standard-4 --worker-boot-disk-size=50 \
--enable-component-gateway 
```
## Carga de archivos al bucket:
A continuación, añadimos los archivos `.py` en el bucket que se creó durante los primeros laboratorios, así como el dataset de accidentes de tráfico.

## Generación de outputs:
Con el bucket y el clúster completamente configurados, ejecutamos el siguiente comando para generar los dos outputs:

```bash
BUCKET=gs://central-mission-436716-i4 
gcloud dataproc jobs submit pyspark --cluster mycluster --region=europe-southwest1 $BUCKET/codigo.py -- $BUCKET/US_Accidents_March23.csv $BUCKET/prueba_normal $BUCKET/prueba_top
```
Siendo `codigo.py` el código en Python, `US_Accidents_March23.csv` el dataset, y `prueba_normal` y `prueba_top` los outputs.
## Verificación de los outputs:
Finalmente, comprobamos el contenido de los outputs generados utilizando este comando:

```bash
gcloud storage ls $BUCKET/output
gcloud storage cat $BUCKET/output/* | more
```
En este caso, deberíamos cambiar `output` por `prueba_normal` y `prueba_top`.

Este apartado nos daría los siguientes resultados:

- **prueba_normal**:

 ![Captura de pantalla 2024-12-18 210309](https://github.com/user-attachments/assets/1dd71d86-d58d-4f5a-ac8a-50f59b32e49c)

- **prueba_top**:

![Captura de pantalla 2024-12-18 210420](https://github.com/user-attachments/assets/1b62e07f-7a2e-4dfc-89b0-39fb499a76b4)

Para acceder a los resultados completos, los outputs se encuentran en el proyecto `GROUP2`, el cual está asociado al correo electrónico: `alvarodschez@gmail.com`.

# Evaluación de rendimiento

## Cálculo del Speed Up

Para evaluar el rendimiento del sistema, se realizaron pruebas utilizando 2 nodos y 4 nodos. En cada caso, se midieron los tiempos de ejecución correspondientes, los cuales se presentan en las capturas adjuntas. A partir de estos tiempos, se calculó el Speed Up utilizando la fórmula:

```
Speed up = TIMEsequential / TIMEparallel
```

donde:
- **TIMEsequential** es el tiempo de ejecución en un nodo (o secuencial).
- **TIMEparallel** es el tiempo de ejecución utilizando nodos.

Este análisis permite ver el incremento en la eficiencia al aumentar el número de nodos empleados.

El tiempo secuencial (tiempo de ejecución en un nodo) es el siguiente:

![Captura de pantalla 2024-12-18 201037](https://github.com/user-attachments/assets/1d95e918-b95c-450d-9f60-779ccce1f804)

A partir de este tiempo hemos podido calcular el Speed up con 2 nodos y 4 nodos:

## Resultados con 2 Nodos

En el caso de 2 nodos, los tiempos de ejecución se compararon con el tiempo secuencial para calcular el Speed Up. La captura adjunta muestra el tiempo obtenido, y el cálculo se realizó utilizando la fórmula mencionada anteriormente:

![Captura de pantalla 2024-12-18 201900](https://github.com/user-attachments/assets/1a929626-298f-48c4-94c8-7e2f4a79036f)

A partir de este tiempo hemos obtenido el siguiente Speed up:

```
Speed up = 121.19 / 67.52 = 1.795
```

## Resultados con 4 Nodos

Al emplear 4 nodos, se repitió el mismo procedimiento para medir los tiempos de ejecución y calcular el Speed Up. En la siguiente captura se puede observar la mejora en el rendimiento al incrementar la cantidad de nodos, evidenciando una mayor eficiencia del sistema:

![Captura de pantalla 2024-12-18 202422](https://github.com/user-attachments/assets/7f76ccaf-33ab-4595-b865-a416a2625b37)

A partir de este tiempo hemos obtenido el siguiente Speed up:

```
Speed up = 121.19 / 59.63 = 2.032
```

## Optimización del Código

Un aspecto relevante de la implementación es que se utilizó el mismo código para realizar dos funcionalidades distintas. Esta reutilización permitió optimizar el desarrollo y reducir el tiempo total de ejecución. Si las funcionalidades se hubieran desarrollado por separado, el tiempo necesario habría sido considerablemente mayor, tanto en términos de ejecución como de mantenimiento del código.

## ¿De qué manera se han obtenido los tiempos para el cálculo?

En base al código especificado anteriormente hemos realizado los siguientes cambios:

1. **Importar `time`:**

```python
from time import time
```

2. **Guardar el tiempo inicial en una variable `start_time`:**

```python
start_time = time()
```

3. **Al final del código, hacer un `print` del tiempo final menos el tiempo inicial que ha sido guardado en la variable `start_time`:**

```python
print(f"Tiempo total de ejecución: {time() - start_time:.2f} segundos")
```
# Características avanzadas

## Novedades de la aplicación

En comparación con ejercicios anteriores, lo novedoso de esta aplicación es la implementación del cálculo del **Top 5 de estados con mayor severidad de accidentes bajo condiciones climáticas específicas**. Además, se optimizó el flujo de procesamiento para generar dos outputs distintos utilizando un único código, lo que simplifica y mejora la eficiencia del proceso.

En resumen, la aplicación aprovecha:

- La capacidad de procesamiento distribuido de **Apache Spark**.
- La infraestructura escalable de **Google Cloud**.
- Las buenas prácticas del laboratorio de Spark.

Todo esto permite ejecutar el análisis de accidentes de tráfico de manera eficiente y obtener resultados útiles para la mejora de la seguridad vial.

# Conclusiones

En definitiva, el análisis de los accidentes de tráfico en Estados Unidos entre 2016 y 2023 ha permitido identificar patrones significativos entre la severidad de los accidentes y las condiciones climáticas, como la lluvia ligera y la niebla, que están asociadas a una mayor gravedad. 

El uso de **Big Data** y **Apache Spark** ha sido clave para procesar grandes volúmenes de datos de manera eficiente, lo que facilita la identificación de áreas y condiciones de alto riesgo. 

Estos resultados son fundamentales para enfocar los esfuerzos preventivos y mejorar la seguridad vial en las zonas más vulnerables.

# Referencias

## Kaggle (Para la obtención del dataset):

Kaggle es una plataforma en línea que ofrece un espacio para la compartición de conjuntos de datos, competiciones de ciencia de datos y recursos educativos. Es ampliamente utilizada por la comunidad de científicos de datos para acceder a datos públicos, aprender y participar en desafíos relacionados con el análisis de datos. 

En este trabajo, se utilizó un conjunto de datos de Kaggle sobre accidentes de tráfico en Estados Unidos entre 2016 y 2023.

[https://www.kaggle.com](https://www.kaggle.com)

## Apuntes del Classroom de la Asignatura (Para la implementación del código):

Los apuntes proporcionados en la asignatura sobre Batch Processing con **Apache Spark** fueron esenciales para la implementación de este análisis. En particular, el tema de Spark explica cómo procesar grandes volúmenes de datos de manera distribuida, utilizando RDDs y operaciones como `map`, `filter`, `reduceByKey`, y `sortBy`. 

Estos conceptos fueron aplicados en el procesamiento de los datos de accidentes de tráfico, lo que nos ha permitido obtener resultados de manera eficiente y en tiempos reducidos.











