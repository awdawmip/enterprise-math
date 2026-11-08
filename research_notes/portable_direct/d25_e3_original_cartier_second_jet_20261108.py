#!/usr/bin/env python3
"""Original E3 exact Hasse/Cartier coefficient modulo p^3 and Hesse two-jet.
This computes the SOURCE-SPECIFIC Weierstrass Hasse polynomial, not the
unexecuted fixed H0/B0 divided-power coefficient [X]U.
"""
from math import comb
import json

def add(u,v,q): return ((u[0]+v[0])%q,(u[1]+v[1])%q)
def mul(u,v,q): return ((u[0]*v[0]+2*u[1]*v[1])%q,(u[0]*v[1]+u[1]*v[0])%q)
def scale(u,c,q): return (u[0]*c%q,u[1]*c%q)
def compute(p,independent=True):
    assert p>=5 and all(p%d for d in range(2,int(p**.5)+1))
    n=(p-1)//2; m=(p-1)//3; q=p**3
    c=scale((2,-1),pow(108,-1,q),q)
    A=(0,0);H=(0,0);J=(0,0);K=(0,0)
    pwr=(1,0); an=1
    for k in range(m+1):
        b=comb(n,k)*comb(p-1-2*k,k)*pow(4,k,q)%q
        H=add(H,scale(pwr,b,q),q)
        A=add(A,scale(pwr,an,q),q)
        # The two original index intervals, all denominators p-units.
        den=list(range(1,2*k,2))+list(range(2*k+1,3*k+1))
        s=sum(pow(t,-1,p*p) for t in den)%(p*p)
        inverses=[pow(t,-1,p) for t in den]
        e2=0;acc=0
        for u in inverses:
            e2=(e2+acc*u)%p
            acc=(acc+u)%p
        J=add(J,scale(pwr,an*s,q),q)
        K=add(K,scale(pwr,an*e2,q),q)
        assert (b-an*(1-p*s+p*p*e2))%q==0,('coefficient',p,k)
        if k<m:
            an=an*(3*k+1)*(3*k+2)*(3*k+3)*pow((k+1)**3,-1,q)%q
            pwr=mul(pwr,c,q)
    assert H==add(add(A,scale(J,-p,q),q),scale(K,p*p,q),q)
    assert all(x%p==0 for x in [H[0],H[1],A[0],A[1]])
    if independent:
        # Different algorithm: actual cubic polynomial F=(x+c)^2+4x^3.
        f=[mul(c,c,q),scale(c,2,q),(1,0),(4,0)]
        cur=[(1,0)]
        for stage in range(n):
            nxt=[(0,0)]*(min(3*(stage+1),2*n)+1)
            for i,u in enumerate(cur):
                if u==(0,0):continue
                for j,v in enumerate(f):
                    if i+j<len(nxt):nxt[i+j]=add(nxt[i+j],mul(u,v,q),q)
            cur=nxt
        assert cur[2*n]==H,('independent polynomial test',p)
    divide=lambda u:(u[0]//p%(p*p),u[1]//p%(p*p))
    return {'p':p,'q_p3':q,'c_mod_p3':c,
      'original_E3_Hasse_coefficient_mod_p3':H,
      'original_E3_H_over_p_mod_p2':divide(H),
      'Hesse_A_mod_p3':A,'Hesse_A_over_p_mod_p2':divide(A),
      'J_mod_p2':(J[0]%(p*p),J[1]%(p*p)),
      'K_mod_p':(K[0]%p,K[1]%p),
      'verified':'independent cubic coefficient + termwise product'}

if __name__=='__main__':
    for p in (13,19,37,373):print(json.dumps(compute(p)))
