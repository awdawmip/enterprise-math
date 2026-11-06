#!/usr/bin/env python3
"""PREFIX-533 exact rooted BRC axis-1 / aAc gate observer classification.
Frozen science: enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Requires only Python 3 standard library. Exact integer and Laurent-polynomial arithmetic.
"""
from collections import defaultdict, Counter
import json

STARS = ((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(j,c): return tuple((-1 if c>0 else 1)*a for a in STARS[j] if a!=abs(c))
PHASES = tuple((j,p,sgn*a) for j in range(4)
               for a in STARS[j] for sgn in (-1,1) for p in near(j,sgn*a))
INDEX={p:i for i,p in enumerate(PHASES)}
assert len(PHASES)==len(INDEX)==48

NEXT=[]
for j,p,c in PHASES:
    other=next(i for i in range(4) if i!=j and abs(c) in STARS[i])
    dest=[(j,c,v) for v in near(j,c) if v!=p]
    dest += [(other,c,v) for v in near(other,c)]
    NEXT.append(tuple(INDEX[x] for x in dest))
NEXT=tuple(NEXT)
assert all(len(e)==3 for e in NEXT)
T=INDEX[(0,1,-3)]
sig=lambda i: (1 if PHASES[i][2]>0 else -1) if abs(PHASES[i][2])==1 else 0
flag=lambda i: int(abs(PHASES[i][2])==1)

# A polynomial is a dictionary (v_power,z_power) -> integer coefficient.
# q=v^2; the final BRC observer has only even nonnegative v powers.
def add_shift(dest,src,shift_v=0,shift_z=0,mult=1):
    for (v,z),c in src.items():
        k=(v+shift_v,z+shift_z)
        dest[k]=dest.get(k,0)+mult*c
def clean(p):return {k:v for k,v in p.items() if v}

# Exact return row e_T^T W^2 for the 49-dimensional rank-one lift.
BACK=[]
for i in range(48):
    weights=Counter()
    for mid in NEXT[i]:
        if T in NEXT[mid]:
            weights[flag(i)+2*flag(mid)+flag(T)]+=1
    BACK.append(dict(weights))

# One backward scalar row for each possible initial axis sign.
R=[]
for init_sig in (-1,0,1):
    f=[{(-abs(sig(i)-init_sig),0):1} for i in range(48)]
    R.append((f,{}))

groups=[list(range(48))]
history=[]
samples={}
early_obs={}
for d in range(49):
    outputs=[clean(R[sig(s)+1][0][s]) for s in range(48)]
    assert all(all(c and v>=0 and v%2==0 for (v,z),c in poly.items()) for poly in outputs)
    assert all(sum(poly.values())==6**d for poly in outputs)
    if d<=7: early_obs[d]=outputs
    newgroups=[]
    for group in groups:
        buckets=defaultdict(list)
        for s in group:
            buckets[tuple(sorted(outputs[s].items()))].append(s)
        newgroups.extend(buckets.values())
    groups=newgroups
    history.append({'d':d,'classes':len(groups)})
    if d==2:
        for s in (INDEX[(0,6,-3)],INDEX[(0,1,-6)]):
            samples[str(PHASES[s])]=[[h,v//2,c] for (v,h),c in sorted(outputs[s].items())]
    if d in (4,5,9,20,48):
        print('depth',d,'classes',len(groups),'max_terms',max(len(x) for x in outputs),flush=True)
    if d==48:break
    newR=[]
    for oldf,oldg in R:
        newf=[]
        for s in range(48):
            poly={}
            for dest in NEXT[s]:
                add_shift(poly,oldf[dest],flag(s)+flag(dest),0,2)
            for power,count in BACK[s].items():
                add_shift(poly,oldg,power,0,count)
            newf.append(clean(poly))
        newg={}
        add_shift(newg,oldf[T],0,1,1)
        add_shift(newg,oldf[T],0,0,-1)
        newR.append((newf,clean(newg)))
    R=newR

assert len(groups)==26
assert history[5]['classes']==26
assert all(h['classes']==26 for h in history[5:])
assert Counter(map(len,groups))==Counter({1:8,2:16,4:2})

# Reproduce the gate-only equivalence relation from rooted backward walks.
row=[int(i==T) for i in range(48)]
rows=[]
for d in range(12):
    rows.append(row)
    row=[sum(row[j] for j in NEXT[s]) for s in range(48)]
gateclasses=defaultdict(list)
for s in range(48):
    gateclasses[tuple(rows[k][s] for k in range(2,12))].append(s)
assert len(gateclasses)==18
for group in groups:
    assert any(set(group)<=set(gc) for gc in gateclasses.values())
a,b=INDEX[(0,6,-3)],INDEX[(0,1,-6)]
assert any(a in gc and b in gc for gc in gateclasses.values())
assert samples[str(PHASES[a])]==[[0,0,24],[0,1,12]]
assert samples[str(PHASES[b])]==[[0,0,36]]

# Independent forward dynamic program with actual INNER/OUTER branch memory.
comparisons=0
for origin in range(48):
    dp={(origin,False,0,0):1}
    for d in range(8):
        hist={}
        for (end,lastinner,k,h),n in dp.items():
            delta=abs(sig(end)-sig(origin))
            assert k>=delta and (k-delta)%2==0
            key=(k-delta,h)
            hist[key]=hist.get(key,0)+n
        assert hist==early_obs[d][origin],(origin,d,hist,early_obs[d][origin])
        comparisons+=len(hist)
        nxt=defaultdict(int)
        for (end,lastinner,k,h),n in dp.items():
            for dest in NEXT[end]:
                kk=k+flag(end)+flag(dest)
                for br in (False,True):
                    hit=int(lastinner and br and dest==T)
                    nxt[(dest,br,kk,h+hit)]+=n
        dp=nxt

result={
    'result':'ALL_CHECKS_PASS',
    'lineage':'PREFIX-533',
    'science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
    'phase_count':48,
    'rank_one_linear_dimension':49,
    'observer':'fixed-origin joint (H,p_L1), retaining labeled native path multiplicity',
    'exact_Cayley_Hamilton_length_bound':'d=0..48 (49 coefficients) over Q(v,z), v^2=q',
    'exact_class_count':26,
    'class_size_histogram':dict(sorted(Counter(map(len,groups)).items())),
    'earliest_full_class_separation_depth':5,
    'gate_only_class_count':18,
    'class_count_by_depth':history,
    'direct_native_forward_dp_depth':7,
    'direct_native_forward_dp_roots':48,
    'independent_coefficients_compared':comparisons,
    'groups':[[list(PHASES[i]) for i in group] for group in groups],
    'depth2_collision_witness_samples':samples,
    'proof_status':'exact algebraic 49-dimensional realization + exhaustive sparse polynomial certificate; unreviewed',
    'unresolved':'Minimal rooted joint denominator and exact bit-cost benchmarks.'
}
with open('PREFIX533_EXACT_EXECUTION.json','w',encoding='utf-8') as fh:
    json.dump(result,fh,ensure_ascii=False,indent=2)
print('ALL_CHECKS_PASS; classes=26; hist='+str(result['class_size_histogram'])+'; coefficients='+str(comparisons))
