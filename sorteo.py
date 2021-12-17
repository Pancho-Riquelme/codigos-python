import random
import numpy as np

arre_mensaje= np.empty(10,dtype='object')
for i in range(0,10):
    arre_mensaje[i]=input("ingrese su numero de telefono")

digito = random.randint(0,9)
print(f"el digito ganador es:{arre_mensaje[digito]}")
print("ha gando un premio de 1200000 felicitaciones")




 
 
