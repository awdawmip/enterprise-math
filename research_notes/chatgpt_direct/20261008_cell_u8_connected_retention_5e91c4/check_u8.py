#!/usr/bin/env python3
"""Finite source-pinned BRC checks; infinite statements are proved in NOTE.md.
No full infinite-state evolution, force calibration or native triad is claimed.
"""
from pathlib import Path
from itertools import permutations,combinations
from fractions import Fraction as Q
import json,gzip,hashlib
import connected_retention as m
r=m.r;ROOT=Path(__file__).parent;EV=ROOT/'evidence';EV.mkdir(exist_ok=True)
checks=0

def ck(x,label):
    global checks
    checks+=1
    if not x:raise AssertionError((checks,label))

def add(a,b):return tuple(x+y for x,y in zip(a,b))

def full_layers(o,L):
    out=[{r.ZERO:r.brc.CWM_ONE}]
    for n in range(1,L+1):
        nxt={}
        for z,v in out[-1].items():
            for p in r.PORTS:
                y=r.advance(z,p)
                nxt[y]=r.merge(nxt.get(y,m.ZERO),r.serial(v,o.edge))
        ck(r.total(nxt.values())==o.series.depth(n),'full ordered-word layer mass/count/dominant')
        for z,v in nxt.items():ck(v==o.g(n,z),'endpoint orbit quotient, not orbit mass')
        out.append(nxt)
    return out

z=r.ZERO;e1=r.direction(0);e2=r.direction(2);e3=r.direction(4)
layouts={'pair_adjacent':(z,e1),'pair_gap':(z,add(e1,e1)),
         'square_221':(z,e1,add(e1,e2),e2),
         'four_chain':(z,e1,add(e1,e1),tuple(3*a for a in e1)),
         'four_star':(z,e1,e2,e3)}
o=m.Overlap();model=m.Candidate(o,24)
full=full_layers(o,5);glue=[]
for n in range(6):
    for target in (z,e1,e2,add(e1,e2),add(e1,e1),e3):
        parts=[]
        for a in range(n+1):
            for x,v in full[a].items():
                w=full[n-a].get(m.difference(x,target),m.ZERO)
                if w.live:parts.append(r.serial(v,w))
        glued=r.total(parts);want=r.total(o.g(n,target) for split in range(n+1))
        ck(glued==want,'two source paths meeting = reversed concatenation plus split')
        glue.append({'n':n,'target':target,'glued':glued})

for N,count in ((2,1),(3,3),(4,16),(5,125)):
    ts=m.trees(N);ck(len(ts)==count,'explicit labelled tree count')
    for T in ts:
        seen={0}
        for _ in range(N):
            for a,b in T:
                if a in seen or b in seen:seen|={a,b}
        ck(seen==set(range(N)) and len(T)==N-1,'spanning tree certificate')

# Positive pair-to-tree algebra, full CWM equality, not just rounded totals.
a=o.k(24,e1);b=o.k(24,add(e1,e2));square=model.score(layouts['square_221'])
rhs=r.serial(a,r.serial(r.merge(a,b),r.merge(a,b)))
rhs=r.total(rhs for _ in range(4))
ck(square['lower']==rhs,'square graph exact tree polynomial 4a(a+b)^2')

# Relative-coordinate tree increment bijections; no distinguished physical origin.
inc=(e1,e2,e3)
bijections=[]
for T in m.trees(4):
    positions={0:z}; todo=list(zip(T,inc));directed=[]
    while todo:
        for j,(edge,v) in enumerate(todo):
            a0,b0=edge
            if a0 in positions and b0 not in positions:
                positions[b0]=add(positions[a0],v);directed.append((a0,b0,v));todo.pop(j);break
            if b0 in positions and a0 not in positions:
                positions[a0]=add(positions[b0],v);directed.append((b0,a0,v));todo.pop(j);break
        else:raise AssertionError('tree traversal failed')
    for a0,b0,v in directed:ck(m.difference(positions[b0],positions[a0])==v,'increment recovered exactly')
    bijections.append({'tree':T,'oriented_edges':directed,'positions':positions})

