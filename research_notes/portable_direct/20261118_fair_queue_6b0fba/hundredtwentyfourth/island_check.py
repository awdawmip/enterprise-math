"""Finite islands for the king-move Gaussian norm sieve. Standard library only."""
import argparse
from collections import Counter
from hashlib import sha256
from math import comb, gcd, isqrt, prod
from pathlib import Path
import json
import re

R = 65
KING = tuple((i,j) for i in (-1,0,1) for j in (-1,0,1) if i or j)
ROOK = ((1,0),(-1,0),(0,1),(0,-1))
GOOD = {(x,y) for x in range(R) for y in range(R) if gcd(x*x+y*y,R)==1}
PERIODICITY_SHA = '1c3929027ce8db0174143c29134a8b38c812b9e27eed0d6d7af11d42acd408aa'


def residue(z):
    return z[0]%R,z[1]%R


def neighbors(z,moves):
    for i,j in moves:
        yield z[0]+i,z[1]+j


def single_cut(c):
    # New hole c plus the complete old four-neighbor hole components touching it.
    bad={c}; queue=[c]; partners=set()
    for z in queue:
        for w in neighbors(z,ROOK):
            if w in bad: continue
            if residue(w) in GOOD: partners.add(w)
            else:
                bad.add(w); queue.append(w)
    return bad,partners


def inside_components(bad,allowed):
    xmin=min(x for x,y in bad); xmax=max(x for x,y in bad)
    ymin=min(y for x,y in bad); ymax=max(y for x,y in bad)
    pool={(x,y) for x in range(xmin,xmax+1) for y in range(ymin,ymax+1) if allowed(x,y)}
    while pool:
        component=[pool.pop()]; outside=False
        for v in component:
            if v[0] in (xmin,xmax) or v[1] in (ymin,ymax): outside=True
            for w in neighbors(v,KING):
                if w in pool:
                    pool.remove(w); component.append(w)
        if not outside: yield frozenset(component)


def base_data():
    contacts={}; fringe={}
    for c in GOOD:
        bad,partners=single_cut(c)
        contacts[c]=[(x-c[0],y-c[1]) for x,y in sorted(partners)]
        fringe[c]=[(x-c[0],y-c[1]) for x,y in sorted(bad)]
    return contacts,fringe


def norm2(u,v):
    return (u[0]-v[0])**2+(u[1]-v[1])**2


def base_census(contacts,fringe):
    singles=Counter(); doubles=Counter(); degrees=Counter(); edge_boundary=Counter()
    pairs=max_one_span=max_two_span=0; two_steps=set(); patch_norms=set()
    def span(bad):
        return max(max(v[i] for v in bad)-min(v[i] for v in bad) for i in (0,1))
    directions=((1,0),(0,1),(1,1),(1,-1))
    for c in sorted(GOOD):
        adj={u for u in neighbors(c,KING) if residue(u) in GOOD}
        degrees[len(adj)]+=1
        for idx,e in enumerate(directions):
            other=c[0]+e[0],c[1]+e[1]
            if other not in adj: continue
            bd=adj|{z for z in neighbors(other,KING) if residue(z) in GOOD}
            edge_boundary[idx,len(bd-{c,other})]+=1
        bad=set(neighbors(c,fringe[c]))
        max_one_span=max(max_one_span,span(bad))
        for shape in inside_components(bad,lambda x,y:residue((x,y)) in GOOD and (x,y)!=c):
            singles[len(shape)]+=1
        for b in neighbors(c,contacts[c]):
            for w in neighbors(b,contacts[residue(b)]): two_steps.add(norm2(c,w))
            two_steps.add(norm2(c,b))
            if b<=c: continue
            pairs+=1
            both=bad|set(neighbors(b,fringe[residue(b)]))
            max_two_span=max(max_two_span,span(both))
            for shape in inside_components(both,lambda x,y:residue((x,y)) in GOOD and (x,y) not in (b,c)):
                bd={v for u in shape for v in neighbors(u,KING) if v not in shape and residue(v) in GOOD}
                assert bd=={b,c}
                doubles[len(shape)]+=1
                points=list(shape)+[b,c]
                patch_norms.update(norm2(u,v) for u in points for v in points)
    assert not singles and degrees=={2:96,3:704,4:1112,5:392}
    assert doubles=={1:96,2:74,3:48,4:12}
    assert patch_norms=={0,1,2,4,5,8,9,18}
    exceptional=[p for p in range(17,max(two_steps)+1,4)
                 if all(p%d for d in range(2,isqrt(p)+1)) and any(t and t%p==0 for t in two_steps)]
    return dict(vertices=len(GOOD),candidate_pairs=pairs,one_hole_span=max_one_span,two_hole_span=max_two_span,one_cut=dict(singles),two_cut=dict(doubles),
                degree=dict(degrees),all_edge_boundaries=[dict(sorted((b,n) for (j,b),n in edge_boundary.items() if j==i)) for i in range(4)],edge_boundary_two=[edge_boundary[i,2] for i in range(4)],
                patch_norms=sorted(patch_norms),two_step_nonzero_norms=sorted(two_steps-{0}),
                triple_possible_primes=exceptional)


