#Tarea 7 Métricas de calidad
#Karla Calderon

#Objetivo General
# Crear resultados estadisticos para análizar las métricas de calidad del presente archivo

#Fuente de Información
#https://www.kaggle.com/datasets/sayedmohsin/sqa-dataset

#Descripción de las variables a medir alineadas con las categorías, subcategorías y métricas según ISO 25000


#Importamos las librerias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargamos el archivo CSV con los datos
file_path = "C:/Users/karla/Downloads/archive/dataset/resulted/class_level_quality_code_smell_mdi.csv"
df = pd.read_csv(file_path)

# 1. Gráfico de Barras para 'Complexity'
plt.figure(figsize=(10, 6))
sns.countplot(x='Complexity', data=df)
plt.title('Distribución de la Complejidad')
plt.show()

# 2. Boxplot para 'Coupling'
plt.figure(figsize=(10, 6))
sns.boxplot(x='Coupling', data=df)
plt.title('Boxplot para el Acoplamiento')
plt.show()

# 3. Histograma para 'Size'
plt.figure(figsize=(10, 6))
sns.histplot(df['Size'], bins=20, kde=True)
plt.title('Histograma para el Tamaño')
plt.show()

# 4. Diagrama de dispersión para 'CBO' vs 'RFC'
plt.figure(figsize=(10, 6))
sns.scatterplot(x='CBO', y='RFC', data=df)
plt.title('Diagrama de Dispersión entre CBO y RFC')
plt.show()

# 5. Gráfico de pastel para 'GodClass'
godclass_counts = df['GodClass'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(godclass_counts, labels=godclass_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Proporción de God Classes')
plt.show()

# 6. Gráfico de Barras para 'Size'
plt.figure(figsize=(12, 6))
sns.countplot(x='Size', data=df)
plt.title('Distribución del Tamaño')
plt.show()

# 7. Comparación de diferentes archivos (Filenames)
plt.figure(figsize=(12, 6))
sns.boxplot(x='filename', y='Complexity', data=df)
plt.xticks(rotation=90)
plt.title('Comparación de Complejidad entre Archivos')
plt.show()


#Conclusiones y Recomendaciones
#La distribución de la complejidad en el código muestra que la mayoría de las clases tienen una complejidad baja, pero hay algunas clases con complejidad significativamente más alta.
#El boxplot del acoplamiento revela que existen algunas clases con niveles de acoplamiento más altos que la mayoría. Esto podría indicar áreas de mejora en términos de desacoplamiento.
#El diagrama de dispersión entre CBO y RFC muestra si hay una relación entre la complejidad y la cantidad de métodos llamados. Puede ser útil para identificar clases con posibles problemas de diseño.
