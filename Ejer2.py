
#           Autor:
#   Armando Augusto Valladares Uc
#   valladaresarmando301@gmail.com  
#   Version 1.01 : 11/05/2025
import numpy as np
import matplotlib.pyplot as plt

# Datos del ejercicio
x = np.array([0, 2, 4, 6, 8])         # Posición (cm)
y = np.array([100, 92, 85, 78, 71])   # Temperatura (°C)

# Cálculo de los coeficientes de regresión lineal
n = len(x)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x2 = np.sum(x**2)

b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
a = (sum_y - b * sum_x) / n

print(f"Coeficientes de la regresión:")
print(f"a (intercepto) = {a:.4f}")
print(f"b (pendiente) = {b:.4f}")

# Predicción usando el modelo
y_pred = a + b * x

# Estimación para x = 5 cm
x_est = 5
y_est = a + b * x_est
print(f"\nTemperatura estimada en x = {x_est} cm: {y_est:.2f} °C")

# Gráfica
plt.figure(figsize=(8,6))
plt.plot(x, y, 'o', label='Datos experimentales')
plt.plot(x, y_pred, '-', color='red', label=f'Ajuste lineal: y = {a:.2f} + {b:.2f}x')
plt.axvline(x_est, linestyle='--', color='gray', label=f'Estimación a x = {x_est} cm')
plt.axhline(y_est, linestyle='--', color='gray')
plt.scatter(x_est, y_est, color='green', zorder=5)
plt.xlabel('Posición (cm)')
plt.ylabel('Temperatura (°C)')
plt.title('Regresión Lineal: Posición vs Temperatura')
plt.legend()
plt.grid(True)
plt.savefig('regresion_temperatura.png', dpi=300)
plt.show()
