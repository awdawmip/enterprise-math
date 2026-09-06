#!/usr/bin/env python3
from collections import Counter
from itertools import product, permutations

# C6 branch patterns and shift-stabilizer memory size.
patterns=tuple(product((0,1),repeat=6))

def shift(b,k): return tuple(b[(r-k)%6] for r in range(6))
def stabilizer(b): return tuple(k for k in range(6) if shift(b,k)==b)
def memory_size(b): return 6//len(stabilizer(b))

cnt=Counter(memory_size(b) for b in patterns)
# divisors of 6 only
assert set(cnt)=={1,2,3,6}
assert cnt[1]==2
assert memory_size((0,1,0,1,0,1))==2
assert memory_size((0,0,1,0,0,1))==3
assert memory_size((0,0,0,0,0,1))==6

# Q-equivariant memoryless law means one-step shift invariant: only constants.
q_equivariant=[b for b in patterns if shift(b,1)==b]
assert q_equivariant==[(0,0,0,0,0,0),(1,1,1,1,1,1)]

# Token-symmetric deterministic branch triples under S3 are exactly III/OOO.
triples=tuple(product((0,1),repeat=3))
perms=tuple(permutations(range(3)))
def permute(t,p): return tuple(t[p[i]] for i in range(3))
symmetric=[t for t in triples if all(permute(t,p)==t for p in perms)]
assert symmetric==[(0,0,0),(1,1,1)]

# Exchangeable stochastic orbit classes are by OUTER count k=0..3.
orbits={k:[t for t in triples if sum(t)==k] for k in range(4)}
assert [len(orbits[k]) for k in range(4)]==[1,3,3,1]

# Local one-token expected branch area coefficient under p=O probability is 2p-1.
# Check for rational test probabilities by direct two-point expectation numerator.
from fractions import Fraction
for p in (Fraction(0),Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(1)):
    # I contributes -1, O contributes +1 in units of a wedge b
    exp=(1-p)*(-1)+p*(1)
    assert exp==2*p-1

print('PASS_X6_EQUIVARIANT_ROTATION_BRANCH_LAWS_V3')
print('C6_patterns',len(patterns))
print('phase_memory_class_counts',dict(sorted(cnt.items())))
print('memoryless_Q_equivariant_deterministic_sections',len(q_equivariant))
print('token_symmetric_joint_deterministic_sections',len(symmetric))
print('exchangeable_joint_orbit_sizes',[1,3,3,1])
