x=int(input())
l=list(map(int,input().split()))
d=x//2
e=0
for i in l:
    if i%2==0:
        e=i
print(e)