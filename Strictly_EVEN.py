x=int(input())
l=[int(i) for i in input().split()]
s=0
c=0
for i in l:
    if i%2==0:
        s+=1
for i in range(x):
    if i%2==0 and l[i]%2==0:
        c+=1
print(c==s)        