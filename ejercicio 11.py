print("-----programa que calcula la herencia en una familia-----")
herencia = float(input("ingrese el valor de la herencia: "))
herenciaM = herencia * 0.40
print(f"la herencia de la madre es: {herenciaM}")
herenciaRestante = herencia -herenciaM
print(f"el valor restante de la herencia: {herenciaRestante} ")
herenciaHijo1 = herenciaRestante * 0.30
herenciaHijo2 = herenciaRestante * 0.20
herenciaHijo3 = herenciaRestante * 0.40
herenciaHijo4 = herenciaRestante * 0.10
print(f"la herencia del hijo 1 es: {herenciaHijo1}")
print(f"la herencia del hijo 2 es: {herenciaHijo2}")
print(f"la herencia del hijo 3 es: {herenciaHijo3}")
print(f"la herencia del hijo 4 es: {herenciaHijo4}")
totalHerencias = herenciaHijo1 + herenciaHijo2 + herenciaHijo3 + herenciaHijo4
print(f"la sumatoria de las herencias de los hijos es de: {totalHerencias} ")