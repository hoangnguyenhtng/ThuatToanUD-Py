# Có n mảnh ruộng có sản lượng a1,a2,a3,...an.  Chín lần lượt theo từng ngày
# Nếu quá K ngày mới thu -> Hỏng
# Năng lực thu m
# a = 8 k = 3 m = 5

from queue import Queue

def main():
    n,k,m=map(int,input().split())
    a=list(map(int,input().split()))
    a=a+[0]*(k-1)
    res=0
    q=Queue()
    for x in a:
        q.put(x)
        while q.qsize()>k: q.get()
        t=m
        while q.qsize()>0 and t>0:
            if t>=q.queue[0]:
                t-=q.get()
            else:
                q.queue[0]-=t
                t=0
        res+=m-t

    print(res)
main()

def Search(n,S):
    res ={n}
    S.put(n)
    while S.qsize()>0:
        x=S.get()
        m=int(x**0.5)+1
        for a in range(1,m):
            if x%a==0:
                y=(a-1)*(x//a+1)
                if y not in res:
                    S.put(y)
                    res.add(y)
    return res

if __name__ == '__main__':
    S=Queue.Queue()
    print(Search(int(input()),S))
    
                