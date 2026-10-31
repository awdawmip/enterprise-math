#!/usr/bin/env python3
"""Exact p^3 Clausen parameter-jet/support/boundary guard.

AUTHOR-SIDE / EXACT FINITE CHECK ONLY / UNREVIEWED / NOT_ADMITTED.
Original source 216 and independent full Gauss series compared modulo p^3;
this executable does not prove a universal LIFT or execute native H0/B0.
"""
from math import comb, factorial


def primes_upto(bound):
    ps = []
    for n in range(7, bound):
        if all(n % d for d in range(2, int(n**0.5)+1)):
            ps.append(n)
    return ps


def gauss_jets(p):
    """Coefficients of H_0,H_1,H_2 in formal t, evaluated at z later.
    The coefficient of t^r is from (-ell+t/6)_k(-2ell+t/3)_k/(k!)^2.
    Work modulo p^3. No floating point or division by p.
    """
    ell = (p - 1)//6
    mod = p**3
    inv6, inv3 = pow(6, -1, mod), pow(3, -1, mod)
    jets = [(1, 0, 0)]
    u0,u1,u2 = 1,0,0
    for k in range(1,p):
        r = k-1
        a,c = r-ell, r-2*ell
        # multiplication by the two linear factors, keeping degrees 0,1,2
        v0 = u0*a % mod
        v1 = (u1*a+u0*inv6) % mod
        v2 = (u2*a+u1*inv6) % mod
        u0,u1,u2 = (v0*c)%mod, (v1*c+v0*inv3)%mod, (v2*c+v1*inv3)%mod
        fac=pow(k*k,-1,mod)
        u0,u1,u2=u0*fac%mod,u1*fac%mod,u2*fac%mod
        jets.append((u0,u1,u2))
    return jets


