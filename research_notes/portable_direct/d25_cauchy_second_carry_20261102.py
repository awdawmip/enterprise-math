#!/usr/bin/env python3
"""Exact second-carry J_0/J_1 theorem, original A_m and B_j coefficients.
Portable author-side integer checks; not an EM-native experiment/admission.
"""
from math import isqrt, comb

def primes(n):
    sieve=bytearray(b'\x01')*(n+1);sieve[:2]=b'\x00\x00'
    for d in range(2,isqrt(n)+1):
        if sieve[d]: sieve[d*d::d]=b'\x00'*(((n-d*d)//d)+1)
    return [p for p in range(7,n+1) if sieve[p] and p%6==1]

def case(p):
    assert p>=7 and p%6==1
    r=(p-1)//6; D=p**3; Q=p*p
    A=[1]*p; B=[1]*p
    inv36=pow(36,-1,D); inv4=pow(4,-1,D)
    for m in range(1,p):
        invm=pow(m,-1,D)
        A[m]=A[m-1]*(2*m-1)*(3*m-2)*(3*m-1)*inv36*pow(invm,3,D)%D
        B[m]=B[m-1]*(2*m-1)*inv4*invm%D
    # Full Cauchy rectangle minus low triangle: exact J0,J1 mod p^3.
    prefB=[0]*(p+1);prefJB=[0]*(p+1)
    for j in range(p):
        prefB[j+1]=(prefB[j]+B[j])%D
        prefJB[j+1]=(prefJB[j]+j*B[j])%D
    J0=J1=0
    for m in range(1,p):
        L=p-m
        Bsum=(prefB[p]-prefB[L])%D
        BJsum=(prefJB[p]-prefJB[L])%D
        J0=(J0+A[m]*Bsum)%D
        J1=(J1+A[m]*(m*Bsum+BJsum))%D
    # Reflection second lift: B_{p-s}/p = U_s(1+p h_s) mod p^2.
    Hp=[0]*p
    for s in range(1,p): Hp[s]=(Hp[s-1]+pow(s,-1,p))%p
    qp8=(pow(8,p-1,Q)-1)//p
    u0=u1=0; uh0=uh1=0
    K0=K1=0; V0=V1=0; M0=M1=0
    for s in range(1,3*r+1):
        u=-pow(4*s*B[s],-1,Q)%Q
        h=(2*(Hp[2*s-1]-Hp[s-1])-qp8)%p
        assert B[p-s]%p==0
        assert B[p-s]//p%Q==u*(1+p*h)%Q,(p,s)
        u0=(u0+u)%Q
        u1=(u1+s*u)%Q
        uh0=(uh0+u*h)%p
        uh1=(uh1+s*u*h)%p
        if s<=2*r:
            K0=(K0+A[s]*u0)%Q
            K1=(K1+A[s]*(s*u0-u1))%Q
            V0=(V0+A[s]*uh0)%p
            V1=(V1+A[s]*(s*uh0-uh1))%p
        else:
            assert A[s]%p==0
            a1=A[s]//p%p
            M0=(M0+a1*u0)%p
            M1=(M1+a1*(s*u0-u1))%p
    # Extra low-j stratum: m in (p/2,2p/3], with v_p(A_m)=2, v_p(B_j)=0.
    L0=L1=0
    for m in range(3*r+1,4*r+1):
        assert A[m]%Q==0
        a2=A[m]//Q%p
        Bsum=(prefB[3*r+1]-prefB[p-m])%p
        BJsum=(prefJB[3*r+1]-prefJB[p-m])%p
        L0=(L0+a2*Bsum)%p
        L1=(L1+a2*(m*Bsum+BJsum))%p
    predicted0=(p*K0+Q*(V0+M0+L0))%D
    predicted1=(p*K1+Q*(V1+K0+M1+L1))%D
    assert predicted0==J0,(p,'J0',predicted0,J0)
    assert predicted1==J1,(p,'J1',predicted1,J1)
    return {'p':p,'class':p%24,'K0':K0%p,'K1':K1%p,
            'J0':J0,'J1':J1,'K0_lift':K0,'K1_lift':K1,
            'V0':V0,'V1':V1,'M0':M0,'M1':M1,'L0':L0,'L1':L1,
            'J0_digit2':J0//Q if J0%Q==0 else None,
            'J1_shift2':((2*J1+p)%D)//Q if (2*J1+p)%Q==0 else None}

def independent_binomial_coefficients(p):
    """Independent direct integer binomial check, distinct from the recurrence."""
    D=p**3; A=[1]*p; B=[1]*p
    inv216=pow(216,-1,D);inv8=pow(8,-1,D)
    for m in range(1,p):
        A[m]=comb(2*m,m)**2*comb(3*m,m)*pow(inv216,m,D)%D
        B[m]=comb(2*m,m)*pow(inv8,m,D)%D
    a=[1]*p;b=[1]*p
    inv36=pow(36,-1,D);inv4=pow(4,-1,D)
    for m in range(1,p):
        invm=pow(m,-1,D)
        a[m]=a[m-1]*(2*m-1)*(3*m-2)*(3*m-1)*inv36*pow(invm,3,D)%D
        b[m]=b[m-1]*(2*m-1)*inv4*invm%D
    assert A==a and B==b, p


def main():
    ps=primes(3000)
    for p in (7,13,19,31,37,43,373):independent_binomial_coefficients(p)
    print('independent integer-binomial vs recurrence coefficient reconstruction p=7,13,19,31,37,43,373 PASS')
    for p in ps:
        res=case(p)
        if p%24 in (13,19):
            assert res['K0']==0 and res['K1']==(p-1)//2,(p,res)
            assert res['J0_digit2'] is not None and res['J1_shift2'] is not None
    print('theorem: all p≡1(mod6) primes <=3000:',len(ps),'exact reflection second lift & full second-carry J0/J1 PASS')
    print('target 13/19 classes:',sum(p%24 in (13,19) for p in ps),'finite K conjectures rechecked (not proved)')
    print('p class K0 K1 J0/p^2 (2J1+p)/p^2 V0 V1 M0 M1 L0 L1 [all mod p]')
    for p in (7,13,19,31,37,43,61,73,373,1171):
        if p not in ps:continue
        d=case(p)
        print(*(d[k] for k in ['p','class','K0','K1','J0_digit2','J1_shift2','V0','V1','M0','M1','L0','L1']))
    print('END PASS; integer arithmetic only; no native Source checkpoint / Result claimed')
if __name__=='__main__':main()
