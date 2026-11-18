"""Fixed row/residue margins on an exposed PFSSV cell; no prime generation or sampling."""
import argparse
from collections import Counter, defaultdict, deque
from fractions import Fraction
from hashlib import sha256
from math import comb, gcd, prod
from pathlib import Path
import json


def fraction(x):
    return str(Fraction(x))


def load_cell(path):
    with path.open('rb') as source:
        first=next(source)
    cell=json.loads(first)
    assert (cell['X'],cell['num'],cell['den'],cell['upper'])==(100000,1,100,101000)
    digest=sha256(first).hexdigest()
    assert digest=="fcfc138fbbddacd089c228b4cb3783e55064b9c9879d84f5de642911ebc860a0"
    return cell,digest


def maxflow(cap,source,sink):
    """Integral augmenting paths in the small bipartite residual network."""
    residual=defaultdict(dict)
    for (u,v),amount in cap.items():
        if amount:
            residual[u][v]=amount
            residual[v].setdefault(u,0)
    total=0
    while True:
        pred={source:None}
        queue=deque([source])
        while queue and sink not in pred:
            u=queue.popleft()
            for v,a in residual[u].items():
                if a and v not in pred:
                    pred[v]=u
                    queue.append(v)
        if sink not in pred:
            return total
        path=[]; v=sink
        while v!=source:
            path.append((pred[v],v))
            v=pred[v]
        amount=min(residual[u][v] for u,v in path)
        for u,v in path:
            residual[u][v]-=amount
            residual[v][u]+=amount
        total+=amount


def reachable(adj,u):
    seen={u}
    queue=[u]
    for j in queue:
        for v in adj[j]-seen:
            seen.add(v)
            queue.append(v)
    return seen


def minmax_block(row,res,caps,initial):
    edge=(row,res)
    network={}
    for (p,r),n in caps.items():
        if (p,r)!=edge:
            network[p,-1-r]=n-initial[p,r]
            network[-1-r,p]=initial[p,r]
    x=initial[edge]
    return x-min(x,maxflow(network,row,-1-res)), x+min(caps[edge]-x,maxflow(network,-1-res,row))