def check(p):
    assert p % 6 == 1 and p >= 7
    mod=p**3
    ell=(p-1)//6
    jets=gauss_jets(p)
    inv2=pow(2,-1,mod)
    zpow=[pow(inv2,k,mod) for k in range(p)]
    # independent coefficients of original infinite Gauss H(z)
    hg=[1]
    for k in range(1,p):
        j=k-1
        hg.append(hg[-1]*(6*j+1)*(3*j+1)*pow(18*k*k,-1,mod)%mod)
    for k,(h0,h1,h2) in enumerate(jets):
        assert (h0+p*h1+p*p*h2)%mod==hg[k], (p,k,'jet')
        if k>ell:
            assert h0 % p == 0, (p,k,'H0support')
        else:
            assert h0%p==comb(ell,k)*comb(2*ell,k)%p
        if k>2*ell:
            assert h1%p==0, (p,k,'H1support')
            # independent cross-wall second-jet coefficient
            wk=(-1)**ell * factorial(ell)*factorial(2*ell)*factorial(k-ell-1)*factorial(k-2*ell-1)
            wk=wk * pow(18*factorial(k)**2,-1,p)%p
            assert wk==h2%p, (p,k,'H2crosswall')
    # Independently original 216 hypergeom coeff via integral binomials
    original=[]
    for n in range(p):
        original.append(comb(2*n,n)**2*comb(3*n,n)*pow(216,-n,mod)%mod)
    # Clausen double convolution coefficientwise, n<p, no q-series assumption in code
    for n in range(p):
        coeff=sum(hg[i]*hg[n-i] for i in range(n+1))%mod
        assert coeff== original[n]*pow(2,n,mod)%mod, (p,n,'Clausen')
    A=sum((6*n+1)*original[n] for n in range(p))%mod
    G=sum(hg[k]*zpow[k] for k in range(p))%mod
    J=sum((12*k+1)*hg[k]*zpow[k] for k in range(p))%mod
    Q=(G*J-A)%mod
    assert Q % (p*p)==0, (p,'Qvaluation')
    R=Q//(p*p)
    # Independent jet computed from zero/first/second parameter differentials.
    H0=sum(j[0]*zpow[k] for k,j in enumerate(jets))%mod
    H1=sum(j[1]*zpow[k] for k,j in enumerate(jets))%mod
    H2=sum(j[2]*zpow[k] for k,j in enumerate(jets))%mod
    N0=sum((12*k+1)*j[0]*zpow[k] for k,j in enumerate(jets))%mod
    N1=sum((12*k+1)*j[1]*zpow[k] for k,j in enumerate(jets))%mod
    N2=sum((12*k+1)*j[2]*zpow[k] for k,j in enumerate(jets))%mod
    assert (H0+p*H1+p*p*H2)%mod==G
    assert (N0+p*N1+p*p*N2)%mod==J
    # All overdegree tails of H_0^2,H_0H_1,H_1^2 vanish; H0 H2 is the unique one.
    for n in range(p,2*p-1):
        # calculate all selected convolution terms for overdegree
        s00=s01=s11=s02=0
        for i in range(max(0,n-p+1),min(p-1,n)+1):
            j=n-i
            if 0<=j<p:
                s00 += jets[i][0]*jets[j][0]
                s01 += jets[i][0]*jets[j][1]
                s11 += jets[i][1]*jets[j][1]
                s02 += jets[i][0]*jets[j][2]
        assert s00%p==s01%p==s11%p==0, (p,n,'overdegree')
    B=0
    for i in range(1,ell+1):
        for a in range(1,i+1):
            k=p-a
            B += 2*(1+6*(i-a))*jets[i][0]*jets[k][2]*zpow[i]*zpow[k]
    B%=p
    assert B==R, (p,B,R,'boundaryR')
    # Crosscheck frozen R recurrence, independently of jets
    gmod=[hg[k]*zpow[k]%p for k in range(p)]
    c=[0,pow(10,-1,p)]
    for a in range(1,ell):
        c.append(c[-1]*36*a*a*pow((6*a+5)*(3*a+2),-1,p)%p)
    R_frozen=sum(2*gmod[i]*sum((1+6*(i-a))*c[a] for a in range(1,i+1)) for i in range(1,ell+1))%p
    assert R==R_frozen, (p,'Rref',R,R_frozen)
    for a in range(1,ell+1):
        assert jets[p-a][2]*zpow[p-a]%p == c[a], (p,a,'frozen c')
    # Additional source-faithful three-jet + one boundary identity through p^3
    assert A == (G*J-p*p*B)%mod, (p,'A jet identity')
    if p%24 in (13,19):
        assert G%p==0, (p,'G factor')
        assert (G*J)% (p*p)==p, (p,'first-digit UR')
        # The second-digit residual: carry/first-and-second derivatives - boundary.
        # Express only units of p: L0=(H0/p+H1), L1=H2, N0,N1.
        assert H0%p==0, (p,'H0modp')
        L0=((H0//p)+H1) % (p*p)
        assert (L0*N0)%p==1, (p,'L0N0')
        delta_jet=((L0*N0-1)//p + L0*N1+H2*N0)%p
        delta=((G*J//p-1)//p)%p  # GJ is modular p^3; GJ//p valid
        assert delta_jet==delta%p, (p,'jet delta',delta_jet,delta)
        residual=((A-p)%mod)//(p*p)
        assert residual == (delta_jet-B)%p, (p,'joint residue')
    else:
        residual=None
    return (p,ell,R, B, residual)


def main():
    checked=[]
    for p in primes_upto(800):
        if p%6==1:
            checked.append(check(p))
    target=[x for x in checked if x[0]%24 in (13,19)]
    print('all p<800 (p mod6=1):',len(checked),'target p mod24=13/19:',len(target))
    print('anchors:',[x for x in checked if x[0] in (7,13,19,37,43,61,67,373)])
    print('PASS_D25_CLAUSEN_UNIQUE_OVERDEGREE_JET_SIGNED_R_EXACT')

if __name__=='__main__':
    main()
