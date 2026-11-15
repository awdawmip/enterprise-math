#!/usr/bin/env python3
"""EC49FPN: exact unrestricted source-config-weighted BRC class16995 expectation.
Weights are counts of the 242 original configs per distinct rooted profile.
Usage: python VERIFY_EC49FPN.py EVIDENCE_DIR [CERTIFICATE_JSON]
"""
import runpy,sys,functools,collections,json
from pathlib import Path
self_path=Path(__file__).resolve()
orig=sys.argv[:];base=orig[1] if len(orig)>1 else str(self_path.parent)
out=Path(orig[2]) if len(orig)>2 else self_path.with_name('EC49FPN_CERTIFICATE.json')
sys.argv=[str(self_path.with_name('VERIFY_EC49FPL.py')),base,str(out.with_suffix('.cap4.json'))]
m=runpy.run_path(str(self_path.with_name('VERIFY_EC49FPL.py')));sys.argv=orig
N,Q=m['N'],m['Q']
FULL=m['FULL'] if 'FULL' in m else m['U']
values=m['values'];partition=m['partition'] if 'partition' in m else m['part']
bits=m['bits']
# Exact aggregation: the same native terminal vector identifies one rooted P-profile.
pids=m['profile_source_ids'] if 'profile_source_ids' in m else m['profile_ids']
term=m['terminal'] if 'terminal' in m else m['term']
ids=m['ids']
freq=collections.Counter(term.values())
w=tuple(freq[term[cid]] for cid in pids)
assert sum(w)==len(ids)==242 and len(w)==112
@functools.lru_cache(None)
def weight(mask):return sum(w[i] for i in bits(mask))
@functools.lru_cache(None)
def Cw(mask):
    if mask.bit_count()<=1:return 0,-1
    sw=weight(mask)
    best=4*sw;which=-1 # Restriction of prior proved global depth-4 tree to any subset.
    seen=set()
    for q in range(Q):
        groups=partition(mask,q)
        if len(groups)==1 or groups in seen:continue
        seen.add(groups)
        lower=sw+sum(weight(g) for g in groups if g.bit_count()>1)
        if lower>=best:continue
        cost=sw
        for g in groups:
            if g.bit_count()>1:
                cost+=Cw(g)[0]
                if cost>=best:break
        if cost<best:best,which=cost,q
        if best==sw:break
    return best,which

first=[242+sum(Cw(g)[0] for g in partition(FULL,q) if g.bit_count()>1) for q in range(Q)]
opt=min(first);bestqs=[q for q,c in enumerate(first) if c==opt]
assert opt==641 and bestqs==[150,209,290,312]
print('WEIGHTED_FIRST_OPT',opt,bestqs,'CACHE',Cw.cache_info(),flush=True)

old=m['tree']
def old_groups(mask,node):
    if mask.bit_count()<=1:return None
    if node is None:raise AssertionError('Depth-4 source witness incomplete')
    q=node['q']
    groups={}
    for i in bits(mask):
        v=values[q][i];groups[v]=groups.get(v,0)|(1<<i)
    return {'q':q,'children':{str(v):old_groups(g,node['children'].get(str(v))) for v,g in groups.items() if g.bit_count()>1}}

def byvalue(mask,q):
    groups={}
    for i in bits(mask):
        v=values[q][i];groups[v]=groups.get(v,0)|(1<<i)
    return groups

def construct(mask,q=None):
    if mask.bit_count()<=1:return None
    if q is None:q=Cw(mask)[1]
    if q==-1:return old_groups(mask,old)
    groups=byvalue(mask,q)
    return {'q':q,'children':{str(v):construct(g) for v,g in sorted(groups.items()) if g.bit_count()>1}}

def validate(t):
    ps=set();counts=collections.Counter();total=0;maxd=0
    for i in range(N):
        node=t;path=[]
        while node is not None:
            q=node['q'];v=values[q][i];path.append((q,v));node=node['children'].get(str(v))
        tup=tuple(path);assert tup not in ps;ps.add(tup)
        d=len(path);counts[d]+=w[i];total+=d*w[i];maxd=max(maxd,d)
    assert len(ps)==N
    return {'weighted_total':total,'max_depth':maxd,'source_configuration_depth_histogram':dict(sorted(counts.items()))}
tree=construct(FULL,bestqs[0]);val=validate(tree)
assert val['weighted_total']==opt
assert val['max_depth']==4 and val['source_configuration_depth_histogram']=={1:12,2:138,3:15,4:77}
cert={'schema':'EC49FPN_CLASS16995_WEIGHTED_EXPECTATION_V1',
      'source_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
      'master_sha256':m['MASTER_HASH'],'root_csv_sha256':m['COST_HASH'],
      'prior':'Uniform on 242 original source configurations (112 rooted profiles with multiplicity)',
      'weights_per_rooted_profile':w,'query_count':Q,'source_count':242,
      'expected_cost_numerator':opt,'expected_cost_denominator':242,
      'optimal_initial_indices':bestqs,'all_initial_costs':first,
      'memoized_subsets':Cw.cache_info().currsize,'verified_tree':tree,
      'verified_tree_stats':val,
      'mathematical_status':'AUTHOR_PROVED_EXACT_FINITE_CHECKED_NOT_REVIEWED'}
out.write_text(json.dumps(cert,indent=2)+'\n')
print('EC49FPN_SOURCE_WEIGHTED_PASS',opt,242,bestqs,val)
