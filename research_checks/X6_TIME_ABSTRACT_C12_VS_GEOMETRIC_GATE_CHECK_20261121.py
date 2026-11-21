#!/usr/bin/env python3
"""Check exact C12 event-clock factor on both source-defined shortest X6 native branches."""
from collections import Counter
import json

def neg(v): return tuple(-z for z in v)
def add(u,v): return tuple(a+b for a,b in zip(u,v))
e=[tuple(int(i==j) for i in range(6)) for j in range(3)]
a=e+[neg(x) for x in e]
z=(0,)*6
states=[(t,r) for t in ('S','I','O') for r in range(6)]
def C(s):
    t,r=s
    return a[r] if t=='S' else z if t=='I' else add(a[r],a[(r+1)%6])
def phi(s):
    t,r=s
    return (2*r+(t!='S'))%12
def succ(s):
    t,r=s
    return [('I',r),('O',r)] if t=='S' else [('S',(r+1)%6)]
checks=0
for s in states:
    for u in succ(s):
        assert (phi(u)-phi(s))%12==1
        checks+=1
fibers=Counter(phi(s) for s in states)
assert len(fibers)==12 and [fibers[k] for k in range(12)]==[1,2]*6
assert len({C(s) for s in states})==13
assert len({phi(('I',r)) for r in range(6)})==6
assert len({C(('I',r)) for r in range(6)})==1
for r in range(6):
    assert phi(('I',r))==phi(('O',r))
    assert C(('I',r))!=C(('O',r))
    checks+=3
# For t in 0..24, any branch selection yields the same abstract temporal residue.
for t in range(25):
    r=(t//2)%6
    options=[('S',r)] if t%2==0 else [('I',r),('O',r)]
    assert all(phi(s)==t%12 for s in options)
    checks+=len(options)
result={'schema':'X6_TIME_ABSTRACT_MICROSTEP_C12_CLOCK_V1','status':'EXACT_FINITE_EXECUTED','states':18,'abstract_clock_states':12,'fiber_sizes_in_phase_order':[fibers[k] for k in range(12)],'verified_microstep_arrows':24,'checks':checks,'mismatches':0,'same_Cell_different_phase_counterexample':{'Cell':list(z),'states':['I_0','I_1'],'phases':[phi(('I',0)),phi(('I',1))]},'same_phase_different_Cell_counterexample':{'phase':phi(('I',0)),'states':['I_0','O_0'],'Cells':[list(C(('I',0))),list(C(('O',0)))]},'source_boundary':'abstract physical microstep-event clock on both shortest branch possibilities; not the frozen geometric nonzero intermediate Gate C12 embedding'}
print(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True))
