
producto_cafe = ["Cafe", 5000, 20]

# 1. Selección con índce
producto = producto_cafe [0]
precio_actual = producto_cafe [1]
unidades_actuales = producto_cafe [2]

# 2. Calcular descuento y precio promocional

descuento_15 = precio_actual * 15 / 100
precio_promocional_15= precio_actual - descuento_15

descuento_20 = precio_actual * 20 / 100
precio_promocional_20 = precio_actual - descuento_20

# 3. Ingreso actual
ingreso_actual = precio_actual * unidades_actuales

# 4. Proyección de unidades (+20%)
aumento_unidades = unidades_actuales * 20 / 100
unidades_proyectadas = unidades_actuales + aumento_unidades

# 5. Ingreso proyectado con promoción
ingreso_proyectado = precio_promocional_15* unidades_proyectadas
diferencia = ingreso_proyectado - ingreso_actual

ingreso_proyectado = precio_promocional_20* unidades_proyectadas
diferencia = ingreso_proyectado - ingreso_actual

#6. Solucion
if diferencia > 0 :
    recomendamos = "Lanzar"
else:
    recomendamos = "No lanzar"
#7.Salidas
    
print("ANÁLISIS DE PROMOCIÓN")
print(f"Producto: {producto}")
print(f"Precio actual: ₡{precio_actual}")
print(f"Unidades actuales: {unidades_actuales}")
print(f"Ingreso actual: ₡{ingreso_actual}")
print("Descuento: 15%")
print(f"Precio en Promocion: ₡{int(precio_promocional_15)}")
print("Descuento: 20%")
print(f"Precio en Promocion: ₡{int(precio_promocional_20)}")
print(f"Unidades proyectadas: {int(unidades_proyectadas)}")
print(f"Ingreso con promoción: ₡{int(ingreso_proyectado)}")
print(f"Diferencia: ₡{int(diferencia)}")
print(f"RECOMENDACIÓN: {recomendamos}.")




    





