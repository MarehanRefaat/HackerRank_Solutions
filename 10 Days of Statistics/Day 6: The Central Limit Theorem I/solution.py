# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
x = int(input())
n = int(input())
mean = int(input())
var = int(input())

m  = mean * n
v = var * math.sqrt(n)
cdf = lambda l : 0.5 + 0.5 * math.erf((l-m)/(v* 2**0.5))
print("%.4f"%cdf(x))
