#!/usr/bin/env python3
"""R665: exact J(6,3) V17 parity descent and three-valued histogram fiber."""
from collections import Counter
from itertools import combinations, permutations
import json
from pathlib import Path
O=(0,1,2); ID=O; RHO=(1,2,0); TAU=(0,2,1)
V=tuple(combinations(range(6),3))
N={u:tuple(v for v in V if len(set(u)&set(v))==2) for u in V}
def mul(a,b):return tuple(a[b[i]] for i in range(3))
def pw(a,n):
    x=ID
    for _ in range(n): x=mul(x,a)
    return x
def parity(a):return sum(a[i]>a[j] for i in range(3) for j in range(i+1,3))%2
def edge(u,v):
    leave=next(iter(set(u)-set(v))); enter=next(iter(set(v)-set(u)))
    return tuple(u.index(leave if t==enter else t) for t in v)
def step(u,v,s):
    leave=next(iter(set(u)-set(v))); enter=next(iter(set(v)-set(u)))
    d=dict(zip(u,s));d[enter]=d[leave]
    return tuple(d[t] for t in v)
def enc(h):
    q=parity(h)
    for r in range(3):
        if mul(pw(RHO,r),pw(TAU,q))==h:return (r,q)
    raise AssertionError(h)
def dec(r,p):return mul(pw(RHO,r),pw(TAU,p))
def run(w):
    h=ID; r=p=0; hist=Counter()
    for u,v in zip(w,w[1:]):
        assert v in N[u]
        s,q=enc(edge(u,v));r=(r+(-1)**p*s)%3;p^=q
        h=step(u,v,h);hist[u,v]+=1
        assert h==dec(r,p)
    hist=tuple(sorted(hist.items()))
    assert p==sum(z*parity(edge(*e)) for e,z in hist)%2
    return h,r,p,hist
arc_checks=frame_checks=0
for u in V:
    for v in N[u]:
        pi=edge(u,v);arc_checks+=1
        assert mul(pi,edge(v,u))==ID
        i=u.index(next(iter(set(u)-set(v))))
        j=v.index(next(iter(set(v)-set(u))))
        assert parity(pi)==(i+j)%2
        for h in permutations(range(3)):
            assert step(u,v,h)==mul(h,pi)
            r,p=enc(h);s,q=enc(pi)
            assert dec((r+(-1)**p*s)%3,p^q)==mul(h,pi)
            frame_checks+=1
assert arc_checks==180 and frame_checks==1080
A=(O,(0,1,3),(0,2,3),O)
B=(O,(0,1,3),(1,2,3),O)
C=(O,(0,2,3),(1,2,3),O)
loops={'A':A,'B':B,'C':C}
assert [run(z)[0] for z in (A,B,C)]==[(0,2,1),(2,1,0),(1,0,2)]
orders={}
for order in permutations('ABC'):
    w=(O,)
    for k in order: w+=loops[k][1:]
    h,r,p,hist=run(w)
    orders[''.join(order)]={'frame':h,'r':r,'p':p,'word':w}
assert len({run((O,)+sum((loops[k][1:] for k in order),()))[3] for order in permutations('ABC')})==1
assert {v['frame'] for v in orders.values()}=={(0,2,1),(1,0,2),(2,1,0)}
assert {v['r'] for v in orders.values()}=={0,1,2}
assert {v['p'] for v in orders.values()}=={1}
ab=run(A+B[1:]);ba=run(B+A[1:])
assert ab[3]==ba[3] and ab[0]!=ba[0] and ab[2]==ba[2]==0
assert all(len({mul(h,edge(u,v)) for h in permutations(range(3))})==6 for u in V for v in N[u])
out={'marker':'R665_DIRECTED_HISTOGRAM_EXACT_TERNARY_D3_RESIDUAL_PASS',
'model':'V17 J(6,3), fixed initial identity frame, exact oriented transition histogram',
'frozen':'R462@18783e01e3646c72b7aab3b16d3f565e83e6446f; R664@7bb93e0223248761592285b2f3c40f2cc3405bc7',
'vertices':len(V),'directed_edges':arc_checks,'frame_update_checks':frame_checks,
'three_loops':{k:[list(t) for t in w] for k,w in loops.items()},
'nine_step_orders':{k:{'frame':list(v['frame']),'r':v['r'],'p':v['p']} for k,v in orders.items()},
'one_common_histogram':True,'distinct_frames_in_fiber':3,'minimal_additional_alphabet':3,
'six_step_AB_BA_different_frames':True,'review':'AUTHOR_SIDE_UNREVIEWED'}
Path(__file__).with_name('R665_EVIDENCE.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(out['marker'], 'vertices',len(V),'arcs',arc_checks,'updates',frame_checks)
print('common 9step 3-frame fiber',out['nine_step_orders'])
