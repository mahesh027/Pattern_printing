#hollow triangle
n=int(input("enter the no.of rows:"))
for i in range(0,n):
    for j in range(0,i+1):
        if j==0 or i==n-1 or i==j:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print("\n")
