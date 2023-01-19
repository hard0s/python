from math import *
a=-1.5
b=1.5
h=0.2
for x in [a,b,h]: #цикл for с шагом h в диапозоне от a до b
    y=(e**x+1)*cos(x)
    print (y)
