n=int(input())
n1=len(str(n))
sqr=n**2
last_no=sqr%10**n1
if last_no==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")