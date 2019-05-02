#for
numeros =  [1,2,3,4,5]
for numero in numeros:
    print(numero)

#list compraration
resultado = [numero for numero in numeros]
print(resultado)

#####################################

for numero in numeros:
    if numero % 2 == 0:
        print(numero)


#for com if
resultado_par = [numero for numero in numeros if numero % 2 == 0]
print(resultado_par)

#####################################