

#inicializar variables
nota=0
ingresos=0
edad=0
morosidad=""
beca="N"
run=""
monto_beca=0
#definir constantes    beca es constante o variable?????
PORCENTAJE_BECA=0.15;

print("Sistema de becas")
print("----------------")
nombre=input("ingrese nombre del alumno: ").upper()
#nombre=nombre.upper() alternativa sobreescribiendo la variable formal.
#input(" ").upper() alternativa usando el input en memoria.
run=input("ingrese run del alumno: ")
#atentos con la asignación correcta de los tipos de datos (string int float).
nota=float(input("ingrese nota promedio del semestre anterior: "))
ingreso=int(input("Ingrese el monto de sus ingresos mensuales: "))
edad=int(input("Ingrese edad: "))
morosidad=input("presenta morosidad (S/N)")

#evaluación de la variable nota con decimales
if (nota>=6.0):

#atentos con la identación, para definir bloques
    
    #evaluación de rangos
    if (ingreso>=350000 and ingreso<=500000):


        if(edad>=18 and edad<=25):

            #evaluación de la variable nota con decimales
            if(morosidad=="N"):
                
                #variable flag para evaluar al final del algoritmo
                beca="S";
                
            else:
                #mensaje para poder saber si no se cumple
                print("presenta morosidad");
        else:
            print("fuera del rango de edad"); 

    else:
        print("fuera del rango de ingresos");
        
else:
    print("no cumple nota minima");
            
      
if(beca=="S"):
    #si obtuvo beca la variable calculamos el monto.
    monto_beca=ingreso*PORCENTAJE_BECA;
    print("--------------------------------------------------------")
    print(f"{nombre}                  {run}")
    print("--------------------------------------------------------")
    print("Cumple con los requisitos")
    print(f"Obtuvo una beca de ${monto_beca}")
    
else:
    #si no obtuvo la beca mostramos mensajes solicitados.
    print("--------------------------------------------------------")
    print(f"{nombre}                  {run}")
    print("--------------------------------------------------------")
    print("No cumple con los requisitos")
    
 
