# ejercicios-01.py
# duraciones en horas
dalto = 1.5
minimo = 2.5
promedio = 4.0
maximo = 7.0

# diferencias:
diferencia_dalto_minimo = (1 - (dalto / minimo)) * 100
print(f"Diferencia dalto-minimo: {diferencia_dalto_minimo:.2f}%")
dalto_promedio = (1 - (dalto / promedio)) * 100
print(f"Diferencia dalto-promedio: {dalto_promedio:.2f}%")
dalto_maximo = (1 - (dalto / maximo)) * 100
print(f"Diferencia dalto-maximo: {dalto_maximo:.2f}%")

# Video sin edición:
crudo_otros = 5.0
crudo_dalto = 3.5

porcentaje_otros = (1 - (promedio / crudo_otros)) * 100
print(f"Porcentaje de otros: {porcentaje_otros:.2f}%")
porcentaje_dalto = (1 - (dalto / crudo_dalto)) * 100
print(f"Porcentaje de dalto: {porcentaje_dalto:.2f}%")

# Cantidad de horas equivalentes a 10 horas de curso:
minimo_10h = (minimo * 10) / dalto
promedio_10h = (promedio * 10) / dalto
maximo_10h = (maximo * 10) / dalto

print(f"Minimo 10h: {minimo_10h:.2f}")
print(f"Promedio 10h: {promedio_10h:.2f}")
print(f"Maximo 10h: {maximo_10h:.2f}")  

