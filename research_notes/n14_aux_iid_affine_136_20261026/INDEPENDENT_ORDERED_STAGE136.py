#!/usr/bin/env python3
"""Independent literal-prefix integer-weight DFS witness for Stage136.

Separately specified recursive Bellman actions and ordered-word enumeration.
Does not reuse the main checker's moment recurrence.
"""
from fractions import Fraction
from functools import lru_cache
import json
N=14
p=(3,1,20)
q=(1,1,10)
KP=Fraction(840571992,1526537)
LQ=Fraction(797676584,1526537)
B=(11,0,1);D=(10,6,2)

@lru_cache(None)
def opt(s):
    n,a,b=s
    priceP=KP*Fraction(2**(a+b),3**a)
    priceQ=LQ
    options={'P':priceP,'Q':priceQ}
    if n<14:
        child=((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
        options['C']=1+sum((Fraction(p[i],24)*opt(child[i])[0] for i in range(3)),Fraction(0))
    m=min(options.values())
    return m,tuple(k for k,x in options.items() if x==m)

scaleP=[24**(N-n) for n in range(N+1)]
scaleQ=[12**(N-n) for n in range(N+1)]
DP=24**N; DQ=12**N
out={}
for w,u in ((0,0),(1,0),(0,1),(1,1)):
    sums=[0]*4
    first={B:[0,0,0],D:[0,0,0]}
    visited=0
    leaves=0
    def dfs(n,a,b,mP,mQ):
        global visited,leaves
        visited+=1
        s=(n,a,b)
        if s in first:
            f=first[s]
            f[0]+=1
            f[1]+=mP*scaleP[n]
            f[2]+=mQ*scaleQ[n]
        _,moves=opt(s)
        if len(moves)==1:action=moves[0]
        elif s==B:action=('Q' if w else 'C')
        elif s==D:action=('P' if u else 'C')
        else:raise RuntimeError((s,moves))
        if action!='C':
            leaves+=1
            sp=mP*scaleP[n]
            sq=mQ*scaleQ[n]
            if action=='Q':sums[0]+=sp
            else:sums[1]+=sq
            sums[2]+=n*sp
            sums[3]+=n*sq
            return
        dfs(n+1,a+1,b,mP*p[0],mQ*q[0])
        dfs(n+1,a,b+1,mP*p[1],mQ*q[1])
        dfs(n+1,a,b,mP*p[2],mQ*q[2])
    dfs(0,0,0,1,1)
    vec=[Fraction(sums[0],DP),Fraction(sums[1],DQ),Fraction(sums[2],DP),Fraction(sums[3],DQ)]
    out[f'{w}{u}']={'values':[str(v) for v in vec],'visited_prefixes':visited,'leaves':leaves,
                    'first_hit':{str(k):{'literal_words':v[0],'P_mass':str(Fraction(v[1],DP)),'Q_mass':str(Fraction(v[2],DQ))} for k,v in first.items()}}
    print((w,u),vec,'nodes',visited,'first_hit',out[f'{w}{u}']['first_hit'])

with open('certificate136.json') as f:cert=json.load(f)
fr=lambda s:Fraction(s)
M00=[fr(v) for v in cert['M00']]
dB=[fr(v) for v in cert['dB']]
dD=[fr(v) for v in cert['dD']]
for w,u in ((0,0),(1,0),(0,1),(1,1)):
    v=[fr(x) for x in out[f'{w}{u}']['values']]
    expected=[M00[i]+w*dB[i]+u*dD[i] for i in range(4)]
    assert v==expected,(w,u,v,expected)
for state in (str(B),str(D)):
    assert len({out[k]['first_hit'][state]['P_mass'] for k in out})==1
    assert len({out[k]['first_hit'][state]['Q_mass'] for k in out})==1
    assert len({out[k]['first_hit'][state]['literal_words'] for k in out})==1
with open('ordered_certificate136.json','w') as f:json.dump(out,f,indent=2)
print('PASS_STAGE136_INDEPENDENT_ORDERED')
