# write a program to find a given number is prime or not

num=int(input("Enter no:"))

for i in range(2,num):
    if(num%2==0):
        print(f"The given no. {num} is not prime")
        break
else:
    print("The given no is prime")