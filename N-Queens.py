def place(k,i,x):
    for j in range(k-1):
        if ((x[j]==i+1) or (abs(x[j]-(i+1))==abs(j-(k-1)))):
            return False
    return True
def nqueens(k,n,x):
    for i in range(n):
        if place(k,i,x):
            x[k-1]=i+1
            if k==n:
                print(x)
            else:
                nqueens(k+1,n,x)
n=int(input("Enter the no.of queens : "))
x=[0 for i in range(n)]
nqueens(1,n,x)