#!/usr/bin/env python3
"""BRC S23 complete-bank sharp inverse coefficient, exact Fraction evidence."""
from fractions import Fraction as Q
import json, random

A=(0,0,0,1,1,1)
B=(2,2,3,2,2,4)
C=(5,6,7,8,9,10)
M=((10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),(0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20))
PAIRS=((3,31),(7,27),(11,23),(15,19))

def R(p,q,r):return (p,(1-p)*q,(1-p)*(1-q)*r,(1-p)*(1-q)*(1-r))
def obs(z,mask):
    v=list(z)
    for i in range(5):
        if mask&(1<<i):v[i]=Q(0)
    s=[R(v[A[i]],v[B[i]],v[C[i]]) for i in range(6)]
    return tuple(tuple(sum((Q(M[j][i],20)*s[i][k] for i in range(6)),Q(0)) for k in range(4)) for j in range(6))

def bank(z,pair,missing):
    N=next(m for m in pair if not m&4);E=next(m for m in pair if m&4)
    o={'N':obs(z,N),'E':obs(z,E)}
    # All four outcome probabilities of the 5 surviving rows in both views,
    # plus predecessor's minimal scalar repair(s) of the deleted row.
    b={ (v,j,t):o[v][j][t] for v in ('N','E') for j in range(6) if j!=missing for t in range(4)}
    if missing in (0,1,3,4): b['E',missing,2]=o['E'][missing][2]
    else:
        gate=3 if missing==2 else 4
        U='N' if not N&(1<<gate) else 'E'
        V='E' if U=='N' else 'N'
        b[U,missing,1]=o[U][missing][1]
        b[V,missing,2]=o[V][missing][2]
    return b

def nine(z,pair,missing):
    b=bank(z,pair,missing)
    N=next(m for m in pair if not m&4);E=next(m for m in pair if m&4)
    U3='N' if not N&8 else 'E';U4='N' if not N&16 else 'E'
    V3='E' if U3=='N' else 'N'; V4='E' if U4=='N' else 'N'
    r=1 if missing==0 else 0
    links=[('N',r,1),(U3,2,1),(U4,5,1),(V3,2,2),(V4,5,2),('E',0,2),('E',1,2),('E',3,2),('E',4,2)]
    return tuple(b[k] for k in links)

def inv(y):
    return (y[0],y[1],y[2],11*y[5]-10*y[6],-9*y[5]+10*y[6],y[3],
            (9*y[7]-5*y[8])/4,(-y[7]+5*y[8])/4,y[4])

def maxdiff(a,b):return max(abs(a[k]-b[k]) for k in a)

random.seed(20261103)
counts={'pairs':0,'deleted_rows':0,'linear_recovery_states':0,'full_bank_pair_bounds':0,'sharp_pairs':0,'noisy_decision_indistinguishability':0}
for pair in PAIRS:
 for missing in range(6):
    counts['deleted_rows']+=1
    for _ in range(40):
        z=tuple(Q(random.randrange(0,101),100) for i in range(11))
        w=tuple(Q(random.randrange(0,101),100) for i in range(11))
        assert inv(nine(z,pair,missing))==z[2:]
        counts['linear_recovery_states']+=1
        dz=max(abs(z[i]-w[i]) for i in range(2,11))
        D=maxdiff(bank(z,pair,missing),bank(w,pair,missing))
        assert dz<=21*D,(pair,missing,dz,D)
        counts['full_bank_pair_bounds']+=1
    for eta in (Q(1,1000),Q(1,100),Q(1,42)):
        base=[Q(1,2)]*11;base[2]=Q(0)
        lo=base.copy();hi=base.copy()
        lo[5]-=21*eta;lo[6]+=19*eta
        hi[5]+=21*eta;hi[6]-=19*eta
        assert all(0<=v<=1 for v in lo+hi)
        lo_b=bank(lo,pair,missing);hi_b=bank(hi,pair,missing)
        assert set(lo_b)==set(hi_b)
        Db=maxdiff(lo_b,hi_b)
        assert Db==2*eta,(pair,missing,Db,eta)
        assert max(abs(hi[i]-lo[i]) for i in range(2,11))==42*eta
        assert max(abs(hi_b[k]-lo_b[k])/2 for k in lo_b)==eta
        counts['sharp_pairs']+=1
        counts['noisy_decision_indistinguishability']+=1
    counts['pairs']+=1
print(json.dumps({'flag':'PASS_BRC_S23_FULL_BANK_SHARP_21_AND_LOCAL_NOISE_MINIMAX_20261103',**counts,'arithmetic':'Python fractions.Fraction only','domain':'four masks, six missing-row patterns, beta_N=beta_E=0, all real cube via analytic proof','sampling':'40 random rational pairs per mask/delete, 3 exact extremal eta'},sort_keys=True))
