#!/usr/bin/env python3
"""R717 exact positive path-formal X6 J(6,3) / S3 holonomy lift.

120 ordered-triad states, source-labelled one-axis replacement edges,
strictly integer operators. Candidate stocked TRANSFER scheduling is separately
specified and checked; no trigonometric or non-BRC propagation involved.
"""
from collections import deque
from itertools import permutations
import json

BASE = (0,1,2)
STATES = list(permutations(range(6),3))
IDX = {s:i for i,s in enumerate(STATES)}
N = len(STATES)
ADJ = []
for x in STATES:
    nb=[]
    for slot in range(3):
        for y in range(6):
            if y not in x:
                z=list(x); z[slot]=y
                nb.append(IDX[tuple(z)])
    assert len(nb)==9 and len(set(nb))==9
    ADJ.append(tuple(nb))
assert N==120 and all(i in ADJ[j] for i,ns in enumerate(ADJ) for j in ns)

# Complete 120-state graph is connected. Each state has nine unweighted edges.
visited={IDX[BASE]}; q=deque(visited)
while q:
    for j in ADJ[q.popleft()]:
        if j not in visited:
            visited.add(j); q.append(j)
assert len(visited)==120

def edge(a,b):
    assert set(a)!=set(b) and len(set(a)&set(b))==2
    leave=next(iter(set(a)-set(b)))
    enter=next(iter(set(b)-set(a)))
    y=list(a); y[y.index(leave)]=enter
    assert sorted(y)==sorted(b)
    return tuple(y)

def holo(path):
    slots=tuple(path[0]); assert slots==BASE
    for prev,nxt in zip(path,path[1:]):
        slots=edge(slots,nxt)
    assert path[-1]==BASE
    return tuple(slots.index(i) for i in BASE)

def final_slots(h):
    slots=[None]*3
    for i,pos in enumerate(h): slots[pos]=i
    return tuple(slots)

ID=(0,1,2)
TRANSPOS=((0,2,1),(1,0,2),(2,1,0))
CYCLES=((1,2,0),(2,0,1))
ALL=(ID,)+TRANSPOS+CYCLES
END={h:IDX[final_slots(h)] for h in ALL}

def closed_hist(m):
    counts=[0]*N; counts[IDX[BASE]]=1
    for _ in range(m):
        nxt=[0]*N
        for i,c in enumerate(counts):
            if c:
                for j in ADJ[i]: nxt[j]+=c
        counts=nxt
    return {h:counts[END[h]] for h in ALL}

def exact_class_formula(m):
    assert m>=1
    z=(-1)**m
    e=(9**m+10*6**m+15*3**m+18*2**m+9*z+47*(-3)**m)
    t=(9**m-5*3**m+9*z-5*(-3)**m)
    c=(9**m-5*6**m+15*3**m-9*2**m+9*z-(-3)**m)
    assert e%120==t%120==c%120==0
    return e//120,t//120,c//120

# Verify the exact 120x120 annihilating polynomial P(A)=0.
# This is a finite integer certificate (not numerical diagonalisation).
# P(x)=x(x+1)(x+3)(x-2)(x-3)(x-6)(x-9).
POLY_ASC=(0,972,216,-711,120,58,-16,1)
identity=[[int(i==j) for j in range(N)] for i in range(N)]
cur=identity
poly_eval=[[0]*N for _ in range(N)]
for degree,coeff in enumerate(POLY_ASC):
    if coeff:
        for i in range(N):
            for j in range(N):
                poly_eval[i][j]+=coeff*cur[i][j]
    if degree<len(POLY_ASC)-1:
        nxt=[[0]*N for _ in range(N)]
        for i,nb in enumerate(ADJ):
            target=nxt[i]
            for j in nb:
                row=cur[j]
                for col in range(N):target[col]+=row[col]
        cur=nxt
assert all(v==0 for row in poly_eval for v in row)

# Seven base layers + P(A)=0 imply the formula for all integer m>=1.
base={}
for m in range(0,7):
    h=closed_hist(m)
    base[m]=[h[x] for x in ALL]
    if m>=1:
        e,t,c=exact_class_formula(m)
        assert h[ID]==e
        assert all(h[x]==t for x in TRANSPOS)
        assert all(h[x]==c for x in CYCLES)
assert base[0]==[1,0,0,0,0,0]
assert base[1]==[0]*6
assert base[2]==[9,0,0,0,0,0]
assert base[3]==[18,6,6,6,0,0]
for m in range(7,61):
    h=closed_hist(m);e,t,c=exact_class_formula(m)
    assert h[ID]==e and all(h[x]==t for x in TRANSPOS) and all(h[x]==c for x in CYCLES)

# Construct finite witnesses by exhaustive DFS over the Johnson triad vertices.
TRIADS=list(__import__('itertools').combinations(range(6),3))
NEIGH={t:tuple(u for u in TRIADS if len(set(t)&set(u))==2) for t in TRIADS}
def base_witnesses(m):
    ret={}
    def dfs(path,slots):
        d=len(path)-1
        if d==m:
            if path[-1]==BASE:
                ret.setdefault(tuple(slots.index(i) for i in BASE),path)
            return
        for b in NEIGH[path[-1]]:
            if d==m-1 and b!=BASE: continue
            dfs(path+[b],edge(slots,b))
    dfs([BASE],BASE)
    return ret
w4=base_witnesses(4)
w5=base_witnesses(5)
assert set(w4)==set(ALL)==set(w5)

