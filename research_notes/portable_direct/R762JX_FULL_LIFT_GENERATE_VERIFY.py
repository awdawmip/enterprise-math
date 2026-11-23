#!/usr/bin/env python3
"""Exact finite full-Euler lifting for a sufficient family, R762JX.
No solver, floats, or native P000 dynamics. Python >=3.10.
For each of four explicit (inactive matching, five singleton colors) slices,
enumerates all 6,435 seven-triple assignments and builds/validates a
42-edge Euler multigraph whenever the triple support graph spans each
component of the flexible support graph.
"""
from itertools import combinations, product
from collections import Counter
import hashlib, json

PORTS = list(combinations(range(6), 2))
COLORS = list(combinations(range(6), 3))
PI = {p:i for i,p in enumerate(PORTS)}
TRI = [tuple(PI[p] for p in combinations(t, 2)) for t in COLORS]
CASES = [
    ((),             (0,1,2,3,4)),
    ((0,),           (4,5,6,7,8)),
    ((0,9),          (5,6,7,8,9)),
    ((0,9,14),       (5,6,7,8,11)),
]

def sides(color, active):
    vertices = [p for p in TRI[color] if p in active]
    assert len(vertices) in (2,3)
    return tuple(combinations(vertices, 2))

def roots_on(n, edges):
    parent=list(range(n))
    def root(i):
        while parent[i]!=i:
            parent[i]=parent[parent[i]]
            i=parent[i]
        return i
    for a,b in edges:
        x,y=root(a),root(b)
        if x!=y:parent[x]=y
    return [root(i) for i in range(n)]

def component_data(M,D):
    active=set(range(15))-set(M)
    full = [k for k in range(20) if k not in D and len(sides(k,active))==3]
    edges = [e for k in full for e in sides(k,active)]
    roots=roots_on(15,edges)
    comp={}
    for v in sorted(active):
        comp.setdefault(roots[v],len(comp))
    labels={v:comp[roots[v]] for v in active}
    c=len(comp)
    return active,full,labels,c

def triple_spans(active, full, T, labels):
    e=[z for k in T if k in full for z in sides(k,active)]
    rr=roots_on(15,e)
    groups={}
    for v,l in labels.items():
        groups.setdefault(l,set()).add(rr[v])
    return all(len(xs)==1 for xs in groups.values())

def quotient_witness(active, labels, c, D, n):
    force=[]
    for k in range(20):
        opts=sides(k,active)
        if k not in D and len(opts)==1:
            force.extend([opts[0]]*n[k])
    f_mask=0
    for u,v in force:
        f_mask ^= (1<<labels[u]) ^ (1<<labels[v])
    candidates=[sides(k,active) for k in sorted(D)]
    for chosen in product(*candidates):
        q=f_mask
        for u,v in chosen:
            q ^= (1<<labels[u]) ^ (1<<labels[v])
        if q:continue
        quot_edges=[(labels[u],labels[v]) for u,v in force+list(chosen)]
        rr=roots_on(c,quot_edges)
        if len(set(rr))==1:
            return list(chosen)
    return None

def parity(edges):
    b=0
    for u,v in edges:b^=(1<<u) ^ (1<<v)
    return b

def triple_parity_correction(full_triples,active,residual):
    generators=[]
    for k in full_triples:
        for uv in sides(k,active):
            generators.append((k,uv))
    basis={}
    for idx,(_,uv) in enumerate(generators):
        v=(1<<uv[0])^(1<<uv[1]); expr=1<<idx
        for p in sorted(basis,reverse=True):
            if (v>>p)&1:
                vec,rep=basis[p];v^=vec;expr^=rep
        if v:
            basis[v.bit_length()-1]=(v,expr)
    expr=0;v=residual
    for p in sorted(basis,reverse=True):
        if (v>>p)&1:
            vec,rep=basis[p];v^=vec;expr^=rep
    if v: return None
    per_color={k:0 for k in full_triples}
    for j,(k,uv) in enumerate(generators):
        if (expr>>j)&1:
            per_color[k]^=(1<<uv[0])^(1<<uv[1])
    assert all(x.bit_count() in (0,2) for x in per_color.values())
    return per_color

def connected_triple_edges(color,target,active):
    opts=list(sides(color,active));assert len(opts)==3
    if target==0:return opts  # triangle 3-cycle; full coverage, degree parity 0
    selected=[e for e in opts if ((1<<e[0])^(1<<e[1]))==target]
    assert len(selected)==1
    edge=selected[0]
    spare=next(e for e in opts if e!=edge)
    # one selected edge plus two copies of a different edge connects all 3 vertices
    return [edge,spare,spare]