def solve(cell):
    rows={record['p']:record for record in cell['rows']}
    sites=defaultdict(list)
    for p,row in rows.items():
        assert sum(row['q_mod_30_counts'])==row['count']
        for q in range(row['qlo'],row['qhi']+1):
            sites[q].append(p)
    shared={q:list(ps) for q,ps in sorted(sites.items()) if len(ps)>1}
    assert shared=={322:[311,313],356:[281,283],372:[269,271],419:[239,241],441:[227,229]}
    raw=sum(row['count'] for row in rows.values())
    assert raw==237
    residues=Counter()
    for row in rows.values():
        for r,k in enumerate(row['q_mod_30_counts']):
            residues[r]+=k
    surplus=raw-236  # Independent unique-address count from the published receipt.
    assert surplus==1 and all(not v or gcd(r,30)==1 for r,v in residues.items())
    eligible_shared={q for q in shared if residues[q%30]}
    assert eligible_shared=={419} and len(shared[419])-1==surplus
    forced_on=eligible_shared
    residues[29]-=surplus
    assert sum(residues.values())==236 and residues[29]==29
    assert all(not n or gcd(r,30)==1 for r,n in residues.items())
    blocks=defaultdict(list)
    for q,ps in sorted(sites.items()):
        if residues[q%30] and q not in forced_on:
            assert len(ps)==1
            blocks[ps[0],q%30].append(q)
    caps={e:len(v) for e,v in blocks.items()}
    initial={}
    for p,r in caps:
        initial[p,r]=rows[p]['q_mod_30_counts'][r]-int(r==29 and p in sites[419])
        assert 0<=initial[p,r]<=caps[p,r]
    for p,row in rows.items():
        assert sum(n for (i,r),n in initial.items() if i==p)+int(p in sites[419])==row['count']
    for r,k in residues.items():
        assert sum(n for (i,j),n in initial.items() if j==r)+int(r==29)==k
    chosen={q for e,qs in blocks.items() for q in qs[:initial[e]]}
    adj=defaultdict(set)
    for (p,r),vs in blocks.items():
        for q in vs:
            u,v=(p,-1-r) if q not in chosen else (-1-r,p)
            adj[u].add(v)
    vertices=set(adj)|{v for vs in adj.values() for v in vs}
    reach={v:reachable(adj,v) for v in vertices}
    flexible=set()
    for (p,r),qs in blocks.items():
        if p in reach[-1-r] and -1-r in reach[p]:
            flexible.update(qs)
    active={p for (p,r),qs in blocks.items() if qs[0] in flexible}|{
            -1-r for (p,r),qs in blocks.items() if qs[0] in flexible}
    groups={min(v for v in active if v in reach[u] and u in reach[v]) for u in active}
    always_one=(chosen-flexible)|forced_on
    always_zero=set(sites)-flexible-always_one
    table={}
    for edge,c in caps.items():
        low,high=minmax_block(*edge,caps,initial)
        assert low<=initial[edge]<=high
        # A block can be rigid in count while its individual slots remain switchable.
        flexible_by_bounds=(low<c and high>0)
        assert flexible_by_bounds==(blocks[edge][0] in flexible)
        table[edge]=(c,initial[edge],low,high)
    face_dim=len(flexible)-len(active)+len(groups)
    internal_dim=sum(c-1 for e,(c,x,l,h) in table.items() if blocks[e][0] in flexible)
    count_dim=face_dim-internal_dim
    exact_orbit=prod(comb(n,initial[e]) for e,n in caps.items())
    assert all((lo,hi) in ((0,0),(c,c),(0,c)) for c,x,lo,hi in table.values())
    digest=lambda vals:sha256(','.join(map(str,sorted(vals))).encode()).hexdigest()
    return ({"frozen":{"rows":len(rows),"zero_rows":sum(not r['count'] for r in rows.values()),
                       "addresses":len(sites),"raw":raw,"unique":sum(residues.values()),
                       "residue_totals":dict(sorted(residues.items())),"shared":shared},
             "row_and_residue_margins":{"forced_zero":len(always_zero),"forced_one":len(always_one),
                         "forced_one_addresses":sorted(always_one),"flexible":len(flexible),
                         "flexible_sha256":digest(flexible),"forced_zero_sha256":digest(always_zero),
                         "active_vertices":len(active),"active_components":len(groups),
                         "flexible_blocks":sum(blocks[e][0] in flexible for e in table),
                         "fixed_count_blocks":sum(lo==hi for c,x,lo,hi in table.values()),
                         "blocks":len(table),"occupancy_polytope_dimension":face_dim,
                         "block_count_polytope_dimension":count_dim},
             "all_blocks_rows_p_r_capacity_frozen_min_max":[[p,r,*v] for (p,r),v in sorted(table.items())],
             "row_by_residue_fiber":{"size":str(exact_orbit),"count_fixed":len(table),
                         "individual_flexible":sum(c for c,x,l,h in table.values() if 0<x<c),
                         "individual_forced_one":1+sum(c for c,x,l,h in table.values() if x==c)},
             "q50009":{"block":list(table[2,29]),"within_block_probability_given_table":
                        fraction(Fraction(initial[2,29],caps[2,29]))}},
            (sites,blocks,table,chosen,always_one,always_zero,flexible))


def examples(data):
    sites,blocks,table,chosen,ones,zeros,flex=data
    # A 4-slot unbiased switch among actual q addresses preserving both coarse margins.
    for p in [2]:
        for k in [3]:
            for r in [29]:
                for s in [1,7,11,13,17,19,23]:
                    edges=((p,r),(p,s),(k,r),(k,s))
                    if not all(e in blocks for e in edges):
                        continue
                    options=[[a for a in blocks[e] if (a in chosen)==wanted]
                             for e,wanted in zip(edges,(True,False,False,True))]
                    if not all(options):
                        continue
                    qs=[v[0] for v in options]
                    def counts(sel):
                        return (Counter(x for q in sel for x in sites[q]), Counter(q%30 for q in sel))
                    assert counts(chosen)==counts(chosen.symmetric_difference(qs))
                    return {"rows":[p,k],"residues":[r,s],"addresses":qs,
                            "before":[1,0,0,1],"after":[0,1,1,0]}
    raise AssertionError("no exact 4-cycle")


