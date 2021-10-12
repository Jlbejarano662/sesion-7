numero = int(input ("pasa el número: "))
cont=0
for i in range (2,numero +1):
    if numero % i==0:
        cont = cont + 1
if cont ==1:
    print("el numero ", numero, " es  primo ")
else:
    print("el numero ", numero, " no es primo") 