# n = int(input())
# a = list(map(float, input().split()))
# m = int(input())
# b = list(map(float, input().split()))
# k = int(input())
# c = list(map(float, input().split()))
# z = max(m,n,k)
# a = a + [0]*(z-n)
# b = b + [0]*(z-n)
# c = c + [0]*(z-n)
# d = [u + v + t for u, v, t in zip(a,b,c)]
# while len(d) > 0 and d[-1] == 0: d.pop()
# for x in d: print("%0.3f" %x, end = " ")
# import math 
# def bp(x) : return x*x

# a = [4,7,2,8]
# b=list(map(math.sqrt,a))
# print(b)

# c = list(map(bp,a))
# print(c)

# d = list(map(lambda x : x % 2,a))
# print(d)