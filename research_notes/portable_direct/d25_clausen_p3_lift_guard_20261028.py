#!/usr/bin/env python3
"""AUTHOR-SIDE exact integer modular guard for D25's Clausen denominator lift.

No native H0/B0 experiment, Source Result, or formal mathematical proof is claimed
by this finite test.  The theorem is in the companion mathematical note.
"""
from math import comb

PRIMES = (7, 13, 19, 31, 37, 43, 61, 67, 73, 211, 373)
TARGET = (13, 19, 37, 43, 61, 67, 211, 373)


def inv(x, modulus):
    return pow(x % modulus, -1, modulus)


def mul_jet(a, b, mod):
    return [(sum(a[j] * b[i-j] for j in range(i+1))) % mod for i in range(3)]


def guard(p):
    assert p > 3 and (p-1)%6==0
    m=(p-1)//6
    M=p**3
    half=inv(2,M)
    third=inv(3,M)
    inv8=inv(8,M)
    H=H2=0
    a_n=1
    E=1
    weighted_A=[]
    Hvals=[]
    G=[1]
    Gj=1
    for j in range(1,m+1):
        Gj=(Gj*(j-1-m)*(j-1-2*m)*inv(j*(2*j-p),M))%M
        G.append(Gj)
    g=sum(G)%M
    gp=sum(j*G[j] for j in range(m+1))%M
    convolution=[sum(G[j]*G[n-j] for j in range(max(0,n-m),min(n,m)+1))%M for n in range(2*m+1)]
    Fsq=(g*g+12*g*gp)%M
    L=sum((6*n+1)*convolution[n] for n in range(2*m+1))%M
    assert Fsq==L
    sumH=0
    sumH2=0
    sumA=0
    for n in range(2*m+1):
        if n:
            a_n=(a_n*(n-1-2*m)*(n-1-3*m)*(n-1-4*m)*inv(2*n**3,M))%M
            E=(E*(2*n*n)*inv((2*n-p)*(n-p),M))%M
            H=(H+inv(n,M))%M
            H2=(H2+inv(n*n,M))%M
        w=(6*n+1)*a_n%M
        weighted_A.append(w)
        Hvals.append((H,H2))
        assert (convolution[n] - a_n*E)%M==0, (p,n,'clausen coefficient')
        Eexp=(1+3*p*half*H + p*p*inv8*(9*H*H+5*H2))%M
        assert E==Eexp, (p,n,'denominator lift')
        sumA=(sumA+w)%M
        sumH=(sumH+w*H)%M
        sumH2=(sumH2+w*(9*H*H+5*H2))%M
    assert (L-sumA-3*p*half*sumH-p*p*inv8*sumH2)%M==0

    # A separate three-factor, s-degree<=2 rising-factorial implementation
    one=(1,0,0)
    x=list(one); y=list(one); z=list(one)
    den=1
    J=[0,0,0]
    ports=[0,0,0]
    for n in range(p):
        if n:
            j=n-1
            x=mul_jet(x, [(j-3*m)%M,half,0],M)
            y=mul_jet(y, [(j-2*m)%M,third,0],M)
            z=mul_jet(z, [(j-4*m)%M,(2*third)%M,0],M)
            den=(den*2*n**3)%M
        prod=mul_jet(mul_jet(x,y,M),z,M)
        factor=((6*n+1)*inv(den,M))%M
        term=[(factor*v)%M for v in prod]
        for i in range(3): J[i]=(J[i]+term[i])%M
        if n<=2*m:
            assert term[0]==weighted_A[n]
        elif n<=3*m:
            assert term[0]==0
        elif n<=4*m:
            assert term[0]==term[1]==0
            ports[2]=(ports[2]+term[2])%M
        else:
            assert term==[0,0,0]
    J0,J1,J2=J
    assert J0==sumA

    # Third independent calculation: the original (2n choose n)^2*(3n choose n)/216^n
    original=0
    for n in range(p):
        t=(comb(2*n,n)**2*comb(3*n,n))%M
        w=(6*n+1)*t*inv(pow(216,n,M),M)%M
        original=(original+w)%M
    assert original==(J0+p*J1+p*p*J2)%M

    D1=(J1-3*half*sumH)%M
    D2=(J2-inv8*sumH2)%M
    assert original==(Fsq+p*D1+p*p*D2)%M

    A_1=sum(comb(m,j)*comb(2*m,j)*inv(pow(2,j,M),M) for j in range(m+1))%M
    assert (g-A_1)%p==0
    # Distinguish the *actual* terminating Clausen A_m(z) from the rational
    # Legendre polynomial transport P_{2m}(sqrt(1-z/2)).  They coincide only mod p.
    old=[1]; leg=[1]; B=[0]; harmonic_2m_tail=0
    for j in range(1,m+1):
        old.append(old[-1]*(j-1-m)*(j-1-2*m)*inv(2*j*j,M)%M)
        leg.append(leg[-1]*(j-1-m)*(2*m+2*j-1)*inv(4*j*j,M)%M)
        harmonic_2m_tail=(harmonic_2m_tail+inv(2*m-j+1,M))%M
        B.append(-old[j]*harmonic_2m_tail%M)
        assert (leg[j]-old[j]-(p*half*B[j]))%p**2==0
    assert (sum(old)-A_1)%M==0
    def moment(coeff):
        c=[sum(coeff[j]*coeff[n-j]
               for j in range(max(0,n-m), min(n,m)+1))%M
           for n in range(2*m+1)]
        f=[(6*n+1)*c[n]%M for n in range(2*m+1)]
        tail=0
        q=[0]*(2*m)
        for n in range(2*m,0,-1):
            tail=(tail+f[n])%M
            q[n-1]=tail
        u=1; val=0
        for s in range(2*m):
            val=(val+q[s]*u)%M
            u=u*(4*(s+1))*inv(2*s+3,M)%M
        return val
    IA=moment(old); IP=moment(leg)
    # The first-order A(z)*B(z) repair under the *same finite moment*.
    product=[sum(old[j]*B[n-j]
                  for j in range(max(0,n-m), min(n,m)+1))%M
             for n in range(2*m+1)]
    V=[(6*n+1)*product[n]%M for n in range(2*m+1)]
    T=0; qs=[0]*(2*m)
    for n in range(2*m,0,-1):
        T=(T+V[n])%M;qs[n-1]=T
    u=1; transport=0
    for s in range(2*m):
        transport=(transport+qs[s]*u)%M
        u=u*4*(s+1)*inv(2*s+3,M)%M
    assert (IP-IA-p*transport)%(p*p)==0
    if p in TARGET:
        assert g%p==0
        gamma=(g//p)%(p*p)
        assert IA%p==IP%p==6%p
        IA6=IA*inv(6,p*p)%(p*p)
        IP6=IP*inv(6,p*p)%(p*p)
        bridgeA=(original//p-IA6)%(p*p)
        bridgeP=(original//p-IP6)%(p*p)
        assert (bridgeA - (12*gamma*gp+D1+p*(gamma**2+D2)-IA6))%(p*p)==0
        assert (bridgeP-bridgeA+p*transport*inv(6,p*p))%(p*p)==0
        assert bridgeA%p==bridgeP%p==0
    else: bridgeA=bridgeP=None
    result={
        'p':p,'m':m,'g':g,'gp':gp,'A1':A_1,
        'Fsq':Fsq,'J0':J0,'J1':J1%p**2,'J2':J2%p,
        'sumH':sumH%p**2,'sumH2':sumH2%p,
        'D1':D1%p**2,'D2':D2%p,'W':original,
        'I_A':IA%p**2,'I_P':IP%p**2,'Legendre_transport':transport%p,
    }
    if p in TARGET:
        assert g%p==0, (p, g, 'CM0')
        assert original%p**2==p, (p, original,'target first digit')
        gamma=(g//p)%p**2
        U=(12*gamma*gp+D1+p*(gamma*gamma+D2))%(p*p)
        assert (original//p)%(p*p)==U
        result.update(gamma=gamma, U=U, second_digit=((U-1)//p)%p,
                      bridgeA_digit=bridgeA//p,bridgeP_digit=bridgeP//p)
    return result


def main():
    out=[guard(p) for p in PRIMES]
    for r in out: print(r)
    p373=next(r for r in out if r['p']==373)
    assert (p373['J0'],p373['J1'],p373['J2'])==(15521276,47909,133)
    assert p373['W']==373
    assert (p373['I_A'],p373['I_P'],p373['Legendre_transport']) == (77590,122350,120)
    assert (p373['bridgeA_digit'],p373['bridgeP_digit'])==(373-159,373-179)
    print('PASS_D25_CLAUSEN_DENOMINATOR_P3_SOURCE_BANDED_BRIDGE',len(out),'primes')


if __name__=='__main__': main()
