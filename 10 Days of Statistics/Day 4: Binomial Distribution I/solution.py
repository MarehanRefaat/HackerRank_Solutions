# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
def bio (x,n,p):
    fac = math.factorial(n)/ (math.factorial(x) * math.factorial(n-x))
    return (fac*math.pow(p,x)*math.pow(1-p,n-x))
a,b= map(float,input().strip().split())

p = a/(a+b)
n = 6
res = 0
for x in range(3,7):
    res = res + bio(x=x,n=n,p=p)
print("%.3f"%res)
