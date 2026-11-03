#!/usr/bin/env python3
"""Stage414-B: exact combinatorial certificates and finite checks for L2.
No dependencies beyond Python standard library. The all-horizon theorem is proved
in PROOF_STAGE414B.md; these finite computations are independent cross-checks.
"""
import itertools
import json
from collections import Counter, defaultdict
from functools import lru_cache

D = tuple(range(1, 7)) + tuple(range(-1, -7, -1))
A, B = 1, -1
TRACES = (
    ('POP',), ('POP', 'POP'), ('POP', 'POP', 'CAN'),
    ('POP', 'POP', (B, A), 'CAN'),
    ('POP', 'POP', (B, B), 'CAN'),
    ('POP', 'CAN', 'POP'),
)

def family(n):
    for r in range(2, n):
        for s in range(r + 2, n):
            for i in (r, s):
                p = tuple(B if j == i else A for j in range(1, n + 1))
                q = tuple(B if j in (r, s) else A for j in range(1, n + 1))
                yield (i, r, s, p, q)

def group(n, i, r, s):
    if s <= n - 4: return 'G0'
    if s == n - 3: return 'G1'
    if s == n - 2: return 'G2' if i == r else 'G3'
    if i == r: return 'G7' if r == n - 3 else 'G4'
    if r == n - 3: return 'G8'
    if r == n - 4: return 'G6'
    return 'G5'

def expected_counts(n):
    if n == 5: return {'G7': 1, 'G8': 1}
    return {g: v for g, v in zip(['G0','G1','G2','G3','G4','G5','G6','G7','G8'],
             [(n-6)*(n-7), 2*(n-6), n-5, n-5, n-5, n-6, 1, 1, 1]) if v > 0}

def safe_key(p,q):
    # Noninverse P tail allows the stronger (3,4) theorem.
    if len(p) < 2 or p[-2] != -p[-1]:
        return ('noninverse', p[-3:], q[-4:])
    return ('inverse', p[-4:], q[-5:])

def z(seq):
    s = [0]*6
    for a in seq: s[abs(a)-1] += 1 if a>0 else -1
    return tuple(s)

@lru_cache(maxsize=50000)
def obs(p,q):
    return (len(p),len(q),z(p),z(q),tuple(sorted(Counter(zip(p,p[1:])).items())),
            tuple(sorted(Counter(zip(q,q[1:])).items())),sum(a==b for a,b in zip(p,q)))

def step(s,a):
    p,q,pop,cancel = s
    if a == 'POP':
        if pop == 0 or not q: return None
        return p,q[:-1],pop-1,cancel
    if a == 'CAN':
        if cancel == 0 or len(p)<2 or len(q)<2 or p[-1]!=-p[-2] or q[-1]!=-q[-2]:
            return None
        return p[:-2],q[:-2],pop,cancel-1
    x,y=a
    return p+(x,),q+(y,),pop,cancel

def signature(p,q,trace):
    s=(p,q,2,1)
    seq=[]
    for a in trace:
        s=step(s,a)
        if s is None:
            seq.append('DISABLED')
            break
        seq.append(obs(s[0],s[1]))
    return tuple(seq)

def candidate_traces(alphabet,n_app):
    # All orderings of up to two pops, one cancel, exactly n_app APPs.
    for n_pop in range(3):
        for n_can in range(2):
            shape=['POP']*n_pop+['CAN']*n_can+['APP']*n_app
            for seq in set(itertools.permutations(shape)):
                for labels in itertools.product(itertools.product(alphabet,repeat=2),repeat=n_app):
                    it=iter(labels)
                    yield tuple(next(it) if a=='APP' else a for a in seq)

