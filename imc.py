print("indice masa corporal")
v1=float(input("ingrese su peso"))
v2=float(input("ingrese su estatura"))
indice=((v1/v2*v2))
print(f"su resultado de imc es{indice}")


if(indice>=60):
    print("esta bien su peso")


else:
    print("mejore su salud")
