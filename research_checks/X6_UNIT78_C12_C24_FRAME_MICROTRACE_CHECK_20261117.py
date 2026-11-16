#!/usr/bin/env python3
"""Exact six-axis C12->C24 frame-preserving history-lift certificate.

Scope: twenty ascending native triads, both orientations and the all-OUTER
twelve-microstate trace. The C24 cover adds a history bit, not a spatial axis.
"""
from itertools import combinations
from collections import defaultdict, Counter
import json

N=6
ID=tuple(range(1,N+1))

def require(c, message):
    if not c:
        raise AssertionError(message)

def compose(g,h):
    return tuple((1 if x>0 else -1)*g[abs(x)-1] for x in h)

def power(g,n):
    out=ID
    for _ in range(n):
        out=compose(g,out)
    return out

def q_triad(S):
    i,j,k=S
    g=list(ID)
    g[i],g[j],g[k]=-(j+1),-(k+1),-(i+1)
    return tuple(g)

def act(g,z):
    out=[0]*N
    for a,coef in enumerate(z):
        if coef:
            v=g[a]
            out[abs(v)-1] += (1 if v>0 else -1)*coef
    return tuple(out)

def unit(i,sign=1):
    z=[0]*N
    z[i]=sign
    return tuple(z)

def add(a,b):
    return tuple(x+y for x,y in zip(a,b))

def outer_cycle(phases):
    return tuple(s for t in range(6) for s in
                 (phases[t],add(phases[t],phases[(t+1)%6])))

def lift_step(k,sheet):
    return (k+1)%12, sheet^(int(k==11))

def check():
    fibers=defaultdict(list)
    sheet_state_count=0
    macro_checks=0
    for S in combinations(range(6),3):
        q=q_triad(S)
        require(power(q,6)==ID,"q^6")
        for eps in (1,-1):
            rot=q if eps==1 else power(q,5)
            phases=[unit(S[0])]
            for t in range(5):
                phases.append(act(rot,phases[-1]))
            require(len(set(phases))==6,"native macro cycle")
            require(act(rot,phases[-1])==phases[0],"macro closes")
            cycle=outer_cycle(phases)
            require(len(cycle)==12 and len(set(cycle))==12,"C12 outer microstates")
            root=cycle[3]
            j,k=S[1:]
            expected=add(unit(k),unit(j,-1)) if eps==1 else add(unit(j),unit(k,-1))
            require(root==expected,"typed signed root")
            expected1=unit(k) if eps==1 else unit(j)
            expected2=add(unit(k),unit(S[0],-1)) if eps==1 else add(unit(j),unit(S[0],-1))
            require(cycle[4]==expected1 and cycle[5]==expected2,"root micro future")
            fibers[root].append({"S":S,"eps":eps,"next1":cycle[4],"next2":cycle[5]})
            for k0 in range(12):
                require(cycle[(k0+2)%12]==act(rot,cycle[k0]),"macro equals two microsteps")
                macro_checks+=1
            for k0 in range(12):
                for s0 in (0,1):
                    cur=(k0,s0)
                    seen=set()
                    for t in range(24):
                        require(cur not in seen,"lift period <24")
                        seen.add(cur)
                        k1,s1=lift_step(*cur)
                        require(k1==(k0+t+1)%12,"lift projection")
                        cur=(k1,s1)
                    require(cur==(k0,s0),"lift exactly period24")
                    cur=(k0,s0)
                    for _ in range(12):
                        cur=lift_step(*cur)
                    require(cur==(k0,1-s0),"nontrivial sheet holonomy")
                    sheet_state_count+=1
    require(len(fibers)==20,"20 signed root cells")
    sizes=Counter(len(v) for v in fibers.values())
    require(dict(sizes)=={1:8,2:6,3:4,4:2},"root fiber histogram")
    multi=0
    for root,entries in fibers.items():
        require(len({e["next1"] for e in entries})==1,"one-step root futures")
        require(len({e["next2"] for e in entries})==len(entries),"two-step frame split")
        multi+=len(entries)>1
    require(multi==12,"ambiguous two-step roots")
    require(sheet_state_count==960 and macro_checks==480,"coverage")
    return {"triads":20,"orientations_per_triad":2,"labeled_root_observations":40,
            "distinct_signed_root_cells":len(fibers),
            "root_fiber_histogram":dict(sorted(sizes.items())),
            "one_microstep_factors_through_root":True,
            "two_microstep_ambiguous_roots":multi,
            "distinct_two_step_labeled_root_successors":40,
            "macro_two_microstep_matches_signed_q_checks":macro_checks,
            "C24_history_lift_states":sheet_state_count,
            "sheet_holonomy_after_12_microsteps":"(k,b)->(k,1-b)",
            "lift_minimal_sheet_bits":1,"max_joint_frame_sheet_states_at_root":8,
            "worst_case_extra_bits_beyond_known_root_phase":3,
            "native_C24_claimed":False,
            "author_scope":"EXACT_FINITE_ALL20_ORIENTED_OUTER;_UNREVIEWED_NOT_ADMITTED"}

if __name__=="__main__":
    print(json.dumps(check(),sort_keys=True,ensure_ascii=False,indent=2))
