n=list(map(int,input().split()))
l=[]
for i in range(n[0],n[1]):
    flag=0
    for j in range(2,i+1):
        if i%j==0:
            flag=flag+1
    if flag==1:
        l.append(i)
print(l)
