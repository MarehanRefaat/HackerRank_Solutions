# Enter your code here. Read input from STDIN. Print output to STDOUT
from sklearn import linear_model

def pre(x, y, x_pred):
  lm = linear_model.LinearRegression()
  lm.fit(x, y)
  y_pred = lm.predict(x_pred)
  return y_pred
def main():
    n,m= map(int,input().strip().split())
    x=[]
    y=[]
    for i in range(m):
        l=list(map(float, input().split()))
        x.append(l[0:n])
        y.append(l[n:])
    q = int(input())
    x_pred = []
    for i in range(q):
        l=list(map(float, input().split()))
        x_pred.append(l[0:n])
  
    result = pre(x, y, x_pred)
    for i in result:
            print(round(float(i),2))
if __name__ == "__main__":
  main()
