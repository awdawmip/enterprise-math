#!/usr/bin/env python3
"""Author-side exact finite-field regressions for GH-80--GH-82.

This checker is NOT an independent reviewer or native Enterprise Math experiment.
All arithmetic is exact in F_p. No network, floating point or external deps.
"""
from math import comb


def primes_below(limit):
    sieve = bytearray(b'\x01') * limit
    sieve[0:2] = b'\x00\x00'
    for n in range(2, int(limit**0.5) + 1):
        if sieve[n]:
            sieve[n*n:limit:n] = b'\x00' * (((limit-1-n*n)//n)+1)
    return [n for n in range(7, limit) if sieve[n] and n % 8 == 7]


def inv(a, p):
    if a % p == 0:
        raise ArithmeticError(f"division by zero modulo {p}")
    return pow(a % p, -1, p)


def coeff_U(p):
    d = (p-3)//4
    h = [1]
    for r in range(d):
        num = pow(4*r+3, 3, p)
        den = (4*r+4)*(4*r+5)*(4*r+6)
        h.append(h[-1] * num * inv(den,p) % p)
    return h


def coeff_F(p):
    m = (p-7)//8
    c=2*m+3
    f=[1]
    for r in range(m):
        f.append(f[-1]*(m-r)**2*inv((r+1)*(c+r),p)%p)
    return f


def product_square(f,p):
    m=len(f)-1
    r=[0]*(2*m+1)
    for i,ai in enumerate(f):
        for j,aj in enumerate(f):
            r[i+j]=(r[i+j]+ai*aj)%p
    return r


def legendre_W_coeff(p):
    m=(p-7)//8
    n=2*m+1
    # W=z^m P_n(sqrt((z-1)/z))/sqrt((z-1)/z)
    # explicit integer-factorial coefficients for P_n(t)/t
    f=[1]*(2*n+1)
    for k in range(1,len(f)):
        f[k]=f[k-1]*k%p
    finv=[1]*len(f)
    finv[-1]=inv(f[-1],p)
    for k in range(len(f)-2,-1,-1):
        finv[k]=finv[k+1]*(k+1)%p
    inv2n=inv(pow(2,n,p),p)
    poly=[0]*(m+1)
    for j in range(m+1):
        a=( (-1)**(m-j) * f[2*m+2+2*j] * finv[m-j]
            *finv[m+1+j] *finv[2*j+1] *inv2n ) %p
        # a*z^(m-j)*(z-1)^j
        for k in range(j+1):
            powz=m-j+k
            poly[powz]=(poly[powz] + a*comb(j,k)*(-1)**(j-k)) % p
    return poly


def ev_deriv2(a,z,p):
    # f, f', f'' using Horner; second derivative literal (no /2)
    f=df=ddf=0
    for v in reversed(a):
        ddf=(ddf*z+2*df)%p
        df=(df*z+f)%p
        f=(f*z+v)%p
    return f,df,ddf


def legendre_jet(n,t,p):
    if n==0: return (1,0)
    a,b=1,t
    da,db=0,1
    for k in range(1,n):
        one=inv(k+1,p)
        nxt=((2*k+1)*t*b-k*a)*one%p
        nd=((2*k+1)*(b+t*db)-k*da)*one%p
        a,b=b,nxt
        da,db=db,nd
    return b,db


def hasse_jet(p,t):
    N=(p-1)//2
    d=(p-3)//4
    b=(1+t)*inv(8,p)%p
    fac=[1]*(N+1)
    for r in range(1,N+1):fac[r]=fac[r-1]*r%p
    invfac=[1]*(N+1)
    invfac[N]=inv(fac[N],p)
    for r in range(N,0,-1): invfac[r-1]=invfac[r]*r%p
    H=K=dH=0
    bpow=1
    bp_prev=1
    n_inv8=inv(8,p)
    for j in range(d+1):
        hj=fac[N]*invfac[N-2*j]*invfac[j]**2%p
        H=(H+hj*bpow)%p
        K=(K+hj*(N-2*j)*inv(j+1,p)*bpow*b)%p
        if j:
            dH=(dH+hj*j*bp_prev*n_inv8)%p
        bp_prev=bpow
        bpow=bpow*b%p
    return H,K,dH


def run():
    all_primes=primes_below(10000)
    full_poly_primes=primes_below(2000)
    full=0; checks=0; samples=[]; inert=split=0
    for p in all_primes:
        m=(p-7)//8; d=2*m+1
        f=coeff_F(p)
        F,Fp,Fpp=ev_deriv2(f,9,p)
        h=coeff_U(p)
        U,Up,Upp=ev_deriv2(h,9,p)
        Hobs=(72*Up+5*U)%p
        Hd= (72*Upp+13*Up)%p   # (8z U'+5U)' at z=9
        assert Hobs==0, (p,'Hobs',Hobs)
        assert U==(1-9)*F*F%p,(p,'U')
        assert Up == (-F*F+2*(1-9)*F*Fp)%p,(p,'Uprime')
        assert Upp == (-4*F*Fp + (1-9)*2*(Fp*Fp+F*Fpp))%p,(p,'Udoubleprime')

        # For p=7 mod 8, t is in the ground field and t^2=8/9.
        sqrt2=pow(2,(p+1)//4,p)
        assert sqrt2*sqrt2%p==2%p
        t=2*sqrt2*inv(3,p)%p
        assert t*t%p==8*inv(9,p)%p
        P,Pp=legendre_jet(d,t,p)
        D=comb(3*m+2,m)%p
        assert D !=0
        # W=D*F=z^m P_d(t(z))/t(z); at z=9
        rhsF=pow(9,m,p)*P*inv(t,p)%p
        assert D*F%p==rhsF,(p,'Legendre F',D*F%p,rhsF)
        assert Hobs== -pow(D,-2,p)*pow(9,d,p)*P*(t*Pp-P)%p,(p,'Legendre H')

        H,K,dH=hasse_jet(p,t)
        assert H==(-1)**d*P%p,(p,'Hasse')
        assert dH==(-1)**d*Pp%p,(p,'Hasse deriv')
        Kright=(-(1+t)*inv(4,p)*H+(1-t*t)*dH)%p
        assert K==Kright,(p,'K formula')
        # exact Cartier scalar relation from CM endomorphism.
        legendre_char=pow((-6)%p,(p-1)//2,p)
        chi=1 if legendre_char==1 else -1
        assert ((chi+1)*K+(2+t)*inv(4,p)*H)%p==0,(p,'CM Cartier')

        if p%24==23:
            inert+=1
            assert (F,Fp,U,Up)==(0,Fp,0,0) and Fp!=0,(p,'inert double zero')
            assert P==0 and Pp!=0,(p,'inert Hasse')
            assert (Hd+1152*Fp*Fp)%p==0 and Hd!=0,(p,'inert simple Hobs')
            if p==23:
                assert h==[1,10,7,21,19,11],h
                assert (U,Up,Upp,Hd)==(0,0,21,17)
        elif p%24==7:
            split+=1
            assert F!=0 and (t*Pp-P)%p==0,(p,'split')
            assert (72*Fp+7*F)%p==0,(p,'split F jet')
            assert (36*Hd-F*F)%p==0 and Hd!=0,(p,'split Hobs slope')
        else: raise AssertionError((p,'class'))
        checks+=1
        if p in [7,23,31,47,71,79,103,127]:
            samples.append((p,m,F,Fp,U,Up,Upp,Hobs,Hd,P,Pp,H,K))

        if p in full_poly_primes:
            # Independent coefficient origins: GH16 U, Gauss F, Legendre W
            sq=product_square(f,p)
            odd=[((sq[r] if r<len(sq) else 0)-(sq[r-1] if r else 0))%p for r in range(d+1)]
            assert h==odd,(p,'full Clausen',h,odd)
            w=legendre_W_coeff(p)
            assert w == [D*x%p for x in f],(p,'full W',w)
            # complete Hobs coefficient polynomial from both sources
            L=[(8*r+5)*x%p for r,x in enumerate(h)]
            def mul(a,b):
                out=[0]*(len(a)+len(b)-1)
                for i,x in enumerate(a):
                    for j,y in enumerate(b):out[i+j]=(out[i+j]+x*y)%p
                return out
            # factor Hobs=F*(16z(1-z)F'+(5-13z)F)
            k=[0]*(m+2)
            # 16z(1-z)F' + (5-13z)F
            for r in range(m+1):
                k[r]=(k[r]+(5+16*r)*f[r])%p
                k[r+1]=(k[r+1]-(13+16*r)*f[r])%p
            assert L==mul(f,k),(p,'full Hobs factor')
            full+=1
    print('PASS_GH80_ODD_CLAUSEN_AND_LEGENDRE full_polynomial_primes=',full)
    print('PASS_GH81_EXTENDED_CM_CLASSIFICATION exact_primes<10000=',checks,'split=',split,'inert=',inert)
    print('PASS_GH82_SIMPLE_OBSTRUCTION_ZERO verified_primes<10000=',checks)
    print('SAMPLES p,m,F,Fprime,U,Uprime,Udoubleprime,Hobs,Hobsprime,P,Pprime,H,K')
    for sample in samples: print(' ',sample)

if __name__=='__main__':
    run()
