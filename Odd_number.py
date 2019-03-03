l=list(map(int,input().split()))
r=[]
for i in range(l[0]+1,l[1]):
    if i%2!=0:
        r.append(i)
for i in range(0,len(r)):
    print(r[i],end=" ")