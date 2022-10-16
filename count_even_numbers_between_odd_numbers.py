x=int(input())
l=list(map(int,input().split()))
e=0
c=0
for i in range(x):
    if(i+2)<x and l[i]%2!=0 and l[(i+1)]%2==0 and l[(i+2)]%2!=0:
        e+=1
print(e)        