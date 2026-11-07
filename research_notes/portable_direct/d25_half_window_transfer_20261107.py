#!/usr/bin/env python3
"""D25 half-window 216/2304 transfer; exact finite arithmetic, author-side.

Scientific input W/S as frozen in D25. Guo-Zudilin 2019 half/full theorem
is used as an external proved input, not reproved by this program.
"""
from math import isqrt


def primes_below(bound):
    sieve = bytearray(b'\x01') * bound
    sieve[0:2] = b'\x00\x00'
    for d in range(2, isqrt(bound-1)+1):
        if sieve[d]:
            sieve[d*d::d] = b'\x00'*len(sieve[d*d::d])
    return [p for p in range(5,bound) if sieve[p]]


def factorial_units(p):
    fac = [1]*p
    for k in range(1,p):
        fac[k] = fac[k-1]*k % p
    invfac = [1]*p
    invfac[p-1] = pow(fac[p-1], -1, p)
    for k in range(p-1,0,-1):
        invfac[k-1] = invfac[k]*k % p
    return fac, invfac


def both_tail_certificates(p):
    """Wilson normalized W tail and S tail in F_p; separate labelled ports."""
    fac,invfac = factorial_units(p)
    inv216, inv2304 = pow(216,-1,p),pow(2304,-1,p)
    wpow,spow=1,1
    cports=[]; hports=[]
    lo=(p+1)//2
    hiW=(2*p-1)//3
    hiS=(3*p-1)//4
    for k in range(hiS+1):
        if lo<=k<=hiW:
            c = (6*k+1)*fac[2*k-p]*fac[3*k-p]*wpow*pow(invfac[k],5,p)%p
            cports.append((k,c))
        if lo<=k<=hiS:
            h = 2*(8*k+1)*fac[4*k-2*p]*spow*pow(invfac[k],4,p)%p
            hports.append((k,h))
        wpow=wpow*inv216%p
        spow=spow*inv2304%p
    return sum(c for _,c in cports)%p, sum(h for _,h in hports)%p,cports,hports


def shifted_6m1_tail(p):
    """Independent shifted truncated 4F3 trace, valid p = 6m+1."""
    if p%6 != 1:
        raise ValueError('p must be 1 mod 6')
    m=(p-1)//6
    fac=[1]*p
    for t in range(1,3*m+3):
        fac[t]=fac[t-1]*t%p
    base=4*fac[3*m+2]*pow(216,-(3*m+1),p)*pow(fac[3*m+1],-5,p)%p
    h=1; weighted=0
    for j in range(m):
        weighted=(weighted+(3*j+2)*h)%p
        if j+1<m:
            # Ratio: ((j+1)(6j+5)(6j+7))/(9(2j+3)^3)
            h=h*(j+1)*(6*j+5)*(6*j+7)*pow(9*(2*j+3)**3,-1,p)%p
    return base*pow(2,-1,p)*weighted%p


def direct_modular_tail(p):
    """Independent all-index modular coefficient recursion, retaining bands."""
    mod=p**3; a=b=1
    wtail=stail=0
    wlow=slow=0
    for k in range(p):
        wa=(6*k+1)*a%mod; sb=(8*k+1)*b%mod
        if k<=(p-1)//2:
            wlow=(wlow+wa)%mod; slow=(slow+sb)%mod
        else:
            wtail=(wtail+wa)%mod; stail=(stail+sb)%mod
        if k+1<p:
            a=a*(2*k+1)*(3*k+1)*(3*k+2)*pow(36*(k+1)**3,-1,mod)%mod
            b=b*(4*k+1)*(4*k+3)*(2*k+1)*pow(288*(k+1)**3,-1,mod)%mod
    return wlow,slow,wtail,stail



