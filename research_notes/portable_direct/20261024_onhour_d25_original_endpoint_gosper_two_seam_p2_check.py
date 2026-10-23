"""D25 original endpoint: exact Gosper and two-seam proof checker.

This is an author-side exact arithmetic verifier, NOT a native benchmark.
"""
from fractions import Fraction as Q
from math import factorial, isqrt

def r_ratio(m, n):
    return Q((4*m+1+2*n)*(3*n+1)*(3*n+2),
             36*(n+1)*(2*m+n+1)*(4*m+n+1))

def kernel(p, n):
    return Q((2*p+1-3*n)*(6*n+2*p+3),
             (3*n+p+2)*(3*n+2*p+1))

def exact(m):
    p=6*m+1
    R=Q(1)
    raw=Q(0)
    defect=Q(0)
    seq=[]
    for n in range(4*m+1):
        raw+=(6*n+2*p-1)*R
        defect+=kernel(p,n)*R
        seq.append(R)
        next_R=R*r_ratio(m,n)
        assert (6*n+2*p-1)*R == -12*(n+1)*next_R+12*n*R+p*kernel(p,n)*R
        R=next_R
    assert raw == -12*(4*m+1)*R+p*defect
    regular=sum((kernel(p,n)*seq[n] for n in range(4*m) if n!=2*m), Q(0))
    two_seams=Q((p+2)*(4*p+1),3*(2*p+1))*(seq[2*m]/p)
    terminal=Q(-8*p*p+14*p-3,4*p-1)*(seq[4*m]/p)
    assert raw/p == regular+two_seams+terminal

def strip(x,p):
    v=0
    while x%p==0:
        x//=p
        v+=1
    return x,v

def primes(limit):
    for p in range(7,limit+1,6):
        if all(p%d for d in range(2,isqrt(p)+1)):
            yield p

def mod_certificate(p):
    assert p%6==1
    m=(p-1)//6
    M=p**3
    unit=1
    val=0
    orig=0
    regular=0
    T2=T4=None
    for n in range(4*m+1):
        assert val==(n>m)
        R=unit*pow(p,val,M)%M
        orig=(orig+(6*n+2*p-1)*R)%M
        if n==2*m:
            T2=unit%(p*p)
        elif n==4*m:
            T4=unit%(p*p)
        else:
            den=(3*n+p+2)*(3*n+2*p+1)
            assert den%p
            num=(2*p+1-3*n)*(6*n+2*p+3)
            regular=(regular+num*pow(den,-1,p*p)*R)%(p*p)
        if n<4*m:
            a=(4*m+1+2*n)*(3*n+1)*(3*n+2)
            b=36*(n+1)*(2*m+n+1)*(4*m+n+1)
            a,va=strip(a,p)
            b,vb=strip(b,p)
            val+=va-vb
            unit=unit*a*pow(b,-1,M)%M
    assert T2 is not None and T4 is not None
    c2=(p+2)*(4*p+1)*pow(3*(2*p+1),-1,p*p)%(p*p)
    c4=(-8*p*p+14*p-3)*pow(4*p-1,-1,p*p)%(p*p)
    K=(regular+c2*T2+c4*T4)%(p*p)
    assert orig%p==0
    assert orig//p%(p*p)==K
    fp=f2=f3=1
    for k in range(1,p):
        fp=fp*k%(p*p)
    for k in range(1,2*m+1):
        f2=f2*k%(p*p)
    for k in range(1,3*m+1):
        f3=f3*k%(p*p)
    A=fp*pow(3,-(p-1),p*p)*pow(f2,-3,p*p)%(p*p)
    G=(-1)**m*f2**3*pow(f3,-2,p*p)%(p*p)
    W=pow(4,p-1,p*p)*f2**3*pow(fp,-1,p*p)%(p*p)
    assert W==G
    target=pow(4*pow(3,-1,p*p),p-1,p*p)
    defect=(A*K-target)%(p*p)
    assert defect==(A*(K-G))%(p*p)
    return p,K,G,defect,T2%p,T4%p

if __name__=="__main__":
    for m in range(1,13):
        exact(m)
    print("EXACT m=1..12 PASS")
    rows=[mod_certificate(p) for p in primes(241)]
    assert len(rows)==25
    print("ORIGINAL EP / TWO-SEAM exact modular matching, 25 primes PASS")
    for row in rows[:8]:
        print(row)
    assert all(row[3]==0 for row in rows)
    print("FINITE author endpoint congruence checks: all 25 have defect 0")
