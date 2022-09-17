N=int(input())
t=N
rev=0
while N>0:
    r=N%10
    rev=rev*10+r
    N=N//10
if t==rev:
    print("True")
else:
    print("False")