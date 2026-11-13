"""Exact obstruction to every order-five translation acting on a common-map eleven-color encoder. Stdlib."""
import argparse,json
from pathlib import Path
from itertools import product,combinations,permutations
from collections import Counter
P=list(product(range(5),repeat=3))
def elems(x):
    while x:
        b=x&-x;x-=b;yield b.bit_length()-1
def forbidden():
    edges=set()
    for d in (1,3):
        for p in P:
            groups={}
            for h,w in enumerate(P):
                active=tuple(k for k in range(3)if (w[k]-p[k])%5 in (0,d))
                key=tuple(w[k] for k in active);groups.setdefault(active,[]).append((h,key))
            for g in groups.values():
                for (a,u),(b,v),(c,w) in combinations(g,3):
                    if u!=v and v!=w and u!=w:edges.add((a,b,c))
    return edges
def enumerate_large(edges):
    N=125;full=(1<<N)-1;bad=[[0]*N for _ in P]
    for tri in edges:
        for a,b,c in permutations(tri):bad[a][b]|=1<<c
    anchored=set();nodes=0
    def dfs(ch,can,forb,size):
        nonlocal nodes
        if size+can.bit_count()<11:return
        nodes+=1
        remaining=can;level=0;order=[]
        while remaining:
            level+=1;cl=remaining
            while cl:
                low=cl&-cl;v=low.bit_length()-1;order.append((v,level));remaining^=low;cl&=remaining&forb[v]
        for v,lev in reversed(order):
            if size+lev<11:return
            bit=1<<v;can^=bit;d=can&~forb[v];c=ch|bit
            if size+1>=11:anchored.add(c)
            if size+1+d.bit_count()>=11:
                dfs(c,d,{w:forb[w]|bad[v][w] for w in elems(d)},size+1)
    dfs(1,full^1,bad[0],1)
    idx={p:i for i,p in enumerate(P)};shifts=[[1<<idx[tuple((x+y)%5 for x,y in zip(w,t))]for w in P]for t in P]
    seen=set();allsets=set()
    for s in sorted(anchored):
        if s in seen:continue
        pts=list(elems(s))
        for sh in shifts:
            t=sum(sh[i]for i in pts);allsets.add(t)
            if t&1:seen.add(t)
    return nodes,anchored,allsets
def direction(v):
    # simultaneous dilation by 2 exchanges the two writer pullback distance classes,
    # independently negating axes preserves undirected pairs; coordinates may be permuted.
    return min(tuple(k*x*s%5 for x,s in zip(w,ss))for k in (1,2,3,4) for ss in product((1,-1),repeat=3)for w in permutations(v)if any(k*x*s%5==1 for x,s in zip(w,ss)))
def check(v,sets,edges):
    ix={p:i for i,p in enumerate(P)};lines=[];rest=set(P)
    while rest:
        r=min(rest);L=[tuple((x+k*d)%5 for x,d in zip(r,v)) for k in range(5)];rest-=set(L);lines.append(tuple(ix[t]for t in L))
    good=lambda t:all(c not in edges for c in combinations(sorted(t),3))
    assert len(lines)==25 and all(good(t) for t in lines)
    pairs=[(i,j)for i,j in combinations(range(25),2)if good(lines[i]+lines[j])]
    ids={p:1<<i for i,l in enumerate(lines)for p in l}
    projections=set()
    for S in sets:
        z=0
        for j in elems(S):z|=ids[j]
        if z.bit_count()>=11:projections.add(z)
    high=max(x.bit_count()for x in projections);fixed=[0]+[1<<i for i in range(25)]+[1<<i|1<<j for i,j in pairs]
    checks=small=0;full=(1<<25)-1
    # Six fixed and one orbit: at least 12 lines must be covered by fixed sets.
    assert (not pairs) or high<=12
    # One fixed and two 5-cycles. At least one rotating class covers >=12 lines.
    for q in projections:
        if q.bit_count()<12:continue
        for f in fixed:
            missing=full^(q|f);k=missing.bit_count()
            if k>13:continue
            checks+=1
            if k<11:
                small+=1;assert not any(q2&missing==missing for q2 in projections)
                # Need also examine size-ten representatives if k<11. This branch
                # is never reached on these five quotient systems.
            else:
                assert missing not in projections # downward closure on projections of size >=11
    assert small==0
    return dict(direction=v,legal_line_pairs=len(pairs),large_projections=len(projections),maximum_lines_hit=high,eligible_fixed_plus_first_orbit=checks,remainder_below_eleven=small)
def run():
    edges=forbidden();nodes,anchor,sets=enumerate_large(edges)
    canonical=sorted({direction(v) for v in P if v!=(0,0,0)})
    reports=[check(v,sets,edges) for v in canonical];assert len(canonical)==5
    return dict(status='PASS',scope='translation symmetry acting by a permutation of all eleven used labels; unrestricted eleven remains separate',forbidden_triples=len(edges),anchored_search_nodes=nodes,anchored_by_size=dict(sorted(Counter(x.bit_count()for x in anchor).items())),all_by_size=dict(sorted(Counter(x.bit_count()for x in sets).items())),quotients=reports,translation_equivariant_eleven_possible=False)
if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--out',type=Path,default=Path(__file__).with_name('translation_results.json'));d=run();a.parse_args().out.write_text(json.dumps(d,indent=2)+'\n');print('PASS',d['all_by_size'])
