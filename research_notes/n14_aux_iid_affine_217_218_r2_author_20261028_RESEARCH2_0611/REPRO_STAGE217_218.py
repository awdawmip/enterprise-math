"""Independent exact N14 two-stage reference: iterative Bellman and full ordered-path mass.
No import from primary author stages. Verifies their published rational certificates.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

D = Path(__file__).resolve().parent
N=14; PN=(3,1,20);QN=(2,2,20)
P=tuple(F(x,24) for x in PN)
ORDERED=[(n,a,b) for n in range(N,-1,-1) for a in range(n,-1,-1) for b in range(n-a,-1,-1)]

def next_state(s,j):
    return (s[0]+1,s[1]+(j==0),s[2]+(j==1))

def value(K):
    table={}
    for s in ORDERED:
        n,a,b=s
        opts={'P':K*F(2**(a+b),3**a),'Q':K}
        if n<14: opts['C']=1+sum(P[j]*table[next_state(s,j)][0] for j in range(3))
        low=min(opts.values())
        table[s]=(low,tuple(k for k,v in opts.items() if v==low),
                  tuple(v-low for v in opts.values() if v>low))
    return table

def evaluate(table,T,u,z):
    # An explicit full ordered word is carried with each stack item. No path quotient.
    stack=[((),1,1,0,0)]
    total=[0,0,0,0]; node_count=0; leaf_count=0
    while stack:
        word,pm,qm,a,b=stack.pop()
        node_count+=1
        n=len(word);s=(n,a,b)
        if s==T: act='P' if u else 'C'
        elif s==(14,0,0):act='P' if z else 'Q'
        else:
            options=table[s][1]
            assert len(options)==1
            act=options[0]
        if act=='C':
            assert n<14
            for j in (2,1,0):
                stack.append((word+(j,),pm*PN[j],qm*QN[j],a+(j==0),b+(j==1)))
        else:
            leaf_count+=1
            mult=24**(14-n)
            total[0]+=(act=='Q')*pm*mult
            total[1]+=(act=='P')*qm*mult
            total[2]+=n*pm*mult
            total[3]+=n*qm*mult
    return tuple(F(v,24**14) for v in total),node_count,leaf_count

def check(stage):
    cert=json.loads((D/f'certificate{stage}.json').read_text(encoding='utf-8'))
    K=F(cert[f'K{stage}']);H=F(cert[f'H{stage}'])
    table=value(K)
    assert len(table)==680 and table[(0,0,0)][0]==H
    ties={str(s):list(table[s][1]) for s in table if len(table[s][1])>1}
    assert ties==cert['tie_actions']
    gap=[g for v in table.values() for g in v[2]]
    assert len(gap)==1238 and min(gap)==F(cert['minimum_gap'])
    T=next(s for s in table if s!=(14,0,0) and len(table[s][1])>1)
    corners={};visits={};leaves={}
    for u,z in product((0,1),repeat=2):
        obs,n,l=evaluate(table,T,u,z)
        corners[f'{u}{z}']=list(map(str,obs))
        visits[f'{u}{z}']=n; leaves[f'{u}{z}']=l
    assert corners==cert['corners']
    assert visits==cert['ordered_visits'] and leaves==cert['ordered_leaves']
    O=tuple(map(F,corners['00']))
    sub=lambda x,y:tuple(a-b for a,b in zip(x,y))
    t=tuple(map(F,corners['10']));z=tuple(map(F,corners['01']));tz=tuple(map(F,corners['11']))
    dt=sub(t,O); dz=sub(z,O); mixed=sub(sub(tz,t),dz)
    assert mixed==(F(0),)*4
    assert list(map(str,dt))==cert['DT'] and list(map(str,dz))==cert['DZ']
    z0=-(O[0]-O[1])/(dz[0]-dz[1])
    zs=-(dt[0]-dt[1])/(dz[0]-dz[1])
    assert (str(z0),str(zs),str(z0+zs)) == (cert['z0'],cert['zs'],cert['z1'])
    assert 0<=z0<=1 and 0<=z0+zs<=1
    def balanced(u):return tuple(O[i]+u*dt[i]+(z0+zs*u)*dz[i] for i in range(4))
    first,last=balanced(F(0)),balanced(F(1))
    assert first[0]==first[1] and last[0]==last[1]
    assert first[2]>first[3] and last[2]>last[3]
    assert first[0]==F(cert[f'alpha{stage-1}']) and first[2]==F(cert[f'V{stage-1}'])
    assert last[0]==F(cert[f'alpha{stage}']) and last[2]==F(cert[f'V{stage}'])
    assert last[2]+2*K*last[0]==first[2]+2*K*first[0]==H
    assert last[0]-first[0]==F(cert[f'width{stage}']) and last[0]>first[0]
    print(f'STAGE{stage}_INDEPENDENT_EXACT_PASS {sum(visits.values())}')

for stage in (217,218): check(stage)
