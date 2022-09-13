n=int(input())
m=n*n
x=0
while (m>0):
    q=m%10
    x=x+q
    m=m//10
if x==n:
    print("Neon Number")
else:
    print("Not Neon Number")
    