def validate():
    checked=0
    max_n=30
    samples={}
    for n in range(5,max_n+1):
        hist=list(family(n))
        assert len(hist)==(n-3)*(n-4)
        assert len({obs(x[3],x[4]) for x in hist})==1
        actual=Counter(group(n,*h[:3]) for h in hist)
        assert dict(actual)==expected_counts(n),(n,actual,expected_counts(n))
        grouped=defaultdict(set)
        signatures=defaultdict(set)
        all_keys=defaultdict(set)
        for i,r,s,p,q in hist:
            g=group(n,i,r,s)
            grouped[safe_key(p,q)].add(g)
            signatures[g].add(tuple(signature(p,q,t) for t in TRACES))
            all_keys[(p[-4:],q[-5:])].add(g)
            checked+=1
        assert all(len(v)==1 for v in grouped.values()),(n,grouped)
        assert len(grouped)==len(actual),(n,len(grouped),len(actual))
        assert all(len(v)==1 for v in signatures.values()),(n,'bad fixed trace groups')
        assert len({next(iter(v)) for v in signatures.values()})==len(actual),(n,'lower certificate failed')
        assert len(all_keys)== {5:2,6:6,7:12,8:13}.get(n,14),(n,'raw45')
        if n in (5,6,7,8,9,10,16,20,30):
            samples[str(n)]={'fiber_size':len(hist),'raw45_states':len(all_keys),
                             'hybrid_states':len(grouped),'exact_classes':len(actual),
                             'sizes':[actual.get('G'+str(j),0) for j in range(9)]}
    # Strict (3,4) componentwise witnesses in F9.
    n=9
    hist=list(family(n)); byidx={(r,s,i):(p,q) for i,r,s,p,q in hist}
    p1,q1=byidx[(2,n-2,2)];p2,q2=byidx[(2,n-2,n-2)]
    assert q1==q2 and p1[-2:]==p2[-2:] and obs(p1,q1)==obs(p2,q2)
    assert signature(p1,q1,TRACES[3])!=signature(p2,q2,TRACES[3])
    p3,q3=byidx[(2,n-4,2)];p4,q4=byidx[(2,n-3,2)]
    assert p3==p4 and q3[-3:]==q4[-3:] and obs(p3,q3)==obs(p4,q4)
    assert signature(p3,q3,TRACES[4])!=signature(p4,q4,TRACES[4])
    # Finite all-12-direction single APP tests plus restricted two APP probes.
    bykey=defaultdict(list)
    for h in hist: bykey[safe_key(h[3],h[4])].append(h)
    representatives=[]
    for k, lst in bykey.items():
        different={}
        for h in lst: different.setdefault((h[3][-4:],h[4][-5:]),h)
        if len(different)>1:
            vals=list(different.values())
            representatives.append((k, vals[0], vals[1]))
    assert len(representatives)==5
    checked_traces=0
    tested_cases=[]
    for k,h1,h2 in representatives:
        for n_app,alphabet in ((0,D),(1,D),(2,(A,B,2,-2))):
            for trace in candidate_traces(alphabet,n_app):
                assert signature(h1[3],h1[4],trace)==signature(h2[3],h2[4],trace),(k,trace)
                checked_traces+=1
        tested_cases.append(k[0]+':'+str((k[1],k[2])))
    return {'status':'STAGE414B_EXACT_NINE_CLASS_PASS',
            'finite_n_range':[5,max_n], 'enumerated_history_pairs':checked,
            'representative_merged_pairs':len(representatives),
            'finite_trace_checks':checked_traces,
            'symbolic_append_alphabet':'12 native directions for one APP; {±E1,±E2} for two APP',
            'max_test_pops':2,'max_test_cancels':1,
            'all_horizon_basis':'mathematical conditional (3,4) suffix theorem, not finite trace search',
            'samples':samples,'lower_witnesses':{
                'P2_vs_P3':'G2 versus G3 in F9, T4 distinguishes',
                'Q3_vs_Q4':'G0 versus G1 in F9, T5 distinguishes'},
            'merged_pair_keys':tested_cases}
if __name__=='__main__':
    print(json.dumps(validate(),sort_keys=True,separators=(',',':')))
