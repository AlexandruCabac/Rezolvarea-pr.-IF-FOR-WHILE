n=int(input())
s1=a=0
for i in range(1,n+1):
    s1=s1*2+i
    if(s1>100):
        a=i
        i=n+1
        for k in range(a+1, n+1):
            s1=s1*2+k
if(a!=0):
    print(s1,"$ și la vârsta de",a," ani suma era mai mare de 100$")
else:
    print(s1,"$ încă nu are un cadou mai mare de 100$")