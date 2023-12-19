# def fib(n):
#     if n == 1: return 1,1
#     x,y = fib(n//2)
#     a = x*x+y**2
#     b = x*y + y*(x-y)
#     if n%2 == 0: return a, b
#     return a+b, a

# if __name__ == "__main__":
#     for n in range (1,201):
#         a, b = fib(n)
#         print(n, a)

""""""
# Nhập: input()
# getline Trả về xâu
# sys.stdin.read() đọc hế stdin
# a = map(int,a) ép kiểu vả một danh sách về kiểu int
# Cho n phần tử a đến an trên 1 dòng : n *a = list(map(int, input().split())

# a = [3,4,5] #list -> Bien
# b = (3,4,5) #tuple -> Hang
a = [3,4,5]
c = a + a
print("C", c)
print ("D ", d )
e = [a] * 2
print ("E" ,*e) 
a1 = [0] * 3
b1 = [a] * 2
print(*b1)
b1[0][0] = 2
print(*b1)
b = []
for i in range (3) : b.append([0]*2)
b[0][0] = 6
print(b)
