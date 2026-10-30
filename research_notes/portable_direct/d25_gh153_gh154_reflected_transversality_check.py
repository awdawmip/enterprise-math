#!/usr/bin/env python3
"""Author-side exact prime-field check of GH153: R_p'(9) simple-zero criterion.
Independent reflected-tail h_j coefficients versus Hasse/Picard-Fuchs factorization.
No native D25 experiment or math admission implied.
"""
from math import comb, prod

PRIMES=(11,19,43,59,67,83,107,131,139,163,179,211,227,251,283,307,331,347,379, 3347)

def calc(p):
    assert p % 8 == 3 and p >= 11
    m=(p-3)//8; d=2*m
    D=comb(3*m+1,m)%p
    assert D
    h=1
    terms=[]
    for j in range(d+1):
        n=d+1+j
        terms.append((n,(8*j+5)*h*pow(n,-1,p)%p))
        if j<d:
            h=h*pow(4*j+3,3,p)*pow((4*j+4)*(4*j+5)*(4*j+6),-1,p)%p
    def Rjet(k):
        return sum(c*prod(range(n-k+1,n+1))*pow(9,n-k,p)
                   for n,c in terms if n>=k)%p
    r0,r1,r2=Rjet(0),Rjet(1),Rjet(2)

    h0=(-1)**m*comb(2*m,m)*pow(4,-m,p)%p
    assert h0
    # f(W)=H_p(1/8+sqrt(2)v) with W=v^2, so coefficients are h0*u_k.
    cs=[h0]
    for k in range(m):
        cs.append(cs[-1]*4*(8*k+1)*(8*k+3)*pow((k+1)*(2*k+1),-1,p)%p)
    w0=pow(144,-1,p)
    f=fp=fpp=0
    for k,c in enumerate(cs):
        f=(f+c*pow(w0,k,p))%p
        if k>=1:fp=(fp+k*c*pow(w0,k-1,p))%p
        if k>=2:fpp=(fpp+k*(k-1)*c*pow(w0,k-2,p))%p
    ode=((2*w0-256*w0*w0)*fpp+(1-384*w0)*fp-12*f)%p
    assert ode==0
    K=((1-128*w0)*fp-8*f)%p
    # The global first-order Picard-Fuchs transport law for K.
    kcs=[((k+1)*(cs[k+1] if k+1<len(cs) else 0)
          -(128*k+8)*cs[k])%p for k in range(m+1)]
    for n in range(m+2):
        kn=kcs[n] if n<len(kcs) else 0
        km=kcs[n-1] if n>0 else 0
        cn=cs[n] if n<len(cs) else 0
        cm=cs[n-1] if n>0 else 0
        residual=((2*n+1)*kn-(256*n-144)*km-4*cn+640*cm)%p
        assert residual==0,(p,n,residual)
    Kprime=((1-128*w0)*fpp-136*fp)%p
    factor=pow(9,4*m,p)*pow(8*D*D,-1,p)%p
    Wprime=pow(128*9*9,-1,p)
    predicted_r1=factor*f*K%p
    predicted_r2=(factor*Wprime*(fp*K+f*Kprime))%p if r1==0 else None
    assert predicted_r1==r1,(p,"r1",predicted_r1,r1)
    if r1==0:
        assert predicted_r2==r2,(p,"r2",predicted_r2,r2)
        assert (f==0) != (K==0)
        if K==0:
            assert Kprime==(-288*f)%p
            branch="ORDINARY_K_ZERO"
            r2_closed=(-pow(9,4*m,p)*f*f*pow(288*D*D,-1,p))%p
        else:
            assert f==0 and fp!=0 and K==fp*pow(9,-1,p)%p
            branch="SUPERSINGULAR_F_ZERO"
            r2_closed=pow(9,4*m,p)*fp*fp*pow(864*864*D*D,-1,p)%p
        assert r2==r2_closed and r2!=0,(p,"nontransverse",r2,r2_closed)
    else:
        branch="NONSTATIONARY"
    return p,m,r0,r1,r2,branch,h0,f,fp,K,D,predicted_r1

if __name__=="__main__":
    records=[calc(p) for p in PRIMES]
    for r in records:
        print("P",r[0],"m",r[1],"R(9)",r[2],"R'(9)",r[3],"R''(9)",r[4],"branch",r[5],"h0",r[6],"f0",r[7],"fp0",r[8],"K0",r[9],"D",r[10])
    q=[r for r in records if r[3]==0]
    assert all(r[4]!=0 for r in q)
    p3347=records[-1]
    assert p3347[0]==3347 and p3347[2]==0 and p3347[3]==0 and p3347[5]=="ORDINARY_K_ZERO"
    # Conditional exceptional point z=5 (W=1/160): look for finite examples,
    # not used as proof of the universal multiplicity classification.
    def isprime(p):
        if p<2:return False
        for d in range(2,int(p**0.5)+1):
            if p%d==0:return False
        return True
    exceptional=[]
    tested=0
    for p in range(11,5000,8):
        if not isprime(p):continue
        tested+=1
        m=(p-3)//8
        h0=(-1)**m*comb(2*m,m)*pow(4,-m,p)%p
        w=pow(160,-1,p)
        coeffs=[h0]
        for k in range(m):
            coeffs.append(coeffs[-1]*4*(8*k+1)*(8*k+3)*pow((k+1)*(2*k+1),-1,p)%p)
        fv=fvprime=0
        for c in reversed(coeffs):
            fvprime=(fvprime*w+fv)%p
            fv=(fv*w+c)%p
        kv=((1-128*w)*fvprime-8*fv)%p
        if kv==0:exceptional.append(p)
    assert tested==167,(tested,exceptional)
    print("GH154_Z5_FINITE_SCAN", "primes",tested,"zero_cases",exceptional)
    assert p3347[4]==2331
    print("PASS_GH153_GH154_REFLECTED_TAIL_CRITICAL_MULTIPLICITIES_EXACT",
          "tested_direct_primes",len(records),"stationary",len(q),
          "p3347_second_derivative",p3347[4],"local_double_root_coefficient",
          p3347[4]*pow(2,-1,3347)%3347)
