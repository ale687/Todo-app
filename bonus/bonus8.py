try:
    width = float(input("Introdusca el ancho del rectangulo:"))
    lenght =  float(input("Introduzca la longitud del rectangulo:"))
    
    if width == lenght:
        exit("eso es un cuadrado")
        
    area = width * lenght
    print(area)
    
except ValueError:
    print("por favor introduza un numero")