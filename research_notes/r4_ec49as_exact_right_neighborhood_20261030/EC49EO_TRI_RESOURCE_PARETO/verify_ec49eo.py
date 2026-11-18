#!/usr/bin/env python3
"""EC49EO native X6 finite exact observer/prefix/multiplier cost verifier."""
from itertools import product, permutations, combinations
from collections import defaultdict
from math import ceil, log2
import json
OPS = {'a':(-1,-1),'b':(-2,-2),'c':(1,2,-1,-2),'d':(2,1,-2,-1), 'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
ATOMS=(('N',0),('N',1),('N',2),('A',0),('A',2),('B',0),('B',1),('AB',0),('BA',0))
BUCKETS=('N','A','B','AB','BA')

def native(w):
    return tuple(k for c in w for k in OPS[c])

def counts(w):
    p=native(w)
    return tuple(p.count(k) for k in range(1,7))

def displacement(w):
    p=native(w)
    return tuple(p.count(k)-p.count(-k) for k in range(1,7))

def transfer(w):
    path=native(w)
    out=[]
    for st,last in ATOMS:
        for v in path:
            if last==1 and v==2:st={'N':'A','B':'BA'}.get(st,st)
            if last==2 and v==1:st={'N':'B','A':'AB'}.get(st,st)
            last=v
        out.append(BUCKETS.index(st))
    return tuple(out)

def rank(ws):
    """Rank of full native terminal observation matrix modulo P.

    P>3**9 bounds every 9x9 binary determinant in absolute value by
    Hadamard, so modular rank==9 is equivalent to rational rank==9.
    Lower ranks are not used to assert exact rational rank values.
    """
    P=1000003; piv={};r=0
    for w in ws:
        t=transfer(w)
        for b in range(5):
            col=[int(x==b) for x in t]
            for i in range(9):
                if col[i]==0:continue
                if i in piv:
                    factor=col[i]
                    for j in range(i,9):col[j]=(col[j]-factor*piv[i][j])%P
                else:
                    inv=pow(col[i],-1,P)
                    piv[i]=[(x*inv)%P for x in col]
                    r+=1;break
    return r

def edges(ws):
    return {native(w)[:i] for w in ws for i in range(1,len(native(w))+1)}

# Constructive paths from EC49EN verified theorem
def interval_words(a,h):
    assert a>=2 and a<=h<=2*a-1
    q=2*a-1-h;u=v=h-a;tail='f'*u+'g'*v
    if q:
        return ('e'+'c'*q+tail,'e'+'d'*q+tail,'c'+'e'+'c'*(q-1)+tail,'d'+'e'+'d'*(q-1)+tail)
    return ('feg'+'f'*(u-1)+'g'*(v-1),'gef'+'f'*(u-1)+'g'*(v-1))

base=('ce','de','ec','ed')
assert rank(base)==9 and len(edges(base))==28
h2_all=[''.join(w) for w in product('abcdefg',repeat=2) if displacement(''.join(w))==(2,0,0,0,0,0)]
assert len(h2_all)==8, h2_all
h2_full=[tuple(w for i,w in enumerate(h2_all) if mask&(1<<i)) for mask in range(1,1<<len(h2_all)) if (lambda pool: len({counts(w) for w in pool})==1 and rank(pool)==9)(tuple(w for i,w in enumerate(h2_all) if mask&(1<<i)))]
assert h2_full and all(set(base).issubset(set(w)) for w in h2_full)


# 3-horizon candidates: enumerate all 3-letter return words exactly (7^3 <=343)
words3=(''.join(w) for w in product('abcdefg', repeat=3))
fibers=defaultdict(list)
for w in words3:
    if displacement(w)==(2,0,0,0,0,0):
        fibers[counts(w)].append(w)
assert sum(len(x) for x in fibers.values())==51
fiber_stats=[]
for p,ws in sorted(fibers.items()):
    if rank(ws)<9: continue
    best=999;best_w=None
    # enumerate every nonempty subset; bound size <=6 for h3 fibers
    for mask in range(1,1<<len(ws)):
        sub=tuple(w for i,w in enumerate(ws) if mask&(1<<i))
        if rank(sub)!=9:continue
        E=len(edges(base+sub))
        if E<best:best=E;best_w=sub
    fiber_stats.append({'p':p,'word_pool':len(ws),'E_with_T2':best,'best_words':best_w,'transfer_types':len(set(transfer(w) for w in base+best_w))})

# Exact H3 Pareto: E and S minimal per key count; every full-rank h3 subset is inspected
points={}
for p,ws in sorted(fibers.items()):
    if rank(ws)<9:continue
    for mask in range(1,1<<len(ws)):
        sub=tuple(w for i,w in enumerate(ws) if mask&(1<<i))
        if rank(sub)!=9:continue
        M=len(set(counts(w) for w in base+sub))
        S=len(set(transfer(w) for w in base+sub))
        E=len(edges(base+sub))
        item=(E,M,S)
        if item not in points:points[item]={'p3':p,'words3':sub}
frontier=sorted((e,m,s) for (e,m,s) in points if not any((e2<=e and m2<=m and s2<=s and (e2,m2,s2)!=(e,m,s)) for e2,m2,s2 in points))
assert frontier==[(36,2,4),(42,1,6)],frontier

# Revisit EC49EN fixed-cover constructions with prefix reuse and native observer checks.
def inherited(H, event_only):
    w=[];start=2;group=[]
    while start<=H:
        end=min(H, 2*start-2 if event_only else 2*start-1)
        for h in range(start,end+1):
            subs=interval_words(start,h)
            assert rank(subs)==9 and all(displacement(x)==(2,0,0,0,0,0) for x in subs)
            assert len({counts(x) for x in subs})==1
            w.extend(subs)
        group.append((start,end));start=end+1
    return {'E':len(edges(w)),'M':len(set(counts(x) for x in w)),'S':len(set(transfer(x) for x in w)),'word_occurrences':len(w),'groups':group}

# Improved S=4, H3 witness uses base leaves and extends each by one f operation.
short3=('ecf','edf','cef','def')
assert len(edges(base+short3))==36
assert rank(short3)==9
assert len({counts(w) for w in short3})==1
assert len({transfer(w) for w in base+short3})==4

report={
 'unit':'EC49EO','status':'PASS','domain':'Exact H=3 native-X6 full return-word subsets and cached observer-transfer signatures',
 'base':{'h':2,'words':base,'E':28,'rank':rank(base),'legal_return_words':h2_all,'full_rank_subsets':len(h2_full)},
 'h3_fibers':fiber_stats,
 'h3_exact_Pareto_EMS':frontier,
 'h3_Pareto_witnesses':[{ 'E':e,'M':m,'S':s,**points[e,m,s]} for e,m,s in frontier],
 'short_h3_witness':{'words':short3,'E':len(edges(base+short3)),'M':2,'S':4},
 'previous_EC49EN_witness_H3':{'M_min':inherited(3,False),'S4':inherited(3,True)},
 'model':'BRC symbolic cache keys are six-axis positive-count exponent vectors, not numerical coincidences',
 'proof_scope':'Full finite h2 and h3 witness-pool enumeration. The H3 Pareto classification does not generalize to H>=4 without additional work.'}
print(json.dumps(report,ensure_ascii=False,indent=2))
