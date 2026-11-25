from fractions import Fraction as Q
from itertools import product
from math import isqrt, prod

H=[0,1,3,6,9,10,15,16,21,30,31,33,36,45,48,49,51,54,
   55,63,64,66,69,70,75,76,78,79,84,85,90,91,93,96,99,100]
gs=(1,3,5,7,15,21,35,105)
K=[max(sum(u%g==b for u in H) for b in range(g)) for g in gs]
assert K==[36,23,11,7,6,4,2,1]
cache={}
def phi2(n):
    if n not in cache:
        cache[n]=(2**n-1)//prod(phi2(d) for d in range(1,n) if n%d==0)
    return cache[n]
def prime(q):
    return q>=2 and all(q%i for i in range(2,isqrt(q)+1))
for n,ps in {
    11:[23,89], 13:[8191], 22:[683], 26:[2731], 27:[262657],
    40:[61681], 44:[397,2113], 48:[97,673], 54:[3,87211],
    60:[61,1321], 72:[433,38737], 96:[193,22253377],120:[4562284561]
}.items():
    assert prod(ps)==phi2(n) and all(map(prime,ps)),(n,ps)
def gap(orders):
    return [Q(c*g,p) for c,g,p in zip(K,gs,orders)]
assert max(gap((16,33,25,28,45,42,35,105)))==36*Q(1,16)
assert max(gap((13,27,20,28,45,42,35,105)))==Q(36,13)
assert max(gap((22,33,55,77,165,231,385,1155)))==Q(23,11)
both=[]
for j,k,w in product(range(4),range(3),range(3)):
    D=Q(11-j,11)*Q(13-k,13)
    both.append((1-D+D*w*Q(13,108)+Q(12-j-k-w,16),j,k,w))
one=[]
for j,w,r in product(range(6),range(3),range(2)):
    D=Q(11-j,11)
    one.append((36*(1-D)+D*(w*Q(13,3)+r*Q(23,6))
                +(11-j-w-r)*max(D*Q(36,13),Q(23,11)),j,w,r))
assert max(both)==(Q(4207,4752),3,0,2) and max(both)[0]<1
assert max(one)==(Q(901,26),0,2,1) and max(one)[0]<36
assert 10*Q(5,26)<2
print(f'both absent: {max(both)}; one absent: {max(one)}; common: {10*Q(5,26)}')
