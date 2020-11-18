n=int(input())
for i in range(2,n+1):
    s=0
    for k in range(1,i):
        if(i%k==0):
            s=s+k
    if(s==i):
        print(s)
