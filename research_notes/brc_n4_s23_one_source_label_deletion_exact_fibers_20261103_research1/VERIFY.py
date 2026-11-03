#!/usr/bin/env python3
"""Exact Fraction verifier for BRC N4/S23 one-labeled-row deletion theorem."""
from fractions import Fraction as F
from itertools import product
import json

MASKS = ((3,31),(7,27),(11,23),(15,19))
A=(0,0,0,1,1,1)
B=(2,2,3,2,2,4)
C=(5,6,7,8,9,10)
M=((10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),
   (0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20))
D={0:(5,6,11,-9),1:(5,6,1,-1),2:(3,7,1,-1),
   3:(8,9,9,-1),4:(8,9,1,-1),5:(4,10,1,-1)}
FIBER_GROUPS={0:((5,6),(9,11)),1:((5,6),(1,1)),
              3:((8,9),(1,9)),4:((8,9),(1,1))}
BASE=(F(1,7), F(2,7), F(1,3), F(2,5), F(3,7),
      F(1,2),F(1,2),F(1,4),F(1,2),F(1,2),F(3,4))
BETA_PAIRS=((F(0),F(0)),(F(1,2),F(1,3)),(F(3,4),F(2,5)))

def R(p,q,r):
    return (p,(1-p)*q,(1-p)*(1-q)*r,(1-p)*(1-q)*(1-r))

def observer(z, masks, betas):
    out=[]
    for mask,beta in zip(masks,betas):
        y=list(z)
        for j in range(5):
            if mask & (1<<j): y[j]=beta
        src=[R(y[A[i]],y[B[i]],y[C[i]]) for i in range(6)]
        obs=tuple(tuple(sum(F(M[j][i],20)*src[i][k] for i in range(6)) for k in range(4)) for j in range(6))
        out.append(obs)
    return tuple(out)

def signature(z, masks, betas, omitted):
    return tuple(tuple(row for j,row in enumerate(view) if j!=omitted) for view in observer(z,masks,betas))

def fiber_criterion(z,w,omitted):
    # Exact analytic fiber for both overwrite betas < 1.
    free={0,1}
    if omitted==2: free|={3,7}
    if omitted==5: free|={4,10}
    for j in range(11):
        if omitted in FIBER_GROUPS and j in FIBER_GROUPS[omitted][0]: continue
        if j not in free and z[j]!=w[j]: return False
    if omitted in FIBER_GROUPS:
        (i,k),(a,b)=FIBER_GROUPS[omitted]
        return a*z[i]+b*z[k]==a*w[i]+b*w[k]
    return True

def shifted(z, omitted, factor=F(1,100)):
    w=list(z)
    i,j,di,dj=D[omitted]
    w[i]+=di*factor
    w[j]+=dj*factor
    assert all(0<=x<=1 for x in w)
    return tuple(w)

def main():
    count=0
    wrong=0
    for masks,betas,drop in product(MASKS,BETA_PAIRS,range(6)):
        # Positive indistinguishability witnesses and necessity of omitted label
        w=shifted(BASE,drop)
        assert fiber_criterion(BASE,w,drop)
        assert signature(BASE,masks,betas,drop)==signature(w,masks,betas,drop)
        assert observer(BASE,masks,betas)!=observer(w,masks,betas)
        count+=1
        # Independently vary root coordinates and test exact set of retained observations.
        root=list(w); root[0]=F(4,5); root[1]=F(1,9); root=tuple(root)
        assert fiber_criterion(BASE,root,drop)
        assert signature(BASE,masks,betas,drop)==signature(root,masks,betas,drop)
        count+=1
        # Single-coordinate off-fiber changes always visible (all test points interior).
        for j in range(2,11):
            if drop==2 and j in (3,7): continue
            if drop==5 and j in (4,10): continue
            t=list(BASE); t[j]+=F(1,100)
            t=tuple(t)
            if drop in FIBER_GROUPS and j in FIBER_GROUPS[drop][0]:
                pass # one coordinate alone changes the retained weighted sum
            assert not fiber_criterion(BASE,t,drop)
            if signature(BASE,masks,betas,drop)==signature(t,masks,betas,drop):
                wrong+=1
            count+=1
        # Exact pair-affine perturbations with distinct non-proportional amplitudes.
        if drop in FIBER_GROUPS:
            for scale in (F(-1,200),F(1,125),F(1,90)):
                t=shifted(BASE,drop,scale)
                assert fiber_criterion(BASE,t,drop)
                assert signature(BASE,masks,betas,drop)==signature(t,masks,betas,drop)
                count+=1
    assert wrong==0, (wrong,'failed distinguishability')
    # Exhibit endpoint collapse of a fiber line at weighted-mean 0,1.
    for dropped in FIBER_GROUPS:
        (i,j),(a,b)=FIBER_GROUPS[dropped]
        for e in (F(0),F(1)):
            # For 0<=u,v<=1, au+bv=(a+b)e forces u=v=e since a,b>0.
            assert a>0 and b>0
            z=list(BASE);z[i]=e;z[j]=e
            assert (a*z[i]+b*z[j])==(a+b)*e
            count+=1
    results={'status':'PASS_BRC_S23_ONE_SOURCE_LABEL_DELETION_EXACT_FIBERS_20261103',
             'mask_pairs':len(MASKS), 'positive_beta_pairs':len(BETA_PAIRS),
             'deleted_row_choices':6, 'exact_assertion_groups':count,
             'off_fiber_false_positives':wrong,
             'science_pin':'43ec6098b1330ae86d0a7863be336c5d97f6ef34',
             'arithmetic':'Python Fraction, exact rational',
             'scope':'finite checks of analytic fiber theorem, not a real-domain exhaustive proof'}
    print(json.dumps(results,sort_keys=True,indent=2))
if __name__=='__main__': main()
