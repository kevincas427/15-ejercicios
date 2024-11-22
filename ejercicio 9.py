alto= float(input("igrese el alto de la pared a la que se le quiere renovar las baldosas: "))
ancho= float(input("ingrese el ancho de la pared a la que se le quiere renovar las baldosas: "))

areaPared= alto*ancho
cantBaldosa=areaPared/3.5
print(f"\nLas cajas de baldosas son de 3.5 metros la cantidad de baldosas que debe usar es: {cantBaldosa}")
print(f"\nteniendo en cuenta que su pared tiene un area de: {areaPared} y")