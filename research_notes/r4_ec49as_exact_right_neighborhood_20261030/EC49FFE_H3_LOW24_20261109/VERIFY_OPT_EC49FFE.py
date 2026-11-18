#!/usr/bin/env python3
"""EC49FFE exact 104-edge combinatorial certificate and HiGHS 106-edge MILP.

Runs with Python >=3.9 and adjacent VERIFY_EC49FFE.py; use --milp to
run optional SciPy/HiGHS binary optimization. No new science inputs.
"""
import json
import sys
from functools import lru_cache
from collections import defaultdict
from VERIFY_EC49FFE import ALPHABET, OPERATIONS, observer, native_prefixes

KEYS = ((3,1,1), (3,2,1), (3,4,1), (3,6,1), (3,7,1))
HIGH = (4,6,8,9)
GROUPS = tuple((h,s) for h in range(2,10)
               for s in ((16,32) if h in HIGH else (1,2,4,8)))
PIN = 'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'

@lru_cache(None)
def words(counts):
    if not any(counts):
        return ('',)
    out=[]
    for i,n in enumerate(counts):
        if n:
            shorter=list(counts);shorter[i]-=1
            out.extend(ALPHABET[i]+w for w in words(tuple(shorter)))
    return tuple(out)

@lru_cache(None)
def candidate_words(h,key,signature):
    x,y,z=key
    t=x+y-h-1
    f=h+1-y-2*z
    g=h+1-x
    if min(t,f,g,z-1)<0:
        return ()
    result=set()
    for c in range(t+1):
        multiset=(z-1,c,t-c,z,f,g)
        result.update(w for w in words(multiset) if observer(w)==signature)
    return tuple(sorted(result))

@lru_cache(None)
def prefixes(word):
    return frozenset(native_prefixes(word))

def get_choices():
    choices=[]
    for h,s in GROUPS:
        opts=tuple(sorted(set(w for k in KEYS for w in candidate_words(h,k,s))))
        assert opts,(h,s)
        choices.append(opts)
    return tuple(choices)

def mis(adj):
    """Exact maximum independent set, not greedy."""
    @lru_cache(None)
    def solve(mask):
        if mask==0:
            return ()
        v=max((i for i in range(len(adj)) if mask>>i&1),
              key=lambda i:((adj[i]&mask).bit_count(),-i))
        no=solve(mask&~(1<<v))
        yes=(v,)+solve(mask&~(1<<v)&~adj[v])
        return yes if len(yes)>len(no) else no
    return solve((1<<len(adj))-1)

def depth_certificate(choices):
    layers=[];lengths=[]
    for pool in choices:
        layer=defaultdict(set)
        for word in pool:
            for p in prefixes(word):
                layer[len(p)].add(p)
        layers.append(layer)
        lengths.append(min(sum(len(OPERATIONS[c]) for c in word) for word in pool))
    witness=[]
    for d in range(1,max(lengths)+1):
        active=[i for i in range(len(GROUPS)) if lengths[i]>=d]
        adj=[0]*len(active)
        for i in range(len(active)):
            for j in range(i+1,len(active)):
                if not layers[active[i]][d].isdisjoint(layers[active[j]][d]):
                    adj[i]|=1<<j;adj[j]|=1<<i
        selected=mis(adj)
        picked=[active[i] for i in selected]
        assert all(layers[a][d].isdisjoint(layers[b][d])
                   for ix,a in enumerate(picked) for b in picked[ix+1:])
        witness.append({'depth':d,'groups':[list(GROUPS[i]) for i in picked]})
    lower=sum(len(row['groups']) for row in witness)
    assert lower==104 and len(witness)==20,(lower,len(witness))
    return {'exact_integer_lower':lower,'per_depth':[len(q['groups']) for q in witness],
            'disjoint_certificate':witness}

def check_witness():
    recorded={2:['de','ed','ce','ec'],3:['deg','edg','ceg','ecg'],
              4:['fegg','gefg'],5:['deggg','edggg','ceggg','ecggg'],
              6:['fegggg','gefggg'],7:['deggggg','edggggg','ceggggg','ecggggg'],
              8:['fegggggg','gefggggg'],9:['feggggggg','gefgggggg']}
    seen=set();selected=[]
    for h,ws in recorded.items():
        assert len(ws)==(2 if h in HIGH else 4)
        for w in ws:
            s=observer(w)
            assert (h,s) in GROUPS and w in set().union(
                *(set(candidate_words(h,k,s)) for k in KEYS))
            selected.append((h,s,w)); seen.update(prefixes(w))
    assert len(selected)==24 and len(seen)==106
    return 106

def run_milp(choices):
    import numpy as np
    from scipy.optimize import milp, Bounds, LinearConstraint
    from scipy.sparse import lil_matrix, csr_matrix
    xs=[(gi,w) for gi,pool in enumerate(choices) for w in pool]
    allpref=sorted({p for gi,w in xs for p in prefixes(w)},key=lambda p:(len(p),p))
    pi={p:i for i,p in enumerate(allpref)}
    nx=len(xs);ny=len(allpref)
    count=len(GROUPS)+sum(len(prefixes(w)) for gi,w in xs)
    A=lil_matrix((count,nx+ny),dtype=float)
    lb=np.full(count,-np.inf); ub=np.zeros(count)
    for i,(gi,w) in enumerate(xs):A[gi,i]=1
    lb[:len(GROUPS)]=ub[:len(GROUPS)]=1
    row=len(GROUPS)
    for i,(gi,w) in enumerate(xs):
        for p in prefixes(w):
            A[row,i]=1;A[row,nx+pi[p]]=-1;row+=1
    assert row==count
    c=np.r_[np.zeros(nx),np.ones(ny)]
    res=milp(c,integrality=np.ones(nx+ny),bounds=Bounds(0,1),
             constraints=LinearConstraint(csr_matrix(A),lb,ub),
             options={'time_limit':90.0,'mip_rel_gap':0.0})
    assert res.status==0 and abs(res.fun-106)<1e-6
    assert abs(res.mip_dual_bound-106)<1e-6 and res.mip_gap==0
    words_chosen=[(GROUPS[gi],w) for i,(gi,w) in enumerate(xs) if res.x[i]>.5]
    assert len(words_chosen)==24
    assert len(set().union(*(prefixes(w) for _,w in words_chosen)))==106
    return {'solver':'scipy.optimize.milp / HiGHS','status':int(res.status),
            'objective':res.fun,'reported_dual_bound':res.mip_dual_bound,
            'reported_mip_gap':res.mip_gap,'candidate_words':nx,
            'distinct_prefix_variables':ny,'constraints':count,
            'selected':[{'h':h,'signature':s,'word':w} for (h,s),w in words_chosen]}

if __name__=='__main__':
    choices=get_choices()
    cert=depth_certificate(choices)
    report={'status':'EXACT_INTEGER_DEPTH_CERT_PASS','science_pin':PIN,
            'keys':[list(k) for k in KEYS], 'high':list(HIGH),
            'group_count':len(GROUPS), 'candidate_words':sum(map(len,choices)),
            'integer_lower':cert['exact_integer_lower'],
            'explicit_witness_cost':check_witness(),
            'per_depth':cert['per_depth'],
            'certificate':cert['disjoint_certificate']}
    if '--milp' in sys.argv:
        report['joint_milp']=run_milp(choices)
    print(json.dumps(report,ensure_ascii=False,indent=2))
