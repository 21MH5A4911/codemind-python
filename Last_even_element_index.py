x=int(input())
l=list(map(int,input().split()))
e=0
for i in range(x):
    if l[i]%2==0:
        e=i
print(e)    