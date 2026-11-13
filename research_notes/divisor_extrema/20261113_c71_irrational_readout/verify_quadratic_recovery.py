"""Independent exact rational model and Q(sqrt(2)) one-readout inverse.
Checks the C71 algebra against the original two-block three-tail kernel.
"""
from fractions import Fraction as F
from math import prod

def matmul(u, v):
    a, b, h, d = u
    e, f, g, i = v
    return (a*e+b*g, a*f+b*i, h*e+d*g, h*f+d*i)

def edge(r, c, m):
    k, v = 2*r+1, c-m
    a = prod(k+4*n for n in range(v, c+1))
    b = prod(k+n for n in range(v, c+1))
    e = (k-1+v)*prod(4*k+n for n in range(v, c+1))
    t = 28*(k-1+4*v)*a*b
    return (t, a*e, t, 4**m*e*b)

def ends(c):
    x = F(840, (c+2)*(c+3)*(c+4))
    y = prod((F(4*n+1, 4*n+4) for n in range(3, c+1)), start=F(1))
    return [y*(x*a+b)/(1+x*y*a)
            for a,b in zip((F(3,32),F(3,2),F(6)),
                           (F(15,32),F(15,8),F(3)))]

def endpoints(c, v, w):
    m = matmul(edge(2,c,c-v), edge(1,v,v-w))
    z = sorted(F(m[0]*e+m[1], m[2]*e+m[3]) for e in ends(w))
    return z[0], z[-1]

def mulq(x, y):
    # coordinate basis (1, t), t=sqrt(2)-1, t*t=1-2*t
    a,b=x; c,d=y
    return a*c+b*d, a*d+b*c-2*b*d

def divq(x, y):
    c,d=y
    n=c*c-2*c*d-d*d
    return mulq(x, ((c-2*d)/n, -d/n))

def recover(q):
    u,v=q
    assert v != 0
    B=(1-u)/v
    A=v+(u-2*v)*B
    return 1+B, 1+A

def check(last=32):
    words=0
    for c in range(2,last+1):
        for v in range(2,c+1):
            for w in range(2,v+1):
                lo,hi=endpoints(c,v,w)
                assert lo < hi
                q=divq((F(1),hi-1),(F(1),lo-1))
                assert recover(q)==(lo,hi)
                g=hi/lo
                h=(hi+1)/(lo+1)
                assert (g+1)*(h-1)/(g-h)==lo+hi
                # exact w-dependent extremal terminal tails
                term=ends(w)
                assert term[0]==min(term)
                assert term[1 if w<=3 else 2]==max(term)
                words+=1
    print(f"PASS exact rational Q(sqrt(2)) recovery: c=2..{last}, {words} arrangements")

if __name__=='__main__':
    check()
