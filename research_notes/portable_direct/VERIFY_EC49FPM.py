#!/usr/bin/env python3
"""Unrestricted uniform-prior terminal-query expectation in class16995.
Run: python VERIFY_EC49FPM.py EVIDENCE_DIR [CERTIFICATE.json]
Imports and executes VERIFY_EC49FPL.py on the same frozen data, then proves unrestricted optimum.
"""
from pathlib import Path
import sys,runpy,functools,json,collections
source=Path(__file__).with_name('VERIFY_EC49FPL.py')
arg=sys.argv[:]
base=arg[1] if len(arg)>1 else str(Path(__file__).resolve().parent)
out=Path(arg[2]) if len(arg)>2 else Path('EC49FPM_CERTIFICATE.json')
sys.argv=[str(source),base,str(out.with_suffix('.cap4.json'))]
m=runpy.run_path(str(source));sys.argv=arg
part=m['part'] if 'part' in m else m['partition']
C4=m['C'];N,Q=m['N'],m['Q']
U=m['U'] if 'U' in m else m['FULL']
values=m['values'] if 'values' in m else m['vals']
bits=m['bits'];INF=m['INF']
@functools.lru_cache(maxsize=None)
def Cinf(mask):
    n=mask.bit_count()
    if n<=1:return 0,-1
    best,which=C4(mask,4) # Valid finite-depth upper bound; INF if unavailable.
    seen=set()
    for q in range(Q):
        groups=part(mask,q)
        if len(groups)==1 or groups in seen:continue
        seen.add(groups)
        lower=n+sum(g.bit_count() for g in groups if g.bit_count()>1)
        if lower>=best:continue
        cost=n
        for g in groups:
            if g.bit_count()>1:
                cost+=Cinf(g)[0]
                if cost>=best:break
        if cost<best:best,which=cost,q
        if best==n:break
    return best,which

first=[]
for q in range(Q):
    first.append(N+sum(Cinf(g)[0] for g in part(U,q) if g.bit_count()>1))
best=min(first);optimal=[q for q,v in enumerate(first) if v==best]
assert best==238 and optimal==[118,119,124,201,203,204]

def groups_by_value(mask,q):
    groups={}
    for i in bits(mask):
        v=values[q][i];groups[v]=groups.get(v,0)|(1<<i)
    return groups

def construct(mask,first=None):
    if mask.bit_count()<=1:return None
    q=Cinf(mask)[1] if first is None else first
    assert q>=0
    groups=groups_by_value(mask,q)
    return {'q':q,'children':{str(v):construct(sub) for v,sub in sorted(groups.items()) if sub.bit_count()>1}}

def validate(tree):
    paths=set();lengths=[]
    for i in range(N):
        node=tree;path=[]
        while node is not None:
            q=node['q'];v=values[q][i]
            path.append((q,v))
            node=node['children'].get(str(v))
        t=tuple(path)
        assert t not in paths
        paths.add(t);lengths.append(len(path))
    assert len(paths)==N and sum(lengths)==best
    return {'max_depth':max(lengths),'histogram':dict(sorted(collections.Counter(lengths).items())),'path_sum':sum(lengths)}

witnesses={}
for q in optimal:
    tr=construct(U,q)
    witnesses[str(q)]={'validation':validate(tr),'tree':tr}
assert witnesses['118']['validation']['histogram']=={1:9,2:84,3:15,4:4}
cert={'schema':'EC49FPM_UNRESTRICTED_EXACT_UNIFORM_EXPECTATION_V1',
      'frozen_scientific_commit':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
      'original_master_sha256':m['MASTER_HASH'],'root_cost_sha256':m['COST_HASH'],
      'scope':'Complete original BRC class16995; exact terminal queries; equal prior on 112 distinct rooted profiles; no depth restriction',
      'distinct_states':N,'primitive_queries':Q,
      'unrestricted_minimum_total_path_length':best,
      'exact_expectation_numerator':best,'exact_expectation_denominator':N,
      'all_first_query_costs':first,'optimal_first_query_indices':optimal,
      'unrestricted_dp_subproblems':Cinf.cache_info().currsize,
      'complete_optimal_witness_trees':witnesses,
      'proof_status':'AUTHOR_PROVED_EXACT_FINITE_CHECKED_NOT_REVIEWED'}
out.write_text(json.dumps(cert,indent=2)+'\n')
print('EC49FPM_UNRESTRICTED_EXACT_PASS',best,N,optimal, {k:v['validation'] for k,v in witnesses.items()})
