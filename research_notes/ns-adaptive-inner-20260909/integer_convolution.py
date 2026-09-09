"""Exact integer accumulation for the SAME Q(sqrt(2),i) convection/Leray law.
No projected-output truncation. Conversion to Fraction occurs only at outputs.
"""
from fractions import Fraction as F
from math import lcm
import exact_packets as ep

def integerize(A):
    if not A:return 1,[]
    D=lcm(*(z.denominator for v in A.values() for x in v for z in x))
    rows=[(k,r,m,tuple(tuple(z.numerator*(D//z.denominator) for z in x) for x in v)) for (k,r,m),v in A.items()]
    return D,rows

def ntime(A,B):
    da,aa=integerize(A);db,bb=integerize(B);out={}
    for p,ra,ma,a in aa:
        for q,rb,mb,b in bb:
            k=(p[0]+q[0],p[1]+q[1],p[2]+q[2])
            if k==(0,0,0):continue
            d=tuple(a[0][j]*q[0]+a[1][j]*q[1]+a[2][j]*q[2] for j in range(4))
            if not any(d):continue
            key=(k,ra+rb,ma+mb)
            if key not in out:out[key]=[[0]*4 for _ in range(3)]
            v=out[key];ar,br,ai,bi=d
            for idx,(cr,dr,ci,di) in enumerate(b):
                # -i * dot(a,q) * b; real and imaginary parts over Q(sqrt2)
                z=(ar*ci+2*br*di+ai*cr+2*bi*dr,
                   ar*di+br*ci+ai*dr+bi*cr,
                   -ar*cr-2*br*dr+ai*ci+2*bi*di,
                   -ar*dr-br*cr+ai*di+bi*ci)
                for j in range(4):v[idx][j]+=z[j]
    ans={};den=da*db
    for (k,r,m),v in out.items():
        n=ep.sq(k);dot=tuple(sum(k[i]*v[i][j] for i in range(3)) for j in range(4))
        num=tuple(tuple(n*v[i][j]-k[i]*dot[j] for j in range(4)) for i in range(3))
        if any(any(x) for x in num):ans[k,r,m]=tuple(tuple(F(z,n*den) for z in x) for x in num)
    return ans
