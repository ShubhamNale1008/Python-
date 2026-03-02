#write a program to greet all people stored in a list stating with letter 's'

l=["Shubham","Harry","Srusti"]

for i in l:              #for name in l:
    print(i)             #  print(name)
                        





l=["Shubham","Harry","Srusti"]

for name in l:
    if(name.startswith("S")):
        print("Good Morning",name)                   #cause list are mutuable so we can print name dirctly