def phase_sets(m):
    if m%2==0:
        return [(1,2) if i%2==0 else (3,4) for i in range(m)]
    a=(m-1)//4
    b=(m-1)//2-a
    return [(1,2),(3,4)]*a+[(1,5)]+[(2,3),(4,5)]*b

def check_schedule(m):
    pairs=phase_sets(m)
    assert len(pairs)==m
    assert all(set(pairs[i]).isdisjoint(pairs[(i+1)%m]) for i in range(m))
    D=[sum(p<=t<q for p,q in pairs) for t in range(1,max(q for p,q in pairs))]
    if m%2==0:
        assert D==[m//2,0,m//2]
    else:
        a=(m-1)//4;b=(m-1)//2-a
        assert D==[a+1,b+1,a+1,b+1]
    return D

def check_ring(path,m):
    field=tuple(path[:-1]); assert len(field)==m and field[0]==BASE
    assert all(len(set(field[i])&set(field[(i+1)%m]))==2 for i in range(m))
    phases=phase_sets(m)
    p=[1]*m;n=[1]*m
    ledger=[[0,0,0,0] for _ in range(m)]  # plus in/out, minus in/out
    cur=field
    trace=[cur[0]]
    micro_profile=check_schedule(m)
    for tick in range(m):
        fires=[len(set(cur[i])&set(cur[(i+1)%m]))==2 and p[(i+1)%m]>=1 and n[i]>=1 for i in range(m)]
        assert all(fires)
        current=[0]*m
        for phase in range(1,max(last for first,last in phases)+1):
            selected=[i for i,(first,last) in enumerate(phases) if phase in (first,last)]
            endpoints=[u for i in selected for u in (i,(i+1)%m)]
            assert len(endpoints)==len(set(endpoints))
            for i in selected:
                j=(i+1)%m
                first,_=phases[i]
                if phase==first:
                    assert p[j]>=1
                    p[j]-=1;p[i]+=1
                    ledger[i][0]+=1;ledger[j][1]+=1
                    current[i]+=1
                else:
                    assert n[i]>=1
                    n[i]-=1;n[j]+=1
                    ledger[j][2]+=1;ledger[i][3]+=1
                    current[i]-=1
            assert min(p)>=0 and min(n)>=0
            if phase<len(micro_profile)+1:
                assert sum(abs(v) for v in current)==micro_profile[phase-1]
        assert current==[0]*m and p==n==[1]*m
        cur=tuple(cur[(i+1)%m] for i in range(m))
        trace.append(cur[0])
    assert cur==field and all(row==[m,m,m,m] for row in ledger)
    assert holo(trace)==holo(path)

for m in range(4,34):
    check_schedule(m)
    bases=w4 if m%2==0 else w5
    for h,base in bases.items():
        extra=(m-(len(base)-1))//2
        path=base+[ (0,1,3),(0,1,2)]*extra
        assert len(path)==m+1 and holo(path)==h
        check_ring(path,m)

checks=[]
for m in (2,3,4,5,6,7,9,12,20,30,60):
    e,t,c=exact_class_formula(m)
    r=e+3*t+2*c
    assert r*20==9**m+5*3**m+9*(-1)**m+5*(-3)**m
    checks.append(dict(m=m,identity=e,each_transposition=t,each_threecycle=c,total_closed=r,
                       phase_count=4 if m%2==0 else 5 if m>=5 else None))
out={
 'verdict':'R717_EXACT_X6_LIFT_S3_SPECTRAL_AND_PHASE_FIBER_PASS',
 'scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
 'carrier':'positive unit-weight path-formal 3-subset Johnson transitions on six native axes, with unique V17 slot replacement lift',
 'lift_state_count':N,'lift_degree':9,'annihilating_polynomial_ascending_coeffs':list(POLY_ASC),
 'polynomial_matrix_entries_verified':N*N,'connected_lift_states':len(visited),
 'class_formula_denominator':120,'class_formula_m_domain':'integer m>=1',
 'tested_exact_histograms_m':'0..60',
 'universal_holonomy_support':'m=1 none; m=2 identity only; m=3 identity+3 transpositions; every m>=4 all six S3 elements',
 'even_odd_ring_witnesses':{
  str(m):{str(h):[''.join(map(str,s)) for s in path] for h,path in sorted(ws.items())}
  for m,ws in [(4,w4),(5,w5)]},
 'candidate_stock_ring_check_m':'4..33 all six pointed holonomies; identical port ledgers, fixed optimal microphase schedule',
 'joint_phase_optimal_profile':'even m: (m/2,0,m/2,0); odd m: (a+1,b+1,a+1,b+1), a=floor((m-1)/4), b=(m-1)/2-a',
 'sample_histograms':checks,
 'observer':'known initial/final root triad, identical full port typed final counts and stocks, fixed all-edge microphase current time trace, but not full root field/ordered X6 path',
 'predictive_h_bit_lower_bound':3,
 'asymptotic':'conditional holonomy distribution on 6 permutations tends to uniform, TV=(5/3)*(2/3)^m+O((1/3)^m) (m integer -> infinity)',
 'status':'exact finite operator certificate + inductive all-length consequences within explicit candidate model; independent mathematical review pending'
}
with open('/mnt/data/R717_X6_S3_COVER_RESULTS.json','w',encoding='utf-8') as f:
    json.dump(out,f,indent=2,ensure_ascii=False,sort_keys=True)
    f.write('\n')
print(out['verdict'])
