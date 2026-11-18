"""K4 port connection groupoids and one typed positive path census. Python 3.10+ stdlib.

Usage: python rotation_check.py --repo /path/to/enterprise-math
"""
import argparse
import hashlib
import json
import sys
from collections import Counter, deque
from itertools import combinations, permutations, product
from pathlib import Path

V = tuple(range(4))
E = tuple(combinations(V, 2))
F = tuple(combinations(V, 3))
S4 = tuple(permutations(V))
S3 = tuple(permutations(range(3)))
colors = range(1, 4)
labels = tuple(product((0, 1), repeat=6))

def compose(p, q):
    return tuple(p[j] for j in q)

def inverse(p):
    return tuple(p.index(j) for j in range(len(p)))

def order(p):
    cur = tuple(range(len(p)))
    for n in range(1, 7):
        cur = compose(p, cur)
        if cur == tuple(range(len(p))):
            return n
    raise AssertionError('unexpected permutation order')

def trans4(a, b):
    p=list(V)
    p[a],p[b]=p[b],p[a]
    return tuple(p)

def raw_transfers(mask):
    table={}
    for (i,j),bit in zip(E,mask):
        r,s=sorted(set(V)-{i,j})
        p=trans4(i,j) if bit else compose(trans4(i,j),trans4(r,s))
        assert {q for q in S4 if q[i]==j and q[j]==i}=={
            trans4(i,j),compose(trans4(i,j),trans4(r,s))}
        table[i,j]=table[j,i]=p
    return table

def raw_bfs(table):
    # Run every successor in the named S4 transport until saturation.
    todo=deque([(0,V)])
    reached={(0,V)}
    while todo:
        v,h=todo.popleft()
        for w in V:
            if v==w:
                continue
            after=compose(table[v,w],h)
            state=(w,after)
            assert after[0]==w
            if state not in reached:
                reached.add(state)
                todo.append(state)
    hol={h for v,h in reached if v==0}
    assert len(reached)==4*len(hol)
    return hol

def s3trans(color):
    others=[j for j in range(3) if j!=color-1]
    p=list(range(3))
    a,b=others
    p[a],p[b]=p[b],p[a]
    return S3.index(tuple(p))

mul=[[S3.index(compose(p,q)) for q in S3] for p in S3]
inv=[S3.index(inverse(p)) for p in S3]
edge_trans=[s3trans(i^j) for i,j in E]
index={e:k for k,e in enumerate(E)}

def ix(i,j):
    return index[tuple(sorted((i,j)))]

def gauge_tag(values):
    loops=tuple(mul[values[ix(0,k)]][mul[values[ix(j,k)]][values[ix(0,j)]]]
                for j,k in combinations(V[1:],2))
    return min(tuple(mul[q][mul[h][inv[q]]] for h in loops) for q in range(6))

def relabel(mask,p):
    return tuple(mask[ix(p[i],p[j])] for i,j in E)

def check_atlas():
    rows={}
    tags={}
    raw_groups=Counter()
    tables=Counter()
    gauges=tuple(product(range(6),repeat=4))
    for mask in labels:
        table=raw_transfers(mask)
        hol=raw_bfs(table)
        linear=tuple(s if b else 0 for s,b in zip(edge_trans,mask))
        for (i,j),p,e in zip(E,(table[e] for e in E),linear):
            actual=tuple((p[i^c]^j)-1 for c in colors)
            assert actual==S3[e]
        orders=[]
        for i,j,k in F:
            h=compose(table[k,i],compose(table[j,k],table[i,j]))
            n=sum(mask[ix(a,b)] for a,b in ((i,j),(j,k),(k,i)))
            assert order(h)==(1,2,3,2)[n]
            orders.append(order(h))
        deg=tuple(sorted((sum(b for e,b in zip(E,mask) if v in e) for v in V),reverse=True))
        cut=any(all(b==(x[i]^x[j]) for (i,j),b in zip(E,mask)) for x in product((0,1),repeat=4))
        expected=1 if max(deg)==0 else 2 if max(deg)==1 else 3 if cut else 6
        assert len(hol)==expected
        tag=gauge_tag(linear)
        rows[mask]=(tag,linear)
        tags.setdefault(tag,[]).append(mask)
        raw_groups[len(hol)]+=1
        tables[deg,len(hol),tuple(sorted(orders))]+=1
    # Independent check of full slot gauge by exhaustive 6^4 recodings.
    for mask,(tag,lin) in rows.items():
        found=set()
        for g in gauges:
            bits=[]
            for k,((i,j),m) in enumerate(zip(E,lin)):
                new=mul[g[j]][mul[m][inv[g[i]]]]
                if new not in (0,edge_trans[k]):
                    break
                bits.append(int(new!=0))
            else:
                found.add(tuple(bits))
        assert found==set(tags[tag])
    invariants=[ms for tag,ms in tags.items() if all(rows[relabel(ms[0],p)][0]==tag for p in S4)]
    strict=[m for m in labels if all(relabel(m,p)==m for p in S4)]
    unmarked=len({min(rows[relabel(m,p)][0] for p in S4) for m in labels})
    assert dict(raw_groups)=={1:1,2:9,3:7,6:47}
    fibers=Counter(map(len,tags.values()))
    assert len(tags)==40 and unmarked==9 and fibers=={1:26,2:6,3:7,5:1}
    assert len(strict)==2 and sorted(map(len,invariants))==[1,3,5]
    return {'edge_order':[list(e) for e in E],
            'holonomy_order_histogram':dict(sorted(raw_groups.items())),
            'named_graph_types':[{'degrees':list(d),'holonomy_order':h,
                'face_permutation_orders':list(f),'labeled_assignments':n}
                for (d,h,f),n in sorted(tables.items())],
            'marked_vertex_gauge_classes':len(tags),'gauge_fiber_histogram':dict(sorted(fibers.items())),
            'labeled_assignments_times_gauges':len(labels)*len(gauges),
            'gauge_classes_mod_vertex_relabeling':unmarked,
            'strict_S4':strict,'S4_fixed_gauge_classes':[sorted(ms) for ms in invariants]}

