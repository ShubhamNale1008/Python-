#percentage of marks

m1=int(input("Enter your marks1:"))
m2=int(input("Enter your marks2:"))
m3=int(input("Enter your marks3:"))
m4=int(input("Enter your marks4:"))
m5=int(input("Enter your marks5:"))
m6=int(input("Enter your marks6:"))

total_marks=m1+m2+m3+m4+m5+m6
percentage=((total_marks*100)/600)

print("Your total percentage is",percentage)

if(percentage>=35):
    print("Congrats you have passed the exam")
else:
    print("Better luck next time")

