#!/usr/bin/env python3
"""Exact finite checks for Ori6 event charge, hidden-observer threshold and odd coset."""
from itertools import permutations, product
from collections import Counter

N=6
S6=tuple(permutations(range(N)))

def parity(p): return sum(p[i]>p[j] for i in range(N) for j in range(i+1,N))%2
A6=tuple(p for p in S6 if parity(p)==0)
ODD=tuple(p for p in S6 if parity(p)==1)
assert len(A6)==len(ODD)==360

def compose(p,q): return tuple(p[q[i]] for i in range(N))
def inv(p):
    out=[0]*N
    for i,j in enumerate(p): out[j]=i
    return tuple(out)

# Ori6 is a homomorphism S6 -> C2.
for p in S6:
    for q in ((0,1,2,3,4,5),(1,0,2,3,4,5),(1,2,0,3,4,5)):
        assert parity(compose(p,q))==(parity(p)^parity(q))

# A6 is normal index 2; every odd element is one coset and one double coset.
o=(1,0,2,3,4,5)
left={compose(r,o) for r in A6}
right={compose(o,r) for r in A6}
double={compose(compose(r,o),s) for r in A6 for s in A6}
assert left==right==set(ODD)==double

# Products of any current charge-zero events stay charge-zero.
current_generators=(
    (1,2,0,3,4,5), # 3-cycle
    (0,1,2,4,5,3), # another 3-cycle on complement
    (1,0,3,2,4,5), # double transposition = even chart lift example
)
assert all(parity(g)==0 for g in current_generators)
for word in product(range(len(current_generators)),repeat=5):
    x=tuple(range(N))
    charge=0
    for k in word:
        x=compose(current_generators[k],x)
        charge ^= parity(current_generators[k])
    assert parity(x)==charge==0

# Ordered k-axis observation: stabilizer fixes the first k visible axes pointwise.
# It contains odd permutations iff at least two axes remain hidden.
stab_stats={}
for k in range(7):
    stab=[p for p in S6 if all(p[i]==i for i in range(k))]
    c=Counter(parity(p) for p in stab)
    stab_stats[k]=(len(stab),c.get(0,0),c.get(1,0))
    assert len(stab)==__import__('math').factorial(N-k)
    if k<=4:
        assert c[0]==c[1]
    else:
        assert c.get(1,0)==0
assert stab_stats[3]==(6,3,3)
assert stab_stats[4]==(2,1,1)
assert stab_stats[5]==(1,1,0)

# Unoriented selected 3-set and cyclically oriented 3-chart also have equal even/odd
# stabilizer halves, so neither observer detects Ori6.
S=frozenset((0,1,2))
set_stab=[p for p in S6 if frozenset(p[i] for i in S)==S]
assert len(set_stab)==36 and Counter(parity(p) for p in set_stab)==Counter({0:18,1:18})
P=frozenset(((0,1),(1,2),(2,0)))
def act_passage(p,P): return frozenset((p[a],p[b]) for a,b in P)
pass_stab=[p for p in S6 if act_passage(p,P)==P]
assert len(pass_stab)==18 and Counter(parity(p) for p in pass_stab)==Counter({0:9,1:9})

# Odd hidden-complement transposition is completely invisible on an ordered 3-axis view.
hidden_swap=(0,1,2,4,3,5)
assert parity(hidden_swap)==1
assert hidden_swap[:3]==(0,1,2)

# Charge ledger: parity of total frame event is parity of odd-event count.
events=((1,2,0,3,4,5),o,(0,1,2,4,5,3),o,o)
x=tuple(range(N)); odd_count=0
for e in events:
    x=compose(e,x); odd_count+=parity(e)
assert parity(x)==odd_count%2

print('PASS_X6_ORI6_EVENT_CHARGE_V8')
print('even_odd_coset_sizes',(len(A6),len(ODD)))
print('odd_double_coset_count',1)
print('ordered_visible_axis_stabilizers',stab_stats)
print('minimum_ordered_visible_axes_for_Ori6_detection',5)
print('selected_3set_even_odd_stabilizer',(18,18))
print('oriented_3chart_even_odd_stabilizer',(9,9))
print('current_even_event_language_changes_Ori6',False)
print('Ori6_charge_is_odd_event_parity',True)
