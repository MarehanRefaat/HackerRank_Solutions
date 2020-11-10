# Enter your code here. Read input from STDIN. Print output to STDOUT
a,b= map(int,input().strip().split())
p = a/b
n = int(input())
q = 1 - p
g = pow(q,n-1)*p
print("%.3f"%g)