def exceptional_census(p,contacts,fringe):
    mod=R*p
    b=next(i for i in range(1,p) if (i*i+1)%p==0)
    half=pow(2,-1,p); inverse=pow(2*b,-1,p); inv_base=pow(R,-1,p)
    seeds=set()
    for c,offsets in contacts.items():
        slopes=[((x+b*y)%p,(x-b*y)%p) for x,y in offsets]
        # A marked center lies on at least one line. Fix that line and count marked neighbors.
        for k in (0,1):
            fixed=sum(v[k]==0 for v in slopes)
            counts=Counter((-v[1-k])%p for v in slopes if v[k])
            free=range(p) if fixed>=2 else (r for r,num in counts.items() if fixed+num>=2)
            for r in free:
                left,right=(0,r) if k==0 else (r,0)
                a=half*(left+right)%p; d=inverse*(left-right)%p
                x=c[0]+R*((a-c[0])*inv_base%p)
                y=c[1]+R*((d-c[1])*inv_base%p)
                seeds.add((x,y))
    def dropped(x,y):
        return (x+b*y)%p==0 or (x-b*y)%p==0
    seed_count=len(seeds); max_sites=max_span=groups=0
    histogram=Counter(); anchors=set(); sample={}
    while seeds:
        c=seeds.pop()
        holes=[c]; reps={c:c}
        for u in holes:
            for z in neighbors(u,contacts[residue(u)]):
                if not dropped(*z): continue
                key=z[0]%mod,z[1]%mod
                if key in reps:
                    assert reps[key]==z, ('nonzero lifted displacement',p,key)
                else:
                    reps[key]=z; holes.append(z); seeds.discard(key)
        assert len(holes)>=3
        groups+=1; max_sites=max(max_sites,len(holes))
        bad={z for u in holes for z in neighbors(u,fringe[residue(u)])}
        for i in (0,1):
            values=[u[i] for u in bad]
            max_span=max(max_span,max(values)-min(values))
        for shape in inside_components(bad,lambda x,y:residue((x,y)) in GOOD and not dropped(x,y)):
            x,y=min(shape); key=(x%mod,y%mod)
            if key in anchors: continue
            bd={v for u in shape for v in neighbors(u,KING) if v not in shape and residue(v) in GOOD}
            if len(bd)<=2: continue
            assert all(dropped(*z) for z in bd)
            anchors.add(key); size=len(shape)
            histogram[size]+=1
            sample[size]=min(key,sample.get(size,key))
    return dict(p=p,eligible_centers=seed_count,groups_with_at_least_three=groups,
                largest_group=max_sites,largest_box_span=max_span,extra=dict(histogram),example_anchors=sample)


class Components:
    def __init__(self):
        self.parent=[]; self.weight=[]
    def allocate(self,length):
        i=len(self.parent); self.parent.append(i); self.weight.append(length); return i
    def root(self,i):
        while self.parent[i]!=i:
            self.parent[i]=self.parent[self.parent[i]]; i=self.parent[i]
        return i
    def merge(self,i,j):
        i,j=self.root(i),self.root(j)
        if i==j: return
        if self.weight[i]<self.weight[j]: i,j=j,i
        self.parent[j]=i; self.weight[i]+=self.weight[j]


def connect_layers(prev,now,d,dsu,wrap):
    """Two horizontal runs in adjacent rows meet if their interval distance is <=1."""
    i=0
    for l,r,t in now:
        while i<len(prev) and prev[i][1]<l-1: i+=1
        j=i
        while j<len(prev) and prev[j][0]<=r+1:
            dsu.merge(t,prev[j][2]); j+=1
    if wrap and prev and now:
        if prev[0][0]==0 and now[-1][1]==d-1: dsu.merge(prev[0][2],now[-1][2])
        if now[0][0]==0 and prev[-1][1]==d-1: dsu.merge(now[0][2],prev[-1][2])


