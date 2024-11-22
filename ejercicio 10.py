print("----Algoritmo para controlar el entrenamiento de un atleta----")
tiempoDia1 = int(input("ingrese el tiempo en entrenados el dia 1: "))
distanciaDia1 = int(input("ingrese la distancia recorrida en metros del dia 1: "))
tiempoDia2 = int(input("ingrese el tiempo en minutos entrenados el dia 2: "))
distanciaDia2 = int(input("ingrese la distancia recorrida en metros del dia 2: "))
tiempoDia3 = int(input("ingrese el tiempo en minutos entrenados el dia 3: "))
distanciaDia3 = int(input("ingrese la distancia recorrida en metros del dia 3: "))

tiempoTotal = tiempoDia1 + tiempoDia2 + tiempoDia3
distanciaTotal = distanciaDia1 + distanciaDia2 + distanciaDia3

promedioTiempo = tiempoTotal // 3
promedioDistancia = distanciaTotal // 3

print(f"el tiempo total de entrenamiento por 3 dias es de: {tiempoTotal} minutos")
print(f"la distancia recorida en los 3 dias de entreanmiento es de: {distanciaTotal} metros")
print(f"su promedio en tiempo es de: {promedioTiempo}")
print(f"su promedio de rrecorrido es: {promedioDistancia}")
