#day con lien tuc khac biet
n = input()
a = list(map(int, input().split()))
p=0
res=0
D={}
for i,x in enumerate(a):
    if x in D.keys() and D[x]>=p: p=D[x]+1
    res=max(res,i-p)
    D[x]=1
print(res+1)