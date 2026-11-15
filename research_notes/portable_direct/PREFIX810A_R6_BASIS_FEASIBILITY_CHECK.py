#!/usr/bin/env python3
"""Exact bounded-fiber move-connectivity tests for fixed and face-adaptive fundamental cycle bases.
Run alongside PREFIX810_R6_CYCLE_OBSERVER_CHECK.py (immutable PREFIX-810 predecessor).
"""
import itertools,json
from PREFIX810_R6_CYCLE_OBSERVER_CHECK import signed_fundamental_cycles, table_fibers


def moves_for(m,n,edges,active):
    cycles=signed_fundamental_cycles(m,n,[edges[e] for e in active])
    ans=[]
    for g in cycles:
        v=[0]*len(edges)
        for j,e in enumerate(active):v[e]=g[j]
        ans.append(v)
    return ans


def connected(xs,moves):
    allowed=set(xs);seen={xs[0]};queue=[xs[0]]
    while queue:
        x=queue.pop()
        for g in moves:
            for sign in (-1,1):
                y=tuple(a+sign*b for a,b in zip(x,g))
                if y in allowed and y not in seen:
                    seen.add(y);queue.append(y)
    return len(seen)


def run_family(m,n,vals):
    edges=[(i,j) for i in range(m) for j in range(n)]
    counts={'capacity_patterns':len(vals)**len(edges),'margin_fibers':0,'complete_tables':0,'multi_table_fibers_tested':0,
            'fixed_basis_disconnected_fibers':0,'adaptive_face_disconnected_fibers':0}
    fixed_witness=None;face_witness=None
    for K in itertools.product(vals,repeat=len(edges)):
        global_moves=moves_for(m,n,edges,[i for i,k in enumerate(K) if k>0])
        F=table_fibers(m,n,edges,K)
        counts['margin_fibers']+=len(F)
        counts['complete_tables']+=sum(map(len,F.values()))
        for margins,xs in F.items():
            if len(xs)<2:continue
            counts['multi_table_fibers_tested']+=1
            fixed_component=connected(xs,global_moves)
            if fixed_component<len(xs):
                counts['fixed_basis_disconnected_fibers']+=1
                if fixed_witness is None:
                    fixed_witness={'capacities':K,'margins':margins,'tables':xs,'basis_moves':global_moves,'component_size':fixed_component}
            # Remove each edge that is already constant on the *entire actual fiber*, then choose a fresh forest.
            active=[i for i in range(len(edges)) if min(x[i] for x in xs)!=max(x[i] for x in xs)]
            face_moves=moves_for(m,n,edges,active)
            adaptive_component=connected(xs,face_moves)
            if adaptive_component<len(xs):
                counts['adaptive_face_disconnected_fibers']+=1
                if face_witness is None:
                    face_witness={'capacities':K,'margins':margins,'tables':xs,'variable_edges':active,'basis_moves':face_moves,'component_size':adaptive_component}
    return dict(rows=m,columns=n,capacity_values=list(vals),**counts,first_fixed_basis_witness=fixed_witness,first_adaptive_face_witness=face_witness)


def main():
    families=[run_family(2,3,(0,1,2)),run_family(3,3,(0,1))]
    w=families[0]['first_fixed_basis_witness']
    assert w['capacities']==(1,1,1,1,1,1) and w['margins']==((1,1),(0,1,1))
    assert len(w['tables'])==2 and w['component_size']==1
    a,b=w['tables']
    assert tuple(y-x for x,y in zip(a,b))==(0,1,-1,0,-1,1)
    assert tuple(w['basis_moves'][1][i]-w['basis_moves'][0][i] for i in range(6))==(0,1,-1,0,-1,1)
    assert families[0]['adaptive_face_disconnected_fibers']==0
    z=families[1]['first_adaptive_face_witness']
    assert z is not None and len(z['tables'])==4 and z['component_size']==1
    assert z['capacities']==(0,1,1,1,1,1,1,1,1)
    assert z['margins']==((1,1,2),(1,1,2))
    assert z['variable_edges']==[1,2,3,4,5,6,7,8]
    # For the adaptive-face 3x3 witness, enumerate every spanning-tree choice.
    graph_edges=[(i,j) for i in range(3) for j in range(3)]
    active=z['variable_edges'];var_edges=[graph_edges[i] for i in active]
    choices=0;connected_choices=0
    for tree_idx in itertools.combinations(range(len(active)),5):
        order=list(tree_idx)+[i for i in range(len(active)) if i not in tree_idx]
        cycles=signed_fundamental_cycles(3,3,[var_edges[i] for i in order])
        if not all(g[5+i]==1 and all(g[5+j]==0 for j in range(3) if j!=i)
                   for i,g in enumerate(cycles)):
            continue  # chosen 5 edges were not actually a spanning tree
        choices+=1
        fullmoves=[]
        for g in cycles:
            v=[0]*9
            for j,k in enumerate(order):v[active[k]]=g[j]
            fullmoves.append(v)
        connected_choices+=int(connected(z['tables'],fullmoves)==len(z['tables']))
    assert choices==36 and connected_choices==30
    keys=['capacity_patterns' ,'margin_fibers','complete_tables','multi_table_fibers_tested','fixed_basis_disconnected_fibers','adaptive_face_disconnected_fibers']
    result={'schema':'PREFIX810A_R6_BASIS_FEASIBILITY_V2','families':families,'totals':{k:sum(x[k] for x in families) for k in keys},
            'conclusion':'Fundamental cycles form a Z-module basis but a preselected basis can disconnect feasible fibers; deleting edges constant across the entire fiber does not always repair the disconnection.',
            'alternative_forest_witness':{'spanning_trees':choices,'connected_basis_choices':connected_choices,'disconnected_basis_choices':choices-connected_choices},'status':'ALL_EXACT_CHECKS_PASSED'}
    print(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2))

if __name__=='__main__':main()