def hypergeometric_ode_boundary(p):
    """Exact truncated 4F3 ODE L T = -p*unit*z^m, checked mod p^2.

    T=sum_{j=0}^{m-1} h_j z^j;
    h_j=(1)_j(5/6)_j(7/6)_j / (3/2)_j^3.
    L=theta(theta+1/2)^3-z(theta+1)^2(theta+5/6)(theta+7/6).
    """
    m=(p-1)//6; M=p*p; inv6=pow(6,-1,M); inv2=pow(2,-1,M)
    hs=[1]
    for j in range(m-1):
        hs.append(hs[-1]*2*(j+1)*(6*j+5)*(6*j+7)
                  *pow(9*(2*j+3)**3,-1,M)%M)
    coeffs=[]
    for j in range(m):
        left=j*pow(j+inv2,3,M)*hs[j]
        right=0 if j==0 else j*j*(j-1+5*inv6)*(j-1+7*inv6)*hs[j-1]
        coeffs.append((left-right)%M)
    assert all(c==0 for c in coeffs), (p,coeffs)
    defect=(-m*m*(m-inv6)*(m+inv6)*hs[-1])%M
    assert defect%p==0 and (defect//p)%p!=0, (p,defect)
    assert defect//p%p==hs[-1]*pow(648,-1,p)%p, (p,defect,hs[-1])
    return hs[-1]%p,(defect//p)%p



def shifted_B_tail_and_ode(p):
    """Shifted 2304 high-band 4F3, differential readout root and ODE defect."""
    if p<=5:
        raise ValueError('requires p>=7')
    n=(p+1)//4; k0=(p+1)//2
    M=p*p; inv4=pow(4,-1,M); inv2=pow(2,-1,M)
    fac=1
    for k in range(1,k0+1):fac=fac*k%p
    base=20*pow(2304,-k0,p)*pow(fac,-4,p)%p
    assert base!=0
    hmod=1; tmod=1; rootsum=0
    for j in range(n):
        rootsum=(rootsum+(8*j+5)*tmod)%p
        if j+1<n:
            tmod=tmod*(j+1)*(4*j+3)*(4*j+5)*pow(18*(2*j+3)**3,-1,p)%p
    root=rootsum*pow(5,-1,p)%p
    # The Guo-Zudilin theorem implies the readout vanishes at z=1/9.
    assert root==0, (p,root)
    hs=[1]
    for j in range(n-1):
        hs.append(hs[-1]*(j+1)*(4*j+3)*(4*j+5)
                  *pow(2*(2*j+3)**3,-1,M)%M)
    for j in range(n):
        left=j*pow(j+inv2,3,M)*hs[j]
        right=0 if j==0 else j*j*(j-1+3*inv4)*(j-1+5*inv4)*hs[j-1]
        assert (left-right)%M==0,(p,j)
    defect=(-n*n*(n-inv4)*(n+inv4)*hs[-1])%M
    assert defect%p==0 and defect//p%p!=0
    sign=1 if p%4==1 else -1
    assert defect//p%p == sign*hs[-1]*pow(128,-1,p)%p,(p,defect,hs[-1])
    return root,base*root%p,hs[-1]%p,defect//p%p


def main():
    sample=(5,7,11,13,19,31,37,43,109,181,373)
    for p in sample:
        c,h,cp,hp=both_tail_certificates(p)
        loww,lows,wt,st=direct_modular_tail(p)
        assert wt%p**2==0 and st%p**2==0
        assert wt//p**2==c and st//p**2==h
        assert h==0
        if p>=7:
            root, norm, _, _ = shifted_B_tail_and_ode(p)
            assert norm==h
        if p%6==1:
            assert c==shifted_6m1_tail(p)
        if p in (7,13,19,181,373):
            print('PORT',p,'W_tail/p2',c,'S_tail/p2',h,
                  'low_transfer/p2',((loww-lows)%(p**3))//p**2,
                  'W_tail_ports',len(cp),'S_tail_ports',len(hp),
                  'W-S mod p3',(loww+wt-lows-st)%(p**3))
    print('11/11 independent direct p^3 term-recursion/port-factorial checks PASS')

    pp=primes_below(2000)
    assert len(pp)==301
    for p in pp:
        _,h,_,_=both_tail_certificates(p)
        assert h==0,(p,h)
    print('301/301 Wilson high-band cancellation checks PASS (consequence of GZ theorem)')

    pp1=[p for p in primes_below(10000) if p%6==1]
    assert len(pp1)==611
    zeros=[]
    for p in pp1:
        hlead,d=hypergeometric_ode_boundary(p)
        c,h,_,_=both_tail_certificates(p)
        assert h==0,(p,h)
        assert c==shifted_6m1_tail(p),(p,c,shifted_6m1_tail(p))
        if c==0:
            zeros.append(p)
    print('611/611 216-tail shifted 4F3 and p-adic ODE checks PASS',
          'W_tail_zero_count',len(zeros),'zero_primes',zeros)
    ppB=[p for p in primes_below(10000) if p>=7]
    assert len(ppB)==1226
    for p in ppB:
        root,observed,lead,db=shifted_B_tail_and_ode(p)
        assert root==0 and observed==0
    print('1226/1226 shifted 2304 polynomial ODE and zero derivative readout checks PASS')
    for p in (7,13,19,109,373,1093,3511):
        hlead,d=hypergeometric_ode_boundary(p)
        br,bv,bh,bd=shifted_B_tail_and_ode(p)
        print('ODE_BOUNDARY',p,'W_lead',hlead,'W_defect_over_p',d,'S_lead',bh,'S_defect_over_p',bd)
    print('AUTHOR_FINITE_VERIFIED, UNREVIEWED, NOT_ADMITTED')

if __name__=='__main__':
    main()
