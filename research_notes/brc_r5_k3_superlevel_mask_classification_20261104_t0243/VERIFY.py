"""Exact author-side rational regression for R5 K3 ratio-locked clock wedge.

The all-real theorem is proved separately in RESEARCH.md. These tests enumerate
all 24 strict source orderings for one exact four-value kernel and test two-level
superlevel masks. Standard-library fractions.Fraction only.
"""
from fractions import Fraction as Q
from itertools import permutations, combinations, product

C = (Q(1,8),Q(1,6),Q(1,16),Q(3,32))
LABEL = ('C','I','BJ','IJ')
UP_FULL=((0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,1,0))
UP_LR=((0,0,0),(0,1,1),(1,0,0),(1,1,0))
STAGES=((0,0,0),(1,0,0),(1,1,0),(1,1,1))
MASKS=(frozenset(),frozenset((0,)),frozenset((0,1)),frozenset((0,2)),frozenset(range(4)))
assert len(set(MASKS))==5
checks=0

def check(b, name):
    global checks
    checks+=1
    assert b, f'{checks} {name}'

def obs(up,js,r,v,p,q):
    x,y,i=up
    w=(Q(1,8),Q(1-x,6),Q(y,16),Q(3*i,32))
    d=Q(y,16)+Q(3*i,32)
    m=[w[j]*STAGES[js[j]][0] for j in range(4)]
    s=[Q(2,3)*m[j]*STAGES[js[j]][1] for j in range(4)]
    u=[s[j]*STAGES[js[j]][2] for j in range(4)]
    return (Q(107,128)-Q(21*x,128)+d/4-sum(s)/2+sum((p[j]*s[j]/8 for j in range(4)),Q(0)),
      Q(13,64)+Q(3*x,64)-d/2+sum(s)/8+sum((q[j]*s[j]/32 for j in range(4)),Q(0)),
      Q(3)+sum(m)+Q(3,2)*sum(s)+sum((r[j]*u[j] for j in range(4)),Q(0)),
      Q(3)+sum(m)/2+Q(3,8)*sum(s)+sum((v[j]*u[j]/4 for j in range(4)),Q(0)))

def dot(n,z): return sum((a*b for a,b in zip(n,z)),Q(0))

def test_case(name,r,k,t,positive_expected,verbose=False):
    v=tuple(k*z for z in r)
    p=(Q(1,4),Q(1,2),Q(3,4),Q(1,3))
    q=(Q(3,4),Q(1,2),Q(1,4),Q(2,3))
    A=tuple((2+Q(2,3)*r[j])*t-Q(3,4)-v[j]/6 for j in range(4))
    plus=frozenset(j for j in range(4) if A[j]>0)
    check(plus==frozenset(positive_expected),name+':superlevel')
    check(all(Q(0)<v[j]<r[j]<1 for j in range(4)) and Q(0)<t<Q(3,8),name+':domain')
    formula_full=sum((C[j]*max(Q(0),A[j]) for j in range(4)),Q(0))
    formula_lr=max(sum((C[j]*A[j] for j in mask),Q(0)) for mask in MASKS)
    delta=formula_full-formula_lr
    check(delta>=0,name+':nonnegative')
    if all(a!=0 for a in A):
        check((delta==0)==(plus in MASKS),name+':mask-iff')
    n=(Q(0),Q(0),t,-Q(1))
    full=[obs(up,j,r,v,p,q) for up in UP_FULL for j in product(range(4),repeat=4)]
    lr=[obs(up,(z,)*4,r,v,p,q) for up in UP_LR for z in range(4)]
    check(len(full)==1536 and len(lr)==16,name+':coverage')
    hF=max(dot(n,w) for w in full)
    hL=max(dot(n,w) for w in lr)
    base=3*(t-1)
    check(hF==base+formula_full and hL==base+formula_lr,name+':formula')
    check(hF-hL==delta,name+':gap')
    witness=obs((0,1,1),tuple(3 if A[j]>0 else 0 for j in range(4)),r,v,p,q)
    check(dot(n,witness)==hF,name+':witness')
    if verbose:
        print(name,'r=',tuple(map(str,r)),'A=',tuple(map(str,A)),
              'pos=',','.join(LABEL[j] for j in range(4) if j in plus),
              'gap=',delta,'distance_inf>=',delta/(1+t),'W=',witness)
    return delta

# Four distinct source clocks: exhaust all 24 permutations with one exact normal.
rvals=(Q(1,5),Q(2,5),Q(3,5),Q(4,5)); k=Q(1,2); t=Q(7,20)
min_gap=None
min_perms=[]
by_low={label:[] for label in LABEL}
for i,r in enumerate(permutations(rvals)):
    low=r.index(Q(1,5))
    positive=[j for j in range(4) if j!=low]
    gap=test_case('STRICT_'+str(i+1),r,k,t,positive,verbose=(i<3))
    check(gap>0,'strict-positive-'+str(i+1))
    by_low[LABEL[low]].append(gap)
    if min_gap is None or gap<min_gap:
        min_gap=gap;min_perms=[r]
    elif gap==min_gap: min_perms.append(r)
check(sum(len(z) for z in by_low.values())==24,'full-24-permutation-coverage')
for key,gaps in by_low.items(): print('LOWEST',key,'count=',len(gaps),'min=',min(gaps),'max=',max(gaps))
print('ALL_STRICT_24_MIN_GAP=',min_gap,'distance_inf>=',min_gap/(1+t))
print('MIN_WITNESS_PERMUTATIONS=',tuple(tuple(map(str,z)) for z in min_perms))

# Two-level rational examples: high subsets of cardinality 1,2,3. All 14 patterns.
hi=Q(4,5);lo=Q(1,5)
for size in (1,2,3):
    for idx in combinations(range(4),size):
        r=tuple(hi if j in idx else lo for j in range(4))
        gap=test_case('TWO_LEVEL_'+''.join(LABEL[j] for j in idx),r,k,t,idx)
        check((gap==0)==(frozenset(idx) in MASKS),'two-level-classification-'+str(idx))
        print('TWO_LEVEL_HIGH',','.join(LABEL[j] for j in idx),'GAP',gap,
            'WEDGE_MATCH',gap==0)
print('ASSERTIONS_TOTAL',checks)
print('PASS_EXACT_R5_K3_RATIO_LOCKED_SUPERLEVEL_MASK_CLASSIFICATION')
