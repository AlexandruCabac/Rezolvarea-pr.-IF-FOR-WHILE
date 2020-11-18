n=int(input())
s1=s2=s3=0
for i in range(1,n+1):
    s1=i**3+s1
    s2=i+s2
    s3=i**2+s3
if((s1-(s2**2))==0):
    print("În cazul (A) sumele sunt egale")
elif(s1-(s2**2)>0):
    print("În cazul (A) prima sumă e mai mare")
else:
    print("În cazul (A) a doua sumă e mai mare")
if(3*s3-(s2+n**2*(n+1))==0):
    print("În cazul (B) sumele sunt egale")
elif(3*s3-(s2+n**2*(n+1))>0):
    print("În cazul (B) prima sumă e mai mare")
else:
    print("În cazul (B) a doua sumă e mai mare") 