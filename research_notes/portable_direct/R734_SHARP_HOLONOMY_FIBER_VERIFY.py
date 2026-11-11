#!/usr/bin/env python3
"""R734: sharp rooted-CNB count-fiber threshold. Stdlib exact arithmetic.
Run: python3 R734_SHARP_HOLONOMY_FIBER_VERIFY.py > R734_SHARP_HOLONOMY_FIBER_RESULTS.json
"""
import itertools
import json
from collections import defaultdict

TRIADS = ["".join(t) for t in itertools.combinations("01234", 3)]
UNIVERSE = [(u, v) for u in TRIADS for v in TRIADS if len(set(u) & set(v)) == 2]
assert len(UNIVERSE) == 60
MASKS = {"A": 211733226574, "B": 5363347296468}
ROOT = "012"

def edge_frame(u, v):
    f = {c: str(i) for i, c in enumerate(u)}
    leave = next(c for c in u if c not in v)
    enter = next(c for c in v if c not in u)
    f[enter] = f.pop(leave)
    return "".join(f[c] for c in v)

def parity(p):
    return sum(p[i] > p[j] for i in range(3) for j in range(i+1, 3)) % 2

def holonomy(path):
    f = {c: str(i) for i, c in enumerate(ROOT)}
    for u, v in zip(path, path[1:]):
        leave = next(c for c in u if c not in v)
        enter = next(c for c in v if c not in u)
        f[enter] = f.pop(leave)
    return "".join(f[c] for c in path[-1])

def is_cnb(path, arcs):
    m = len(path)-1
    if m < 3 or path[0] != ROOT or path[-1] != ROOT:
        return False
    if any((u,v) not in arcs for u,v in zip(path,path[1:])):
        return False
    return all(path[(j-1)%m] != path[(j+1)%m] for j in range(m))

def enumerate_rooted(arcs, max_m):
    out = defaultdict(list)
    for u,v in arcs:
        out[u].append(v)
    for x in out.values():
        x.sort()
    frontier = [[ROOT]]
    for m in range(1,max_m+1):
        nxt = []
        for p in frontier:
            for v in out.get(p[-1],()):
                if len(p)>1 and v == p[-2]:
                    continue
                nxt.append(p+[v])
        frontier = nxt
        yield m,[p for p in frontier if is_cnb(p,arcs)]

def counts(path,index):
    n=[0]*15
    y=[0]*12
    for u,v in zip(path,path[1:]):
        i=index[(u,v)]
        n[i]+=1
        y[i//12]+=1
        y[i%12]+=1
    return tuple(n),tuple(y)

def glue(a,b):
    assert a[0]==a[-1]==b[0]==b[-1]==ROOT
    return a+b[1:]

def verify(name,mask):
    arcs=[e for i,e in enumerate(UNIVERSE) if mask>>i&1]
    assert len(arcs)==15
    valid=set(arcs)
    ix={e:i for i,e in enumerate(arcs)}
    edge_signs=[parity(edge_frame(*e)) for e in arcs]
    bins=dict(enumerate_rooted(valid,11))
    expected={1:0,2:0,3:1,4:1,5:1,6:2,7:2,8:2,9:3,10:3,11:3}
    grades=[]
    seeds={}
    for m in range(1,12):
        bn=defaultdict(lambda:defaultdict(list))
        by=defaultdict(lambda:defaultdict(list))
        for p in bins[m]:
            n,y=counts(p,ix)
            h=holonomy(p)
            assert parity(h)==sum(a*b for a,b in zip(n,edge_signs))%2
            bn[n][h].append(p)
            by[y][h].append(p)
        kn=max((len(s) for s in bn.values()),default=0)
        ky=max((len(s) for s in by.values()),default=0)
        assert kn==ky==expected[m],(name,m,kn,ky)
        grades.append({"m":m,"rooted_cnb_histories":len(bins[m]),
                      "arc_count_fibers":len(bn),
                      "four_port_ledger_fibers":len(by),
                      "max_named_holonomies_per_fiber":kn,
                      "three_holonomy_fibers":sum(len(s)==3 for s in bn.values())})
        if m in (9,10,11):
            winners=[(n,g) for n,g in bn.items() if len(g)==3]
            assert winners
            n,g=min(winners,key=lambda x:x[0])
            paths={h:min((list(p) for p in group)) for h,group in g.items()}
            assert len(paths)==3
            y=counts(next(iter(paths.values())),ix)[1]
            for h,p in paths.items():
                assert is_cnb(p,valid) and holonomy(p)==h
                assert counts(p,ix)==(n,y)
            seeds[str(m)]={"common_arc_counts":list(n),
                           "common_four_port_ledger":list(y),
                           "paths":dict(sorted(paths.items()))}
    pump=(["012","014","013","012"] if name=="A" else
          ["012","123","124","012"])
    assert is_cnb(pump,valid)
    outgoing={v for u,v in arcs if u==ROOT}
    incoming={u for u,v in arcs if v==ROOT}
    assert pump[-2] not in outgoing
    assert pump[1] not in incoming
    assert pump[-2]!=pump[1]
    np,yp=counts(pump,ix)
    for m in (9,10,11):
        lifted=[glue(pump,p) for p in seeds[str(m)]["paths"].values()]
        assert all(is_cnb(p,valid) for p in lifted)
        assert len({holonomy(p) for p in lifted})==3
        assert len({counts(p,ix)[0] for p in lifted})==1
        assert len({counts(p,ix)[1] for p in lifted})==1
        assert counts(lifted[0],ix)[0]==tuple(
            a+b for a,b in zip(np,seeds[str(m)]["common_arc_counts"]))
    return {"arc_mask":mask,"num_arcs":15,
            "positive_rooted_CNB_exhaustive_to_length":11,
            "finite_exact_grades":grades,"base_witnesses":seeds,
            "universal_three_step_pump":{"path":pump,"holonomy":holonomy(pump),
                 "arc_counts":list(np),"four_port_ledger":list(yp),
                 "root_outgoing":sorted(outgoing),
                 "root_incoming":sorted(incoming)},
            "all_length_max_fiber_theorem":
                 "m=1,2:0; m=3..5:1; m=6..8:2; every m>=9:3"}

def main():
    result={"schema":"R734_SHARP_THREE_STATE_FIBER_THRESHOLD_V1",
            "source_science_pin":"a72226e2430ffa4786321ac86e7f0c599d5f0389",
            "model":"two positive V17 15-arc carriers, CNB root 012",
            "arithmetic":"exact integer/finite set; all-length bound plus 3-step induction",
            "carriers":{}}
    for name,mask in MASKS.items():
        result["carriers"][name]=verify(name,mask)
    result["status"]="PASS"
    print(json.dumps(result,indent=2,ensure_ascii=False))

if __name__=="__main__":
    main()
