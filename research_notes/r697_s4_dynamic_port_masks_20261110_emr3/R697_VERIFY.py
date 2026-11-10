#!/usr/bin/env python3
"""R697 exact verification using integers and fractions.Fraction."""
from itertools import combinations, permutations
from fractions import Fraction
from math import comb, factorial
import json

AXES=frozenset(range(4))
SETS=[frozenset(c) for k in range(5) for c in combinations(AXES,k)]
S4=list(permutations(range(4)))
assert len(SETS)==16 and len(S4)==24

def act(A,p): return frozenset(p[x] for x in A)
def sig(A,B): return (len(A),len(B),len(A & B))

# Orbit types are exactly (r,s,t).
orbits={}
for A in SETS:
    for B in SETS:
        orbits.setdefault(sig(A,B),set()).add((A,B))
assert len(orbits)==35 and sum(map(len,orbits.values()))==256
for key,pairs in orbits.items():
    a,b=next(iter(pairs))
    assert {(act(a,p),act(b,p)) for p in S4}==pairs
row={r:sum(k[0]==r for k in orbits) for r in range(5)}
assert list(row.values())==[5,8,9,8,5]
for (r,s,t),pairs in orbits.items():
    A=next(A for A in SETS if len(A)==r)
    assert sum(len(B)==s and len(B & A)==t for B in SETS)==comb(r,t)*comb(4-r,s-t)
assert sum(row.values())-5==30
v=1
for n in row.values(): v*=n
assert v==14400

# Count all allowed targets for deterministic equivariant update.
fixed_by_size={}
for A in SETS:
    stabilizer=[p for p in S4 if act(A,p)==A]
    targets={B for B in SETS if all(act(B,p)==B for p in stabilizer)}
    assert targets=={frozenset(),A,AXES.difference(A),AXES}
    fixed_by_size.setdefault(len(A),set()).add(len(targets))
assert [next(iter(fixed_by_size[r])) for r in range(5)]==[2,4,4,4,2]
assert 2*4*4*4*2==256

def drop(A,B):
    if not A: return Fraction(int(not B))
    return Fraction(1,len(A)) if B.issubset(A) and len(B)==len(A)-1 else Fraction(0)

h=Fraction(2,5)
def T(A,B):
    if not A: return Fraction(int(not B))
    return h*int(A==B)+(1-h)*drop(A,B)

for A in SETS:
    assert sum((drop(A,B) for B in SETS),Fraction())==1
    assert sum((T(A,B) for B in SETS),Fraction())==1
    for B in SETS:
        for p in S4:
            assert T(A,B)==T(act(A,p),act(B,p))
            assert drop(A,B)==drop(act(A,p),act(B,p))

Q={}
for r in range(5):
    for s in range(5):
        vals={sum((T(A,B) for B in SETS if len(B)==s),Fraction()) for A in SETS if len(A)==r}
        assert len(vals)==1
        Q[r,s]=next(iter(vals))
for r in range(1,5):
    assert Q[r,r]==h and Q[r,r-1]==1-h
assert Q[0,0]==1

# Ordered deletion trajectories: every sequence has mass (r-k)!/r!.
for r in range(1,5):
    A=frozenset(range(r))
    for k in range(r+1):
        hist=list(permutations(A,k))
        total=Fraction()
        for seq in hist:
            mass=Fraction(1)
            active=A
            for x in seq:
                mass*=Fraction(1,len(active));active=active-{x}
            assert mass==Fraction(factorial(r-k),factorial(r))
            total+=mass
        assert total==1

# Compare exact 16-state probability and its 5-state strong lump.
mass={A:Fraction(int(A==AXES)) for A in SETS}
small={r:Fraction(int(r==4)) for r in range(5)}
trace=[]
for n in range(13):
    projected={r:sum((mass[A] for A in SETS if len(A)==r),Fraction()) for r in range(5)}
    assert projected==small and sum(mass.values(),Fraction())==1
    expected=sum((Fraction(comb(n,j))*(1-h)**j*h**(n-j) for j in range(4,n+1)),Fraction())
    assert small[0]==expected
    trace.append({'n':n,'halt':[small[0].numerator,small[0].denominator]})
    mass={B:sum((mass[A]*T(A,B) for A in SETS),Fraction()) for B in SETS}
    small={s:sum((small[r]*Q[r,s] for r in range(5)),Fraction()) for s in range(5)}
assert trace[8]['halt']==[64557,78125]
assert Fraction(4,1)/(1-h)==Fraction(20,3)

evidence={
 'marker':'R697_S4_MASK_DYNAMICS_BRC_EXACT_PASS',
 'orbit_count':35,'pair_count':256,'permutations_checked':24,
 'orbit_modes_by_input_size':row, 'kernel_dimension':30,
 'equivariant_extreme_kernels':14400,'deterministic_equivariant_maps':256,
 'orbit_table':[{'r':r,'s':s,'t':t,'pairs':len(pairs),
                 'targets_per_input':comb(r,t)*comb(4-r,s-t)}
                for (r,s,t),pairs in sorted(orbits.items())],
 'h':[2,5], 'mean_halt_from_four':[20,3], 'trace':trace
}
print(evidence['marker'], 'HALT(8)=',trace[8]['halt'])
if __name__=='__main__':
    with open('R697_EVIDENCE.json','w',encoding='utf-8') as f:
        json.dump(evidence,f,indent=2,ensure_ascii=False)
