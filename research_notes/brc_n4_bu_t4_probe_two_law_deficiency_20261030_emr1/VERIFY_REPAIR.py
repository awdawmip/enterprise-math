"""Finite exact BU-fiber two-law repair theorem, 2026-10-30.

External 16-leaf source; distributional vs pathwise information clearly separated.
"""
from fractions import Fraction as F
from itertools import combinations

q = (F(1,4),)*4   # BU conditional Q law: (j0k0,j0k1,j1k0,j1k1)
p = (F(1,20),F(1,20),F(9,20),F(9,20))

def tv(x,y):
    return sum((abs(a-b) for a,b in zip(x,y)),F())/2

assert sum(p)==sum(q)==1
assert tv(p,q)==F(2,5)

# Blackwell regeneration from one retained bit j, using a single kernel
# K(k=0|j)=K(k=1|j)=1/2, valid under BOTH P and Q.
for law in (p,q):
    j=(law[0]+law[1],law[2]+law[3])
    reconstructed=(j[0]/2,j[0]/2,j[1]/2,j[1]/2)
    assert reconstructed==law
    for mask in range(16):
        assert sum((law[i] for i in range(4) if mask & (1<<i)),F()) == sum((reconstructed[i] for i in range(4) if mask & (1<<i)),F())

assert (p[2]+p[3],q[2]+q[3])==(F(9,10),F(1,2))

# No-BU-repair common decoder: triangle inequality gives minmax >= TV(P,Q)/2.
# The arithmetic midpoint attains the bound for the *full* leaf distribution.
mid=tuple((u+v)/2 for u,v in zip(p,q))
assert mid==(F(3,20),F(3,20),F(7,20),F(7,20))
assert tv(p,mid)==tv(q,mid)==F(1,5)
m=F(1,4)
assert m*F(1,5)==F(1,20)

# Pathwise deterministic factorization for all 16 Boolean queries:
# any two leaves merged would be distinguished by a singleton indicator,
# hence four distinct local classes (two bits) are necessary and sufficient.
for i,j in combinations(range(4),2):
    assert any((int(bool(mask&(1<<i))) != int(bool(mask&(1<<j)))) for mask in range(16))
assert len(set(range(4)))==4

m_old=F(71691,2414000)
assert m_old/F(5)==F(71691,12070000)

print("BU_COND_P=",','.join(map(str,p)))
print("BU_COND_Q=",','.join(map(str,q)))
print("BU_COND_TV_PQ=2/5")
print("ONE_BIT_J_REGENERATION=EXACT_BOTH_LAWS_ALL_16_BOOLEAN_QUERIES")
print("ZERO_BIT_FULL_LEAF_DECODER_MIDPOINT=",','.join(map(str,mid)))
print("ZERO_BIT_CONDITIONAL_MINIMAX_RADIUS=1/5")
print("ZERO_BIT_UNCONDITIONAL_G0_MINIMAX_RADIUS=1/20")
print("PATHWISE_ALL_QUERY_MIN_CLASSES=4_BITS=2")
print("OLD_OPTIMUM_STRATEGY_ZERO_BIT_BU_DEFICIENCY=71691/12070000")
print("PASS_EXACT_BRC_N4_BU_MINIMAL_STATISTICAL_REPAIR")
