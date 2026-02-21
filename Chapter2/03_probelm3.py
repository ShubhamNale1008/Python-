# to find which number is largest among three numbers

print("Enter three numbers:")

a=int(input("Enter no.1:"))
b=int(input("Enter no.2:"))
c=int(input("Enter no.3:"))

if (a>b) and (a>c):
    print("largest no.is",a)

elif (b>a) and (b>c):
    print("largest no.is",b)

else:
    print("largest no.is",c)