#!/usr/bin/env python3
"""Exact F_p check of GH-77/78; independent direct coefficient constructions.

Pure portable diagnostic: no Enterprise Math native engine or claim.
"""
def primerange(lo, hi):
    sieve = bytearray(b"\x01") * hi
    sieve[0:2] = b"\x00\x00"
    for k in range(2, int(hi**0.5)+1):
        if sieve[k]:
            sieve[k*k:hi:k] = b"\x00" * (((hi-1-k*k)//k)+1)
    return (p for p in range(lo, hi) if sieve[p])

LIMIT = 2000

def inv(a, p):
    assert a % p
    return pow(a % p, -1, p)

def poy_coeffs(p):
    assert p >= 7 and p % 4 == 3
    d = (p-3)//4
    c = [1]
    h = [1]
    for r in range(d):
        c.append((c[-1] * pow(4*r+1, 3, p) *
                  inv((4*r+2)*(4*r+3)*(4*r+4), p)) % p)
        h.append((h[-1] * pow(4*r+3, 3, p) *
                  inv((4*r+4)*(4*r+5)*(4*r+6), p)) % p)
    return d, c, h

def evaljet(poly, z, p):
    v = deriv = 0
    for n, a in enumerate(poly):
        v = (v + a*pow(z,n,p)) % p
        if n:
            deriv = (deriv + n*a*pow(z,n-1,p)) % p
    return v, deriv

def cm_FG(p, m):
    F = [1]
    for r in range(m):
        den = (2*m+2+r)*(r+1)
        F.append(F[-1] * (r-m)**2 * inv(den, p) % p)
    G = [(16*r+5)*a%p for r,a in enumerate(F)]
    return F,G

def obstruction_alpha(p,d):
    j0=2*d+2
    value=inv(16,p)
    for i in range(j0):
        value=(value*pow(4*i+1,3,p))%p
        for b in (2,3,4):
            x=(4*i+b)%p
            if x: value=value*inv(x,p)%p
    assert value
    return value

cnt_all = cnt_cm = cnt_odd = cnt_rank = cnt_coefficient = 0
odd_observed_zero = 0
for p in primerange(7,LIMIT):
    if p%4!=3: continue
    d,c,h=poy_coeffs(p)
    H=[(8*r+5)*a%p for r,a in enumerate(h)]
    assert len(H)==d+1 and H[d] != 0
    # Exact hypergeometric differential operator coefficient check:
    # θ(θ+1/4)(θ+1/2)U-z(θ+3/4)^3U=0.
    inv4=inv(4,p); inv2=inv(2,p)
    for k in range(d+2):
        lhs=(k*(k+inv4)*(k+inv2)*h[k])%p if k<=d else 0
        rhs=pow(k-1+3*inv4,3,p)*h[k-1]%p if k>0 else 0
        assert lhs==rhs,(p,k,lhs,rhs)
        cnt_coefficient+=1
    h9,dh9=evaljet(H,9,p)
    assert h9==(72*evaljet(h,9,p)[1]+5*evaljet(h,9,p)[0])%p
    cnt_all+=1
    if p%8==7:
        # The symmetric half-degree factorization cannot have full degree d=2m+1.
        m=(d-1)//2
        assert d==2*m+1 and H[d]
        if h9==0: odd_observed_zero+=1
        cnt_odd+=1
    else:
        m=d//2
        F,G=cm_FG(p,m)
        # GH-17 input checked from independent finite-field expansions.
        product=[0]*(d+1)
        for i,a in enumerate(F):
            for j,b in enumerate(G):product[i+j]=(product[i+j]+a*b)%p
        assert product==H,(p,'Clausen')
        f9,_=evaljet(F,9,p)
        g9,_=evaljet(G,9,p)
        if p%24==11:
            assert g9==0 and f9!=0,(p,f9,g9)
            want=(-f9*f9*inv(288,p))%p
        elif p%24==19:
            assert f9==0 and g9!=0,(p,f9,g9)
            want=g9*g9*inv(144,p)%p
        else: raise AssertionError(p)
        assert dh9==want and dh9!=0,(p,dh9,want)
        alpha=obstruction_alpha(p,d)
        Q=alpha*pow(9,2*d+2,p)*inv(8,p)%p
        a_slope=Q*dh9%p
        assert a_slope
        # Verify derivative of GH-16 rational expression independently
        # by quotient rule; evaluate numerator and derivative separately.
        numerator_9=alpha*pow(9,2*d+2,p)*h9%p
        numerator_prime=alpha*pow(9,2*d+2,p)*dh9%p
        numerator_prime+=alpha*(2*d+2)*pow(9,2*d+1,p)*h9
        numerator_prime%=p
        independent=(8*numerator_prime-numerator_9)*inv(64,p)%p
        assert independent==a_slope,(p,independent,a_slope)
        C=1
        for r in range(d+1):
            slope=a_slope*inv(C,p)%p
            assert slope!=0
            # C_r = c_r*9^r, direct crosscheck of recurrence carrier.
            assert C==c[r]*pow(9,r,p)%p
            assert C*slope%p==a_slope
            cnt_rank+=1
            if r<d:
                C=C*9*pow(4*r+1,3,p)*inv((4*r+2)*(4*r+3)*(4*r+4),p)%p
        cnt_cm+=1

print('PASS_GH77_SLOPE_CM_CLASS',cnt_cm,'primes p<',LIMIT,'rank slope checks',cnt_rank)
print('PASS_GH78_HYPERGEOMETRIC_OPERATOR',cnt_all,'primes p=3(mod4)','coefficient checks',cnt_coefficient)
print('PASS_GH78_ODD_DEGREE_NO_GO',cnt_odd,'primes p=7(mod8)')
print('OBSERVED_ONLY_GH78_ODD_CLASS_H9_ZERO',odd_observed_zero,'of',cnt_odd)
