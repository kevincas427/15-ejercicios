primerOperador1 = float(input("ingrese el costo por llamada al primer operador: "))
tiempoOperador1= float(input("ingrese el tiempo que duro en la primer llamada al primer operador: "))


tiempoOperador2 = float(input("ingrese el tempo que duro en la segunda llamada al primer operador:  "))

totalPimerLlamada = primerOperador1 * tiempoOperador1 
totalSegundaLlamada = primerOperador1 * tiempoOperador2
totalOperador1 = totalPimerLlamada + totalSegundaLlamada

print(f"el costo de la primer llamada al operador 1 es: {totalPimerLlamada}")
print(f"el costo de la segunda llamada llamada al operador 1 es: {totalSegundaLlamada}")

print(f"el total del costo de las llamadas al primero operador es: {totalOperador1}")



segundoOperador1 = float(input("ingrese el costo por llamada al segundo operador: "))
tiempoOperador21 = float(input("ingrese el tiempo que duro en la primer llamada al segundo operador: "))


tiempoOperador22 = float(input("ingrese el tiempo que duro en la segunda llamada al segundo operador: "))


totalPrimerLlamada2 = segundoOperador1 * tiempoOperador21
totalSegundaLlamada2 = segundoOperador1 * tiempoOperador22
totalOperador2 = totalPrimerLlamada2 + totalSegundaLlamada2

totalLlamadas = totalOperador1 + totalOperador2



print(f"el costo de la primer llamada al segundo operador es: {totalPrimerLlamada2}")
print(f"el costo de la segunda llamada al segundo operador es: {totalSegundaLlamada2}")

print(f"el total del costo de las llamadas al segundo operador es: {totalOperador2}")



print(f"el total de las llamadas en general es: {totalLlamadas}")

print("gracias por preferir nuestro programa ") 