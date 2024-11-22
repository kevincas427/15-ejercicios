"""El sistema de liquidación que hacen los conductores de buses y los colectivos a las 
diferentes empresas consiste en tomar un número de la registradora al iniciar el día y otro 
al terminarlo . La diferencia de estos dos números determina el numero de pasajeros 
transportados en el día. Realizar un algoritmo que permita leer estos dos números y el 
valor del pasaje. Calcular e imprimir el total de pasajeros, el valor liquidado al conductor y 
el total liquidado a la empresa. Tenga en cuenta que la empresa recibe tres cuartas partes 
del dinero mientras el conductor recibe el resto."""

#datos de inicio
inicial = int(input("ingrese el numero de pasajeros iniciales: "))
final = int(input("ingrese el numero final de pasajeros: "))
valorPasaje = float(input("ingrese el valor del pasaje actual en pesos colombianos: "))

#pasajeros transportados
pasaTra = final-inicial

#liquidacion
valorLiquidacion = valorPasaje * pasaTra
liquidacionEmpresa = valorLiquidacion * 0.75
liquidacionConductor = valorLiquidacion *0.25

#imprimir valores(Resultado final)
print(f"el total de pasajeros transportados es: {pasaTra}")
print(f"\nEl valor de la liquidacion del conducor es: {liquidacionConductor} pesos colombianos")
print(f"\nEl valor de la liquidacion de la empresa es: {liquidacionEmpresa} pesos colombianos")