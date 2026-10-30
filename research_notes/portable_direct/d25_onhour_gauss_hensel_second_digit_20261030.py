#!/usr/bin/env python3
"""Exact p-local Gauss-Hensel second-digit diagnostic (author-side, NOT native)."""

def is_prime(n):
    if n < 2: return False
    for k in range(2, int(n**0.5)+1):
        if n % k == 0: return False
    return True

def gauss_rows(p, modulus):
    # c_n=(1/6)_n(1/3)_n/(n!)**2, 0<=n<p;
    # all denominator inversions are p-units.
    coeff=[1]
    for n in range(p-1):
        rat=(6*n+1)*(3*n+1)*pow(18*(n+1)**2,-1,modulus)%modulus
        coeff.append(coeff[-1]*rat%modulus)
    return coeff

def eval_poly(coeff, z, modulus):
    v=d1=d2=0
    for c in coeff[::-1]:
        d2=(d2*z+2*d1)%modulus
        d1=(d1*z+v)%modulus
        v=(v*z+c)%modulus
    return v,d1,d2

def reflected_r(p, coeff):
    m=(p-1)//6; inv2=pow(2,-1,p)
    B=[]; zpow=1
    for i in range(m+1):
        B.append(coeff[i]*zpow%p)
        zpow=zpow*inv2%p
    C=[0]*(m+1)
    C[1]=pow(10,-1,p)
    for a in range(1,m):
        C[a+1]=C[a]*36*a*a*pow((6*a+5)*(3*a+2),-1,p)%p
    R=0
    for i in range(1,m+1):
        for a in range(1,i+1):
            R+=2*B[i]*(1+6*(i-a))*C[a]
    return R%p


def original_ab_weighted(p, modulus):
    a=b=1; aw=bw=0
    for n in range(p):
        aw=(aw+(6*n+1)*a)%modulus
        bw=(bw+(8*n+1)*b)%modulus
        if n+1<p:
            u=pow(n+1,-3,modulus)
            a=a*(2*n+1)*(3*n+1)*(3*n+2)*pow(36,-1,modulus)*u%modulus
            b=b*(4*n+1)*(4*n+2)*(4*n+3)*pow(576,-1,modulus)*u%modulus
    return aw,bw

def direct_original_binomial_ab(p):
    from math import comb
    mod=p**3; A=B=0
    base216=pow(216,-1,mod); base2304=pow(2304,-1,mod)
    x=y=1
    for n in range(p):
        A=(A+(6*n+1)*comb(2*n,n)**2*comb(3*n,n)*x)%mod
        B=(B+(8*n+1)*comb(2*n,n)**2*comb(4*n,2*n)*y)%mod
        x=x*base216%mod; y=y*base2304%mod
    return A,B

def verify_one(p, verbose=True):
    assert is_prime(p) and p>3 and p%24 in (13,19)
    M=p**3; z=pow(2,-1,M)
    c=gauss_rows(p,M)
    f,fp,fpp=eval_poly(c,z,M)
    assert f%p==0 and fp%p != 0, ('CM zero not simple',p)
    # The exact p-local truncated hypergeometric differential equation has
    # boundary term -(p-1+1/6)*(p-1+1/3)*c_(p-1)*z^(p-1).
    assert (fpp+fp-pow(9,-1,M)*2*f)%p**2==0, ('ODE check',p)
    R=reflected_r(p,c)
    h=(f//p)%(p*p)
    d24=(6*h*fp-1)%p
    assert d24==0, ('First digit failed',p,d24)
    lift=(6*h*fp+p*(h*h-R)-1)%(p*p)
    assert lift==0, ('LIFT counterexample',p,lift)

    # Genuine Hensel root of G_p modulo p^3: Newton correction twice.
    root=z
    for j in range(2):
        value, deriv, _=eval_poly(c,root,M)
        assert deriv%p!=0
        root=(root-value*pow(deriv,-1,M))%M
    assert eval_poly(c,root,M)[0]==0
    diff=(z-root)%M
    assert diff%p==0
    d=diff//p  # modulo p^2, because z and root are fixed mod p^3.
    t=pow(fp,-2,p*p)
    d_pred=(t*pow(6,-1,p*p)+p*(R*t*pow(6,-1,p)-t*t*pow(54,-1,p)))%(p*p)
    # Residual transport: error in second Hensel digit is a UNIT multiple of
    # the original signed scalar Delta-R, not merely a zero/nonzero equivalence.
    assert (d-d_pred)%p==0
    assert (6*fp*fp*((d-d_pred)%(p*p)//p)-lift//p)%p==0
    # Negative control: alter the observer R by +1 without altering G or d.
    # This is NOT a substitute frozen R; it tests the transport orientation.
    R_alt=(R+1)%p
    d_alt=(t*pow(6,-1,p*p)+p*(R_alt*t*pow(6,-1,p)-t*t*pow(54,-1,p)))%(p*p)
    lift_alt=(6*h*fp+p*(h*h-R_alt)-1)%(p*p)
    assert (d-d_alt)%p==0 and lift_alt%p==0
    assert lift_alt//p==(p-1)
    assert (6*fp*fp*((d-d_alt)%(p*p)//p)-lift_alt//p)%p==0
    assert d==d_pred,(p,d,d_pred)
    reformed=((6*d+4*p*d*d)*fp*fp-1-p*R)%(p*p)
    assert reformed==0,(p,reformed)
    aw,bw=original_ab_weighted(p,M)
    assert bw==p%M,('2304 target',p,bw)
    assert aw==p%M,('216 target',p,aw)
    assert ((aw-p)//p)%(p*p)==lift,('Clausen R alignment',p)
    if p in (13,19,373):
        assert (aw,bw)==direct_original_binomial_ab(p),('raw integer binomial',p)
    if verbose:
        print(f'p={p} mod24={p%24} R={R} Gp/p={h} Gp_prime_mod_p2={fp%(p*p)} root_mod_p3={root} d={d} predicted_d={d_pred} LIFT_residue={lift}')
    return (p,R,h,fp%(p*p),root,d,d_pred)

if __name__=='__main__':
    ps=[p for p in range(13,501) if is_prime(p) and p%24 in (13,19)]
    out=[verify_one(p,p in (13,19,37,43,211,373)) for p in ps]
    print(f'PASS_GAUSS_HENSEL_SECOND_DIGIT: {len(out)} target primes p<501')
