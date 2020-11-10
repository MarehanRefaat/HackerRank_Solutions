# Enter your code here. Read input from STDIN. Print output to STDOUT
def g (p,q,n):
    return pow(q,n-1)*p
a,b= map(int,input().strip().split())
p = a/b
n = int(input())
q = 1 - p
res = 0
for i in range(1,n+1):
    res = res + g(p,q,i)
#g =  pow(q,n-1)*p
print("%.3f"%res)
