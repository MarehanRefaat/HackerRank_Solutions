from statistics import median
n = int(input())
arr_1=[int(x) for x in input().split()]
arr_2= sorted(arr_1)
t=int(len(arr_2)/2)
if n%2 == 0:
    low = arr_2[:t]
    high = arr_2[t:]
else :
    low = arr_2[:t]
    high = arr_2[t+1:]
print(int(median(low)))
print(int(median(arr_2)))
print(int(median(high)))
