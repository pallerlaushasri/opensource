T=int(input())
for i in range(0,T):
    n,a=list(map(int,input().split()))
    r=n-a
    if(r>=0):
        print(r)
    else:
        print(0)
