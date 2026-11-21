#!/usr/bin/env python3
"""R88: exact finite cross-check of a universally proved conditioning lemma.
No dependencies. Work is a conditional four-readout integer histogram, not native X6 dynamics.
"""
import json
from fractions import Fraction

P=30
pairs=((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))
S=(10,-5,1)
T=(9,-5,1)

def q(a):
    return max(sum(max(c,0) for c in a),sum(max(-c,0) for c in a))

def gaps(a):
    x,y,z=a
    v=(0,2*x+6*y+12*z,6*x+24*y+60*z,14*x+78*y+252*z)
    return tuple(abs(v[i]-v[j])//2 for i,j in pairs)

def F(g,w):
    return max(Fraction(g[k],w[i]+w[j]) for k,(i,j) in enumerate(pairs))

def directions(p):
    for x in range(-p,p+1):
        for y in range(-p,p+1):
            for z in range(-p,p+1):
                a=(x,y,z)
                if a==(0,0,0): continue
                if next(c for c in a if c)!=abs(next(c for c in a if c)): continue
                if q(a)<=p: yield a

assert q(S)==11 and q(T)==10 and q(tuple(2*x for x in S))==22
assert gaps(S)==(1,0,1,1,0,1)
assert gaps(T)==(0,3,6,3,6,3)

samples=[(1,1,r,r) for r in (1,2,5,8,10,11,12,17)]+[(3,5,7,9),(2,11,3,4),(1,4,9,2)]
ss=[]
for w in samples:
    m=min(w); M=max(w)
    d=min(w[0],w[2])+min(w[1],w[3])
    FS=F(gaps(S),w)
    assert FS==Fraction(1,d)
    FT=F(gaps(T),w)
    if w[0]==w[1]==1 and w[2]==w[3]:
        assert FT/FS==Fraction(12,w[2]+1)
    examined=0
    for a in directions(P):
        examined+=1
        ga=gaps(a)
        if a==S: continue
        Fa=F(ga,w)
        if a[0]==10*a[2] and a[1]==-5*a[2]:
            assert abs(a[2])>=2
            assert Fa/FS==abs(a[2])
        else:
            assert ga[1]>=6 or ga[4]>=6, (a,ga)
            assert (Fa/FS)*(M+m)>=12*m,(a,ga,w)
        if M<11*m: assert Fa>FS,(a,w)
    assert examined==47305,examined
    ss.append({'w':w,'ratio_max_min':str(Fraction(M,m)),
               'F_s':str(FS),'F_t':str(FT),'directions_checked':examined,
               'uniform_uniqueness_checked':M<11*m})
results={
 'schema':'X6_R88_SHARP_CONDITIONING_AUTHOR_CROSSCHECK_V1',
 'frozen_science':'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json',
 'limit_p':P,
 'unoriented_vectors_per_weight':47305,
 'profiles_tested':len(samples),
 'total_vector_profile_pairs':47305*len(samples),
 'status':'PASS; AUTHOR_COMPUTATION; UNIVERSAL CLAIM USES SYMBOLIC PROOF',
 'cases':ss,
 'next_problem':'Classify individual anisotropic weight chambers where s11 remains uniquely minimizing beyond ratio 11, and test named-Port triadic future-fiber transfer separately.'}
print(json.dumps(results,ensure_ascii=False,indent=2))