def endpoint_lift(cap,mean,edge,lo,hi):
    # One flow for the means conditional on either endpoint of the chosen block.
    if lo==hi:
        return mean[edge]==lo
    d=hi-lo
    w=mean[edge]-lo
    assert 0<w<d
    network={}
    rows=Counter(); cols=Counter()
    for (p,r),c in cap.items():
        m=mean[p,r]
        lower=max(0,d*m-(d-w)*c)
        upper=min(w*c,d*m)
        if (p,r)==edge:
            lower=upper=w*hi
        if lower>upper:
            return False
        rows[p]+=w*m-lower
        cols[r]+=w*m-lower
        network[p,-1-r]=upper-lower
    if min(rows.values())<0 or min(cols.values())<0:
        return False
    source,sink=10000,-10000
    network.update({(source,p):a for p,a in rows.items()})
    network.update({(-1-r,sink):a for r,a in cols.items()})
    return maxflow(network,source,sink)==sum(rows.values())


def sharp_law(data):
    sites,blocks,table,_,_,_,_=data
    target=(2,29)
    core={f:c for f,(c,x,_,_) in table.items() if 0<x<c}
    xcore={f:table[f][1] for f in core}
    bounds={f:minmax_block(*f,core,xcore) for f in core}
    assert all(endpoint_lift(core,xcore,e,*v) for e,v in bounds.items())
    exceptional={e:v for e,v in bounds.items() if v!=(0,core[e])}
    assert exceptional=={(2,29):(0,13),(29,29):(1,1),(31,17):(1,1)}
    assert bounds[target]==(0,13)
    assert bounds[29,29]==bounds[31,17]==(1,1)
    assert sum(v[1] for e,v in table.items() if e[1]==29 and v[1]==v[0])==14
    # B(13)-B(4) is the sum of five 4-cycles with their given multiplicities.
    delta=Counter()
    for p,r,w in [(3,11,5),(5,11,1),(7,11,1),(17,13,1),(23,11,1)]:
        delta[2,29]+=w; delta[p,29]-=w; delta[p,r]+=w; delta[2,r]-=w
    for s in range(14):
        amounts={e:Fraction(9*v[1]+(s-4)*delta[e],9) for e,v in table.items()}
        assert all(0<=a<=table[e][0] for e,a in amounts.items())
        assert amounts[target]==s
        for axis in range(2):
            for val in {e[axis] for e in table}:
                assert sum(a-table[e][1] for e,a in amounts.items() if e[axis]==val)==0
    # Kruskal forest, no probabilistic computations.
    parent={}
    def find(v):
        parent.setdefault(v,v)
        while parent[v]!=v:
            parent[v]=parent[parent[v]]
            v=parent[v]
        return v
    questions=[]
    for (p,r),c in sorted(core.items()):
        a,b=find(p),find(-1-r)
        if a==b:
            count=table[p,r][1]
            questions.append({"block":[p,r],"addresses":blocks[p,r][:2],
                              "uniform_cooccupancy":str(Fraction(count*(count-1),c*(c-1)))})
        else:
            parent[a]=b
    components=len({find(v) for v in parent})
    assert len(core)-len(parent)+components==len(questions)==37
    return {"block_law_with_all_address_means":{
                    "saturated_original_blocks":len(table)-len(core),
                    "partial_blocks_with_all_laws_from_0_to_capacity":len(core)-len(exceptional),
                    "partial_exception_intervals":[[*e,*v] for e,v in sorted(exceptional.items())],
                    "each_endpoint_lift_verified":True},
            "actual_block_example":{"p":2,"r":29,"two_addresses":blocks[target][:2],
                    "sharp_count_support":[0,13],"mean":4,"sharp_P_count_zero":["0","9/13"],
                    "sharp_P_named_pair_given_symmetry":["3/68","3/17"],
                    "endpoint_delta_B13_minus_B4":[[p,r,k] for (p,r),k in sorted(delta.items())],
                    "fixed_positive_counts_inside_partial_blocks":sorted([list(e)+[lo] for e,(lo,hi) in bounds.items() if lo==hi])},
            "pair_identification":{"partial_blocks":len(core),"vertices":len(parent),
                    "components":components,"minimum_same_block_pair_queries":len(questions),
                    "one_optimal_query_list":questions}}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--source',type=Path,
                    default=Path('research_artifacts/PFSSV_REVISION_20260908/cell_profiles.jsonl'))
    args=ap.parse_args()
    cell,h=load_cell(args.source)
    result,data=solve(cell)
    result["cycle_example"]=examples(data)
    result.update(sharp_law(data))
    result["source_first_line_sha256"]=h
    print(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True))


if __name__=='__main__':
    main()
