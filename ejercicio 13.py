print("-----programa para determinar el area de un terreno-----")
areaTotal = float(input("\n ingrese el area total del terreno que desea dividir: "))
areaCultivo = areaTotal * 0.40
areaConstruccion = areaTotal * 0.25
areaZonasverdes = areaTotal * 0.15
areaOcupada = areaCultivo + areaConstruccion + areaZonasverdes
areaRestanteTotal = areaTotal - areaOcupada


print(f"\n El area de los cultivos del terreno equivale a: {areaCultivo} metros")
print(f"\n El area de la construccion del terreno equivale a: {areaConstruccion} metros")
print(f"\n El area de las zonas verdes del terreno equivale a: {areaZonasverdes} metros")
print (areaRestanteTotal)