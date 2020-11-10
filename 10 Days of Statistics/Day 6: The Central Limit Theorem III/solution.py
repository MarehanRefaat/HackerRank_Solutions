# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
#x = int(input())
n = int(input())
mean = float(input())
var = float(input())
x = float(input())
z = float(input())
A = mean - (var/math.sqrt(n)) * z
B = mean + (var/math.sqrt(n)) * z
print("%.2f"%A)
print("%.2f"%B)
