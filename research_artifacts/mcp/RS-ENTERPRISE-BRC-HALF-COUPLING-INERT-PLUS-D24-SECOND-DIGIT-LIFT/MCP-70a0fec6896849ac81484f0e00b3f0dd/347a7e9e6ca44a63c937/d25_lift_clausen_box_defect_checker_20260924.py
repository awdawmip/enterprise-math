#!/usr/bin/env python3
from math import isqrt

def primes_lt(n):
    out=[]
    for x in range(2,n):
        ok=True
        for q in range(2,isqrt(x)+1):
            if x%q==0:
                ok=False; break
        if ok:
            out.append(x)
    return out

def vp_mod_p3_residue(a,p):
    # a is canonical residue mod p^3 of a p-adic integer known to have v<3.
    if a%p:
        return 0
    if a%(p*p):
        return 1
    return 2

def xs_mod(p):
    M=p**3
    x=[1]
    for j in range(p-1):
        num=(6*j+1)*(3*j+1)
        den=36*(j+1)*(j+1)
        x.append(x[-1]*(num%M)*pow(den,-1,M)%M)
    return x

def y_mod(p,m):
    # y_r = 2^(r-1)(r-1)!^2/[18(5/6)_r(2/3)_r], r>=1
    y=[None]*(m+1)
    if m:
        y[1]=pow(10,-1,p)
        for r in range(1,m):
            num=36*r*r
            den=(6*r+5)*(3*r+2)
            y[r+1]=y[r]*(num%p)*pow(den%p,-1,p)%p
    return y

def direct_W(p):
    M=p**3
    a=1
    w=1
    for k in range(p-1):
        # a_{k+1}/a_k for
        # (1/2)_k(1/3)_k(2/3)_k/(k!)^3 * 2^{-k}
        num=(2*k+1)*(3*k+1)*(3*k+2)
        den=36*(k+1)**3
        a=a*(num%M)*pow(den,-1,M)%M
        w=(w+(6*(k+1)+1)*a)%M
    return w

def test_prime(p):
    assert p%6==1
    m=(p-1)//6
    M=p**3
    x=xs_mod(p)
    y=y_mod(p,m)

    # Exact p-adic strata of the Clausen half-series.
    for j in range(p):
        expected = 0 if j<=m else (1 if j<=2*m else 2)
        got=vp_mod_p3_residue(x[j],p)
        if got!=expected:
            return ("x_valuation",j,got,expected)

    # High-tail reflection, normalized after the two forced p factors.
    for r in range(1,m+1):
        high=x[p-r]
        if high%(p*p):
            return ("high_not_p2",r)
        if (high//(p*p))%p != y[r]:
            return ("reflection",r,(high//(p*p))%p,y[r])

    S=sum(x)%M
    D=sum((j*x[j])%M for j in range(p))%M

    # O(m) evaluation of the triangular defect
    # C = sum_{1<=r<=j<=m}(6(j-r)+1)x_j y_r mod p.
    Y0=0
    Y1=0
    C=0
    for j in range(1,m+1):
        Y0=(Y0+y[j])%p
        Y1=(Y1+j*y[j])%p
        C=(C+(x[j]%p)*(((6*j+1)*Y0-6*Y1)%p))%p

    rhs=(S*S+12*S*D-2*(p*p)*C)%M
    W=direct_W(p)
    if rhs!=W:
        return ("clausen_box_defect",rhs,W)

    # This is regression/falsification only, not the proof of LIFT.
    if (W-p)%M:
        return ("lift_regression",W,p)
    return None

def main():
    targets=[p for p in primes_lt(5000) if p%24 in (13,19)]
    failures=[]
    counts={13:0,19:0}
    for p in targets:
        counts[p%24]+=1
        err=test_prime(p)
        if err:
            failures.append((p,err))
    print("targets",len(targets))
    print("classes",counts)
    print("failures",failures)

if __name__=="__main__":
    main()
