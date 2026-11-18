#!/usr/bin/env python3
"""Exact all-f R5 global query-alphabet cardinality phase diagram. Python stdlib."""
import hashlib, itertools, json, pathlib, sys
H='50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
Q=1744659037213380157479321600000
D=1882951873548292168718745600000
raw=pathlib.Path(sys.argv[1]).read_bytes()
assert hashlib.sha256(raw).hexdigest()==H
s=json.loads(raw)
assert s['mask_count']==256
K=range(214,315)
N={k:tuple(map(int,s['counts_and_cohorts'][str(k)]['counts'])) for k in K}
assert all(len(N[k])==256 for k in K)
pairs=list(itertools.combinations(range(256),2))
assert len(pairs)==32640
assert max(len(set(zip(N[k],N[t]))) for k in K for t in range(k+1,315))==128

def gap(k,a,b):return abs(N[k][a]-N[k][b])
def budgets(a,b,tau):return [k for k in K if gap(k,a,b)>tau]
def cover(ks,tau):return all(any(gap(k,a,b)>tau for k in ks) for a,b in pairs)
force={(0,1):list(range(216,221)),(0,64):list(range(224,291)),
       (16,32):list(range(298,312))}
for (a,b),ks in force.items():
    assert budgets(a,b,Q-1)==ks and budgets(a,b,Q)==ks
counter={216:(11,14),217:(4,10),218:(9,12),219:(9,12),220:(9,12)}
for k,(a,b) in counter.items():
    assert gap(k,a,b)<=Q
    assert all(gap(j,a,b)==0 for j in range(222,315))
extra={(9,12):[215,216,217],(4,10):[217,218,219],(11,14):[217,218]}
for (a,b),ks in extra.items(): assert budgets(a,b,Q-1)==ks
assert cover((217,224,298),Q-1)
assert cover((217,218,224,298),D-1)
# Every choice within the 67-by-14 near-Q families has the same pairwise separation signature.
def mask(k):return sum(1<<i for i,(a,b) in enumerate(pairs) if gap(k,a,b)>=Q)
assert all(mask(k)==mask(224) for k in range(224,291))
assert all(mask(k)==mask(298) for k in range(298,312))
assert mask(217)|mask(224)|mask(298)==(1<<32640)-1
assert max(gap(k,11,14) for k in K)==D
assert min(max(gap(k,a,b) for k in (217,224,298)) for a,b in pairs)==Q
assert min(max(gap(k,a,b) for k in (217,218,224,298)) for a,b in pairs)==D
print(json.dumps({'pass':'R5_QUERY_ALPHABET_ALL_F','Q':str(Q),'D':str(D),
 'alphabet_if_tau_less_Q':[217,224,298],
 'alphabet_if_Q_less_equal_tau_less_D':[217,218,224,298],
 'no_finite_identification_if_tau_greater_equal_D':True,
 'max_two_query_joint_classes':128,'checked_pairs':32640,
 'near_Q_exact_successful_three_alphabets':938,
 'unique_cheapest_near_Q_triple':[217,224,298],
 'frozen_input_sha256':H},indent=2))
