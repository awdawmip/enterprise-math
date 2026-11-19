#!/usr/bin/env python3
"""R762GL fixed named Port/Link incidence gate. Exact integer checker.
Requires only Python 3 standard library. Independent brute-force crosscheck.
"""
import itertools
import json
from collections import defaultdict
from math import comb

V = range(4)
EDGES = tuple(itertools.combinations(V, 2))
EDGEID = {e: i for i, e in enumerate(EDGES)}
STARS = tuple(tuple(EDGEID[tuple(sorted((v,w)))] for w in V if w!=v) for v in V)
ZERO = (0,)*6
IDENT = tuple(range(6))
K = ((0,1,2,3), (1,0,3,2), (2,3,0,1), (3,2,1,0))

def compose(p, q):
    return tuple(p[q[i]] for i in range(6))

def apply(p, x):
    out = [0]*6
    for i, v in enumerate(x):
        out[p[i]] = v
    return tuple(out)

def inverse(p):
    out = [0]*6
    for i, v in enumerate(p):
        out[v] = i
    return tuple(out)

def cycle(star):
    p = list(IDENT)
    a,b,c = star
    p[a],p[b],p[c] = b,c,a
    return tuple(p)

def event(v,s):
    x = tuple(s if i in STARS[v] else 0 for i in range(6))
    p = cycle(STARS[v])
    return (x,p if s==1 else inverse(p))

def mul(a,b):
    x,p = a
    y,q = b
    py = apply(p,y)
    return tuple(x[i]+py[i] for i in range(6)), compose(p,q)

def allowed(a,edge=(0,1)):
    return tuple(v for v in edge if v!=a)

def dp_counts(letters,M):
    states = {(ZERO,IDENT): 1}
    out = {}
    for m in range(M+1):
        nz = {x[0]: n for (x,p),n in states.items() if p==IDENT and len(set(x))==1}
        ret = sum(n for (x,p),n in states.items() if p==IDENT and len(set(x))==1 and x[0]==0)
        nonzero = sum(n for (x,p),n in states.items() if p==IDENT and len(set(x))==1 and x[0]!=0)
        out[m] = {"return_zero": ret, "return_nonzero": nonzero, "words": sum(states.values()), "state_count":len(states)}
        assert out[m]["words"] == len(letters)**m
        if m<M:
            nxt = defaultdict(int)
            for st,n in states.items():
                for letter in letters:
                    nxt[mul(st,letter)] += n
            states = dict(nxt)
    return out

def brute_count(letters,m):
    result = 0
    for word in itertools.product(letters,repeat=m):
        st = ZERO,IDENT
        for letter in word:
            st = mul(st,letter)
        result += int(st==(ZERO,IDENT))
    return result

def main():
    mark=(0,1)
    Ke = [q for q in K if tuple(sorted((q[0],q[1]))) == mark]
    assert Ke == [(0,1,2,3),(1,0,3,2)]
    tables = {}
    for omitted in V:
        star_vertices=allowed(omitted,mark)
        letters=tuple(event(v,s) for v in star_vertices for s in (-1,+1))
        table=dp_counts(letters,10)
        for m, data in table.items():
            assert data["return_nonzero"]==0
            if len(star_vertices)==1:
                assert data["return_zero"] == (comb(m,m//2) if m%2==0 else 0)
        assert table[2]["return_zero"] == 2*len(star_vertices)
        if omitted in (0,2):
            for m in (2,4,6,8):
                assert brute_count(letters,m)==table[m]["return_zero"]
        tables[str(omitted)] = {
            "remaining_vertices":list(star_vertices),
            "allowed_letters":len(letters),
            "zero_depth_returns_even_m":{str(m):table[m]["return_zero"] for m in (0,2,4,6,8,10)},
            "nonzero_depth_returns_all_m_0_to_10":sum(table[m]["return_nonzero"] for m in table),
            "state_count_m10":table[10]["state_count"]
        }
    assert tables["0"]["zero_depth_returns_even_m"] == tables["1"]["zero_depth_returns_even_m"]
    assert tables["2"]["zero_depth_returns_even_m"] == tables["3"]["zero_depth_returns_even_m"]
    assert tables["0"]["zero_depth_returns_even_m"]["2"] == 2
    assert tables["2"]["zero_depth_returns_even_m"]["2"] == 4
    result={
        "schema":"R762GL_NAMED_PORT_SYMMETRY_BREAK_CHECK_V1",
        "review":"NOT_REVIEWED",
        "status":"PASS",
        "model":"signed K4 STAR affine semidirect candidate, not native TRIADIC_CLOSURE_E license",
        "marked_edge":[0,1],
        "K_marked_edge_stabilizer":[list(q) for q in Ke],
        "finite_horizon_m":"0..10 exact DP, 2/4/6/8 independent full-word oracle",
        "omitted_STARs":tables
    }
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=="__main__":
    main()
