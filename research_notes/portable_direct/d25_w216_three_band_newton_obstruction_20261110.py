"""D25 signed W216: exact three-band harmonic decomposition of q1,q2 mod p^3.
Author-side math checker; no native H0/B0 execution or formal admission.
"""
from math import comb

def coefficients(p, n, precision):
    mod = p**precision
    unit, valuation = 1, 0
    for k in range(n):
        residue = unit*pow(p,valuation,mod)%mod if valuation < precision else 0
        yield k, residue, valuation
        if k+1 == n:
            break
        numerator, net = 1, 0
        for factor in (2*k+1,2*k+2,3*k+1,3*k+2,3*k+3):
            while factor % p == 0:
                factor //= p
                net += 1
            numerator = numerator*factor % mod
        den = k+1
        while den%p == 0:
            den //= p
            net -= 5
        valuation += net
        assert valuation >= 0
        unit = unit*numerator*pow(216*pow(den,5,mod),-1,mod)%mod

def signed_firstjet(p):
    assert p>=7 and p%6==1
    m=(p-1)//6
    mod=p**3
    arr=list(coefficients(p,p,3))
    lin=[0,0,0]
    quad=[0,0,0]
    H=[0]*(3*p)
    K=[0]*(3*p)
    for j in range(1,3*p):
        if j%p:
            H[j]=(H[j-1]+pow(j,-1,p*p))%(p*p)
            K[j]=(K[j-1]+pow(j,-2,p))%p
        else:
            H[j]=H[j-1]
            K[j]=K[j-1]
    d=pow(pow(216,p-1,mod),-1,mod)
    t=(d-1)%mod
    logd=(t-t*t*pow(2,-1,mod))%mod
    assert logd%p==0
    ell=logd//p
    for b,A,v in arr:
        if v>=3:
            continue
        assert (v==0 and b<=2*m) or (v==1 and 2*m<b<=3*m) or (v==2 and 3*m<b<=4*m)
        u=(ell+2*H[2*b]+3*H[3*b]-5*H[b])%(p*p)
        k=(4*K[2*b]+9*K[3*b]-5*K[b])%p
        h=6*b+1
        if v==0:
            one=p*A*(h*u+6)
            two=p*p*A*(h*(u*u-k)*pow(2,-1,p)+6*u)
        elif v==1:
            one=A*(3*h+p*(h*u+6))
            two=A*p*3*(h*u+6)
        else:
            one=A*5*h
            two=A*6*h
        lin[v]=(lin[v]+one)%mod
        quad[v]=(quad[v]+two)%mod
    block=[0]*3
    initial=[]
    for j,A,v in coefficients(p,3*p,3):
        block[j//p]=(block[j//p]+(6*j+1)*A)%mod
        if j<3:
            assert v==0
            initial.append(A)
    C=[block[j]*pow(initial[j],-1,mod)%mod for j in range(3)]
    direct=(C[0],(C[1]-C[0])%mod,(C[2]-2*C[1]+C[0])%mod)
    h1,h2=sum(lin)%mod,sum(quad)%mod
    reduced=(block[0],(h1+h2)%mod,(2*h2)%mod)
    assert direct==reduced,(p,direct,reduced)
    assert all(x%(p*p)==0 for x in quad)
    chi=1 if p%3==1 else -1
    return {"p":p,
            "S0_S1_S2": [x//(p*p) for x in quad],
            "sum_mod_p":h2//(p*p),
            "q0_q1_q2_mod_p3":list(direct),
            "candidate_holds":direct==tuple(x%mod for x in (chi*p,6*chi*p,0)),
            "two_exact_paths_agree":True}

def independent_q2_p4(p):
    """Independent original integer binomial input; modulus p^4, three full blocks."""
    mod=p**4
    inv216=pow(216,-1,mod)
    power=1
    blocks=[0]*3
    a=[None]*3
    for k in range(3*p):
        value=(comb(2*k,k)**2*comb(3*k,k)*power)%mod
        if k<3:
            a[k]=value
        blocks[k//p]=(blocks[k//p]+(6*k+1)*value)%mod
        power=power*inv216%mod
    C=[blocks[j]*pow(a[j],-1,mod)%mod for j in range(3)]
    q2=(C[2]-2*C[1]+C[0])%mod
    return q2

if __name__=="__main__":
    for p in (7,13,19,37,43,73,109,373):
        result=signed_firstjet(p)
        assert result["candidate_holds"] and result["sum_mod_p"]==0
        print("EXACT_BANDS_AND_NEWTON",result)
    for p,expected in ((13,4),(19,18),(373,185)):
        q2=independent_q2_p4(p)
        assert q2==expected*p**3
        print("STRICT_MOD_P4_COUNTERWITNESS",p,q2,expected)
