#!/usr/bin/env python3
"""EC49FQK independent complete-bitmask Bellman checker.

Requires frozen_original_master.txt and EC49FPG_PROFILE.csv, SHA256s checked
in EC49FQJ_NATIVE_DATA.load_native, and EC49FQJ_NATIVE_DATA.py from PR #2542.
Execute: python EC49FQK_VERIFY.py frozen_original_master.txt EC49FPG_PROFILE.csv
The separate portable archive contains identical inputs and the extended
independent replay / witness / SHA256 validation program.
"""
from collections import defaultdict
from functools import lru_cache
from fractions import Fraction
import sys
from EC49FQJ_NATIVE_DATA import load_native

V, m, reps = load_native(sys.argv[1], sys.argv[2])
assert len(V)==228 and len(m)==141 and sum(m)==310
N=len(m); FULL=(1<<N)-1
parts={}
response=[]
for q, values in enumerate(V):
    fibers={}
    for i,value in enumerate(values):
        fibers[value]=fibers.get(value,0)|(1<<i)
    blocks=tuple(fibers.values())
    response.append(blocks)
    parts.setdefault(tuple(sorted(blocks)),q)
assert len(parts)==209

def indices(mask):
    while mask:
        bit=mask&-mask
        yield bit.bit_length()-1
        mask^=bit

def solve(a,b,x):
    """All integer arithmetic, no depth limit, 228 physical forced-first checks."""
    W=[310*(b-a)+141*a*z for z in m]
    total=sum(W)
    assert total==141*310*b
    @lru_cache(None)
    def mass(s):return sum(W[i] for i in indices(s))
    @lru_cache(None)
    def optimum(s):
        if s.bit_count()<2:return 0
        w=mass(s); best=10**40
        for blocks,q in parts.items():
            childs=[v for block in blocks if (v:=block&s)]
            if len(childs)<2:continue
            cost=x if q>=144 else 1
            live=[v for v in childs if v.bit_count()>1]
            lower=cost*w+sum(mass(y) for y in live)
            if lower>=best:continue
            candidate=cost*w
            for y in live:
                candidate+=optimum(y)
                if candidate>=best:break
            if candidate<best:best=candidate
        assert best<10**40
        return best
    val=optimum(FULL)
    forced=[]
    for q, blocks in enumerate(response):
        if len(blocks)<2:forced.append(None);continue
        forced.append((x if q>=144 else 1)*total+
                      sum(optimum(z) for z in blocks if z.bit_count()>1))
    return Fraction(val,total),[q for q,c in enumerate(forced) if c==val],optimum.cache_info().currsize

def predicted(lam,x):
    if x<=3:uR,uT,mR,mT=5,293,5,704
    else:uR,uT,mR,mT=4,296,4,707
    return (1-lam)*Fraction(uR*x+uT,141)+lam*Fraction(mR*x+mT,310)

# Four load-bearing new corners, six more exact independent controls.
expected={
 (155,1847,1):(Fraction(7861,3694),[32,34,140,142]),
 (155,1847,2):(Fraction(3993,1847),[140,142]),
 (155,1847,3):(Fraction(8111,3694),[140,142]),
 (155,1847,4):(Fraction(8211,3694),[140,142]),
 (620,3299,1):(Fraction(7080,3299),[16,23,140,142]),
 (620,3299,2):(Fraction(7185,3299),[16,23,140,142]),
 (620,3299,3):(Fraction(7290,3299),[16,23,140,142]),
 (620,3299,4):(Fraction(7374,3299),[16,23,140,142]),
 (620,3299,5):(Fraction(7458,3299),[16,23,140,142]),
 (1,5,4):(Fraction(244312,109275),[16,23])
}
for (a,b,x),(want,first) in expected.items():
    got,actions,nstates=solve(a,b,x)
    assert (got,actions)==(want,first),(a,b,x,got,actions)
    assert (got==predicted(Fraction(a,b),x))==(Fraction(155,1847)<=Fraction(a,b)<=Fraction(620,3299))
    print("BELL_PASS",a,b,x,str(got),actions,nstates,flush=True)

# Terminal fibers and exact four-required-root-observations lower bound.
terminal_fibers=defaultdict(list)
for i in range(N):
    terminal_fibers[tuple(V[q][i] for q in range(144))].append(i)
pairs=[z for z in terminal_fibers.values() if len(z)>1]
assert len(terminal_fibers)==139 and len(pairs)==2 and all(len(z)==2 for z in pairs)
assert all(m[i]==1 for pair in pairs for i in pair)
assert sorted(sorted(reps[i] for i in pair) for pair in pairs)==[[17928,38165],[24541,38166]]
print("FIBER_FOUR_ROOT_LOWER_BOUND_PASS",flush=True)

# Symbolically check the exact sharp prior thresholds; native correct
# witness-tree replay and complete machine certs are supplied in the archive.
alpha=Fraction(155,1847); beta=Fraction(620,3299)
lo=lambda z:-2*(1-z)/141+48*z/310
hi=lambda z: 2*(1-z)/141-19*z/310
assert lo(alpha)==0 and lo(0)<0
assert hi(beta)==0 and hi(Fraction(1,5))<0
print("EC49FQK_INDEPENDENT_EXACT_BELLMAN_SHARP_RAY_PASS",flush=True)
