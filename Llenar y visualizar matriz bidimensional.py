arreglo1=[0,0,0,0,0]
arreglo2=[0,0,0,0,0]
arreglo3=[0,0,0,0,0]
arreglo4=[0,0,0,0,0]
arreglo5=[0,0,0,0,0]
for i in range (1,6):
    arreglo1[i - 1] = float(input("Este es tu primer arreglo, dame el número {}: ".format(i)))
for i in range (1,6):
    arreglo2[i - 1] = float(input("Este es tu segundo arreglo, dame el número {}: ".format(i)))
for i in range (1,6):
    arreglo3[i - 1] = float(input("Este es tu tercer arreglo, dame el número {}: ".format(i)))
for i in range (1,6):
    arreglo4[i - 1] = float(input("Este es tu cuarto arreglo, dame el número {}: ".format(i)))
for i in range (1,6):
    arreglo5[i - 1] = float(input("Este es tu quinto arreglo, dame el número {}: ".format(i)))
print(arreglo1)
print(arreglo2)
print(arreglo3)
print(arreglo4)
print(arreglo5)
