print("***Credito***")

nombre = ""
rut = ""
monto_credito = 0
plazo_cuotas = 0
edad = 0
nacionalidad = ""
sueldo = 0
antiguedad_laboral = 0
morosidad = ""
credito = "N"
TASA_MENSUAL = 1.46

nombre = input("Ingrese Nombre:").upper()
rut = input("Ingrese RUT:")
monto_credito = int(input("Monto solicitado:"))
plazo_cuotas = int(input("Cuotas:"))
edad = int(input("Edad:"))
nacionalidad = input("Ingrese nacionalidad:").upper()
sueldo = int(input("Ingrese sueldo:"))
antiguedad_laboral = int(input("Ingrese antiguedad laboral:"))
morosidad = input("Ingrese morosidad(S/N):").upper()

if(monto_credito >=500000):
    if(plazo_cuotas >= 3 and plazo_cuotas <= 84):
        if(edad >= 24 and edad <= 79):
            if(nacionalidad == "CHILENA"):
                if(sueldo >= 250000):
                    if(antiguedad_laboral >= 3):
                        if(morosidad == "N"):
                            credito = "S"
                            monto_maximo = (sueldo*10)
                            monto_pagar = (monto_credito*TASA_MENSUAL)

                        
                        else:
                            print("Es moroso")
                    else:
                        print("No cumple con antiguedad laboral.")
                else:
                    print("sueldo minimo no valido.")
            else:
                print("No cumple con la nacionalidad.")
        else:
            print("No cumple con la edad.")
    else:
        print("Plazo cuotas invalido.")
else:
    print("El monto minimo es $500000.")


if (credito =="S"):
    print("----------------------------------------------")
    print(f"{nombre}  {rut}")
    print("----------------------------------------------")
    print("Cumple con los requisitos")
    print(f"Sueldo:${sueldo}")
    print(f"Monto maximo:${monto_maximo}")
    print(f"Monto solicitado:${monto_credito}")
    print(f"Tasa mensual:{TASA_MENSUAL}%")
    print(f"Cuotas:{plazo_cuotas}")
    print(f"Monto a pagar:${monto_pagar}")
else:
    print("----------------------------------------------")
    print(f"{nombre}  {rut}")
    print("----------------------------------------------")
    print("No cumple con los requisitos.")
