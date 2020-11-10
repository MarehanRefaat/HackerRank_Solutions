# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

n,m= map(int,input().strip().split())
x = float(input())
y=  float(input())
cdf = lambda l : 0.5 + 0.5 * math.erf((l-n)/(m* 2**0.5))
ans_1 = (1 - cdf(x))*100 # mulipty by 100 because it's percentage %
ans_2 = (1 - cdf(y))*100
ans_3 = cdf(y)*100
print("%.2f"%ans_1)
print("%.2f"%ans_2)
print("%.2f"%ans_3)
