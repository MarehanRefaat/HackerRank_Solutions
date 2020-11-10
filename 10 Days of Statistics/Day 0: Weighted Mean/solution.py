N = input()
X = map(float,raw_input().split())
W = map(float,raw_input().split())
x=list(X)
w=list(W)
p=[]
for i in range(N):
        p.append(x[i]*w[i])
        mul= (sum(p)/sum(w))
print(round(mul,1))
