import random
#Generar numero Secreto entre 1 y 20
numero_secreto = random.randint(1, 20)

#control de intentos
intentos = 0

#indicaciones y pistas
print("!Juega! Adivina el número (1 al 20)")
print("Pistas: frio, tibio, caliente, hirviendo.")

#proceso del juego. 
while True:
    juego = int(input("Ingrese tu Número "))
    
    #comparar los intentos del juego contra el numero secreto
    comparacion = abs(juego - numero_secreto)
    
    if juego == numero_secreto:
        print(f"¡Felicitaciones! Adivinaste en {intentos} intentos.")
        break
    else:
        # Dirección
        if juego < numero_secreto:
            print("El número secreto es mayor.")
        else:
            print("El número secreto es menor.")

        # Pistas de temperatura
        if comparacion <= 2:
            print("Pista: ¡Hirviendo!.. ¡QUEMA,QUEMA!")
        elif comparacion <= 5:
            print("Pista: caliente.. ¡Eyyy ya casi!")
        elif comparacion <= 10:
            print("Pista: tibio.. ¡Vamos bien! ")
        else:
            print("Pista: frío.. ¡Congelado! ")

