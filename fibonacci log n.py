def fib(n):
    if n == 1: return 1,1
    x,y = fib(n//2)
    a = x*x+y**2
    b = x*y + y*(x-y)
    if n%2 == 0: return a, b
    return a+b, a

if __name__ == "__main__":
    for n in range (1,201):
        a, b = fib(n)
        print(n, a)

