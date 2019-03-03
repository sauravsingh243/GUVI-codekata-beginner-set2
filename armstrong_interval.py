n=list(map(int,input().split()))
l=[]
for i in range(n[0],n[1]):
    copy1,copy2=i,i
    s=0
    while(copy1>0):
        b=copy1%10
        s=s+(b**3)
        copy1=copy1//10
    if(s==copy2):
        l.append(i)
for _ in l:
    print(_,end=" ")