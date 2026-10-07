"""Microreto: el portero del café."""

energia = int(input("Cuanta energia tienes de 0-100?: "))
trae_cafe = input("¿Traes café? (si/no): ").lower().strip()== "si"

mensaje = "Completa las reglas del portero."

if energia < 30 and not(trae_cafe):
    mensaje = "Acceso denegado: necesita dormir o tomar cafe"
elif energia >= 30 or trae_cafe:
    mensaje = "Acceso permitido: pasa, pero comparte cafe"
else:
    mensaje = "El guarda esta confundido, revisa las repuestas"

print(mensaje)
mensaje "Acceso denegado: necesita dormir y cafe"