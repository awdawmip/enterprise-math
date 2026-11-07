#!/usr/bin/env python3
"""R5 exact stop-time error family: rank/hull dichotomy. Python 3 stdlib only."""
from fractions import Fraction as F
from itertools import product
from math import lcm

# Fixed off-diagonal Q/P carrier; source and time decisions are genuine STOP/CONTINUE.
Q={(0,0):F(49,100),(0,1):F(1,100),(1,0):F(1,100),(1,1):F(49,100)}
RU=(F(3,4),F(5,4)); RV=(F(1,2),F(1),F(3,2)); TX=(F(1,16),F(1,8))
def kernel(t,u):
    return (F(1,2)+t,F(1,2)-2*t,t) if u==0 else (t,F(1,2)-2*t,F(1,2)+t)
rows=[(x,u,v,RV[v]*Q[x,u]*kernel(TX[x],u)[v],Q[x,u]*kernel(TX[x],u)[v])
      for x,u,v in product(range(2),range(2),range(3))]
D=lcm(*(z.denominator for row in rows for z in row[3:]))
assert D==3200 and all(p>0 and q>0 for x,u,v,p,q in rows)
assert sum(r[3] for r in rows)==sum(r[4] for r in rows)==1
R=[(x,u,v,int(p*D),int(q*D)) for x,u,v,p,q in rows]

def obs(bits, full):
    tp=tq=sp=sq=0
    for x,u,v,p,q in R:
        early=(bits>>x)&1
        middle=(bits>>(2+(2*x+u if full else u)))&1
        last=(bits>>(6+6*x+3*u+v if full else 4+v))&1
        tau=2 if not early else (3 if not middle else (4 if not last else 5))
        tp+=tau*p;tq+=tau*q
        if tau==2:sp+=p;sq+=q
    return sp,sq,tp,tq

def det4(a):
    m=[[F(x) for x in row] for row in a];ans=F(1)
    for k in range(4):
        i=next((i for i in range(k,4) if m[i][k]),None)
        if i is None:return F(0)
        if i!=k:m[i],m[k]=m[k],m[i];ans=-ans
        pivot=m[k][k];ans*=pivot
        for j in range(k+1,4):
            c=m[j][k]/pivot
            for z in range(k,4):m[j][z]-=c*m[k][z]
    return ans

# Previous 2D time hull's 10 exact facet inequalities (see frozen precursor).
FACETS=[((2074,-2707),F(-1266)),((1,-1),F(633,1600)),
        ((22,-19),F(474,25)),((1958,-1603),F(3979,2)),
        ((2,-1),F(5)),((-2,3),F(5)),((-318,373),F(1243,4)),
        ((-46,53),F(1041,25)),((-1,1),F(1217,3200)),
        ((-4050,2833),F(-2434))]
lam=F(1949,2298);a,b=lam.numerator,lam.denominator
hi_full=None;hi_lr=None
for full in (False,True):
    max_val=None;argmax=None
    n=(1<<18) if full else 128
    # Exact 10 inequalities: no float, every deterministic FULL policy covered.
    for bits in range(n):
        sp,sq,tp,tq=obs(bits,full)
        for (np,nq),beta in FACETS:
            assert np*tp+nq*tq<=int(beta*D)
        h=b*tp-a*tq-b*sq  # b*D*(TP-lambda*TQ-SQ)
        if max_val is None or h>max_val:max_val=h;argmax=bits
    if full:hi_full=F(max_val,b*D);max_full_bits=argmax
    else:hi_lr=F(max_val,b*D);max_lr_bits=argmax
assert hi_full==F(202049,229800),(hi_full,max_full_bits)
assert hi_lr==F(202000,229800),(hi_lr,max_lr_bits)
delta=hi_full-hi_lr
assert delta==F(49,229800)>0

idx=(49,10,66,6);zero=obs(0,False)
B=[obs(i,False) for i in idx]
base_det=det4([[(row[k]-zero[k])/F(D) for k in range(4)] for row in B])
assert base_det==F(147,500000),base_det

# epsilon probabilities at times 2,3,4,5: exact late-affine lifting.
examples=[(F(3,4),F(1,4),F(1,4),F(1,4)),
          (F(1,4),F(1,2),F(1,2),F(1,2)),
          (F(2,5),F(1,5),F(3,10),F(2,5)),
          (F(1,2),F(1,5),F(2,5),F(3,5)),
          (F(1,5),F(3,10),F(2,5),F(1,2))]
print('P_Q_PATHS',len(rows),'EXACT_COMMON_DENOMINATOR',D)
print('FULL_BOOLEAN_POLICIES',1<<18,'LR_BOOLEAN_POLICIES',128)
print('TIME_HULL_FACETS_RECHECKED',len(FACETS))
print('H0=TP-(1949/2298)TQ-Q(tau=2)')
print('H0_FULL',hi_full,'H0_LR',hi_lr,'UNIFORM_GAP',delta)
print('RANK4_BASE_S_P_S_Q_T_P_T_Q',base_det,'INDICES',idx)
for eps in examples:
    e2,e3,e4,e5=eps
    assert all(F(0)<x<F(1) for x in eps)
    assert e3-2*e4+e5==0
    BB=e4-e3;AA=e3-3*BB;cc=e2-(AA+2*BB)
    assert all(eps[t-2]==AA+BB*t+(cc if t==2 else 0) for t in range(2,6))
    target_det=base_det*cc*cc
    def lift(z):
        sp,sq,tp,tq=(F(x,D) for x in z)
        return AA+BB*tp+cc*sp,AA+BB*tq+cc*sq,tp,tq
    v0=lift(zero)
    four_det=det4([[v-v0[j] for j,v in enumerate(lift(row))] for row in B])
    assert four_det==target_det,(eps,target_det,four_det)
    if cc:
        transformed_gap=(hi_full-AA/cc)-(hi_lr-AA/cc)
        assert transformed_gap==delta
        print('CASE',','.join(map(str,eps)),'c',cc,'DET4',four_det,'H_GAP',transformed_gap)
    else:
        assert four_det==0
        print('CASE',','.join(map(str,eps)),'c',cc,'RANK_AT_MOST_2_HULL_EQUAL',True)
print('PASS_EXACT_R5_LATE_AFFINE_TIME_ERROR_COMPLETE_DICHOTOMY')
