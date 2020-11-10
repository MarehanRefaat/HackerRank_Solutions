# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
lamb = float(input())
k = int(input())
res = (pow(lamb,k)*math.exp(-lamb))/math.factorial(int(k))
print("%.3f"%res)
