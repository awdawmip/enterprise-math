#!/usr/bin/env python3
"""Exact finite-ring D25 diagnostic; NOT an executed native H0/B0 benchmark."""
PRIMES=(13,19,37,43,211,373)
def add(a,b,m):
    return ((a[0]+b[0])%m,(a[1]+b[1])%m)
def mul(a,b,m):
    return ((a[0]*b[0]+2*a[1]*b[1])%m,
            (a[0]*b[1]+a[1]*b[0])%m)
def sigma(a,m):
    return (a[0]%m,-a[1]%m)
def mm(A,B,m):
    return tuple(tuple(add(mul(A[i][0],B[0][j],m),
                           mul(A[i][1],B[1][j],m),m)
                       for j in (0,1)) for i in (0,1))
def red(A,m):
    return tuple(tuple((x[0]%m,x[1]%m) for x in row) for row in A)
def test(p):
    assert p%24 in (13,19) and pow(2,(p-1)//2,p)==p-1
    p2,p3=p*p,p*p*p
    z,o=(0,0),(1,0)
    A0=((z,(p,0)),(o,z))
    A1=((z,(p+p2,0)),(o,z))
    AT=((z,(p,p2)),(o,z))
    mats=(A0,A1,AT)
    assert all(red(A,p2)==red(A0,p2) for A in mats)
    assert red(A0,p)==(((0,0),(0,0)),((1,0),(0,0)))
    vals=[]
    for A in mats:
        sq=mm(A,tuple(tuple(sigma(x,p3) for x in row) for row in A),p3)
        assert red(sq,p2)==(((p,0),z),(z,(p,0)))
        assert all(x[0]%p==x[1]%p==0 for row in sq for x in row)
        vals.append(tuple((sq[i][i][0]//p%p2,sq[i][i][1]//p%p2) for i in (0,1)))
    assert vals==[((1,0),(1,0)),((1+p,0),(1+p,0)),
                  ((1,p),(1,p2-p))]
    return vals
if __name__=="__main__":
    checks=[test(p) for p in PRIMES]
    print("PASS_D25_NATIVE_FROBENIUS_EVEN_RANK_AND_P3_PRECISION_WITNESS",len(checks),"primes")
    print("P373_U_LIFTS_MOD_P2",checks[-1])
    print("NATIVE_H0_B0_EXECUTED",False)
