"""Plantilla guiada: análisis de ventas de dos tiendas, sin ciclos."""

ventas_centro = [125000, 98000, 147000, 132000, 110000]
ventas_norte = [140000, 135000, 150000, 145000, 155000]
meta_centro = 640000
meta_norte = 700000


# TODO: calcula total, cantidad, mayor y menor para Centro.
total_centro = sum(ventas_centro) #total de ventas semana
cantidad_centro = len(ventas_centro)#cantidad de dias registradas
promerdio_centro = total_centro / cantidad_centro#promedio ventas diarias
menor_centro = min(ventas_centro)# ventas minimas
mayor_centro = max(ventas_centro)#ventas maximas
porcentaje_centro = total_centro * 100 / meta_centro # para porcentajes de meta regla de 3

# TODO: calcula total, cantidad, mayor y menor para norte.
total_norte = sum(ventas_norte) #total de ventas semana
cantidad_norte = len(ventas_norte)#cantidad de dias registradas
promerdio_norte = total_norte / cantidad_norte#promedio ventas diarias
menor_norte = min(ventas_norte)# ventas minimas
mayor_norte = max(ventas_norte)#ventas maximas
porcentaje_norte = total_norte * 100 / meta_norte # para porcentajes de meta

# TODO: calcula promedio, rango, diferencia y porcentaje para Centro.
if total_centro > meta_centro:
    estado_centro = "meta superada"
elif total_centro == meta_centro:
    estado_centro ="meta alcanzada"
else:
    estado_centro = "meta NO Alcanzada"
    
if total_norte > meta_norte:
    estado_norte = "meta superada"
elif total_norte == meta_norte:
    estado_norte ="meta alcanzada"
else:
    estado_norte = "meta NO Alcanzada"

# TODO: repite los indicadores para Norte.
if total_centro > total_norte:
    tienda_mayor_ventas = "Tienda del Centro"
elif total_norte > total_centro:
    tienda_mayor_ventas = "Tienda del norte"
else:
    tienda_mayor_venta = "Ambas tiendas el misto total"
    
print("COMPARACION SEMANAL DE TIENDAS")
print(f"Centro | total: {total_centro:,.2f} | meta{total_norte:,.2f} | cumplimiento {porcentaje_centro:.0f}%")
print("COMPARACION SEMANAL DE TIENDAS")
print(f"norte | total: {total_norte:,.2f} | meta{total_centro:,.2f} | cumplimiento {porcentaje_norte:.0f}%")





# TODO: decide si cada tienda superó, igualó o no alcanzó su meta.

# TODO: compara los totales y los rangos.

# TODO: presenta un reporte con etiquetas claras y f-strings.
# TODO: escribe las tres conclusiones solicitadas en la guía.
