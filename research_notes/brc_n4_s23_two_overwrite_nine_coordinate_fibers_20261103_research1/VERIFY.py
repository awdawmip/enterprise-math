#!/usr/bin/env python3
"""Exact source-labelled two-view fiber checks; no approximate arithmetic."""
from fractions import Fraction as F
from itertools import product
from random import Random
import json

A=(0,0,0,1,1,1); B=(2,2,3,2,2,4); C=(5,6,7,8,9,10)
M=((10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),
   (0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20))
PAIRS=((3,31),(7,27),(11,23),(15,19))
BETA_CHOICES=(F(0),F(1,2),F(1))

def branch(p,q,r):
    return p,(1-p)*q,(1-p)*(1-q)*r,(1-p)*(1-q)*(1-r)

def raw(z,mask,beta):
    y=list(z)
    for k in range(5):
        if mask & (1<<k): y[k]=beta
    return tuple(branch(y[A[i]],y[B[i]],y[C[i]]) for i in range(6))

def observed(z,mask,beta):
    v=raw(z,mask,beta)
    return tuple(tuple(sum((F(M[j][i],20)*v[i][k] for i in range(6)),F(0))
                       for k in range(4)) for j in range(6))

def unmix(p):
    r0=tuple(11*p[0][k]-10*p[1][k] for k in range(4))
    r1=tuple(10*p[1][k]-9*p[0][k] for k in range(4))
    r2=p[2]
    r3=tuple((9*p[3][k]-5*p[4][k])/4 for k in range(4))
    r4=tuple((5*p[4][k]-p[3][k])/4 for k in range(4))
    r5=p[5]
    return r0,r1,r2,r3,r4,r5

def masks(pair):
    return tuple(sorted(pair,key=lambda m:(m & 4)!=0))

def views(pair,bn,be):
    n,e=masks(pair)
    return ((n,bn),(e,be))

def inactive(z,pair,bn,be):
    v=views(pair,bn,be)
    result={0,1}
    for k in (2,3,4):
        if not any(beta<1 and not(mask & (1<<k)) for mask,beta in v):
            result.add(k)
    for i,c in enumerate(C):
        g=B[i]
        if not any(beta<1 and ((mask & (1<<g)) or z[g]<1)
                   for mask,beta in v):
            result.add(c)
    return result

def invert_visible(z,pair,bn,be):
    v=views(pair,bn,be)
    raws=[unmix(observed(z,mask,beta)) for mask,beta in v]
    ret={}
    for k in (2,3,4):
        for (_,beta),r in zip(v,raws):
            if beta<1 and not(_ & (1<<k)):
                i=B.index(k)
                ret[k]=r[i][1]/(1-beta)
                break
    for i,c in enumerate(C):
        g=B[i]
        for (mask,beta),r in zip(v,raws):
            q=beta if mask & (1<<g) else z[g]
            if beta<1 and q<1:
                ret[c]=r[i][2]/((1-beta)*(1-q))
                break
    return ret

def eq_views(z,w,pair,bn,be):
    return all(observed(z,mask,beta)==observed(w,mask,beta)
               for mask,beta in views(pair,bn,be))

def run():
    rng=Random(20261103)
    regime_counts={'both_open':0,'N_only':0,'E_only':0,'both_closed':0}
    signatures=fiber_equalities=separations=inverse_matches=0
    max_dimension=0
    for pair in PAIRS:
        n,e=masks(pair)
        assert ((n&3)==3 and (n&4)==0 and (e&7)==7)
        for bn,be in product(BETA_CHOICES,repeat=2):
            regime=('both_open' if bn<1 and be<1 else
                    'N_only' if bn<1 else 'E_only' if be<1 else 'both_closed')
            for flags in product((False,True),repeat=3):
                z=[F(1,3),F(2,3)] + [F(1) if f else F(1,3) for f in flags] + [F(2,5)]*6
                free=inactive(z,pair,bn,be)
                vis=invert_visible(z,pair,bn,be)
                assert set(vis)==set(range(2,11))-free
                assert all(z[k]==val for k,val in vis.items())
                inverse_matches+=len(vis)
                signatures+=1
                regime_counts[regime]+=1
                max_dimension=max(max_dimension,len(free)-2)
                # Each predicted free coordinate may vary independently; compare all on 16 structured corners.
                zz=z.copy()
                for k in free: zz[k]=F(0)
                assert eq_views(z,zz,pair,bn,be)
                fiber_equalities+=1
                for t in range(16):
                    w=z.copy()
                    for k in free:
                        w[k]=F(rng.randrange(7),6)
                    assert eq_views(z,w,pair,bn,be)
                    fiber_equalities+=1
                # Each predicted visible coordinate is distinguishable even at singular boundaries.
                for k in range(2,11):
                    if k not in free:
                        w=z.copy()
                        w[k]=F(0) if z[k]>0 else F(1)
                        assert not eq_views(z,w,pair,bn,be), (pair,bn,be,flags,k)
                        separations+=1
    out={'status':'PASS_BRC_S23_TWO_OVERWRITE_NINE_PARAMETER_COMPLETE_FIBERS_20261103',
         'frozen_pin':'43ec6098b1330ae86d0a7863be336c5d97f6ef34',
         'arithmetic':'Python standard library fractions.Fraction',
         'pairs':[list(p) for p in PAIRS],
         'beta_values':['0','1/2','1'],
         'upstream_flags_per_setting':8,
         'signatures':signatures,'regime_counts':regime_counts,
         'fiber_observer_equalities':fiber_equalities,
         'identifiable_coordinate_separations':separations,
         'coordinate_reconstructions':inverse_matches,
         'maximum_remaining_fiber_dimension':max_dimension,
         'proof_scope':'all real parameters by analytic inverse; finite checker is corroboration',
         'independent_review':'PENDING'}
    print(json.dumps(out,indent=2,ensure_ascii=False))
if __name__=='__main__':run()
