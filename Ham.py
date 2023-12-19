#range: (bat dau, ket thuc + 1, cong sai)
#filter (chi so , gia tri)
#map
#enum
#zip (ghep 2 danh sach )
# '''
# a = list(range(10))
# print(a)
# print(*a,sep=" + ", end=" = ")
# print(sum(a))
# b = list(range(4,9,2)) #tu 4 den 9 va cach deu 2
# print(b)
# c = list(range(10,0,-1))
# print(c)
# '''

# a = [1,2,4,5,6,6]
# b = list(enumerate(a)) 
# print(b)
# s = 0
# for i,x in enumerate(a,1):s+=i*x #tinh tong chi so nhan gia tri
# print(s)

# a = [4,7,5,3,2]
# b = "anhem"
# c = list(zip(a,b))
# print(c)
# e = [123,1,23,432,42,42,454,34]
# d=zip(a,e,a[::-1])
# print(list(d))

# a = [4,5,2,8,3,7,2,1]
# b = filter(lambda x:x%2==0,a) #loc so chan
# print(list(b))
# print
import math

def chinhphuong(n):
    if n < 0: return 0
    if n%3>1 or n%4>1: return 0
    m=math.trunc(math.sqrt(n))
    return m*m==n
a = [4,7,2,8,3,7,2,1]
b = filter(lambda x:x%2 == 0, a) #loc c chan
print(list(b))
c = list(filter(chinhphuong,a))
print(c)