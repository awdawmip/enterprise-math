#!/usr/bin/env python3
"""Exact finite saturation and uniqueness certificate for all R=1..65536.
Imports the frozen R284CO observer, checks its unmodified population hash.
"""
import hashlib,json
from collections import Counter
from pathlib import Path
from R284CO_spectral_witness_checker import P,D,Z,SELECT,FROZEN_SHA,words,arcs,dist

X,A=words(),arcs()
n=len(X)
rows=[[] for _ in range(63)]
for i,x in enumerate(X):
    for k,d in enumerate(sorted(dist(x,a) for a in A)[1:]):
        rows[k].append((d,i))
for row in rows:row.sort(reverse=True)

# tau[i] is the first rank at which i belongs to a whole included tie block
# in at least one level.  Thus M_R={i:tau[i]<=R} is the set of forced sites.
tau=[n+1]*n
tie_runs=[]
for k,row in enumerate(rows):
    lo=0
    while lo<n:
        hi=lo+1
        while hi<n and row[hi][0]==row[lo][0]:hi+=1
        for j in range(lo,hi):
            i=row[j][1]
            if hi<tau[i]:tau[i]=hi
        if hi-lo>1:
            tie_runs.append((k,lo,hi,[i for _,i in row[lo:hi]],row[lo][0]))
        lo=hi
assert all(t<=n for t in tau)
threshold=max(tau)
terminal=[(X[i],i) for i,t in enumerate(tau) if t==threshold]

# Only tie-boundary ranks below saturation can have discretionary choices.
by_rank={}
for k,lo,hi,ids,value in tie_runs:
    for r in range(max(1,lo+1),min(threshold,hi-1)+1):
        by_rank.setdefault(r,[]).append((k,lo,hi,ids,value))
exceptions=[]
nonzero_quota=[]
for r in sorted(by_rank):
    groups=[]
    for k,lo,hi,ids,value in by_rank[r]:
        forced=[i for i in ids if tau[i]<=r]
        missing=[i for i in ids if tau[i]>r]
        q=r-lo
        deficit=max(0,q-len(forced))
        if deficit:
            groups.append({'level':k+2,'cutoff':value,'size':hi-lo,
                           'quota':q,'forced':len(forced),'deficit':deficit,
                           'unforced_residues':sorted(X[i] for i in missing)})
    if groups:
        nonzero_quota.append(r)
        assert len(groups)==1 and groups[0]['deficit']==1 and len(groups[0]['unforced_residues'])==2,(r,groups)
        mand=[X[i] for i,t in enumerate(tau) if t<=r]
        opts=groups[0]['unforced_residues']
        def digest(v):return hashlib.sha256(b''.join(y.to_bytes(8,'big') for y in sorted(v))).hexdigest()
        exceptions.append({'rank':r,'minimum_core_size':len(mand)+1,'minimum_core_count':2,
                           'mandatory_size':len(mand),'residual_constraint':groups[0],
                           'core_sha256':sorted(digest(mand+[x]) for x in opts)})
assert nonzero_quota == [779,1263,1563,7587],nonzero_quota
assert [e['minimum_core_size'] for e in exceptions]==[21944,25997,27499,42637]
assert sum(t<=20000 for t in tau)==61404
assert sum(t<=64 for t in tau)==3712
assert threshold>20000
assert all(t<=threshold for t in tau)
# At r=threshold, every word is forced. At all higher r, every word remains forced.
# Thus every minimum core is unique there, and r=n forces X by cardinality.
cert={
 'schema':'R284CW_COMPLETE_65536_RANK_UNIQUENESS_SATURATION_V1',
 'status':'AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED',
 'source':{'frozen_import':'R284CO_spectral_witness_checker.py','P':P,'D':D,'Z':Z,
           'SELECT':SELECT,'frozen_population_sha256':FROZEN_SHA},
 'domain':{'codewords':n,'labeled_arcs':len(A),'nonconstant_distance_levels':len(rows),
           'rank_min':1,'rank_max':n,'exact_distance_evaluations':n*len(A)},
 'saturation':{'first_rank_whole_population_mandatory':threshold,
               'mandatory_at_rank_before':sum(t<threshold for t in tau),
               'last_added_sites':len(terminal),'last_added_residues':sorted(x for x,i in terminal),
               'mandatory_at_rank_64':sum(t<=64 for t in tau),
               'mandatory_at_rank_20000':sum(t<=20000 for t in tau)},
 'tie_boundary_ranks_below_saturation':len(by_rank),
 'simultaneous_tie_boundary_ranks_below_saturation':sum(len(x)>1 for x in by_rank.values()),
 'ranks_with_nonzero_residual_quota':nonzero_quota,
 'nonunique_minimum_core_ranks_all_65536':nonzero_quota,
 'exceptional_cores':exceptions,
 'argument':'M_R={x:min_k(end_rank_of_full_equal_value_block_containing_x at level k)<=R}. Every site in M_R is forced. Only incomplete cutoff tie blocks can impose residual quotas. The exact enumerated nonzero quotas are four independent binary choices. At R>=max_x tau(x), M_R=X, so unique minimum core is X.',
 'independent_review':'NOT_REVIEWED'}
out=Path(__file__).with_name('R284CW_complete_rank_saturation_certificate.json')
out.write_text(json.dumps(cert,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'threshold':threshold,'terminal_count':len(terminal),
                  'terminal_residues':cert['saturation']['last_added_residues'],
                  'rank_before':cert['saturation']['mandatory_at_rank_before'],
                  'tie_ranks':len(by_rank),'simultaneous':cert['simultaneous_tie_boundary_ranks_below_saturation'],
                  'exceptions':[ (e['rank'],e['minimum_core_size']) for e in exceptions]},ensure_ascii=False))
