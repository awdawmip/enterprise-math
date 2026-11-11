"""Exclude every positive integer inventory for the hidden word 55.

Only Python integers are used. Baker's explicit irrationality inequality and
Legendre's convergent criterion are the two stated external inputs.
"""
from math import gcd,isqrt


def cube_root_floor(n):
    hi = 1 << ((n.bit_length()+2)//3)
    while True:
        candidate = (2*hi + n//(hi*hi))//3
        if candidate>=hi:
            assert hi**3 <= n < (hi+1)**3
            return hi
        hi = candidate


def convergents(p,q,limit):
    a0,b0,a1,b1 = 0,1,1,0
    out=[]
    while q:
        h,rem=divmod(p,q)
        a0,a1=a1,h*a1+a0
        b0,b1=b1,h*b1+b0
        out.append((a1,b1))
        if b1>=limit: break
        p,q=q,rem
    return out


def main():
    assert 120000000**200 < 10**(180*9)
    B=10**180
    scale=10**450
    base=cube_root_floor(4*scale**3)
    lo=convergents(base,scale,B)
    hi=convergents(base+1,scale,B)
    assert lo==hi and lo[-1][1]>=B
    candidates={(a,b) for b in range(1,121) for a in range(b+1,2*b) if gcd(a,b)==1}
    candidates.update((a,b) for a,b in lo if 120<b<B and b<a<2*b)
    thue=[]
    square=[]
    for a,b in sorted(candidates):
        d=4*b**3-a**3
        if d<=0 or 60%d:continue
        thue.append((a,b,d))
        g2,rem=divmod(4*b-a,d)
        if rem or isqrt(g2)**2!=g2:continue
        g=isqrt(g2); x,y=g*a,g*b
        square.append((x,y))
    print('convergents',len(lo),'primitive candidates',len(candidates))
    print('negative Thue divisors',thue,'admissible x,y',square)
    assert square==[(3,2)] and all((x-y)%3 for x,y in square)
if __name__=='__main__':
    main()
