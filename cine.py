#inicializacion de constantes
entrada=1500


print("peliculas ")
pelicula=int(input("escoga pelicula (cars avengers titanic)"))

if(pelicula==1  or pelicula==2 or pelicula==3):
    cantidad=int(input("escoga cantidad de entradas a comprar"))
    entrada=1500
    dinero=int(input("ingrese dinero"))
    total=entrada*cantidad
    vuelto=dinero-total
  
    print(F"su vuelto es{vuelto}")
    print("disfrute su pelicula")

else:
    print("su opcion es invalida")
    
