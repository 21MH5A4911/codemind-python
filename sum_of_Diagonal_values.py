r,c=map(int,input().split())
m=[]
e=[]
s=0
for i in range(r):
    l=list(map(int,input().split()))
    m.append(l)
for i in range(r):
    for j in range(c):
        if i==j or i+j==r-1:
            s+=m[i][j]
print(s)  