def construct(M,D,T):
    active,full,labels,c=component_data(M,D)
    if not triple_spans(active,full,T,labels):return None
    other=set(range(20))-set(D)-set(T)
    assert len(D)==5 and len(T)==7 and len(other)==8
    n={k:1 if k in D else (3 if k in T else 2) for k in range(20)}
    sing=quotient_witness(active,labels,c,D,n)
    assert sing is not None, 'JW.1 quotient property failed for this exact case'
    mult={k:[] for k in range(20)}
    for k,edge in zip(sorted(D),sing):mult[k].append(edge)
    triples_full=[]
    for k in sorted(set(range(20))-set(D)):
        opts=list(sides(k,active))
        if len(opts)==1:
            mult[k]=[opts[0]]*n[k]
        elif n[k]==2:
            mult[k]=opts[:2] # two distinct sides, spans all 3 vertices
        else:
            triples_full.append(k)
            mult[k]=opts # 3-cycle, spans all 3 vertices
    current=parity(e for lst in mult.values() for e in lst)
    correction=triple_parity_correction(triples_full,active,current)
    assert correction is not None, 'triple support failed span despite graph test'
    for k in triples_full:
        mult[k]=connected_triple_edges(k,correction[k],active)
    assert verify(M,D,T,mult)
    return mult

def verify(M,D,T,mult):
    active=set(range(15))-set(M)
    if set(mult)!=set(range(20)):return False
    n={k:1 if k in D else (3 if k in T else 2) for k in range(20)}
    degree=Counter();edges=[]
    for k,lst in mult.items():
        allowed=set(sides(k,active))
        if len(lst)!=n[k]:return False
        for edge in lst:
            if tuple(edge) not in allowed:return False
            degree.update(edge);edges.append(tuple(edge))
    if len(edges)!=42:return False
    if any(degree[v]<2 or degree[v]%2 for v in active):return False
    if any(degree[v] for v in M):return False
    roots=roots_on(15,edges)
    if len({roots[v] for v in active})!=1:return False
    return True

def compact_certificate(mult):
    return [[list(e) for e in mult[k]] for k in range(20)]

def main():
    rows=[];first=[];aggregate=hashlib.sha256()
    for M,D in CASES:
        active, full,labels,c=component_data(M,D)
        passes=0;failed=0;chosen_count=0
        choices=list(set(range(20))-set(D))
        for T in combinations(sorted(choices),7):
            if not triple_spans(active,full,T,labels):
                failed+=1
                continue
            cert=construct(M,D,T)
            assert cert is not None and verify(M,D,T,cert)
            passes+=1
            capsule={'M':list(M),'D':list(D),'T':list(T),'edges_by_color':compact_certificate(cert)}
            record=json.dumps(capsule,sort_keys=True,separators=(',',':')).encode()
            aggregate.update(len(record).to_bytes(4,'big')+record)
            if passes==1:
                first.append(capsule)
        assert passes+failed==6435
        row={'inactive_port_indices':list(M),'inactive_ports':[''.join(map(str,PORTS[x])) for x in M],
             'singleton_color_indices':list(D),'singleton_colors':[''.join(map(str,COLORS[x])) for x in D],
             'flexible_component_count':c,'triple_sets_total':6435,
             'triple_graph_spanning':passes,'triple_graph_not_spanning':failed,
             'exact_42_event_certificates_verified':passes}
        print(row,flush=True)
        rows.append(row)
    out={'schema':'R762JX_FULL_EULER_SPANNING_TRIPLES_V1','date':'2026-11-23',
         'model':'unsigned six-axis composite Port-Euler observer',
         'unreviewed_prerequisite':'R762JW theorem JW.1 (finite quotient-side coverage)',
         'total_checked':sum(r['triple_sets_total'] for r in rows),
         'total_sufficient_cases':sum(r['triple_graph_spanning'] for r in rows),
         'full_valid_euler_certificates':sum(r['exact_42_event_certificates_verified'] for r in rows),
         'ordered_44_to_42_reinflation_cases':5*sum(r['exact_42_event_certificates_verified'] for r in rows),
         'canonical_serialized_certificates_sha256':aggregate.hexdigest(),
         'rows':rows,'example_certificates':first}
    with open('R762JX_EXACT_EVIDENCE.json','w') as f:json.dump(out,f,indent=2)
    assert out['total_sufficient_cases']==448+428+813+495
    assert not verify(tuple(CASES[0][0]),tuple(CASES[0][1]),tuple(first[0]['T']),{k:[] for k in range(20)})
    print('TOTAL',out['total_checked'],out['total_sufficient_cases'],'DIGEST',aggregate.hexdigest(),flush=True)
if __name__=='__main__':main()
