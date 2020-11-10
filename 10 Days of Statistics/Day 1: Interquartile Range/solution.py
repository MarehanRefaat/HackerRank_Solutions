# Enter your code here. Read input from STDIN. Print output to STDOUT
from statistics import median
N = int(input())
A=[int(x) for x in input().split()]
B=[int(x) for x in input().split()]
s = []
for i in range(N):
    s += [A[i]]*B[i]
s.sort()
t=int(len(s)/2)
if N%2 == 0 :
    low =s[:t]
    high =s[t:]
else :
    low = s[:t]
    high = s[t+1:]
q_1 = int(median(low))
q_3 = int(median(high))
result = float(q_3 - q_1)
print("%0.1f"%result)
