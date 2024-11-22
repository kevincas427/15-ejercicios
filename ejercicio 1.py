


salario = float(input("ingrese el valor del empleado actualmente: "))
retencion = salario * 0.18
retencionTotal = salario - retencion
bonificacion = salario *  0.013
bonificacionTotal = retencionTotal + bonificacion
salarioTotal = bonificacionTotal 
print(f"su retencion del salario es: {retencion}")
print(f"su bonificacion del salario es: {bonificacion}")
print(f"su salario total contando bonificaciones es: {salarioTotal}")

