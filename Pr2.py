n=int(input())
s=0
for i in range(1,n+1):
    a=1
    for k in range(i,0,-1):
        a=a*k        
    s=s+a
print(s)