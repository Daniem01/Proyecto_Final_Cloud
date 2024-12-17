
#!/usr/bin/python

from pyspark import SparkConf, SparkContext
import sys

# Configuración de Spark
conf = SparkConf().setAppName("AccidentesClimaPorEstado")
sc = SparkContext.getOrCreate(conf)

# Leer el archivo de entrada
lines = sc.textFile(sys.argv[1])

# Filtrar las líneas que no tienen encabezado y que tienen severidad válida (no vacía)
filtered_lines = lines.filter(lambda line: "ID" not in line.split(',')[0] and line.split(',')[2] != '' and line.split(',')[14] != '' and line.split(',')[28] != '')

# Cachear las líneas filtradas para reutilizarlas
filtered_lines = filtered_lines.cache()

# Transformar los datos relevantes ((State, Weather_Condition), (Severity, 1))
# Si la condición del clima o el estado son nulos, asignamos "Otros"
data = filtered_lines.map(lambda line: line.split(',')) \
                     .map(lambda fields: (
                         (fields[14],  # Estado
                          fields[28]),  # Condición climática
                         (int(fields[2]), 1)  # Severidad y conteo
                     ))

# Reducir por clave ((State, Weather_Condition)) para sumar severidad y contar accidentes
aggregated = data.reduceByKey(lambda acc, value: (acc[0] + value[0], acc[1] + value[1]))  # (sum_severity, count)

# Calcular el promedio de severidad por estado y condición climática
averaged = aggregated.mapValues(lambda x: (round(x[0] / x[1], 2), x[1]))  # (avg_severity, count)

# Cachear los promedios para reutilizarlos en varias operaciones
averaged = averaged.cache()

# Ordenar primero por estado y luego por promedio de severidad (de mayor a menor)
sorted_result = averaged.sortBy(lambda x: (x[0][0], -x[1][0]))  # (State, Weather_Condition), (avg_severity, count)

# Guardar el resultado en el archivo de salida
sorted_result.map(lambda x: f"{x[0][0]},{x[0][1]},{x[1][0]:.2f},{x[1][1]}").saveAsTextFile(sys.argv[2])

# Obtener el top 5 de estados con la condición climática que tiene mayor promedio de severidad
top_5 = averaged.takeOrdered(5, key=lambda x: -x[1][0])  # Ordenar por promedio de severidad en orden descendente

# Convertir el top 5 en un RDD y guardarlo en el archivo de salida
sc.parallelize(top_5) \
  .map(lambda x: f"{x[0][0]},{x[0][1]},{x[1][0]},{x[1][1]}") \
  .saveAsTextFile(sys.argv[3])