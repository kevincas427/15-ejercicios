def mostrarmenu():
    print("---------------menu de opciones---------------")
    print("seleccioneel operador")
    print("1 - claro")
    print("2 - movistar")
    print("3 - otro")
    print("4 - salir")
    def main():
        while True:
            mostrarmenu() 
            opcion = int(input("elija una opcion: "))
            if opcion == 1: 
                print("el costo de la llamada por minuto de este operador es 100.00")
                llamadasC = int(input("ingrese la cantidad de llamadas que hizo con este operador: "))
                if llamadasC > 1:
                    for i in range(llamadasC):
                        minutosXllamadas = float(input(f"ingrese la cantidad de minutos quehizo en la llamada {i+1}: "))
                        costo = minutosXllamadas * 100
                        print(f"el costo de la llamada al operador claro es = {costo}")