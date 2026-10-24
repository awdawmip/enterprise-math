#!/usr/bin/env python3
"""Second author checker: independent Bellman minimization, ordered-word hits, backward risks."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import comb
import verify_n14_72 as m
import json


def stop(n,a,b):
    st=(n,a,b)
    if st in m.SP:return 'P'
    if st in m.SQ:return 'Q'
    if 8*3**a>=9*2**(a+b+m.N-n):return 'P'
    if 8*3**(a+m.N-n)<9*2**(a+b+m.N-n):return 'Q'
    return 'C'

def word_count(target,via=None):
    t,aa,bb=target;survivors=through=0
    for w in product(range(3),repeat=t):
        if w.count(0)!=aa or w.count(1)!=bb:continue
        a=b=0;seen=False
        for n,i in enumerate(w):
            seen |= (n,a,b)==via
            if stop(n,a,b)!='C':break
            a+=i==0;b+=i==1
        else:
            survivors+=1;through+=seen
    return comb(t,aa)*comb(t-aa,bb),survivors,through

def backward(u,s):
    @lru_cache(None)
    def run(n,a,b):
        st=(n,a,b)
        if st==m.A: earlyp=u; earlyq=F()
        elif st==m.B: earlyp=F(); earlyq=s
        else:
            z=stop(n,a,b)
            if z=='P':return F(),F(1),F(),F()
            if z=='Q':return F(1),F(),F(),F()
            earlyp=earlyq=F()
        kids=[run(n+1,a+(i==0),b+(i==1)) for i in range(3)]
        cont=1-earlyp-earlyq
        return (earlyq+cont*sum((m.P[i]*kids[i][0] for i in range(3)),F()),
                earlyp+cont*sum((m.Q[i]*kids[i][1] for i in range(3)),F()),
                cont*(1+sum((m.P[i]*kids[i][2] for i in range(3)),F())),
                cont*(1+sum((m.Q[i]*kids[i][3] for i in range(3)),F())))
    return run(0,0,0)

def min_dp():
    D={};ties={};positive=0;comp=0
    for n in range(m.N,-1,-1):
        for a in range(n+1):
            for b in range(n-a+1):
                st=(n,a,b)
                costs={'P':m.LQ*F(2**(a+b),3**a),'Q':m.LP}
                if n<m.N:costs['C']=1+sum(m.P[i]*D[(n+1,a+(i==0),b+(i==1))] for i in range(3))
                v=min(costs.values());D[st]=v
                opts=[z for z,c in costs.items() if c==v]
                if len(opts)>1:ties[st]=opts
                assert stop(n,a,b) in opts,(st,opts)
                positive+=sum(c>v for c in costs.values());comp+=len(costs)-1
    return D[0,0,0],ties,positive,comp

def check():
    na,la,_=word_count(m.A);nb,lb,_=word_count(m.B)
    d1,l1,v1=word_count((10,4,0),m.A)
    d2,l2,v2=word_count((10,5,0),m.A)
    assert (na,la,nb,lb)==(126,126,12,12)
    assert (d1,l1,v1,d2,l2,v2)==(210,210,126,252,126,126)
    root,ties,pos,comp=min_dp()
    assert root==m.V+m.G*m.AL and pos==1238 and comp==1240
    assert set(ties)=={m.A,m.B} and set(ties[m.A])=={'C','P'} and set(ties[m.B])=={'C','Q'}
    corner={(u,s):backward(F(u),F(s)) for u in (0,1) for s in (0,1)}
    assert all(corner[1,1][i]-corner[1,0][i]-corner[0,1][i]+corner[0,0][i]==0 for i in range(4))
    X=corner[0,0][0]-corner[1,0][0]
    Y=corner[1,0][1]-corner[0,0][1]
    E=corner[0,1][0]-corner[0,0][0]
    H=corner[0,0][1]-corner[0,1][1]
    h=(X+Y)/(E+H);eta=E*h-X
    assert h==F(805329,128000000) and eta==F(2865625,1761205026816)
    for u in (F(),F(1,6),F(1,3),F(1,2),F(2,3),F(5,6),F(1)):
        ep,eq,tp,tq=backward(u,m.S+h*u)
        assert ep==eq==m.AL+eta*u and tp==m.V-m.G*eta*u and tp>tq
    return dict(status='AUTHOR_CROSSCHECK_PASS_DRIVER_UNREVIEWED',nominal_A=na,live_A=la,nominal_B=nb,live_B=lb,descendants=[[d1,l1,v1],[d2,l2,v2]],Bellman_ties=str(ties),strict=pos,nonchosen=comp,h72=str(h),eta72=str(eta),alpha72=str(m.AL+eta),V72=str(m.V-m.G*eta),four_mixed_terms_zero=True)
if __name__=='__main__':print(json.dumps(check(),indent=2))
