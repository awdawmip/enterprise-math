# Stage113 portable exact checker (external iid ternary horizon N=14).
# AUTHOR-SIDE computational certificate, not independent Driver admission.
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
P=(F(1,8),F(1,24),F(5,6))
Q=(F(1,12),F(1,12),F(5,6))
A=(10,3,0); C=(5,2,3)
K=F(814106972531223,875100809116)
L=F(189992854025880,218775202279)
alpha0=F(13084629132464364707,37682150988866125824)
V0=F(1930486644885404154985,150728603955464503296)
u0=F(66372737348901,70438400000000)
@lru_cache(None)
def ratio(s):
    n,a,b=s
    return F(2**(a+b),3**a)
@lru_cache(None)
def H(n,a,b):
    options=[K*ratio((n,a,b)),L]
    if n<14:
        children=((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
        options.append(1+sum(P[j]*H(*children[j]) for j in range(3)))
    return min(options)

def bellman():
    actions={}; ties={}; gaps=[]
    for n in range(15):
        for a in range(n+1):
            for b in range(n-a+1):
                s=(n,a,b)
                o={'P':K*ratio(s),'Q':L}
                if n<14:
                    child=((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
                    o['C']=1+sum(P[j]*H(*child[j]) for j in range(3))
                best=min(o.values()); mini=[tag for tag,v in o.items() if v==best]
                actions[s]=mini[0]
                if len(mini)>1: ties[s]=mini
                gaps.extend(v-best for tag,v in o.items() if tag!=mini[0])
    assert len(actions)==680 and len(gaps)==1240
    assert sum(x>0 for x in gaps)==1238 and sum(x==0 for x in gaps)==2
    assert min(x for x in gaps if x>0)==F(3797211181,1312651213674)
    assert ties=={A:['P','C'],C:['Q','C']}
    return actions

def moments(actions,u,w):
    # Independent positive P,Q mass of every live count state; count quotient
    # is valid for iid conditional suffixes, not an erasure of ordered provenance.
    alive={(0,0,0):(F(1),F(1),1)}
    eP=eQ=tP=tQ=F(0)
    hits={A:[0,F(0),F(0)],C:[0,F(0),F(0)]}
    for n in range(15):
        nxt=defaultdict(lambda:[F(0),F(0),0])
        for s,(mp,mq,cnt) in alive.items():
            if s in hits:
                hits[s][0]+=cnt;hits[s][1]+=mp;hits[s][2]+=mq
            if s==A:sp,sq,cont=u,F(0),1-u
            elif s==C:sp,sq,cont=F(0),w,1-w
            elif actions[s]=='P':sp,sq,cont=F(1),F(0),F(0)
            elif actions[s]=='Q':sp,sq,cont=F(0),F(1),F(0)
            else:sp,sq,cont=F(0),F(0),F(1)
            eP+=mp*sq; eQ+=mq*sp
            tP+=n*mp*(sp+sq); tQ+=n*mq*(sp+sq)
            if cont:
                children=((n+1,s[1]+1,s[2]),(n+1,s[1],s[2]+1),(n+1,s[1],s[2]))
                for j,c in enumerate(children):
                    z=nxt[c];z[0]+=mp*P[j]*cont;z[1]+=mq*Q[j]*cont;z[2]+=cnt
        alive=nxt
    assert not alive
    return dict(eP=eP,eQ=eQ,tP=tP,tQ=tQ,hits=hits)

def main():
    act=bellman()
    b=moments(act,F(0),F(0))
    a=moments(act,F(1),F(0))
    c=moments(act,F(0),F(1))
    d=moments(act,F(1),F(1))
    fields=('eP','eQ','tP','tQ')
    du={x:a[x]-b[x] for x in fields}
    dw={x:c[x]-b[x] for x in fields}
    assert all(d[x]-a[x]-c[x]+b[x]==0 for x in fields)
    assert b['hits'][A]==[120,F(390625,5971968),F(390625,20155392)]
    assert b['hits'][C]==[6,F(1,147456),F(1,41472)]
    slope=-(dw['eP']-dw['eQ'])/(du['eP']-du['eQ'])
    assert slope==F(123866061659,986137600000000)
    eta=F(218775202279,19538893105337991168)
    end=moments(act,u0+slope,F(1))
    start=moments(act,u0,F(0))
    assert (start['eP'],start['eQ'],start['tP'])==(alpha0,alpha0,V0)
    assert (end['eP'],end['eQ'])==(alpha0+eta,alpha0+eta)
    assert end['tP']==V0-(K+L)*eta
    assert H(0,0,0)==V0+(K+L)*alpha0
    assert start['tP']>start['tQ'] and end['tP']>end['tQ']
    assert F(0)<u0<u0+slope<F(1)
    print('PASS_STAGE113_EXACT_AUTHOR', 'alpha113',end['eP'],'V113',end['tP'])
if __name__=='__main__': main()
