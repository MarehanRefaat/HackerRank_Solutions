# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
from scipy import stats
N = int(input())
arr_1=input().strip().split(' ')
A=np.array(arr_1,float)
for i in range(N):
    mean  = sum(A)/N
print(mean)
Med = sorted(list(A))
if N%2 == 0:
    median = (Med[int(N/2)-1] + Med[int(N/2)])/2
else:
    median = Med[int((N+1)/2)]
print(median)    
print(int(stats.mode(Med)[0]))
