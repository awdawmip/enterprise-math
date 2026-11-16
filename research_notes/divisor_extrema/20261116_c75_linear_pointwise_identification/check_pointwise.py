"""Exact arithmetical controls of the coarse/fine projections and spacings."""
from fractions import Fraction as F
from functools import lru_cache
from math import comb, prod
import json

def rising(n, length):
    return prod(range(n, n + length))

@lru_cache(None)
def rate(n, s, k):
    length = n - s + 1
    rho = F(4 * prod(4*j+k for j in range(s, n+1)), 4**length*rising(s+k, length))
    a = F((s+k-1)*rising(n+k+1, 3*k), 28*(4*s+k-1)*rising(s+k, 3*k))
    return rho, a

@lru_cache(None)
def tail(s):
    Y = F(prod(4*j+1 for j in range(3, s+1)), 4**(s-2)*rising(4, s-2))
    W = F((s+2)*(s+3)*(s+4), 840)
    ends = [(F(5), F(3,32)), (F(5,4), F(3,2)), (F(1,2),F(6))]
    p_real = [(1+W/(Y*e))/(1+j*W) for j,e in ends]
    p_zero = [1/(1+j*W) for j,e in ends]
    direct = [Y*(e/W+j*e)/(1+Y*e/W) for j,e in ends]
    assert [1/p for p in p_real] == direct
    return p_real, p_zero, direct

def nu2(q):
    n, d = abs(q.numerator), q.denominator
    if n == 0:
        return None
    return (n & -n).bit_length() - (d & -d).bit_length()

def qwidth(pair):
    return max(pair) / min(pair) - 1

def words(c,v,w):
    rho1, a1 = rate(c,v,5)
    rho2, a2 = rate(v,w,3)
    preal, pzero, tail_z = tail(w)
    j,k = sorted(range(3), key=tail_z.__getitem__)[::2]
    data = {}
    for tail_type, endpoints in [('physical',preal),('zero',pzero)]:
        for mid_t in [0, a2/rho2]:
            for top_t in [0, a1/rho1]:
                mid = [(1+mid_t*endpoints[idx])/(1+a2*endpoints[idx]) for idx in (j,k)]
                end = [(1+top_t*p)/(1+a1*p) for p in mid]
                R = end[0]/end[1]
                R0 = (1+a1*mid[1])/(1+a1*mid[0])
                assert (R/R0-1) == top_t*(mid[0]-mid[1])/(1+top_t*mid[1])
                assert mid[0] != mid[1]
                data[tail_type,bool(mid_t),bool(top_t)] = qwidth(end)
    zs = [(rho2+rho2/a2*inp)/(1+rho2/a2*inp) for inp in tail_z]
    lo, hi = min(zs), max(zs)
    g = data['physical', True, True]
    Q = data['physical', True, False]
    assert Q == (hi-lo)*a1/(lo*(a1+hi))
    tau = rho1/a1
    phys = [(rho1+tau*z)/(1+tau*z) for z in zs]
    assert g == qwidth(phys)
    return len(data)

def residual(c,u,y, freeze_tail):
    rho1, a = rate(c,u,5)
    rho2, b = rate(u,y,3)
    pr,pz, direct = tail(y)
    j,k=sorted(range(3),key=direct.__getitem__)[::2]
    def val(t,s,p):
        mid = [(1+s*p[m])/(1+b*p[m]) for m in [j,k]]
        end = [(1+t*q)/(1+a*q) for q in mid]
        return end[0]/end[1]
    p = pr if freeze_tail else pz
    R0 = val(0,0,p)
    Rtop = val(a/rho1,0,p)
    Rtrue = val(a/rho1,b/rho2,pr)
    leading = nu2(Rtop/R0-1)
    actual = nu2(Rtrue/R0-1)
    assert leading == actual
    return dict(c=c,u=u,y=y,actual=actual,outer_only=leading,tail_retained=freeze_tail)

def main():
    assert F(6909,10000)**15 < F(1,256) < F(6910,10000)**15
    assert F(5400,10000)**9 < F(1,256) < F(5401,10000)**9
    entropy = 0
    for K in (1,3,5):
        for n in range(2,55):
            for s in range(2,n+1):
                r = rate(n,s,K)[0]
                length=n-s+1
                divisible=4**length * 2**(length-length.bit_count()) * comb(n+K,length)
                assert divisible%r.denominator==0
                entropy+=1
    total = sum(words(c,v,w) for c in range(2,23) for v in range(2,c+1) for w in range(2,v+1))
    records=[residual(c,u,y,fr) for c,u,y,fr in [(1200,829,448,False),(1400,967,522,False),(1300,895,37,True),(1450,1002,8,True),(256,160,2,True)]]
    print(json.dumps(dict(exact_entropy_checks=entropy, centered_and_physical_orientations=total, exact_shortest_outer_residual=records),indent=2))

if __name__ == '__main__':
    main()
