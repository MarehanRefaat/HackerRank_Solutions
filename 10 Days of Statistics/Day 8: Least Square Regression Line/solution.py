# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import statistics
n = 5
x = []
y = []
for i in range(n):
    l=list(map(int, input().split()))
    x.append(l[0])
    y.append(l[1])
sum_x = sum(x)
sum_y = sum(y)
sum_sqar = math.pow(sum_x,2)
a_2 = []
for i, j in zip(x,y):   
    a_2.append(i * j)
a_3 = sum(a_2)
    
a_4 = [] 
for i,j in zip(x,x):   
   a_4.append(i * j)
a_5 = sum(a_4)
b = ((n*a_3)- (sum_x * sum_y)) / ((n*a_5)-sum_sqar)
y_m = statistics.mean(y)
x_m = statistics.mean(x)
a = y_m - (b * x_m)
x_pred = 80
y_pred = a + (b*x_pred)
print("%.3f"%y_pred)
