valorInicial = float(input("ingrese el valor incial del desempleo: "))
primerTrimestre = valorInicial * 0.095
primerTrimestreF = valorInicial + primerTrimestre
segundoTrimestre = primerTrimestreF * 0.015 
segundoTrimestreF = primerTrimestreF - segundoTrimestre
print(f"la tasa de desemplro en ibague es: {segundoTrimestreF}")