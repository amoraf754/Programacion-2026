#solución Mision Kit Seguro
#Autor: Andrey Mora a Fecha 2026/10/06

nombre = input("Nombre: ").strip() .upper()
kit = input("Tipo de kit: ").strip() .lower()
autorizacion = input ("Tiene Autorizacion (si/no)?: ").lower() .strip() == "si"

try:
    cantidad = int(input("Ingrese la cantidad: "))
except ValueError:
    print("Erro cantidad invalidad, asignada -1")
    cantidad = -1
    
try:
    dias = int(input("Dias de prestamo: "))
except ValueError:
    print:("cantidad de dias invialidad, asignada -1")
    cantidad = -1

resultado = ""
if not nombre or kit == "" or cantidad <1 or dias < 1 :
     resultado = "Datos Inválidos!!"
elif autorizacion and cantidad = 3 dias <= 7:# not dias >7
    resultado = f"Solicitud aprobada para {nombre}: {cantidad} kit (s) de {kit}"
elif cantidad > 3 or dias > 7:
    resultado = "Solicitud enviada a revisión"
else:
    resultado = "Solicitud rechazada: Se requiere autorizacion"
    
    print(resultado)
    
     
print(resultado)