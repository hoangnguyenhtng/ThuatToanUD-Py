# if bthuc logic : A
# if bthuc logic : A 
# else : B
# if bt1 : A1
# else bt2 : A2
#....
# else : An
# A if bthuc logic else B
import math
def dem(t):
    if t > 0 : return [-math.sqrt(t),math.sqrt(t)]
    return [] if t<0 else [0]
def pttp(a,b,c):
    if a==b==c==0: return "vo so nghiem"
    d=b*b-4*a*c
    if a==b==0 or d<0: return []
    if a==0: return dem(-c/b)
    if d==0: return dem(-b/2/a)
    d=math.sqrt(d)
    return dem((-b-d)/2/a) + dem((-b+d)/2/a)
if __name__ == '__main__':
    a,b,c = map(float,input().split())
    print(pttp(a,b,c))