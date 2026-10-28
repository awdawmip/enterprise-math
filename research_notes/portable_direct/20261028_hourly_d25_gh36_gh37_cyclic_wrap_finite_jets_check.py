#!/usr/bin/env python3
"""Exact F_p checks for GH-36 cyclic return band and GH-37 finite Laurent jets.
Only standard-library arithmetic. Computational checks are not universal proofs.
"""
from math import isqrt


def primes(bound):
    return [p for p in range(7, bound) if p % 4 == 3 and all(p % k for k in range(2, isqrt(p)+1))]


def iv(a,p):
    a %= p
    assert a, (a,p)
    return pow(a,-1,p)


def direct_jet(p,z,r):
    """Complete ungrouped cyclic rational sum at x=r+epsilon: x^-2,-1,0.
    A product factor with zero residue contributes its known epsilon valuation.
    """
    z%=p
    assert z not in (0,1)
    a=b=h=0
    v,u,l,eta=0,1,0,0
    for j in range(p):
        fj=(8*(r+j)+1)%p
        if v==0:
            h=(h+fj*u)%p
        elif v==-1:
            b=(b+fj*u)%p
            h=(h+u*(fj*l+8))%p
        elif v==-2:
            a=(a+fj*u)%p
            b=(b+u*(fj*l+8))%p
            h=(h+u*(fj*(l*l+eta)*iv(2,p)+8*l))%p
        elif v>0:
            pass
        else:
            raise AssertionError((p,z,r,j,v))
        if j==p-1: break
        x=r+j
        n=(4*x+1)%p
        ds=[(4*x+i)%p for i in (2,3,4)]
        v+= 3*(n==0)-sum(e==0 for e in ds)
        u=u*z*(64 if n==0 else n**3)%p
        for e in ds: u=u*iv(4 if e==0 else e,p)%p
        if n:
            l=(l+12*iv(n,p))%p
            eta=(eta-48*iv(n*n,p))%p
        for e in ds:
            if e:
                l=(l-4*iv(e,p))%p
                eta=(eta+16*iv(e*e,p))%p
    scale=iv(z-1,p)
    return tuple(x*scale%p for x in (a,b,h))


def direct_wrap_jet(p,z,r):
    """Ungrouped *original-shift* late terms j=p-r,...,p-1.
    Deliberately does not use the cyclic t_(r+j-p)/t_r identity.
    """
    if r==0: return (0,0)
    v,u,l,eta=0,1,0,0
    w0=w1=0
    for j in range(p):
        if j>=p-r:
            assert v==0, (p,z,r,j,v)
            fj=(8*(r+j)+1)%p
            w0=(w0+fj*u)%p
            w1=(w1+u*(fj*l+8))%p
        if j==p-1: break
        x=r+j
        n=(4*x+1)%p
        ds=[(4*x+i)%p for i in (2,3,4)]
        v+=3*(n==0)-sum(e==0 for e in ds)
        u=u*z*(64 if n==0 else n**3)%p
        for e in ds:u=u*iv(4 if e==0 else e,p)%p
        if n:
            l=(l+12*iv(n,p))%p
            eta=(eta-48*iv(n*n,p))%p
        for e in ds:
            if e:
                l=(l-4*iv(e,p))%p
                eta=(eta+16*iv(e*e,p))%p
    return w0,w1