def read_rectangle(primes,x0,x1,y0,y1,wrap,targets,strip_voltage=False):
    # Direct norm sieve with horizontal run unions. No hole-cluster calculation is used here.
    d=x1-x0+1
    patterns={}
    for p in primes:
        if p in (5,13): continue
        b=next(z for z in range(p) if z*z%p==p-1)
        patterns[p]=(b,{a:bytes((d-1-a)//p+1) for a in range(p) if a<d})
    base={r:bytearray((i%R,r) in GOOD for i in range(x0,x1+1)) for r in range(R)}
    dsu=Components(); tags={}; first=[]; prev=[]; seam={}
    for y in range(y0,y1+1):
        mask=bytearray(base[y%R])
        for p,(b,zeros) in patterns.items():
            for residue_x in {(b*y-x0)%p,(-b*y-x0)%p}:
                if residue_x<d: mask[residue_x::p]=zeros[residue_x]
        now=[]
        for run in re.finditer(b'\x01+',mask):
            l,r=run.span(); t=dsu.allocate(r-l); now.append((l,r-1,t))
        if strip_voltage:
            seam[y]=(now[0][2] if now and now[0][0]==0 else None,
                     now[-1][2] if now and now[-1][1]==d-1 else None)
        for x0t,y0t in targets:
            if y0t==y:
                tags[x0t,y0t]=next(t for l,r,t in now if l<=x0t-x0<=r)
        if wrap and now and now[0][0]==0 and now[-1][1]==d-1:
            dsu.merge(now[0][2],now[-1][2])
        if y==y0: first=now
        else: connect_layers(prev,now,d,dsu,wrap)
        prev=now
    if wrap: connect_layers(first,prev,d,dsu,True)
    if strip_voltage:
        assert not wrap and len(tags)==1
        # Collapse cut-rectangle components, then put the actual period label on each seam edge.
        adjacency={}
        for y,(_,right) in seam.items():
            if right is None: continue
            u=dsu.root(right)
            for j in (-1,0,1):
                left=seam.get(y+j,(None,None))[0]
                if left is None: continue
                v=dsu.root(left)
                adjacency.setdefault(u,[]).append((v,1))
                adjacency.setdefault(v,[]).append((u,-1))
        origin=dsu.root(next(iter(tags.values())))
        potential={origin:0}; todo=[origin]; winding=0
        for u in todo:
            for v,k in adjacency.get(u,[]):
                if v not in potential: potential[v]=potential[u]+k; todo.append(v)
                else: winding=gcd(winding,potential[u]+k-potential[v])
        return dict(cut_components_in_anchor_orbit=len(todo),winding_gcd=winding)
    if targets:
        return len({dsu.root(t) for t in tags.values()})==1 and len(tags)==len(targets)
    return Counter(w for i,w in enumerate(dsu.weight) if dsu.parent[i]==i)


def main(source):
    if source: assert sha256(source.read_bytes()).hexdigest()==PERIODICITY_SHA
    contacts,fringe=base_data()
    base=base_census(contacts,fringe)
    normal={n:2*c for n,c in base['two_cut'].items()}
    rows=[exceptional_census(p,contacts,fringe) for p in base['triple_possible_primes']]
    full={}
    for p in (17,29,37):
        Q=R*p
        hist=read_rectangle((5,13,p),0,Q-1,0,Q-1,True,())
        assert sum(n*c for n,c in hist.items())==2304*(p-1)**2
        large=max(hist); assert hist.pop(large)==1 and large>Q
        row=next(z for z in rows if z['p']==p)
        expected=Counter(normal)+Counter(row['extra'])
        assert hist==expected
        full[p]=dict(finite=dict(hist),unbounded_component_cells=large)
    primes=[k for k in range(17,8713,4) if all(k%d for d in range(2,isqrt(k)+1))]
    spans={z['p']:z['largest_box_span'] for z in rows}
    candidates=sum(1 for p in primes if p<=4*max(base['two_step_nonzero_norms'])
                   for q in primes if p<q<=8*(max(base['two_hole_span'],spans.get(p,0))+2)**2)
    p,q=17,29
    def coupon(size,b):
        return sum((-1)**i*comb(b,i)*prod(prime-size-i for prime in (p,q))**2 for i in range(b+1))
    singleton=sum(n*coupon(1,b) for b,n in base['degree'].items())
    domino=sum(n*coupon(2,b) for row in base['all_edge_boundaries'] for b,n in row.items())
    Q=R*p*q
    crossings={r:read_rectangle((5,13,p,q),-r,Q+r,-r,r,False,[(0,1),(Q,1)]) for r in (36,37)}
    assert crossings=={36:False,37:True}
    voltages={r:read_rectangle((5,13,p,q),0,Q-1,-r,r,False,[(0,1)],True) for r in (36,37)}
    assert [voltages[r]['winding_gcd'] for r in (36,37)]==[0,1]
    return dict(periodicity_tex_sha256=PERIODICITY_SHA,base=base,universal_pair_cut_histogram=normal,
                exceptional_rows=rows,independent_whole_tori=full,
                two_new_primes=dict(candidate_pairs_before_17_29_check=candidates,p=p,q=q,horizontal_period=Q,box_crossings=crossings,infinite_strip_voltage=voltages,isolated=singleton,dominoes=domino))


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--source',type=Path,help='optional fixed external periodicity.tex')
    args=parser.parse_args()
    print(json.dumps(main(args.source),indent=2,sort_keys=True))
