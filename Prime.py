n=input()
flag=0
for i in range(2,n+1):
    if n%i==0:
        flag=flag+1
if flag==1:
    print"YES"
else:
    print "NO"