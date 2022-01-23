# Promedio de tres notas - Condicional
print("Ingrese la primera nota")
N1=int(input())
print("Ingrese la segunda nota")
N2=int(input())
print("Bien, casi terminamos")
print("Ingrese la tercera y última nota")
N3=int(input())
Resultado=(N1+N2+N3)/3

if (Resultado>=10.5):
    print("Usted, aprobó el curso con:", Resultado)
else:
    print("Siga esforzándose. Usted obtuvo:", Resultado)