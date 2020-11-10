
import math

n,m= map(int,input().strip().split())
z = float(input())
x,y= map(int,input().strip().split())
cdf = lambda l : 0.5 + 0.5 * math.erf((l-n)/(m* 2**0.5))
print("%.3f"%cdf(z))
print("%.3f"%(cdf(y)-cdf(x)))
