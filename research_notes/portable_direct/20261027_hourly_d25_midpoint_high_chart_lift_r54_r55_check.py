"""Author-side exact modular checks for D25 R54/R55.

No floating-point arithmetic and no native H0/B0 execution.
The factorial unit table is valid here because all arguments are < p**2.
"""
from math import gcd

SPECIAL = {139, 199, 277}

def primes_upto(n):
    for v in range(13, n + 1):
        if v % 6 != 1:
            continue
        if all(v % d for d in range(2, int(v**0.5) + 1)):
            yield v

def unit_fact_table(p, modulus, last):
    assert last < p * p
    a = [1] * (last + 1)
    for i in range(1, last + 1):
        x = i // p if i % p == 0 else i
        a[i] = a[i - 1] * x % modulus
    return a

def normalized(kind, k, p, modulus, tbl):
    assert k < p
    if kind == "W":
        weight = 6 * k + 1
        val = 2 * k // p + 3 * k // p
        numerator = weight * tbl[2 * k] * tbl[3 * k]
        denominator = pow(tbl[k], 5, modulus) * pow(216, k, modulus)
    else:
        weight = 8 * k + 1
        val = 4 * k // p
        numerator = weight * tbl[4 * k]
        denominator = pow(tbl[k], 4, modulus) * pow(2304, k, modulus)
    assert weight % p != 0
    assert gcd(denominator, p) == 1
    return val, numerator * pow(denominator, -1, modulus) % modulus

def mod_rat(num, den, modulus):
    assert gcd(den, modulus) == 1
    return num * pow(den, -1, modulus) % modulus

def transitions(k, modulus):
    a = mod_rat((6*k+7)*(2*k+1)*(3*k+1)*(3*k+2),
                36*(6*k+1)*(k+1)**3, modulus)
    b = mod_rat((8*k+9)*(2*k+1)*(4*k+1)*(4*k+3),
                288*(8*k+1)*(k+1)**3, modulus)
    return a, b

def original_sums(p):
    modulus = p**3
    fs = [1] * (4*p)
    for i in range(1, 4*p):
        fs[i] = fs[i-1] * i % modulus
    iw, is_ = pow(216, -1, modulus), pow(2304, -1, modulus)
    pw, ps = 1, 1
    h = (p-1)//2
    W = S = WH = SH = 0
    for k in range(p):
        invf = pow(fs[k], -1, modulus)
        w = ((6*k+1) * fs[2*k] * fs[3*k] * pow(invf,5,modulus) * pw) % modulus
        s = ((8*k+1) * fs[4*k] * pow(invf,4,modulus) * ps) % modulus
        W=(W+w)%modulus; S=(S+s)%modulus
        if k <=h:
            WH=(WH+w)%modulus; SH=(SH+s)%modulus
        pw=pw*iw%modulus; ps=ps*is_%modulus
    return W,S,WH,SH

