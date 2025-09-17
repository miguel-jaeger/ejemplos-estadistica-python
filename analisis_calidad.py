# crear virtual enviroment
# python -m venv .venv

# activar virtual env
#.venv\Scripts\activate

# instalar librerias
# pip install pandas numpy matplotlib seaborn

# para ejecutar el código
# python analisis_calidad.py


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

# Simulación de datos
data = {
    'tiempo_respuesta': np.concatenate([
        np.random.normal(loc=200, scale=30, size=50),
        np.repeat(500, 5),
        np.random.normal(loc=150, scale=10, size=45)
    ]),
    'codigo_error': ['200 OK'] * 75 + ['404 Not Found'] * 15 + ['500 Internal Server Error'] * 10
}
df = pd.DataFrame(data)

print("Datos simulados (primeras 5 filas):")
print(df.head())
print("\nAnálisis estadístico descriptivo del tiempo de respuesta:")
print(df['tiempo_respuesta'].describe())
print("\nFrecuencia de códigos de error:")
print(df['codigo_error'].value_counts())

# Histograma
plt.figure(figsize=(10, 6))
sns.histplot(df['tiempo_respuesta'], kde=True, bins=15)
plt.title('Distribución de los Tiempos de Respuesta', fontsize=16)
plt.xlabel('Tiempo de Respuesta (ms)', fontsize=12)
plt.ylabel('Frecuencia', fontsize=12)
plt.show()

# Gráfico de barras
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='codigo_error', order=df['codigo_error'].value_counts().index)
plt.title('Frecuencia de Códigos de Error', fontsize=16)
plt.xlabel('Código de Error', fontsize=12)
plt.ylabel('Cantidad', fontsize=12)
plt.xticks(rotation=45)
plt.show()
