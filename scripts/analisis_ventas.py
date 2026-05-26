
import pandas as pd

df = pd.read_csv("datos/sales_sample_2024.csv")

print("Primeras filas del dataset:")
print(df.head())

print("\nVentas totales:")
print(df["sales_amount"].sum())

print("\nPromedio de ventas:")
print(df["sales_amount"].mean())

print("\nVenta máxima:")
print(df["sales_amount"].max())

print("\nVenta mínima:")
print(df["sales_amount"].min())
