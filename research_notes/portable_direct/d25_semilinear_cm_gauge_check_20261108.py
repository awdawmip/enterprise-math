#!/usr/bin/env python3
"""Exact D25 CM semilinear candidate and quartic parity checks.
Not an execution of original E3 native H0/B0, divided-power [X]U or
a certificate of identifying the candidate with geometric Frobenius.
"""
from math import comb

def add(x,y,q): return ((x[0]+y[0])%q,(x[1]+y[1])%q)
def mul(x,y,q): return ((x[0]*y[0]+2*x[1]*y[1])%q,(x[0]*y[1]+x[1]*y[0])%q)
def sig(x,q): return (x[0]%q,-x[1]%q)
def inv(x,p):
    n=(x[0]*x[0]-2*x[1]*x[1])%p
    return (x[0]*pow(n,-1,p)%p,-x[1]*pow(n,-1,p)%p)
def neg(x,p): return (-x[0]%p,-x[1]%p)
def norm(x,p): return mul(x,sig(x,p),p)

def coeff(p):
    Q=p**3
    n=p-1
    c=(2*pow(108,-1,Q)%Q,-pow(108,-1,Q)%Q)
    powers=[(1,0)]
    for j in range(1,(n+2)//3+1):
        powers.append(mul(powers[-1],c,Q))
    a=b=(0,0)
    for j in range(n//3+1):
        z=comb(2*j,j)*comb(n-j,2*j)
        a=add(a,(z*powers[j][0],z*powers[j][1]),Q)
    for j in range(1,(n+2)//3+1):
        z=comb(2*j,j)*comb(n-j+1,2*j-1)*pow(2,-1,Q)
        b=add(b,(z*powers[j][0],z*powers[j][1]),Q)
    assert a[0]%p==a[1]%p==0,(p,a)
    A=(a[0]//p%p,a[1]//p%p)
    beta=(4*pow(72,-1,p)%p,-pow(72,-1,p)%p)
    B=mul(inv(beta,p),(b[0]%p,b[1]%p),p)
    assert mul(A,B,p)==(1,0)
    return A,B,beta

def quartic_delta(p):
    if p%4==1:
        return (pow(pow(2,-1,p),(p-1)//4,p),0)
    # alpha²=s/2: p-1=4h+2.
    return (0,pow(pow(2,-1,p),(p+1)//4,p))

def run(p):
    A,B,beta=coeff(p)
    q=p*p
    u=B
    v=((-p*A[0])%q,(p*A[1])%q)
    # Phi^2=M sigma(M): diagonal v sigma(u), u sigma(v).
    left=mul(v,sig(u,q),q)
    right=mul(u,sig(v,q),q)
    assert left==right==((-p)%q,0),(p,A,B,left,right)
    wrong=(((-p*A[0])%q),(-p*A[1])%q)
    wrong_square=mul(wrong,sig(u,q),q)
    assert wrong_square!=((-p)%q,0),(p,wrong_square)
    d=quartic_delta(p)
    assert mul(d,d,p)==((-1)%p,0)
    nd=norm(d,p)
    expected=(-1%p,0) if p%4==1 else (1,0)
    assert nd==expected
    return {'p':p,'A':A,'B_CM':B,
            'unit_port_u':u,'p_port_over_p':neg(sig(A,p),p),
            'upper_p_port_mod_p2':v,'phi2':left,
            'wrong_phi2':wrong_square,
            'delta':d,'delta_square':mul(d,d,p),
            'delta_sigma_delta':nd}

def is_prime(n):
    return n>=2 and all(n%d for d in range(2,int(n**.5)+1))

if __name__=='__main__':
    for p in (13,19,37,43,61,67,211,373):
        print(run(p))
    target=[p for p in range(13,2001)
            if p%24 in (13,19) and is_prime(p)]
    assert len(target)==77
    for p in target:
        d=quartic_delta(p)
        assert mul(d,d,p)==((-1)%p,0)
        assert norm(d,p)==((p-1 if p%4==1 else 1),0)
    print('PASS_D25_CM_SEMILINEAR_CANDIDATE_8_PRIMES; QUARTIC_77_PRIMES')
