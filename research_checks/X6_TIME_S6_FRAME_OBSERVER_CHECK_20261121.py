"""Exact S6 frame-local signed-axis observer checks. Python stdlib, integer-only."""
from itertools import permutations
from math import factorial
import json
N=6
I=tuple(range(N))
FRAMES=list(permutations(range(N)))
def mul(a,b): return tuple(a[b[j]] for j in range(N))
def subgroup(gs):
    seen={I}; stack=[I]
    while stack:
        p=stack.pop()
        for g in gs:
            q=mul(p,g)
            if q not in seen: seen.add(q); stack.append(q)
    return sorted(seen)
def rotate(x,s,h): return x,mul(s,h)
def step(x,s,j,eps=1):
    y=list(x); y[s[j]]+=eps
    return tuple(y),s
def signature(s,H,J):
    x=(0,)*N
    return tuple(step(*rotate(x,s,h),j)[0] for h in H for j in J)
swap=(1,0,2,3,4,5)
swap23=(0,1,3,2,4,5)
cycle=(1,2,3,4,5,0)
cases=[('no_local_events',[],[]),('single_port_identity',[],[0]),
       ('three_ports_identity',[],[0,1,2]),
       ('single_port_swap01',[swap],[0]),
       ('single_port_two_swaps',[swap,swap23],[0]),
       ('single_port_cycle6',[cycle],[0]),
       ('all_ports_identity',[],list(range(N)))]
results=[]
for name,gens,J in cases:
    H=subgroup(gens); O=tuple(sorted({h[j] for h in H for j in J}))
    sig_fibers={}; restrict_fibers={}
    for idx,s in enumerate(FRAMES):
        sig_fibers.setdefault(signature(s,H,J),set()).add(idx)
        restrict_fibers.setdefault(tuple(s[j] for j in O),set()).add(idx)
    assert {frozenset(v) for v in sig_fibers.values()}=={frozenset(v) for v in restrict_fibers.values()}
    cls=factorial(N)//factorial(N-len(O))
    assert len(sig_fibers)==cls
    results.append(dict(case=name,group_size=len(H),local_axes=J,orbit=list(O),
       classes=cls,bits=(cls-1).bit_length(),each_fiber=factorial(N-len(O))))
diamonds=[]
for name,g in [('swap01',swap),('cycle6',cycle)]:
    total=nonzero=0
    for s in FRAMES:
        for j in range(N):
            for eps in [-1,1]:
                x=(0,)*N
                after_step_then_R=rotate(*step(x,s,j,eps),g)
                after_R_then_step=step(*rotate(x,s,g),j,eps)
                assert after_step_then_R[1]==after_R_then_step[1]
                delta=tuple(a-b for a,b in zip(after_step_then_R[0],after_R_then_step[0]))
                expected=tuple(eps*((int(k==s[j]))-(int(k==s[g[j]]))) for k in range(N))
                assert delta==expected
                assert sum(a*a for a in delta) in (0,2)
                total+=1
                nonzero+=int(any(delta))
    diamonds.append(dict(generator=name,checked=total,nonzero=nonzero))
assert [(v['classes'],v['bits']) for v in results]==[(1,0),(6,3),(120,7),(30,5),(30,5),(720,10),(720,10)]
assert [(v['checked'],v['nonzero']) for v in diamonds]==[(8640,2880),(8640,8640)]
if __name__=='__main__':
    print(json.dumps(dict(schema='X6_TIME_S6_FRAME_OBSERVER_FINITE_CERT_V1',
      date='2026-11-21',frames=len(FRAMES),cases=results,
      diamonds=diamonds,all_exact_assertions_pass=True,
      model_scope='S6 frame-local coordinate observer; physical triadic dynamics not assumed'),indent=2,sort_keys=True))
