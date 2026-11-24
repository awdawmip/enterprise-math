"""Fixed-slot-order CRT replay; returns all exact-nine roots up to fixed cap."""
from minimum import *
import reference

def all_candidates(bound,shapes,reverse=False):
    ns=Counter()
    ks=set()
    for shape in shapes:
        levels=tuple(sorted(shape,key=lambda y:(len(y),y),reverse=reverse))
        def rec(i,m,x,chosen):
            ns[i]+=1
            if i==len(levels):
                ks.update(range(x,bound,m));return
            for b,q,_ in levels[i]:
                if q in chosen:continue
                # Symmetric CRT formula using q-adic starting point.
                y=b+q*((x-b)*invmod(q,m)%m) if m>1 else b
                if y>=bound:continue
                rec(i+1,m*q,y,chosen|{q})
        rec(0,1,0,frozenset())
    return ks,dict(ns)
bound=10**9
frozen=read('minima.json');r={}
union=set()
for tag,s in [('C',C),('T',T),('W',W)]:
    ks,nodes=all_candidates(bound,s)
    if tag=='C' or tag=='T':
        a,_=all_candidates(bound,s,reverse=True)
        assert a==ks
    union.update(ks)
    keep=sorted(k for k in ks if reference.literal(A+S*k,8) is None)
    assert (keep[0] if keep else None)==(frozen[tag]['answer']['k'] if frozen[tag]['answer'] else None)
    r[tag]={'n_compatible_roots':len(ks),'nodes':nodes,'exact9_indices':keep}
g=sorted(k for k in union if reference.literal(A+S*k,8) is None)
assert g[0]==frozen['global']['answer']['k']
for k in r['T']['exact9_indices']:
    assert reference.high_only_geometry(A+S*k)
    assert reference.predicate(A+S*k,9,840) is None
assert not reference.high_only_geometry(A+S*g[0])
for k in sorted(union):
    assert reference.literal(A+S*k,9) is not None
    assert (lower_budget(k) is None)==(k in g)
common=read('common_min.json')['answer']
limit=common['k']+1
ks,counts=all_candidates(limit,C)
assert min(k for k in ks if reference.literal(A+S*k,8) is None)==common['k']
assert len(ks)==1
print(json.dumps(dict(bound=bound,branches=r,all_ninth_dictionary_roots=len(union),exact9_indices=g,common_until_candidate={"bound":limit,"candidates":sorted(ks),"nodes":counts}),indent=2))