def check(p):
    h = (p-1)//2
    N = (3*p-1)//4 + 1
    m = p*p
    tbl=unit_fact_table(p,m,4*(N+1))
    wh_v, uh = normalized('W',h,p,m,tbl)
    sh_v, vh = normalized('S',h,p,m,tbl)
    wn_v, wn= normalized('W',N,p,m,tbl)
    sn_v, sn= normalized('S',N,p,m,tbl)
    wn1_v, wn1 = normalized('W',N+1,p,m,tbl)
    sn1_v, sn1 = normalized('S',N+1,p,m,tbl)
    assert (wh_v,sh_v,wn_v,sn_v,wn1_v,sn1_v)==(1,1,3,3,3,3)

    a_h = mod_rat((6*h+7)*(3*h+1)*(3*h+2),36*(6*h+1)*(h+1)**3,m)
    b_h = mod_rat((8*h+9)*(4*h+1)*(4*h+3),288*(8*h+1)*(h+1)**3,m)
    delta = (a_h-b_h)%m
    assert delta%p==mod_rat(7,108,p)
    c=wn*pow(uh,-1,m)%m
    d=sn*pow(vh,-1,m)%m
    c1=wn1*pow(uh,-1,m)%m
    d1=sn1*pow(vh,-1,m)%m
    aN,bN=transitions(N,m)
    assert c*aN %m ==c1 and d*bN %m ==d1

    lam=1 if p in SPECIAL else 0
    determinant=(c*d*(aN-bN))%m
    if lam==1:
        assert determinant%p==0 and determinant%m!=0
    else:
        assert determinant%p!=0
    poly=2688*N**4+6160*N**3+4456*N**2+1166*N+85
    den=288*(N+1)**3*(6*N+1)*(8*N+1)
    dm=p**(lam+1)
    dn=mod_rat((2*N+1)*poly,den,dm)
    assert (dn%p==0)==(lam==1)
    e=(dn//p**lam)%p
    assert e!=0

    # R54 cross-rank midpoint -> high joint-jet chart.
    inv_delta=pow(delta,-1,p)
    T00=(-c*b_h+d*a_h)*inv_delta%p
    T01=(c-d)*inv_delta%p
    T10=(-e*d*a_h)*inv_delta%p
    T11=e*d*inv_delta%p
    det=(T00*T11-T01*T10)%p
    assert det==c*d*e*inv_delta%p and det!=0
    eps=1 if pow(6,(p-1)//2,p)==1 else -1
    assert (uh%p,vh%p)==(4*eps%p,3%p)
    D0=(uh-vh)%p
    D1=(a_h*uh-b_h*vh)%p
    X=(wn-sn)%p
    Y=(e*sn)%p
    assert (T00*D0+T01*D1)%p==X
    assert (T10*D0+T11*D1)%p==Y
    assert det == c*d*e*mod_rat(108,7,p)%p

    # R55 original W/S scalar and complete companion-high cancellation.
    W,S,WH,SH=original_sums(p)
    assert (W-SH)%p==0  # first-digit class-check only
    assert W%p**2==p and WH%p**2==p
    assert S%p**3==p and SH%p**3==p
    assert W%p==0 and S%p==0
    assert (S-SH)%p**3==0
    upper=(W-WH)%p**3
    assert upper%p**2==0
    U=upper//p**2 %p
    A=(W//p)*pow(uh,-1,m)%m
    B=(S//p)*pow(vh,-1,m)%m
    assert A%p==pow(uh,-1,p)
    assert B%p==pow(vh,-1,p)
    assert A%p!=0 and B%p!=0
    # Full W/S scalar on arbitrary normalized free source pair is
    # p*(A*u-B*v). Source-faithful high/half decomposition is checked.
    assert ((WH//p)*pow(uh,-1,m)+p*U*pow(uh,-1,m)-A)%m==0
    assert ((SH//p)*pow(vh,-1,m)-B)%m==0
    if p in SPECIAL:
        # A nonzero free state p*(d,c) has the SAME unmodified
        # high-high pair mod p^2 as the zero state, but not same full-sum
        # scalar mod p^3. Both source labels remain distinguishable in Y.
        u=p*(d%p)
        v=p*(c%p)
        Z0=(c*u-d*v)%m
        Z1=(c1*u-d1*v)%m
        assert Z0==Z1==0
        # Witness also works within unit-amplitude states: choose a base
        # satisfying the full-sum lift, then perturb by the singular fiber.
        base_u = 1
        base_v = A*pow(B,-1,m)%m
        assert base_v%p and (p*(A*base_u-B*base_v))%(p**3)==0
        pert_u=(base_u+u)%m
        pert_v=(base_v+v)%m
        assert pert_u%p and pert_v%p
        assert (c*pert_u-d*pert_v - (c*base_u-d*base_v))%m==0
        assert (c1*pert_u-d1*pert_v - (c1*base_u-d1*base_v))%m==0
        F=(p*(A*pert_u-B*pert_v))%(p**3)
        missing=(A*(d%p)-B*(c%p))%p
        assert missing == -X*pow(uh*vh,-1,p)%p
        assert missing and F == p*p*missing
        return p,h,N,X,Y,det,U,missing,F,('SPECIAL',)
    else:
        # Plain pair has unit determinant: two digits suffice, and
        # one digit cannot suffice for this free-source lift predicate.
        u=p; v=0
        F=(p*(A*u-B*v))%(p**3)
        assert F!=0
        return p,h,N,X,Y,det,U,None,F,('ORDINARY',)

if __name__=='__main__':
    rows=[check(p) for p in primes_upto(997)]
    exceptions=[r for r in rows if r[-1]==('SPECIAL',)]
    assert len(rows)==79 and [r[0] for r in exceptions]==[139,199,277]
    for row in [r for r in rows if r[0] in (13,19,37,139,181,199,277,373)]:
        print(row)
    print('PASS: 79 primes p<1000, chart matrices, full W/S scalar, exact exceptional fiber witnesses')
