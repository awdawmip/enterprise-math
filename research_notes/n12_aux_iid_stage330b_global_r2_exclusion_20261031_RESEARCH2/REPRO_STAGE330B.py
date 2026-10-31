#!/usr/bin/env python3
"""Stage330-B: exact dyadic interval certificate for the Bernoulli BRC r2 sign.

Only Python stdlib integer and Fraction arithmetic is used. Every leaf is a
closed rectangle; overlap at shared boundaries is harmless. No sampling.
"""
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
import json

D = 1 << 16
D3 = D ** 3
WEIGHTS = (1, 3, 3, 1)
TARGET = (61, 21, 9, 9)
THRESHOLD = F(61, 10000)

@lru_cache(maxsize=None)
def endpoint(n):
    return tuple(27 * n ** k * (D - n) ** (3 - k) for k in range(4))

@lru_cache(maxsize=None)
def bernstein_ranges(a, b):
    qa, qb = endpoint(a), endpoint(b)
    lo = [min(qa[k], qb[k]) for k in range(4)]
    hi = [max(qa[k], qb[k]) for k in range(4)]
    # B1 maximum at 1/3 and B2 maximum at 2/3, both equal 4/27.
    if 3*a <= D <= 3*b:
        hi[1] = max(hi[1], 4*D3)
    if 3*a <= 2*D <= 3*b:
        hi[2] = max(hi[2], 4*D3)
    return tuple(lo), tuple(hi)

def residual_ranges(rect):
    a,b,c,d = rect
    lx,hx = bernstein_ranges(a,b)
    ly,hy = bernstein_ranges(c,d)
    lo = tuple(32*(4*lx[k]+ly[k])-27*TARGET[k]*D3 for k in range(4))
    hi = tuple(32*(4*hx[k]+hy[k])-27*TARGET[k]*D3 for k in range(4))
    # Actual r_k lie in [lo,hi]/(160*27*D**3).
    return lo, hi

def classify(rect):
    lo,hi = residual_ranges(rect)
    if lo[2] > 0:
        return 'R2_POSITIVE'
    mindist = sum(WEIGHTS[k]*(lo[k] if lo[k]>0 else -hi[k] if hi[k]<0 else 0)
                  for k in range(4))
    # b >= mindist / (1024 * 27 * D**3).
    if 10000*mindist > 61*1024*27*D3:
        return 'B_EXCEEDS_THRESHOLD'
    return None

def certify(rect, output, depth=0):
    kind = classify(rect)
    if kind is not None:
        output.append((kind, *rect, depth))
        return
    a,b,c,d = rect
    if b-a == d-c == 1:
        raise AssertionError('dyadic resolution insufficient: '+str(rect))
    if b-a > 1 and (d-c == 1 or 4*(b-a) >= d-c):
        m=(a+b)//2
        children=((a,m,c,d),(m,b,c,d))
    else:
        assert d-c > 1
        m=(c+d)//2
        children=((a,b,c,m),(a,b,m,d))
    for child in children:
        certify(child, output, depth+1)

def B(k,z):
    return z**k*(1-z)**(3-k)

def residual(x,y):
    return tuple((4*B(k,x)+B(k,y))/5-F(TARGET[k],160) for k in range(4))

def b_cost(x,y):
    r=residual(x,y)
    return F(5,32)*sum(WEIGHTS[k]*abs(r[k]) for k in range(4))

def exact_interval(k, left, right):
    v=(B(k,left),B(k,right))
    critical=F(k,3)
    if left <= critical <= right:
        v += (B(k,critical),)
    return min(v), max(v)

def root_box_beta_lower():
    # An inherited, slightly enlarged isolating rectangle for (x*,y*).
    xlo,xhi=F(231,1000),F(232,1000)
    ylo,yhi=F(555,1000),F(556,1000)
    lo=[];hi=[]
    for k in range(4):
        ax,bx=exact_interval(k,xlo,xhi)
        ay,by=exact_interval(k,ylo,yhi)
        lo.append((4*ax+ay)/5-F(TARGET[k],160))
        hi.append((4*bx+by)/5-F(TARGET[k],160))
    assert lo[2]>0 and hi[3]<0
    lower=F(5,32)*(3*lo[2]-hi[3])
    assert lower>F(3,1000)
    return lower

def main():
    leaves=[]
    certify((0,D,0,D),leaves)
    assert all(classify(e[1:5])==e[0] for e in leaves)
    assert sum((e[2]-e[1])*(e[4]-e[3]) for e in leaves)==D3//D
    assert all(0<=e[1]<e[2]<=D and 0<=e[3]<e[4]<=D for e in leaves)
    counts={kind:sum(row[0]==kind for row in leaves)
            for kind in ('R2_POSITIVE','B_EXCEEDS_THRESHOLD')}
    print('DYADIC_D =',D)
    print('LEAVES =',len(leaves),'CLASS_COUNTS =',counts,'MAX_DEPTH =',max(e[5] for e in leaves))
    print('AREA_SUM =',sum((e[2]-e[1])*(e[4]-e[3]) for e in leaves),'EXPECTED =',D*D)
    manifest=json.dumps(leaves,separators=(',',':'))
    print('CERT_MANIFEST_SHA256 =',sha256(manifest.encode()).hexdigest())
    print('CERT_MANIFEST_JSON =',manifest)
    anchor=(F(2311,10000),F(1111,2000))
    b_anchor=b_cost(*anchor)
    assert b_anchor<F(379,100000)
    beta_lower=root_box_beta_lower()
    print('ANCHOR_B =',str(b_anchor),'BETA_STAR_LOWER =',str(beta_lower))
    # Inherited epsilon_dagger < 0.002181407228; beta* <= b(anchor).
    assert b_anchor+F(2181407228,10**12)<THRESHOLD
    for name,x,y,sign in (
        ('R3_POS',F(9,40),F(31,50),1),
        ('R3_NEG',F(9,40),F(3,5),-1),
    ):
        residuals=residual(x,y)
        bc=b_cost(x,y)
        assert bc<THRESHOLD and bc-beta_lower<F(2181407226,10**12)
        assert residuals[2]>0 and sign*residuals[3]>0
        print(name,'x=',str(x),'y=',str(y),'b=',str(bc),
              'r2=',str(residuals[2]),'r3=',str(residuals[3]))
    print('STAGE330B_GLOBAL_R2_CHAMBER_EXCLUSION_EXACT_PASS')

if __name__=='__main__':
    main()
