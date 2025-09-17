# Crear un DataFrame con un valor faltante para el ejemplo.
import pandas as pd


df_con_na = pd.DataFrame({
    'timestamp': ['2025-09-17 10:00:00', '2025-09-17 10:01:00', '2025-09-17 10:02:00'],
    'user_id': ['user1', 'user2', 'user3'],
    'status_code': [200, 404, pd.NA] # pd.NA representa un valor faltante.
})

print("\nDataFrame con valores faltantes:")
print(df_con_na)

# Eliminar filas con cualquier valor faltante.
df_limpio = df_con_na.dropna()

print("\nDataFrame después de eliminar valores faltantes:")
print(df_limpio)
