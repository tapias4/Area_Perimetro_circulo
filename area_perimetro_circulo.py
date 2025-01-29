import math

print("############################")
print("Area perimetro del circulo")
print("############################")


# input
r=input("digite el valor del radio: ")
r = int(r)

# processing
p = 2*math.pi*r
a = math.pi*r**2

# output
print("########################")
print("el area es : " + str(a))
print("el perimetro es: " + str(p))
print("########################")