# Positive all-word tails; they certify coefficients, not finite hard walls.
links=[]
for v in (z,e1,add(e1,e1),add(e1,e2),tuple(3*a for a in e1),add(add(e1,e2),e3)):
    vals=[o.interval(L,v) for L in (12,18,24,28)]
    for (lo,hi),(lo2,hi2) in zip(vals,vals[1:]):
        ck(lo.total<=lo2.total<=hi.total,'longer exact prefix inside earlier whole-tail interval')
        ck(hi2.total<=hi.total,'nested uniform-tail upper bounds')
    links.append({'displacement':v,'intervals':{str(L):vals[i] for i,L in enumerate((12,18,24,28))}})

queries={}
for name,cells in layouts.items():
    q=model.one_query(cells);queries[name]=q
    ck(q['surrogate_mass'].total==1,'all proposals, accept and reject branches retained')
    ck(q['true_query_TV_from_surrogate_upper']<Q(1,10**9),'single-query approximation certificate')
    for rec in q['records']:
        lo,hi=map(Q,rec['accept']);ck(0<=lo<=hi<=1,'acceptance interval')
        if rec['collision']:continue
        new=rec['proposed_score'];old=q['score'];y=rec['proposed_cells']
        ck(len(set(y))==len(y),'joint exclusion')
        ck(sum(sum(abs(t-s) for t,s in zip(x,yy)) for x,yy in zip(cells,y))==1,
           'exactly one native-edge material displacement')
        aa=Q(rec['surrogate_accept']);ck(lo<=aa<=hi,'rational surrogate inside true-law interval')
        rev=old['lower'].total/(old['lower'].total+new['lower'].total)
        ck(old['lower'].total*aa==new['lower'].total*rev,'surrogate detailed balance pair')
    for branch in q['branches']:ck(branch['weight'].live,'no negative or silently dropped branch')

sq=queries['square_221']
ck(len(sq['records'])==48 and len(sq['branches'])==88,'complete original-square proposal space')
ck(sum(x['collision'] for x in sq['records'])==8,'eight occupied destinations retained as waits')
classes={}
for rec in sq['records']:
    if rec['collision']:continue
    kind='in_slice_extension' if r.axis(rec['port'])<2 else 'transverse_departure'
    classes.setdefault(kind,[]).append(rec)
ck(len(classes['in_slice_extension'])==8 and len(classes['transverse_departure'])==32,'all vacancy proposals classified')
for values in classes.values():
    ck(len({x['surrogate_accept'] for x in values})==1,'symmetry class exact equality')

# Label, chart and signed-axis covariance, checked without reusing a transformed kernel.
base=layouts['square_221'];basev=model.score(base)['lower']
shift=(3,-2,4,1,-3,2)
ck(model.score(tuple(add(x,shift) for x in base))['lower']==basev,'translation covariance')
for perm in permutations(range(4)):
    ck(model.score(tuple(base[i] for i in perm))['lower']==basev,'material relabelling covariance')
for j in range(6):
    perm=list(range(6));perm[0],perm[j]=perm[j],perm[0]
    moved=tuple(tuple(-x[perm[k]] if k%2 else x[perm[k]] for k in range(6)) for x in base)
    ck(model.score(moved)['lower']==basev,'six-axis signed permutation covariance')

# Four units can split into two internally connected dimers. Pair-sum never loses
# its two fixed bonds; every spanning tree necessarily has a cross-group edge.
splits=[]
for R in (2,3,4,5,6):
    off=tuple(R*a for a in e2);cells=(z,e1,off,add(off,e1))
    pair=r.total(o.k(24,m.difference(cells[i],cells[j])) for i,j in combinations(range(4),2))
    s=model.score(cells)
    ck(pair.total>=2*a.total,'disconnected dimers retain internal pair score')
    for T in m.trees(4):ck(any((i<2)!=(j<2) for i,j in T),'every full tree crosses the split')
    splits.append({'R':R,'pair_sum':pair,'tree_score':s})
for first,second in zip(splits,splits[1:]):
    ck(second['tree_score']['upper'].total<first['tree_score']['lower'].total,
       'strict finite split-score separation with whole-tail certificate')

