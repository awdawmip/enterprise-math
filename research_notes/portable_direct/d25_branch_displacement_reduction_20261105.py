"""Exact composition check of a branch-displacement certificate against inherited six-port table.
Not an independent recalculation of the six-port itself.
"""
from math import comb
from d25_clausen_one_jet_hensel_20261105 import direct_jets

DATA={13:(130,45,(5,8,10)),19:(351,292,(1,17,9)),373:(3122,44787,(82,158,266))}

def check(p):
    n=(p-1)//6; mod=p**3
    g,v,_,_=direct_jets(p,mod)
    f=g*(g+6*v)%mod
    K=(6*v*v+(8+6*p)*g*v+4*pow(3,-1,mod)*(p-1)**2*g*g)%mod
    branch='G' if g%p==0 else 'L'
    c=(2 if branch=='G' else 10)*pow(3,-1,mod)%mod
    d=f*pow(K,-1,mod)%mod
    x=pow(2,-1,mod); root=(x-d-c*d*d)%mod
    delta=(x-root)%mod
    assert delta%p==0
    mu=delta//p
    harmonic=harmonic2=0; U1=U11=U2=0
    for k in range(2*n+1):
        if k:
            harmonic=(harmonic+pow(k,-1,mod))%mod
            harmonic2=(harmonic2+pow(k,-1,mod)**2)%mod
        w=(6*k+1)*(-1)**k*comb(2*n,k)*comb(3*n,k)*comb(4*n,k)*pow(2,-k,mod)%mod
        U1=(U1+w*harmonic)%mod
        U11=(U11+w*harmonic*harmonic)%mod
        U2=(U2+w*harmonic2)%mod
    alpha=3*pow(2,-1,mod)*U1%mod
    beta=(9*U11+5*U2)*pow(8,-1,mod)%mod
    portA,portB,(portC,portD,portE)=DATA[p]
    F=(portA+portB-alpha)%(p*p)
    H=(portC+portD+portE-beta)%p
    assert (f-K*delta+K*c*delta*delta)%mod==0
    W=(f+p*F+p*p*H)%mod
    assert W==p
    r1=(K*mu+F-1)%p
    h=(K*mu+F-1)%(p*p)
    assert r1==0 and h%p==0
    r2=((h//p)+H-K*c*mu*mu)%p
    assert r2==0
    return {'p':p,'branch':branch,'mu_mod_p':mu%p,'K_mod_p':K%p,
            'F_mod_p2':F,'H_mod_p':H,'stage1':r1,'stage2':r2,'W_mod_p3':W}

if __name__=='__main__':
    for p in DATA: print(check(p))
