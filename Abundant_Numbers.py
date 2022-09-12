s=int(input())
j=1
for i in range(1,s):
    if s%i==0:
        j+=i
if (j>s):
    print(True)
else:
    print(False)