def word_orbit(w):
    rev=tuple(reversed(w))
    return {u[k:]+u[:k] for u in (w,rev) for k in range(6)}

def branch_brc(repo):
    package=repo/'src'/'enterprise_math'
    kernel=package/'brc_weighted.py'
    sha=hashlib.sha256(kernel.read_bytes()).hexdigest()
    assert sha=='4f3e356227a1c964d33a3ddae94922463ba28097a43b8d1b8f6cd9ca5615fc9f'
    sys.path.insert(0,str(repo/'src'))
    from enterprise_math import brc_weighted as brc
    assert Path(brc.__file__).resolve()==kernel.resolve()
    # Six coordinate slots, first three selected for this sample. A scheduled
    # path always retains its word and ordered native signed-unit microsteps.
    a=((1,0,0,0,0,0),(0,-1,0,0,0,0),(0,0,1,0,0,0),
       (-1,0,0,0,0,0),(0,1,0,0,0,0),(0,0,-1,0,0,0))
    zero=(0,)*6
    cutoff={}
    for w in labels:
        mids=tuple(tuple(x+y for x,y in zip(a[k],a[(k+1)%6])) if w[k] else zero
                   for k in range(6))
        cells=tuple(v for k in range(6) for v in (a[k],mids[k]))
        assert all(sum(abs(x-y) for x,y in zip(v,cells[(k+1)%12]))==1 for k,v in enumerate(cells))
        cutoff[w]=len(set(cells))==12 and zero not in mids
    assert sum(cutoff.values())==1
    triads=tuple(combinations(range(6),3))
    atlas_edge_action=[tuple(ix(p[i],p[j]) for i,j in E) for p in S4]
    triad_orbits={
        frozenset(tuple(sorted(p[i] for i in t)) for p in atlas_edge_action) for t in triads}
    assert sorted(map(len,triad_orbits))==[4,4,12]
    orbits={min(word_orbit(w)) for w in labels}
    necklace={min(w[i:]+w[:i] for i in range(6)) for w in labels}
    assert (len(necklace),len(orbits))==(14,13)
    out={}
    for name,schedules in [('constant',[(0,)*6,(1,)*6]),
                           ('alternating',[(0,1,0,1,0,1),(1,0,1,0,1,0)])]:
        counts=[brc.CWM_ZERO for k in range(8)]
        for w in schedules:
            path=brc.cwm_edge(1)
            for _ in range(12):
                path=brc.cwm_propagate(path,brc.cwm_edge(1))
            for i,keep in enumerate([True,*w,cutoff[w]]):
                if keep:
                    counts[i]=brc.cwm_recoalesce(counts[i],path)
        assert all(s.count==s.total for s in counts)
        out[name]={'positive_scheduled_paths':counts[0].count,
                'outer_counts_by_edge':[s.count for s in counts[1:7]],
                'complete_nonzero_C12_count':counts[7].count}
    assert out['constant']['complete_nonzero_C12_count']==1 and out['alternating']['complete_nonzero_C12_count']==0
    return {'cyclic_word_orbits':len(necklace),'dihedral_word_orbits':len(orbits),
            'K4_subgroup_orbit_sizes_on_all_twenty_triads':sorted(map(len,triad_orbits)),
            'scope':'one marked triad, full ordered shortest path and declared nonzero C12 readout',
            'kernel_revision':'c0f816e2ab6be0145a3edd1a77488bddfd42a2f6',
            'kernel_sha256':sha,'models':out,'end_to_end_steps_per_path':12}

if __name__=='__main__':
    cli=argparse.ArgumentParser()
    cli.add_argument('--repo',type=Path,default=Path.cwd())
    repo=cli.parse_args().repo.resolve()
    print(json.dumps({'atlas':check_atlas(),'paths':branch_brc(repo)},indent=2,sort_keys=True))
