a=0
b=1
rango= int(input("Ingresa el rango de la secuencia: "))
print(a)
print(b)

for i in range(rango):
    fibonacci= a + b
    a=b
    b=fibonacci
    print(fibonacci)
   


