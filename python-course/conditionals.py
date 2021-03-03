#Usuario da un dato

x= 30

#Operador de comparación. <, ==. True or False

#If. Hacer una pregunta y si es True  hace lo que está debajo con un tab
#if x<30:
   # print("x is less than 30")


#Else si es False haz esto.

if x<20:
    print("x is less than 20")
else:
    print("x is grater than 20")



color = "red"

if color=="blue":
    print("blue")
else:
    print("unvalid color")

#Otra comparación adicional. elif

color = "red"

if color=="blue":
    print("blue")
elif color == "red":
    print("It'red")
else:
    print("unvalid color")


#Revalidación. Condicional anidada

name ="Juan"
Lastname = "Santos"

if name == "Juan":
    if Lastname == "Carter":
        print("You are Juan Carter")
    else:
        print("You are not Juan Carter")
else:
        print("You are not Juan")

#Operadores lógicos. and, or, not.
#<=. Menor o igual

x= 3
y=2
if x>2 and x <= 10:
    print("x is greater than two and less than or equal to ten")
elif (x>2 and x<=20):
        print("x is greater than two or less than or equal to twenty")
elif not x==y:
    print("x is not equal y")




