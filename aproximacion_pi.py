#Cristian Javier Martinez Blanco
#20182020155
import math

def inscribe (n,d):
    # n = numero de poligonos
    # p = inscrito
    # d = decimales
    p = n * math.sin(math.pi/n) * math.cos(math.pi/n)
    inscri = round(p,d)
    return inscri

def circumscribed (n,d):
    # n = numero de poligonos
    # q = circunscrito
    # d = decimales
    q = n*math.tan(math.pi/n)
    circum = round(q,d) 
    return circum

def num_polygon (x):
    # x = numero elevado
    num = pow(2,x)
    return num


if __name__ == "__main__":
    try:
        while True:
            x = 2
            while True:
                decimals = int(input("\nPor favor ingrese el numero de decimales a ver (Si desea salir escriba -1): ")) 
                if(decimals >= 0):
                    salir = False
                    break;
                elif(decimals == -1):
                    salir = True;
                    break;
                else:
                    print("\nhas seleccionado un valor no valido, por favor intentalo nuevamente")

            if(salir):
                break;

            else:
                print("\n\n")
                while True:
                    if(circumscribed(num_polygon(x),decimals) == inscribe(num_polygon(x),decimals)):
                        print("             Informacion obtenida")
                        print("_________________________________________________")
                        print("Numero pi obtenido con {:} decimales = {:}".format(decimals, circumscribed(num_polygon(x),decimals)))
                        print("Numero de poligonos utilizados      = {:}".format(num_polygon(x)))
                        print("_________________________________________________\n")
                        break;
                    else:
                        x += 1
    except:
        print("\nHubo un pequeño error en el programa,\nprobablemente en el ingreso de decimales, \npor favor intentelo nuevamente")

        
        


