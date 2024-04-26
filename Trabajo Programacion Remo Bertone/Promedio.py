nota1 = int(input("ingrese la nota 1 : "))
nota2 = int(input("ingrese la nota 2 : "))
nota3 = int(input("ingrese la nota 3 : "))

prom = (nota1+nota2+nota3)/3

if prom >=7 :
    print("promocionado")

else : 

    if prom >=4 :
        print("Regular")

    if prom< 4 :
        print("Reprobado")
