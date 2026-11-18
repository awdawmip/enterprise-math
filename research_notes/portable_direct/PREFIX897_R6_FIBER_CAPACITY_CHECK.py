#!/usr/bin/env python3
"""PREFIX-897 exact first-fiber pigeonhole census; no floating point."""
from math import gcd
P=32; N=1<<P; T=N*(P+1)
A,B=262145,524287
Q=range(A,B+1,2)
S={262147,280001,300001,320003,340007,360007,380003,400009,420001,440003,460001,480007,500383,510007,520001,524285}
AX={q for q in Q if any((2**h-1)%q==0 or (2**h+1)%q==0 for h in range(1,P))}
U=S|AX|{400011+2*j for j in range(256)}|{480011+2*j for j in range(256)}
assert len(U)==552

def fiber(q1,q2):
    return (P+1)*((N+q1-1)//q1)>q2

def interval(q):
    low=max(A,(T+q-1)//q)
    high=min(B,(P+1)*((N+q-1)//q)-1)
    low+=(low%2==0)
    high-=(high%2==0)
    return low,high

# Method A: weighted reciprocal-class accounting (without a symmetry set).
count=dict(first=0,both=0,symmetric=0,outside_U=0,outside_U_ZZ=0)
for q1 in Q:
    low,high=interval(q1)
    for q2 in range(low,high+1,2):
        assert q1*q2>=T and fiber(q1,q2)
        count['first']+=1
        reverse=fiber(q2,q1)
        count['both']+=reverse
        weight=1 if reverse else 2
        count['symmetric']+=weight
        if q1 not in U and q2 not in U:
            count['outside_U']+=weight
            if q1//gcd(q1,q2)*q2>=N:
                count['outside_U_ZZ']+=weight

# Method B: independent explicit set symmetrization.
X=set()
for q1 in Q:
    low,high=interval(q1)
    for q2 in range(low,high+1,2):
        assert fiber(q1,q2) and q1*q2>=T
        X.add((q1,q2))
reverse_X={(b,a) for a,b in X}
Y=X|reverse_X
assert count['first']==len(X)
assert count['both']==len(X&reverse_X)
assert count['symmetric']==len(Y)
assert count['outside_U']==sum(a not in U and b not in U for a,b in Y)
assert count['outside_U_ZZ']==sum(a not in U and b not in U and a//gcd(a,b)*b>=N for a,b in Y)

assert count=={'first':1016538,'both':629230,'symmetric':1403846,
               'outside_U':1393078,'outside_U_ZZ':1377112}
assert 7566243102+count['outside_U_ZZ']==7567620214
print({'schema':'PREFIX897_R6_FIBER_CAPACITY_V1',**count,
       'prior_prefix896_union':7566243102,
       'new_four_family_union':7567620214,
       'unexcluded_in_this_union':9612248970})
