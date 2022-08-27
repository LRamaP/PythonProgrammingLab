n=int(input("enter the rows"))
ch=input("enter the character")
opt=int(input("Enter 1 for Full square 2 for hallow square"))
if (opt==1):
    for j in range(n):
        for i in range(n):
            print(ch,end=" ")
        print()
else:
    for j in range(1,n+1):
        for i in range(1,n+1):
            if(i==1 or i==n or j==1 or j==n):
                print(ch,end=" ")
            else:
                print(" ",end=" ")
        print()
print("End of Program")
