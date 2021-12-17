v1=0
v2=0
res_suma=0
valor1=0
valor2=0
res_resta=0
res_multiplicacion=0
res_division=0
acu=0
acudivision=0
acumulti=0
acusumador=0
acuresta=0
continuar="S"


print("menu calculadora")
print("_ _ _ _ _ _ _ _")

print("desea sumar opcion 1")
print("desea restar opcion 2")
print("desea multiplicar opcion3")
print("desea dividir opcion 4")
print("desea ver el balance opcion5")

while(continuar=="S"):
    opcion=int(input("eliga que opcion quiere ejecutar"))
if(opcion==1):
    print("ingrese valores")
    v1=int(input("ingrese valor 1"))
    v2=int(input("ingrese valor 2"))
    res_suma=valor1+valor2
    print(f"su resultado es{res_suma}")
    acu=acusumador+res_suma
elif(opcion==2):
    print("ingrese valores")
    valor1=int(input("ingrese valor 1"))
    valor2=int(input("ingrese valor 2"))
    res_resta=valor1-valor2
    print(f"su resultado es{res_resta}")
    acu=acuresta+res_resta
elif(opcion==3):
    print("ingrese valores")
    valor1=int(input("ingrese valor 1"))
    valor2=int(input("ingrese valor 2"))
    res_multiplicacion=valor1*valor2
    print(f"su resultado es{res_multiplicacion}")
    acu=acumulti+res_multiplicacion
elif(opcion==4):
    print("ingrese valores")
    valor1=int(input("ingrese valor 1"))
    valor2=int(input("ingrese valor 2"))
    res_division=valor1/valor2
    print(f"su resultado es{res_division}")
    acu=acudivision+res_division
    


elif(opcion==5):
    print(f"el acumulador de sumas es{acusumador}")
    print(f"el acumulador de resta es {acuresta}")
    print(f"el acumulador de multis es {acumulti}")
    print(f"el acumulador de divisiones es {acudivision}")

    seguir=input("desea seguir")
    if(seguir=="N"):
        break
        
     
