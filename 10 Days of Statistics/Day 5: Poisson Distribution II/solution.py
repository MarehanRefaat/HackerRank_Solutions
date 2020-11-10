# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m= map(float,input().strip().split())
cost_x = 160 + 40*(n+pow(n,2))
cost_y = 128 + 40*(m+pow(m,2))

print("%.3f"%cost_x)
print("%.3f"%cost_y)
