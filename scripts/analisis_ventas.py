
import pandas as pd

df = pd.read_csv("datos/sales_sample_2024.csv")

print("Primeras filas del dataset:")
print(df.head())

print("\nVentas totales:")
print(df["sales_amount"].sum())
