#pyramid
n=int(input("enter the no.of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print("\n")
print("--------------------------------------")

#inverted pyramid
n=int(input("enter no.of rows:"))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print("*",end=" ")
    print("\n")
