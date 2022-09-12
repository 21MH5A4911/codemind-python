s=int(input())
sum1=0
for i in range(1,s):
    if s%i==0:
        sum1=sum1+i
if sum1==s:
    print(True)
else:
    print(False)