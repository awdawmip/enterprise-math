#!/usr/bin/env python3
"""Independent exact second-digit re-coalescence checks against stored p³ source evaluator."""
from d25_source_second_jet_lift_20261106 import jets, direct

def verify():
    for p, expected_k, expected_c, lam, expected_local in (
        (13,4,5,7,8),(19,10,10,18,5),(373,134,67,371,187)
    ):
        P=p*p;v=(-pow(3,-1,P),-pow(2,-1,P),-2*pow(3,-1,P))
        delta=(1,0,1);A,H=jets(p)
        val=(A[0]+A[2])%P
        assert val%p==0
        k=(val//p+sum(v[i]*H[i][j]*delta[j] for i in range(3) for j in range(3)))%p
        c=sum(delta[i]*H[i][j]*delta[j] for i in range(3) for j in range(3))*pow(2,-1,p)%p
        assert (k,c)==(expected_k,expected_c)
        assert (k*lam+c*lam*lam)%p==0 and lam%p!=0
        w0=direct(p,v)
        w1=direct(p,tuple(v[i]+lam*delta[i] for i in range(3)))
        assert w0==w1==p
        local=lam*((p-1)//2)*pow(2,-1,p)%p
        assert local==expected_local and local!=0
        print("p",p,"k",k,"c",c,"lambda",lam,"j1_delta_over_p",local)
    print("PASS 3/3: exact p³ scalar re-coalescence with distinct labelled sources")

if __name__=="__main__":verify()
