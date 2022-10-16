n=int(input())
s=list(map(int,input().split()))
if (sum(s)//n) in s:
    print('True')
else:
    print('False')