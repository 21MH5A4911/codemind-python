a,b=map(int,input().split())
x=0
while x<=b:
    x+=1
    if (a*x)%b==0:
        print(a*x)
        break