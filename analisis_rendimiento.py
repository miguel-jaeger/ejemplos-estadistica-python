import numpy as np

# Datos de ejemplo: Tiempos de respuesta de un servidor
tiempos_respuesta = np.array([250, 265, 240, 275, 255, 280, 290, 250, 310])

print("Array de tiempos de respuesta:")
print(tiempos_respuesta)

# Calcular la desviación estándar de los tiempos de respuesta
desviacion_estandar = np.std(tiempos_respuesta)

print("\nDesviación estándar de los tiempos de respuesta:")
print(f"{desviacion_estandar:.2f} ms")