# Exact two-material excluded-origin normalization from the entire lattice sum.
k0l,k0u=o.interval(24,z);k1l,k1u=o.interval(24,e1);S=o.full_link_mass
ck(k0u.total<S,'positive two-material exclusion normalization')
normalization=(S-k0u.total,S-k0l.total)
pair_adjacent=(12*k1l.total/normalization[1],12*k1u.total/normalization[0])
ck(0<pair_adjacent[0]<=pair_adjacent[1]<1,'all-future stationary adjacent fraction interval')

# The formulas do not use primality/square labels; parameter tests are predeclared.
parameter_checks=[]
for lam in (Q(1,60),Q(1,36)):
    oo=m.Overlap(lam);mm=m.Candidate(oo,24);ss=mm.score(base)
    aa=oo.k(24,e1);bb=oo.k(24,add(e1,e2))
    poly=r.serial(aa,r.serial(r.merge(aa,bb),r.merge(aa,bb)))
    ck(ss['lower']==r.total(poly for _ in range(4)),'tree identity at a separate parameter')
    ck(ss['lower'].total>0 and ss['upper'].total>ss['lower'].total,'nonzero bounded infinite score')
    parameter_checks.append({'lambda':lam,'square_score':(ss['lower'].total,ss['upper'].total)})

summary={'status':'CONDITIONAL_CONNECTED_OVERLAP_CANDIDATE_NOT_NATIVE_FORCE',
 'event_id':'EM-20261008-CELL-U8-CONNECTED-RETENTION-5E91C4',
 'checks':checks,'BRC_calls':dict(r.CALLS),'lambda':str(o.lam),'rho':str(o.rho),
 'link_total_depth':24,'uniform_link_tail':str(o.tail(24)),
 'walk_cache':o.walk.cache_info()._asdict(),'trees_checked':{str(n):len(m.trees(n)) for n in range(2,6)},
 'link_total_all_space':str(S),'two_material_stationary_adjacent_interval':list(map(str,pair_adjacent)),
 'scores':{name:[str(q['score']['lower'].total),str(q['score']['upper'].total)] for name,q in queries.items()},
 'square_proposals':48,'square_collision_proposals':8,'square_retained_surrogate_branches':88,
 'square_surrogate_move_weight':str(sq['surrogate_move'].total),
 'square_true_query_TV_upper':str(sq['true_query_TV_from_surrogate_upper']),
 'square_acceptance_classes':{name:{'count':len(rows),'interval':rows[0]['accept']} for name,rows in classes.items()},
 'split_scores':[{ 'R':v['R'],'pair_sum_lower':str(v['pair_sum'].total),
                   'connected_lower':str(v['tree_score']['lower'].total),'connected_upper':str(v['tree_score']['upper'].total)} for v in splits],
 'parameter_checks':m.encode(parameter_checks),
 'theorems':['overlap_positive_summable_with_exact_split_path_identity',
             'graph_product_relative_partition_finite_iff_connected',
             'positive_disconnected_mixture_has_infinite_relative_partition',
             'connected_tree_score_admits_finite_exclusion_relative_invariant_law',
             'declared_Barker_native_edge_proposals_satisfy_detailed_balance'],
 'native_force':False,'native_triad_lift':False,'physical_time':False,'physical_probability':False,
 'material_reaction_derived':False,'dynamical_field_replaced':False,'long_trajectory_executed':False,
 'infinite_localization_from_finite_cutoff':False,'prime_claim':False,'independent_review':False}

summary['BRC_calls']=dict(r.CALLS)
trace={'full_bulk_layers':full,'gluing':glue,'tree_increment_bijections':bijections,'link_intervals':links,
       'queries':queries,'splits':splits,'pair_normalization':normalization}
raw=(json.dumps(m.encode(trace),ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n').encode()
packed=gzip.compress(raw,mtime=0);(EV/'full_trace.json.gz').write_bytes(packed)
summary.update(trace_sha256=hashlib.sha256(raw).hexdigest(),trace_bytes=len(raw),
               trace_compressed_sha256=hashlib.sha256(packed).hexdigest())
(EV/'results.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(summary,indent=2,ensure_ascii=False))
