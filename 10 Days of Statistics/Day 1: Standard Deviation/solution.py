# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics
n= int(input())
A=[int(x) for x in input().split()]
std= statistics.pstdev(A)
print("%.1f"%std)
