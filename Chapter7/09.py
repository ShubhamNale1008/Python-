# to print star pattern

# using for loop
n=int(input("Enter The Number:"))

for i in range(1,n+1):
    print(" " * (n-i),end=" ")
    print("*" * (2*i-1),end=" ")
    print("")




#using while loop
n=int(input("Enter the no:"))

i=1
while(i<=n):
     print(" " * (n-i),end=" ")
     print("*"*(2*i-1),end=" ")
     print(" ")
     i+=1
 



