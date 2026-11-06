"""R583 algebraic all-order correction sign and singularity: exact rational checks."""
from fractions import Fraction
from math import comb

# Power-series arithmetic over Q, truncation to n terms.
def mul(a,b,n):
    out=[Fraction(0) for _ in range(n)]
    for i,x in enumerate(a[:n]):
        for j,y in enumerate(b[:n-i]): out[i+j]+=x*y
    return out

def derivative(a): return [i*a[i] for i in range(1,len(a))]

def inverse(a,n):
    assert a[0]!=0
    out=[Fraction(1,1)/a[0]]
    for m in range(1,n):
        out.append(-sum(a[j]*out[m-j] for j in range(1,min(m+1,len(a))))/a[0])
    return out

N=36
# w=1-sqrt(1-2t) = sum_{n>=1} Catalan_{n-1} * t^n / 2^{n-1} ?
# exact binomial for sqrt expansion, n>=1 coeff = binom(2n,n)/(2^n*(2n-1)).
w=[Fraction(0)] + [Fraction(comb(2*m,m),2**m*(2*m-1)) for m in range(1,N+1)]
assert w[1]==1 and w[2]==Fraction(1,2)
s=[Fraction(1)-w[0]]+[-v for v in w[1:]]
a=[Fraction(1)-w[0]/2]+[-v/2 for v in w[1:]]
q=[Fraction(1)-2*w[0]]+[-2*v for v in w[1:]]
# B=alpha * sqrt(s) /q^(3/2), log B derivative = alpha'/alpha + .5 s'/s -1.5 q'/q.
D=mul(derivative(a),inverse(a,N),N)
Ds=mul(derivative(s),inverse(s,N),N)
Dq=mul(derivative(q),inverse(q,N),N)
bs=[]
for m in range(1,N+1):
    direct=-D[m-1]-Ds[m-1]/2+Fraction(3,2)*Dq[m-1]
    lag=(Fraction(comb(2*m-1,m-1),2**m)
       + Fraction(1,2)*sum(Fraction(comb(m+r-1,r),2**r) for r in range(m))
       - 3*2**(m-1)*sum(Fraction(comb(m+r-1,r),4**r) for r in range(m)))
    assert direct==lag, (m,direct,lag)
    assert lag<0, (m,lag)
    bs.append(lag)
print('b_1..b_12=',[str(x) for x in bs[:12]])
print('b_16=',bs[15], 'b_36 approximate=',float(bs[-1]))
print('normalized b_36 / (8/3)^36=',float(bs[-1]/Fraction(8,3)**N))
print('R583_BM_ALL_ORDER_EXACT_36_PASS')
