#!/usr/bin/env python3
"""Exact finite check for a conditional signed-Port whole-triad C12 loop model.
No P000 physical port law, independent fiber sensor, or admission is asserted.
"""
import json
from pathlib import Path
from math import gcd

assertions = 0

def check(condition):
    global assertions
    assertions += 1
    assert condition

def add(a,b):
    return tuple(x+y for x,y in zip(a,b))

def sub(a,b):
    return tuple(x-y for x,y in zip(a,b))

def neg(a):
    return tuple(-x for x in a)

unit = [tuple(int(i==j) for i in range(6)) for j in range(3)]
shell = unit + [neg(u) for u in unit]
cycle = []
for r in range(6):
    cycle += [shell[r], add(shell[r], shell[(r+1)%6])]
check(len(cycle)==12)
check(len(set(cycle))==12)

steps = [sub(cycle[(q+1)%12],cycle[q]) for q in range(12)]
check(all(sum(abs(x) for x in d)==1 for d in steps))
for k in range(6):
    check(cycle[2*k] == shell[k])
    check(cycle[2*k+1] == add(shell[k],shell[(k+1)%6]))
    check(steps[2*k]==shell[(k+1)%6])
    check(steps[2*k+1]==neg(shell[k]))

for s in [1,-1]:
    counts = {p:0 for p in unit+[neg(x) for x in unit]}
    for q in range(12):
        d = sub(cycle[(q+s)%12],cycle[q]);counts[d]+=1
        check(sum(abs(x) for x in d)==1)
    check(all(v==2 for v in counts.values()))
    check(sum(v for p,v in counts.items() if -1 in p)==6)

# Distinguish two OUTER directed exits at the *same native Cell*.
for q in range(12):
    next_fwd=cycle[(q+1)%12];next_back=cycle[(q-1)%12]
    check(next_fwd!=next_back)
    check(sub(next_fwd,cycle[q])!=sub(next_back,cycle[q]))

# Single labeled intact positive frame stays on exactly one occupied Cell.
frame=(0,1,2)

def run(modulus, orientation, loops, with_fiber=True):
    assert modulus % 6 == 0 and orientation in (-1,1)
    occupied={cycle[0]:frame}
    cell=cycle[0];q=0;z=0
    # Assumed *directed* available signed ports, not a P000 physical admission.
    weights={5:3,10:3}
    z_at_return=[]
    for t in range(loops*12):
        qnext=(q+orientation)%12
        nextcell=cycle[qnext]
        dx=sub(nextcell,cell)
        check(sum(abs(v) for v in dx)==1)
        check(occupied.get(cell)==frame)
        check(nextcell not in occupied)
        del occupied[cell]
        occupied[nextcell]=frame
        if with_fiber:
            crossed_edge=q if orientation==1 else qnext
            z=(z+orientation*weights.get(crossed_edge,0))%modulus
        cell=nextcell;q=qnext
        check(len(occupied)==1 and occupied.get(cell)==frame)
        if (t+1)%12==0:
            check(q==0 and cell==cycle[0])
            check(occupied=={cycle[0]:frame})
            z_at_return.append(z)
            if with_fiber:
                check(z==(orientation*(t+1)//12*6)%modulus)
            else:check(z==0)
    return z_at_return

results={}
for m in range(0,6):
    N=6*(2**m)
    order=N//gcd(N,6)
    forward=run(N,1,order+1)
    reverse=run(N,-1,order+1)
    check(forward[-1]==6%N)
    check(reverse[-1]==-6%N)
    check(forward[order-1]==0 and reverse[order-1]==0)
    check(len(set([0]+forward[:order-1]))==order)
    check(len(set([0]+reverse[:order-1]))==order)
    check(run(N,1,3,with_fiber=False)==[0,0,0])
    results[f'C{N}']={'order_of_6':order,'minimum_fixed_origin_loop_memory_bits':m,'minimum_combined_chirality_and_loop_memory_bits':m+1,'minimum_combined_chirality_and_loop_states':2**(m+1),'forward_one_lap':6%N,'reverse_one_lap':(-6)%N,'zero_fiber_3_laps':[0,0,0]}

# Minimal reachable-orbit compression: at each Cell keep only k modulo 2**m,
# with z(q,k) = prefix(q) + 6k modulo 6*2**m.
# This is the exact original two-edge 3+3 cochain on one initial orbit,
# not an assertion that arbitrary C_N initial fibers only have 2**m states.
weights={5:3,10:3}
prefix=[0]
for q in range(11):
    prefix.append(prefix[-1]+weights.get(q,0))
for m in range(6):
    M=2**m;N=6*M
    for q in range(12):
        for k in range(M):
            for orientation in (-1,1):
                qnext=(q+orientation)%12
                knew=(k+(1 if q==11 else 0))%M if orientation==1 else (k-(1 if q==0 else 0))%M
                previous=(prefix[q]+6*k)%N
                following=(prefix[qnext]+6*knew)%N
                traversed_edge=q if orientation==1 else qnext
                check((following-previous)%N==(orientation*weights.get(traversed_edge,0))%N)
                check((qnext-orientation)%12==q)

# Test discrete inverse correctness on all 12 positions, all C24 precision fibers.
for q in range(12):
    for z in range(24):
        for s in [-1,1]:
            qnext=(q+s)%12
            edge=q if s==1 else qnext
            znext=(z+s*{5:3,10:3}.get(edge,0))%24
            back_edge=q if s==1 else qnext
            zback=(znext-s*{5:3,10:3}.get(back_edge,0))%24
            check(zback==z)
            check((qnext-s)%12==q)

out={'schema':'EM_EXACT_CONDITIONAL_SIGNED_PORT_C24_GUARD_V1','unit':'Unit241','status':'EXACT_FINITE_EXECUTED_UNREVIEWED_NOT_ADMITTED','assertions':assertions,'failed_assertions':0,'outer_cycle_distinct_native_cells':12,'chirality_minimum_hidden_states_at_fixed_cell':2,'C6_to_C192_fibers':results,'signed_port_assumption':'ALL_REQUIRED_SIGNED_DIRECTED_PORTS_AVAILABLE','physical_precision_fiber_law_admitted':False,'source_frozen_pin':'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389'}
path=Path(__file__).with_name('X6_TIME_SIGNED_PORT_CHIRAL_GUARD_AND_C24_FIBER_RESULTS_20261121_1900.json')
path.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(out,ensure_ascii=False))
