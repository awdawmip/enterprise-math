#!/usr/bin/env python3
"""Author-only exact D25 weighted 3F2 jet check, NOT native H0/B0."""
from math import comb


def witness(p):
    assert p>=7 and p%6==1
    m=(p-1)//6
    q=p**3
    roots=(3*m,2*m,4*m)
    cs=(pow(2,-1,q),pow(3,-1,q),2*pow(3,-1,q)%q)
    inv2=pow(2,-1,q)
    u=1
    E=J=e=0
    S0=S1=S2=0
    W=0
    bands=[0]*4
    for n in range(p):
        if n:
            i=n-1
            for r,c in zip(roots,cs):
                if i==r:
                    u=u*c%q
                    e+=1
                else:
                    inv=pow(i-r,-1,q)
                    u=u*(i-r)%q
                    x=c*inv%q
                    E=(E+x)%q
                    J=(J-x*x)%q
            u=u*pow(2*n**3,-1,q)%q
        wt=6*n+1
        original=wt*comb(2*n,n)**2*comb(3*n,n)*pow(216,-n,q)%q
        W=(W+original)%q
        calc=wt*pow(p,e,q)*u*(1+p*E+p*p*inv2*(E*E+J))%q
        assert calc==original, (p,n,calc,original)
        assert e==(n>2*m)+(n>3*m)+(n>4*m)
        bands[e]=(bands[e]+original)%q
        v=wt*u%q
        if e==0:
            S0=(S0+v)%q
            S1=(S1+v*E)%q
            S2=(S2+v*inv2*(E*E+J))%q
        elif e==1:
            S1=(S1+v)%q
            S2=(S2+v*E)%q
        elif e==2:
            S2=(S2+v)%q
        else:
            assert original==0
    assert W==(S0+p*S1+p*p*S2)%q
    assert W==sum(bands)%q and bands[3]==0
    assert (S0+p*S1-p)%p**2==0
    carry=((S0+p*S1-p)%q)//p**2
    return {"p":p,"m":m,"W":W,"band_sums":bands,
            "p2_carry":carry,"S2_mod_p":S2%p,
            "Delta_minus_R":(carry+S2)%p}


if __name__=="__main__":
    for p in [13,19,37,43,211,373]:
        print(witness(p))
