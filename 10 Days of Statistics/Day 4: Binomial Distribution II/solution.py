# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
def bio (x,n,p):
    fac = math.factorial(n)/ (math.factorial(x) * math.factorial(n-x))
    return (fac*math.pow(p,x)*math.pow(1-p,n-x))
a,b= map(int,input().strip().split())

p = a/100
n = b
res = 0
for x in range(0,3):
    res = res + bio(x=x,n=n,p=p)
print("%.3f"%res)
ras = 0
for x in range(2,n+1):
    ras = ras + bio(x=x,n=n,p=p)
print("%.3f"%ras)
