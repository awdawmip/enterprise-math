"""R284EW H=2 early-visible four-generation tag and recycle checks."""
from itertools import combinations


def popcount(x):
    return x.bit_count()


def build(u):
    if u == 0:
        # Four-vertex Gray cycle: each adjacent update is a single bit.
        c = (0b00, 0b01, 0b11, 0b10)
        edges = [(0,1,[0]),(1,2,[1]),(2,3,[0]),(3,0,[1])]
        return 2,c,edges
    A, B, C = u, 3*u+1, u+1
    def block(indices):
        return sum(1 << i for i in indices)
    aa=list(range(A));bb=list(range(A,A+B));cc=list(range(A+B,A+B+C))
    tags=(0,block(bb+cc),block(aa+cc),block(aa+bb))
    # Long B flips first, then alternate between the shorter changing block and B.
    long_schedule=lambda short,cap: bb[:cap] + [z for i in range(len(short)) for z in (short[i],bb[cap+i])]
    BC=long_schedule(cc,2*u)
    BA=long_schedule(aa,2*u+1)
    edges=[(0,1,BC),(1,2,BA),(2,3,BC),(3,0,BA)]
    return A+B+C,tags,edges


def case(u):
    n, tags, edges = build(u)
    want=5*u+2
    assert n==want
    edges_required={(0,1),(1,2),(2,3),(0,3)}
    pairs=[]
    for a,b in combinations(range(4),2):
        d=popcount(tags[a]^tags[b])
        req=4*u+1 if (a,b) in edges_required else 2*u+1
        assert d>=req,(u,a,b,d,req)
        pairs.append([a,b,d])
    masks=[sum(1<<i for i in coords)
           for r in range(u+1)
           for coords in combinations(range(n),r)]
    total=0
    for a,b,order in edges:
        assert len(order)==popcount(tags[a]^tags[b])
        assert len(set(order))==len(order)
        assert all((tags[a]^tags[b]) & (1<<j) for j in order)
        state=tags[a]
        seen=[]
        for j in range(len(order)+1):
            possible=set()
            for flipmask in masks:
                y=state^flipmask
                hits=[i for i,c in enumerate(tags) if popcount(y^c)<=u]
                assert len(hits)<=1,(u,a,b,j,y,hits)
                possible.add(hits[0] if hits else None)
                total+=1
            assert possible.issubset({a,b,None}),(u,a,b,j,possible)
            seen.append(possible)
            if j<len(order):
                state^=1<<order[j]
        assert state==tags[b]
        assert seen[0]=={a} and seen[-1]=={b}
        assert all(a not in later for i,p in enumerate(seen) if b in p for later in seen[i:]),(u,a,b,'rollback')
    return {"u":u,"tag_bits":n,"pair_distances":pairs,
            "readout_cases":total,"all_checks_passed":True}


def banks():
    checked=0
    for H in range(10):
        # At preparation of generation p, live reader-start generations
        # occupy the interval [p-1-H,p-1].
        for p in range(1,101):
            live=range(max(0,p-1-H),p)
            assert all(p%(H+2)!=g%(H+2) for g in live)
            checked+=1
        # H+1 banks collide with generation 0 at preparation H+1.
        p=H+1
        assert p%(H+1)==0 and 0 in range(max(0,p-1-H),p)
    return {"H_values":"0..9","round_robin_checks":checked,"lower_bound_witnesses":10}


if __name__=='__main__':
    import json
    print(json.dumps({"four_generation_tags":[case(u) for u in range(4)],
                      "bank_recycle":banks()},indent=2,ensure_ascii=False))
