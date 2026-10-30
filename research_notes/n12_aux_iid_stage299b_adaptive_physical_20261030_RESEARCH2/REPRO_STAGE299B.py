#!/usr/bin/env python3
"""Stage299-B: exact rational BRC source-tagged adaptive/physical gap replay.

Finite witness only. Real-mixture lower bounds and minimax optimality
are mathematical proofs in PROOF_STAGE299B.md, not extrapolated from a grid.
"""
from fractions import Fraction as F
from itertools import product

Z=F(0); U=F(1); H=F(1,2)
RAW_WORDS=list(product((0,1), repeat=3))  # context G, first port X, second port Y


def iid(theta):
    return ((1-theta)**2, theta*(1-theta), theta*(1-theta), theta**2)


def raw_law(word_law):
    # G=0 and G=1 each have 1/2 mass, independent of the ordered ports.
    return {(g,x,y):H*word_law[2*x+y]
            for g,x,y in RAW_WORDS}


def tv(a,b):
    assert set(a)==set(b)
    return sum((abs(a[k]-b[k]) for k in a),Z)/2


def policy_kernel(raw, policy):
    """Public action B reveals Y only when G=0; C reveals Y only when G=1.

    pi is a deterministic tuple of four actions indexed by (G,X).
    Output path preserves (G,X,action,observable Y or 'MASK').
    """
    out={}
    for (g,x,y),p in raw.items():
        a=policy[2*g+x]
        visible=y if (a=='B' and g==0) or (a=='C' and g==1) else 'MASK'
        path=(g,x,a,visible)
        out[path]=out.get(path,Z)+p
    return out


def complete_tv(a,b):
    keys=set(a)|set(b)
    return sum((abs(a.get(k,Z)-b.get(k,Z)) for k in keys),Z)/2


def risk(original, sim, policy):
    return sum((complete_tv(policy_kernel(original[s],policy),
                           policy_kernel(sim[s],policy)) for s in range(3)),Z)/3

p0=(F(3,16),F(5,16),F(5,16),F(3,16))
p1=(F(1,8),F(3,8),F(3,8),F(1,8))
p2=iid(F(1,16))
mid=tuple((a+b)/2 for a,b in zip(p0,p1))
u=iid(H)
original=[raw_law(p) for p in (p0,p1,p2)]
free=[raw_law(mid),raw_law(mid),raw_law(p2)]
physical=[raw_law(u),raw_law(u),raw_law(p2)]
assert len(RAW_WORDS)==8 and all(len(v)==8 for v in original)
assert all(all(p>0 for p in v.values()) and sum(v.values(),Z)==U for v in original)
assert all(all(p>0 for p in v.values()) and sum(v.values(),Z)==U for v in free+physical)
assert mid==(F(5,32),F(11,32),F(11,32),F(5,32))
assert complete_tv(original[0],original[1])==F(1,8)
assert complete_tv(original[0],free[0])==complete_tv(original[1],free[1])==F(1,16)
assert complete_tv(original[0],physical[0])==F(1,8)
assert complete_tv(original[1],physical[1])==F(1,4)
assert complete_tv(original[2],physical[2])==Z

# The two positive-rational BRC sources have the same first-port marginal,
# while the third one forces any alternative label merge above the optimum.
for s in (0,1):
    pfirst=sum((v for (g,x,y),v in original[s].items() if x==1),Z)
    assert pfirst==H
pfirst2=sum((v for (g,x,y),v in original[2].items() if x==1),Z)
assert pfirst2==F(1,16)
forced_other_merge_lower=(H-pfirst2)/3
assert forced_other_merge_lower==F(7,48)>F(1,8)

policies=list(product(('B','C'),repeat=4))
assert len(policies)==16
reveal=('B','B','C','C')
assert reveal in policies
free_scores={pi:risk(original,free,pi) for pi in policies}
physical_scores={pi:risk(original,physical,pi) for pi in policies}
assert free_scores[reveal]==max(free_scores.values())==F(1,24)
assert physical_scores[reveal]==max(physical_scores.values())==F(1,8)
assert all(q<=F(1,24) for q in free_scores.values())
assert all(q<=F(1,8) for q in physical_scores.values())
assert free_scores[('B',)*4]==free_scores[('C',)*4]==F(1,48)
assert max(free_scores[('B',)*4],free_scores[('C',)*4])==F(1,48)

# Physical mixture universal algebra checks for 17 exact trial parameters,
# including all endpoints. This is a finite *cross-check*, not the continuum proof.
trial=[F(i,16) for i in range(17)]
for theta in trial:
    q=iid(theta)
    assert q[1]+q[2] <= H
    assert q[1]==q[2]
    assert sum(q,Z)==U
for k in range(17):
    w=F(k,16)
    q=tuple(w*iid(F(1,4))[i]+(U-w)*iid(F(3,4))[i] for i in range(4))
    assert q[1]+q[2]<=H

# Contrast: in an all-physical 3-to-2 instance, source-pair mixing is
# again a shared-IID port. No-gap theorem is proved at all policy horizons.
ph=[raw_law(iid(p)) for p in (F(1,4),H,F(3,4))]
pair_dists={(i,j):complete_tv(ph[i],ph[j]) for i,j in ((0,1),(0,2),(1,2))}
assert pair_dists=={(0,1):F(5,16),(0,2):H,(1,2):F(5,16)}
assert min(pair_dists.values())/3==F(5,48)
q01={key:(ph[0][key]+ph[1][key])/2 for key in RAW_WORDS}
assert q01==raw_law(tuple((iid(F(1,4))[i]+iid(H)[i])/2 for i in range(4)))
# one persistent Bernoulli choice of Theta=.25 or .5 each with 1/2
assert (complete_tv(ph[0],q01)+complete_tv(ph[1],q01))/3==F(5,48)

print('STAGE299B_POSITIVE_RATIONAL_ADAPTIVE_SHARED_PORT')
print('RAW_POSITIVE_BRANCHES=24; policies=16; mixed_probe=17 theta + 17 two-atom points')
print('FREE_ADAPTIVE_EXACT=',F(1,24))
print('SHARED_IID_ADAPTIVE_EXACT=',F(1,8))
print('STRICT_GAP_EXACT=',F(1,12))
print('FREE_FIXED_EXACT=',F(1,48))
print('ALTERNATIVE_MERGE_LOWER=',forced_other_merge_lower)
print('ALL_PHYSICAL_NO_GAP_EXAMPLE=',F(5,48))
print('STAGE299B_ADAPTIVE_SHARED_PORT_EXACT_PASS')
