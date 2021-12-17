#inicializacion de variables
acum=0
prom=0.0
cont=0
nombre=""
edad=0
con="S"
contadorjovenes=0
contadoradultosjovenes=0

#ciclo que realiza todo el programa cuando el valor de la variable con es igual a "S" es decir
#cuando el usuario desea seguir ingresando personas, inicialmente le damos el valor "S" para que entre la primera
#vez, luego dentro del ciclo queda a criterio del usuario el valor que coloque a la variable con
while(con=="S"):
    
    #mensaje para saber que el ciclo esta funcionando.
    print("****** ciclo funciona *******")

    #ingresamos el nombre de la persona
    nombre=input("ingrese su nombre: ").upper()
    
    #ingresamos la edad con un ciclo valida que ante cualquier edad que sea mayor o igual a 120 o cualquier edad menor 
    #o igual a cero nuevamente vuelva a pedir la edad, inicialmente le damos un valor 1 válido para que entre al ciclo, 
    #luego dentro del ciclo queda a criterio del usuario el valor que coloque a la variable edad
    edad=0
    while(edad<=0 or edad>=120):
        edad=int(input("ingrese su edad: "))

    #dentro del ciclo esta sentencia selectiva permite que se incremente el contador de jovenes
    #cuando la edad es mayor o igual a 18 y al mismo tiempo menor o igual a 20
    if(edad>=18 and edad<=20):
        contadorjovenes=contadorjovenes+1
        
    #dentro del ciclo esta sentencia selectiva permite que se incremente el contador de adultos jovenes
    #cuando la edad es mayor o igual a 21 y al mismo tiempo menor o igual a 30
    if(edad>=21 and edad<=30):
        contadoradultosjovenes=contadoradultosjovenes+1
    #dentro del cilo muestra para cada ingreso de personas un mensaje personalizado
    print(f"estimado {nombre} su edad es {edad}")

    #dentro del ciclo, para cada persona, con los datos ingresado, acumula la edad e incrementa un contador para saber cuantas
    #veces se ha realizado el ciclo
    acum=acum+edad
    cont=cont+1

    #ingresamos la opcion de continuar si o no, con un ciclo que valida que ante cualquier dato que sea distinto a "S" o "N" 
    #nuevamente vuelva a pedir la opcion de continuar, inicialmente le damos un valor nulo para que entre al ciclo al ser
    #distinto a "S" o "N", luego dentro del ciclo queda a criterio del usuario el valor que coloque a la variable con
  
    con=""
    while(con!="S" and con!="N" ):
        con=input("desea continuar (S/N)").upper()

#fuera del ciclo, mostramos un mensaje ara indicar que ahora mostraremos los resultados, despues de acumular y contar la
#información
print("***********  Resultados son: ******************")

#en este nivel, fuera del ciclo, calculamos el promedio de edad, ya que fuera de ciclo puedo saber correctamente cual fue la suma
#de las edades (acum) y el numero de personas o ciclos realizados (cont)
prom=acum/cont

#mostramos los resultados.
print(f" Promedio de edad: {prom}")
print(f" Total de personas es: {cont}")






