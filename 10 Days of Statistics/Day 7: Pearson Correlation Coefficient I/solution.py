# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics
n = int(input())
x=list(map(float, input().split()))
y=list(map(float, input().split()))
m_x = statistics.mean(x)
m_y = statistics.mean(y)
var_x = statistics.pstdev(x)
var_y = statistics.pstdev(y)
mul_1 = []
for i in range(n):
     mul_1.append((x[i]- m_x)*(y[i] - m_y))
res = sum(mul_1)
p = res / (n * var_x * var_y)
print("%.3f"%p)
