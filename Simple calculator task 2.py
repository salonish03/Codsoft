# To create a simple calculator

print("----Welcome to simple calculator----")

a=float(input("Enter first number"))
b=float(input("Enter second number"))
print("1 Adddition")
print("2 Subtraction")
print("3 Multiplication")
print("4 Division")
print("5 Modulus")

c=int(input("Enter the arithmetic operation number from 1 to 5"))


if c==1:
    d=a+b
    print("Addition is",d)
    
elif c==2:
    e=a-b
    print("Subtraction is",e)

elif c==3:
    f=a*b
    print("Multiplication is",f)

elif c==4:
    g=a/b
    print("Division is",g)

elif c==5:
    h=a%b
    print("Modulus is",h)

else:
    print("wrong Number input")

