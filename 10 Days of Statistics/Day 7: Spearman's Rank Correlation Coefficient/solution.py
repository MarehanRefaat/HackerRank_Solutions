# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
x = [float(i) for i in input().strip().split(" ")]
y = [float(i) for i in input().strip().split(" ")]
x_s = sorted(list(x))
y_s = sorted(list(y))
d = ([(x_s.index(x[i])-y_s.index(y[i]))**2 for i in range(n)])
res = 1-6*sum(d)/(n*(n**2-1))
print("%.3f"%res)
    
