'''
En clase de programación, se sacan 4 notas del 15%,30%,30%,25% respectivamente. Se 
pide diseñar un algoritmo que permita mostrar la nota definitiva de un estudiante. 
Teniendo en cuenta que la primera nota consta del promedio de dos talleres, la segunda 
de tres evaluaciones, la tercera nota de un trabajo final y la última es el promedio de 4 
quizzes. 
'''
#nota talleres
nT1=float(input	("ingrese la nota del primer taller: "))
nT2=float(input	("ingrese la nota del segundo  taller: "))
pNT=(nT1+nT2)/2
promedio1 = pNT*0.15

#nota evaluaciones
nE1=float(input("ingrese la nota de la primera evaluacion: "))
nE2=float(input("ingrese la nota de la segunda evaluacion: "))
nE3=float(input("ingrese la nota de la tercer evaluacion: "))
pNE=(nE1+nE2+nE3)/3
promedio2= pNE*0.30

#trabajo final
bTF= float(input("ingrese la nota del taller final: "))
promedio3 = bTF*0.30

#nota quizzes
nQ1= float(input("ingrese la nota del primer Quiz: "))
nQ2= float(input("ingrese la nota del segundo Quiz: "))
nQ3= float(input("ingrese la nota del tercer Quiz: "))
nQ4= float(input("ingrese la nota del cuarto Quiz: "))
promedio4 = (nQ1+nQ2+nQ3+nQ4)/4

print(f"\nlas notas adquiridas son basadas en porcentajes las cuales son: ")
print(f"{promedio1}%")
print(f"{promedio2}%")
print(f"{promedio3}%")
print(f"{promedio4}%")
print(f"la sumatoria de estas es: {promedio1+promedio2+promedio3+promedio4}")