def bands(p,z):
    """Independent source-index band formulas from GH-35, extended to finite jets."""
    d=(p-3)//4
    j0=(p+1)//2
    c=1; ellpref=0; J=0; C=[1]; Lpref=[0]
    T=0; partial_deriv=0
    for r in range(d+1):
        f=8*r+1
        T=(T+f*c)%p
        partial_deriv=(partial_deriv+c*(8+f*ellpref))%p
        if r<d:
            a=4*r+1; den=[4*r+i for i in (2,3,4)]
            ell=12*iv(a,p)-sum(4*iv(t,p) for t in den)
            elldot=-48*iv(a*a,p)+sum(16*iv(t*t,p) for t in den)
            c=c*z*a**3*iv(den[0]*den[1]*den[2],p)%p
            ellpref=(ellpref+ell)%p
            J=(J+elldot)%p
            C.append(c); Lpref.append(ellpref)
    Cd=c; L=ellpref; fd=(8*d+1)%p
    Tminus=(T-fd*Cd)%p
    alpha, lamstar, etastar =1,0,0
    for i in range(j0):
        n=(4*i+1)%p
        assert n
        ds=[(4*i+j)%p for j in (2,3,4)]
        den=1
        for e in ds:den=den*(4 if e==0 else e)%p
        alpha=alpha*n**3*iv(den,p)%p
        lamstar=(lamstar+12*iv(n,p)-sum(4*iv(e,p) for e in ds if e))%p
        etastar=(etastar-48*iv(n*n,p)+sum(16*iv(e*e,p) for e in ds if e))%p
    k,h=1,1
    rho,lam,eta=0,0,0
    one0=oned=two0=twod=0
    Q=H=K=D=0
    for s in range(d+1):
        zs=pow(z,s,p); fk=8*s+3; fh=8*s+5
        one0=(one0+k*zs*(8+fk*(L-6+rho)))%p
        oned=(oned+k*zs*(8+fk*(-6+rho)))%p
        M=(lamstar+lam)%p; N=(etastar+eta)%p
        two0=(two0+h*zs*(8*M+fh*(M*M+N)*iv(2,p)))%p
        Md=(M-L)%p; Nd=(N-J)%p
        twod=(twod+h*zs*(8*Md+fh*(Md*Md+Nd)*iv(2,p)))%p
        Q=(Q+fk*k*zs)%p
        K=(K+h*zs)%p
        H=(H+fh*h*zs)%p
        D=(D+fh*h*lam*zs)%p
        if s<d:
            # First-pole regularized tail
            ak=4*s+2; bk=[4*s+j for j in (3,4,5)]
            rho=(rho+12*iv(ak,p)-sum(4*iv(t,p) for t in bk))%p
            k=k*ak**3*iv(bk[0]*bk[1]*bk[2],p)%p
            # Double-pole regularized tail
            ah=4*s+3; bh=[4*s+j for j in (4,5,6)]
            lam=(lam+12*iv(ah,p)-sum(4*iv(t,p) for t in bh))%p
            eta=(eta-48*iv(ah*ah,p)+sum(16*iv(t*t,p) for t in bh))%p
            h=h*ah**3*iv(bh[0]*bh[1]*bh[2],p)%p
    one0=2*z*Cd*one0%p
    oned=2*z*oned%p
    two0=alpha*pow(z,j0,p)*two0%p
    twod=alpha*pow(z,j0,p)*iv(Cd,p)*twod%p
    # Regular contribution to cyclic sum at r=d includes the WRAPPED return.
    wrapped=z*Tminus*iv(Cd,p)%p
    regular0=T
    regulard=(fd+wrapped)%p
    s=iv(z-1,p)
    H0=(regular0+one0+two0)*s%p
    Hd=(regulard+oned+twod)*s%p
    B1=(2*z*Cd*Q)*s%p
    B2=alpha*pow(z,j0,p)*(lamstar*H+8*K+D)*s%p
    A=alpha*pow(z,j0,p)*H*s%p
    return dict(p=p,z=z,T=T,fd=fd,Cd=Cd,L=L,J=J,H0=H0,Hd=Hd,A=A,
                B=(B1+B2)%p,B1=B1,B2=B2,
                Q=Q,K=K,H=H,D=D,
                one0=one0,oned=oned,two0=two0,twod=twod,
                regular0=regular0,regulard=regulard,wrapped=wrapped,
                Tminus=Tminus,delta_deriv=(partial_deriv-C[d]*(8+fd*L))%p)


def test():
    cases=0; targets=0
    for p in primes(1500):
        d=(p-3)//4
        for z in (2,9):
            if z%p in (0,1):continue
            b=bands(p,z)
            exact0=direct_jet(p,z,0)
            exactd=direct_jet(p,z,d)
            assert exact0==(b['A'],b['B'],b['H0']), (p,z,'rank0',exact0,b)
            assert exactd[2]==b['Hd'], (p,z,'rankd',exactd,b)
            assert exactd[0]*b['Cd']%p==b['A'],(p,z,'rankdA')
            assert (b['Cd']*exactd[1]-b['B']+b['A']*b['L'])%p==0,(p,z,'rankdB')
            assert (b['Cd']*b['oned']-b['one0'])%p == (-b['L']*b['B1']*(z-1))%p,(p,z,'first band')
            assert (b['Cd']*b['twod']-b['two0'])%p == (-b['L']*b['B2']*(z-1)+b['A']*(z-1)*(b['L']**2-b['J'])*iv(2,p))%p,(p,z,'second band')
            assert (b['Cd']*b['regulard']-b['regular0'])%p == ((z-1)*(b['T']-b['fd']*b['Cd']))%p,(p,z,'wrap band')
            assert (b['Cd']*(b['Hd']+b['fd'])-b['H0']+b['B']*b['L']+
                    b['A']*(b['J']-b['L']**2)*iv(2,p)-b['T'])%p==0,(p,z,'GH15')
            # Verify wrapped band's constant and first jet at all true ranks r, using direct t_j coefficients.
            if p<=83:
                C=1;Lr=0; P=0; P1=0
                for r in range(d+1):
                    wrap0=(z*P*iv(C,p))%p
                    wrap1=(z*(P1-Lr*P)*iv(C,p))%p
                    # Check actual late j products at shifted x=r, WITHOUT using wrap identity.
                    assert direct_wrap_jet(p,z,r)==(wrap0,wrap1), (p,z,r,'wrap jet')
                    if r<d:
                        f=8*r+1
                        P=(P+f*C)%p
                        P1=(P1+C*(8+f*Lr))%p
                        Lr=(Lr+12*iv(4*r+1,p)-sum(4*iv(4*r+i,p) for i in (2,3,4)))%p
                        C=C*z*(4*r+1)**3*iv((4*r+2)*(4*r+3)*(4*r+4),p)%p
            if z==9 and p%24==19:
                targets+=1
                assert b['A']==0
            cases+=1
    print('PASS_GH36_GH37_EXACT_JETS',cases,'(p,z) cases; target p=19 mod24',targets)
    for p in (7,11,19,23,43,67):
        b=bands(p,9)
        print('EXACT',p,'T',b['T'],'wrapped',b['wrapped'],
              'H0',b['H0'],'Hd',b['Hd'],'A',b['A'],'B',b['B'],
              'pole_band_diff', ((b['Cd']*(b['oned']+b['twod'])-b['one0']-b['two0'])*iv(9-1,p))%p)


if __name__=='__main__': test()
