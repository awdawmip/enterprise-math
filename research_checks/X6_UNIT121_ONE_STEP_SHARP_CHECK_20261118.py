#!/usr/bin/env python3
"""Unit121: exhaustive [-2,2]^6 observer-fiber and named-step certificate."""
import json
from collections import defaultdict, Counter
from itertools import product
from math import factorial

def ensure(ok, message):
    if not ok: raise RuntimeError(message)

def rho(z):
    m=min(z)
    return tuple(v-m for v in z)

def G(z): return sum(v*v for v in z)

def B(z):
    t=sum(map(abs,z)); f=1
    for v in z: f*=factorial(abs(v))
    return factorial(t)//f

def step(z,j,e):
    a=list(z); a[j]+=e
    return tuple(a)

def run():
    groups=defaultdict(list)
    for z in product(range(-2,3),repeat=6):
        groups[(rho(z),G(z))].append(z)
    byG=Counter(); same=diff=steps=bad=0
    for (r,g),fiber in groups.items():
        ensure(len(fiber)<=2,'fiber cardinality')
        if len(fiber)!=2: continue
        a,b=sorted(fiber); c=b[0]-a[0]
        ensure(c and all(b[j]-a[j]==c for j in range(6)),'diagonal identity')
        ensure(sum(a)==-3*c,'reflection identity')
        byG[g]+=1
        if B(a)==B(b): same+=1
        else: diff+=1
        for j in range(6):
            for e in (-1,1):
                u,v=step(a,j,e),step(b,j,e)
                steps+=1
                if rho(u)!=rho(v) or G(v)-G(u)!=2*e*c: bad+=1
    x=(-1,-1,-1,0,0,0); y=(0,0,0,1,1,1)
    u,v=step(x,0,1),step(y,0,1)
    ensure((rho(x),G(x),B(x))==(rho(y),G(y),B(y)),'witness input')
    ensure((G(u),G(v),B(u),B(v))==(2,4,2,24),'witness output')
    ensure(len(groups)==14883 and sum(byG.values())==742,'census')
    ensure((same,diff,steps,bad,min(byG))==(562,180,8904,0,3),'counts')
    return {'schema':'X6_UNIT121_NAMED_STEP_EXACT_CERT_V1','date':'2026-11-18',
            'domain':'[-2,2]^6','states':15625,'fibers':len(groups),
            'double_fibers':sum(byG.values()),'current_BRC_equal_fibers':same,
            'current_BRC_unequal_fibers':diff,'named_steps_checked':steps,
            'violations':bad,'first_ambiguous_G':min(byG),
            'double_fibers_by_G':{str(k):byG[k] for k in sorted(byG)},
            'witness':{'x':x,'y':y,'rho':rho(x),'G':3,'BRC':6,
                       'step':'+e0','x_next':u,'y_next':v,
                       'rho_next':rho(u),'G_next':[G(u),G(v)],
                       'BRC_next':[B(u),B(v)]},
            'status':'AUTHOR_EXACT_EXECUTED_UNREVIEWED_NOT_ADMITTED'}

if __name__=='__main__': print(json.dumps(run(),sort_keys=True,separators=(',',':')))
