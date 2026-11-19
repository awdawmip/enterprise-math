"""Finite exact comparison ledger for R11's full 144 one-delay inputs.

Standard-library integer state comparison only. For the physical reference
and repaired BRC kernels use delay_source.py with the original archive.
--cases exports the compact full-prefix certificates as JSON lines.
"""
import argparse
import hashlib
import itertools
import json
from collections import Counter
from math import comb
from pathlib import Path

LOC=tuple(range(728,736))
SLOTS=(((1,1),(2,2)),((0,1),(1,2),(2,1),(2,3)))


def background(a):
    parity=a%2  # a=0 is physical time 1
    q=(2,1,1) if not parity else (1,1,0)
    b=2 if not parity else 1
    return (tuple([q]*8),{(v,j,j,r):1 for v in range(8) for j,r in SLOTS[parity]},
            tuple([(0,)*9]*8),tuple(b if i in LOC else (a+1)%3 for i in range(5832)))


def step(s):
    q,pp,ww,bb=s
    q=[list(row) for row in q]; pp2=Counter();b=[(old+1)%3 for old in bb];flow=Counter()
    for (v,j,role,r),n in pp.items():
        if r>1:pp2[v,j,role,r-1]+=n
        else:
            q[v^(4>>j)][role]+=n
            flow[f'handoff:{v}:{j}:{role}']+=n
    for v,g in enumerate(LOC):
        if b[g]==0 and min(q[v])>0:
            b[g]=1;q[v]=[x-1 for x in q[v]]
            flow[f'groups:{v}:0']+=1
            for j in range(3):
                pp2[v,j,j,j+1]+=1
                flow[f'commit:{v}:{j}:{j}']+=1
    return tuple(map(tuple,q)),dict(pp2),ww,tuple(b),dict(flow)


def inject(s,v,j,r):
    q,pp,ww,bb=s
    p=dict(pp);assert p.pop((v,j,j,r))==1
    key=(v,j,j,r+1);p[key]=p.get(key,0)+1
    return q,p,ww,bb


def patch(state,base):
    def rows(st,v):
        q,p,w,b=st
        return [v,list(q[v]),sorted([j,role,r,n] for (w0,j,role,r),n in p.items() if w0==v),
                list(w[v]),b[LOC[v]]]
    assert all(x==y for i,(x,y) in enumerate(zip(state[3],base[3])) if i not in LOC)
    return [rows(state,v) for v in range(8) if rows(state,v)!=rows(base,v)]


def inventory(st):
    q,p,w,b=st
    values=[list(row) for row in q]
    for (v,j,role,r),n in p.items():
        assert role==j
        values[v^(4>>j)][j]+=n
    return values


def state_bound():
    # Directed node->role inventory, opposite edge sum four, remaining
    # differences an integral gradient of the rooted release potential.
    even=[0,3,5,6];odd=[1,2,4,7]; fields=0;weighted=0
    for values in itertools.product(range(-4,5),repeat=3):
        potential=dict(zip(even,(0,*values)))
        count=weight=1
        for u in odd:
            neighbors=[potential[u^(4>>j)] for j in range(3)]
            options=range(max(neighbors)-2,min(neighbors)+3)
            count*=len(options); local=0
            for y in options:
                prob=1
                for j,z in enumerate(neighbors):
                    diff=y-z
                    prob*=comb(2+diff+j+1,j+1)*comb(2-diff+j+1,j+1)
                local+=prob
            weight*=local
        fields+=count;weighted+=weight
    return {'directed_inventories':24,'independent_conservation_laws':17,
            'integer_gradient_profiles':fields,'waiting_pending_allocations_upper':weighted,
            'including_material_and_background_clock_upper':9*weighted,
            'previous_upper':3**9*comb(119,71)}


def main(cases_path):
    bg=[background(a) for a in range(6)]
    flows=[]
    for a,s in enumerate(bg):
        *out,inc=step(s);assert tuple(out)==bg[(a+1)%6]
        assert inventory(s)==[[2]*3 for _ in range(8)]
        flows.append(inc)
    cases=[];times=Counter();maxpending=0
    for a,s0 in enumerate(bg):
        for v in range(8):
            for j,r in SLOTS[a%2]:
                st=inject(s0,v,j,r);obs=Counter();steps=[];diff={}
                for h in range(r+2):
                    px=patch(st,bg[(a+h)%6])
                    if h<r:assert [z[0] for z in px]==[v]
                    elif h==r:assert {z[0] for z in px}=={v,v^(4>>j)}
                    else:assert not px
                    if h<=r:assert all(st!=s for s in bg)
                    assert inventory(st)==[[2]*3 for _ in range(8)]
                    assert sum(sum(row) for row in st[0])+sum(st[1].values())==48
                    for z in diff:obs[z]+=diff[z]
                    cum={k:n for k,n in obs.items() if n}
                    label=f'handoff:{v}:{j}:{j}'
                    assert cum==({label:-1} if h==r else {})
                    steps.append(dict(h=h,patch=px,flow_delta=cum,inc_delta=diff))
                    maxpending=max(maxpending,len(st[1]))
                    if h<=r:
                        *out,inc=step(st);st=tuple(out)
                        target=flows[(a+h)%6]
                        diff={z:n for z in target.keys()|inc.keys() if (n:=inc.get(z,0)-target.get(z,0))}
                times[r+1]+=1
                cases.append(dict(a=a,v=v,j=j,role=j,r=r,ticks=r+1,phase_shift=0,
                             classification='RECOVERED',budget=256,steps=steps,full_checks=256,
                             aligned_tail='same_clock_cycle',max_distance=1,max_support=2))
    assert len(cases)==144 and times=={2:72,3:48,4:24}
    lines=b''.join((json.dumps(row,sort_keys=True,separators=(',',':'))+'\n').encode() for row in cases)
    if cases_path:cases_path.write_bytes(lines)
    return dict(scope='8 labelled material nodes / all six full source phases / one occupied slot delayed once',
                candidate_count=len(cases),checked_source_horizon=256,first_recovery=dict(sorted(times.items())),
                maximum_positive_pending_slots_prefix=maxpending,first_recovery_prefix_ticks=sum(r['ticks'] for r in cases),
                original_historical_regression={'phase':0,'node':0,'port':2,'remaining':2,'source':'R11 counterexample from physical time 1'},
                injected_remaining_4=sum(c['r']==3 for c in cases),above_emission_duration=sum(c['r']+1>c['j']+1 for c in cases),
                phases_analytic_subset_inputs=3*(2**16+2**32),
                local_recomputed_material_nodes=sum(4*c['r']+6 for c in cases),
                ever_nonzero_cumulative_readings=['handoff:v:j:j at elapsed t=r, value -1'],
                certificate_lines_sha256=hashlib.sha256(lines).hexdigest(),finite_state_bound=state_bound())


if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--cases',type=Path);args=ap.parse_args()
    print(json.dumps(main(args.cases),sort_keys=True,indent=2))
