
#           Autor:
#   Armando August Valladares
#   valladaresarmando301@gmail.com  
#   Version 1.01 : 11/05/2025
#
import numpy as np
import matplotlib.pyplot as plt

# Datos de presión (kPa) y caudal (L/min)
x = np.array([50, 70, 90, 110, 130])
y = np.array([15, 21, 27, 33, 39])

# Cálculo de coeficientes
n = len(x)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x2 = np.sum(x**2)

# Fórmulas de regresión lineal
b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
a = (sum_y - b * sum_x) / n

print(f"Coeficientes de la regresión:")
print(f"a (intercepto) = {a:.4f}")
print(f"b (pendiente) = {b:.4f}")

# Predicción para x = 100 kPa
x_pred = 100
y_pred = a + b * x_pred
print(f"\nPredicción del caudal para 100 kPa: {y_pred:.2f} L/min")

# Generar valores para la recta
y_fit = a + b * x

# Gráfica
plt.figure(figsize=(8,6))
plt.plot(x, y, 'o', label='Datos experimentales')
plt.plot(x, y_fit, '-', label=f'Ajuste lineal: y = {a:.2f} + {b:.2f}x', color='red')
plt.axvline(x=100, color='gray', linestyle='--', label='Presión = 100 kPa')
plt.axhline(y=y_pred, color='gray', linestyle='--', label=f'Caudal ≈ {y_pred:.2f} L/min')
plt.xlabel('Presión (kPa)')
plt.ylabel('Caudal (L/min)')
plt.title('Regresión Lineal: Caudal vs Presión')
plt.legend()
plt.grid(True)
plt.savefig('caudal_vs_presion.png', dpi=300)
plt.show()
