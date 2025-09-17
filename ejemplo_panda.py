# Ejemplo de uso de pandas
#python -m venv .venv
#.\.venv\Scripts\activate
#pip install pandas numpy

import pandas as pd
import io

# Simulamos el contenido de un archivo CSV de logs.csv
csv_data = """
timestamp,user_id,status_code
2025-09-17 10:00:00,user1,200
2025-09-17 10:01:00,user2,404
2025-09-17 10:02:00,user3,200
2025-09-17 10:03:00,user4,500
2025-09-17 10:04:00,user5,200
2025-09-17 10:05:00,user6,404
2025-09-17 10:06:00,user7,403
2025-09-17 10:07:00,user8,500
2025-09-17 10:08:00,user9,200
2025-09-17 10:09:00,user10,200
"""
# Leemos los datos CSV en un DataFrame de pandas
# Usamos io.StringIO para leer los datos simulados como si fueran un archivo.
df = pd.read_csv(io.StringIO(csv_data))

print("DataFrame original:")
print(df)

# Convertimos la columna 'timestamp' a tipo datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

print("\nDataFrame con 'timestamp' convertido a datetime:")
print(df)   
