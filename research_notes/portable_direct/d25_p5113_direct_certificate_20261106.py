"""Exact independent p=5113 D25 source-line certificate, no Hessian dependency.
Mod p^3 all j! denominators (0<=j<p) are invertible.
"""
import math

def weighted_sum(p, v):
    mod=p**3
    m=(p-1)//6
    s=(2*m,3*m,4*m)
    b=[1,1,1]
    z=1
    total=0
    inv=[0]+[pow(i,-1,mod) for i in range(1,p)]
    half_neg=pow(-2,-1,mod)
    for j in range(p):
        total=(total+(6*j+1)*z*b[0]*b[1]*b[2])%mod
        if j<p-1:
            for i in range(3):
                b[i]=b[i]*(s[i]+p*v[i]-j)*inv[j+1]%mod
            z=z*half_neg%mod
    return total

def verify():
    p=5113
    assert all(p%d for d in range(2,math.isqrt(p)+1))
    v=(-pow(3,-1,p),-pow(2,-1,p),-2*pow(3,-1,p))
    mod=p**3
    base=weighted_sum(p,v)
    assert base==77356458584
    vals={}
    for lam in (1,-1,2,5,17,53):
        current=weighted_sum(p,(v[0]+lam,v[1],v[2]+lam))
        delta=(current-base)%mod
        assert delta%(p*p)==0
        vals[lam]=delta//(p*p)
        print('lambda',lam,'sum',current,'delta_div_p2',vals[lam])
    inv2=pow(2,-1,p)
    k=(vals[1]-vals[-1])*inv2%p
    c=(vals[1]+vals[-1])*inv2%p
    assert (k,c)==(3118,0)
    assert all(vals[lam]==k*lam%p for lam in vals)
    q=(pow(2,p-1,p*p)-1)//p
    assert (q,(-3*q)%p)==(665,k)
    m=(p-1)//6
    s=(2*m,3*m,4*m)
    def port1(u):
        return pow(-2,-1,p*p)*math.prod(s[i]+p*u[i] for i in range(3))%(p*p)
    delta_port=((port1((v[0]+1,v[1],v[2]+1))-port1(v))%(p*p))//p
    assert delta_port==1278
    print('PASS',p,'k',k,'c',c,'q2',q,'U1_source_port',delta_port)
if __name__=='__main__':
    verify()
