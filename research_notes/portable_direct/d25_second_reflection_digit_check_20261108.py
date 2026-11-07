#!/usr/bin/env python3
"""D25 second reflection digit: source-separated, all-exact modular checker."""
from math import comb

def is_prime(p):
    return p > 1 and all(p % d for d in range(2, int(p ** 0.5) + 1))

def check(p):
    assert p >= 13 and p % 24 in (13, 19) and is_prime(p)
    m = (p - 1) // 6
    p2, p3, p4 = p*p, p**3, p**4
    b = [1] * p
    for k in range(p-1):
        b[k+1] = b[k]*(6*k+1)*(3*k+1)*pow(36*(k+1)**2, -1, p4) % p4
    for k in range(p):
        v = int(k > m) + int(k > 2*m)
        assert b[k] % p**v == 0 and b[k] % p**(v+1) != 0, (p,k,v)
    q = [comb(m,i)*comb(2*m,i)*pow(2, -i, p2) % p2 for i in range(m+1)]
    c = [0] * (2*m+1)
    c[1] = pow(10, -1, p2)
    for a in range(1,2*m):
        c[a+1] = c[a]*36*a*a*pow((6*a+5)*(3*a+2),-1,p2) % p2
    assert all((b[i]-q[i])%p==0 for i in range(m+1))
    assert all(((b[p-a]//p2)-c[a])%p==0 for a in range(1,2*m+1))
    d = [0] * (m+1)
    for i in range(1,m+1):
        d[i] = ((b[i]-q[i])%p2)//p
    v = [0] * (2*m+1)
    for a in range(1,2*m+1):
        v[a] = ((b[p-a]//p2-c[a])%p2)//p
    u = {i:(b[i]//p)%p for i in range(m+1,2*m+1)}
    slow = 2*sum((1+6*(i-a))*(d[i]*c[a]+q[i]*v[a])+6*q[i]*c[a]
                 for i in range(1,m+1) for a in range(1,i+1))%p
    smid = 2*sum((1+6*(i-a))*u[i]*c[a]
                 for i in range(m+1,2*m+1) for a in range(1,i+1))%p
    R = 2*sum(q[i]*sum((1+6*(i-a))*c[a] for a in range(1,i+1))
              for i in range(1,m+1))%p2
    # Independent full Clausen cutoff, from b[i] and suffix zeroth/first moments
    suffix = [(0,0)]*(p+1)
    sb = sj = 0
    for j in range(p-1,-1,-1):
        sb = (sb+b[j])%p4
        sj = (sj+j*b[j])%p4
        suffix[j] = (sb,sj)
    Q = sum(b[i]*((6*i+1)*suffix[p-i][0]+6*suffix[p-i][1])
            for i in range(1,p))%p4
    assert Q%p2==0
    correction = ((Q//p2-R)%p2)//p
    assert correction==(slow+smid)%p, (p,correction,slow,smid)
    # Independent weighted hypergeometric flow and first-digit interface
    z = 1
    W = 0
    for k in range(p):
        W = (W+(6*k+1)*z)%p4
        if k < p-1:
            z = z*(2*k+1)*(3*k+1)*(3*k+2)*pow(36*(k+1)**3,-1,p4)%p4
    M = sum(b)%p4
    N = sum(k*b[k] for k in range(p))%p4
    h = (M+12*N)%p4
    assert (M*h-W)%p4==Q
    assert M%p==0 and W%p3==p
    gh = ((M//p)*h)%(p**3)
    assert (gh-1)%p==0
    Delta = ((gh-1)%(p**3))//p
    next_w = ((W-p)%p4)//p3
    next_lift = ((Delta-R)%p2)//p
    assert next_lift==(next_w+correction)%p
    return (p,m,R,Q//p2,slow,smid,correction,next_w,next_lift)

def middle_normalization(p):
    """Compute the new H/K middle port without using any intermediate b coefficients."""
    m = (p-1)//6
    q_m = comb(2*m,m)*pow(2,-m,p)%p
    c = [0]*(2*m+1)
    c[1] = pow(10,-1,p)
    for a in range(1,2*m):
        c[a+1] = c[a]*36*a*a*pow((6*a+5)*(3*a+2),-1,p)%p
    H = [0]*(2*m+1)
    U = V = 0
    for i in range(1,2*m+1):
        U = (U+c[i])%p
        V = (V+i*c[i])%p
        H[i] = ((6*i+1)*U-6*V)%p
    K = 1
    sigma = 0
    for r in range(1,m+1):
        sigma = (sigma+K*H[m+r])%p
        if r<m:
            K = K*3*r*(6*r+1)*pow((6*r+5)**2,-1,p)%p
    smid = q_m*pow(25,-1,p)*sigma%p
    return (p,q_m,sigma,smid)

if __name__ == "__main__":
    primes = [p for p in range(13,2001) if p%24 in (13,19) and is_prime(p)]
    assert len(primes)==77
    rows = [check(p) for p in primes]
    k_rows = [middle_normalization(p) for p in primes]
    assert all(k_rows[i][3]==rows[i][5] for i in range(77))
    for p in (13,19,37,43,67,211,373):
        print(next(row for row in rows if row[0]==p))
    assert all(a[4]!=0 and a[5]!=0 and a[6]!=0 for a in rows)
    print("PASS: 77 frozen-prime exact second reflection, LIFT-2 and normalized K/H middle-port certificates")
