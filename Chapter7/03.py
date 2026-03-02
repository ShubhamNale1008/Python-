#write a program to generate a multiplication table for a given number


#using for loop
num=int(input("Enter a number:"))

for i in range(1,11):                
    print(f"{num}*{i}={num*i}")



#using while loop
num=int(input("Enter a number:"))
i=1
while(i<=10):
     print(f"{num}*{i}={num*i}")       #   OR print(num*i)
     i+=1

