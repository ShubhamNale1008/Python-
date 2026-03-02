#Write a program to find the factorial of a given number


n=int(input("ENter the number:"))

factorial=1
for i in range (1,n+1):
    factorial=factorial*i
    
print(factorial)
