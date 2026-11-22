"""Exact Q-arithmetic reproducer for R114 wall-loss classification.

Upstream input: X6 R90 complete twelve-direction catalog and weight-region
facet atlas (2026-11-22). All six pair observers are retained.
No external dependencies. Run: python x6_r114_facet_jump_verify.py
"""
from fractions import Fraction as Q
from itertools import combinations
from collections import Counter
from json import dump
from pathlib import Path

# Facet inequalities a0+a1*s+a2*X+a3*Y>=0, in published R90 order.
FACETS = {
    "I": [
        ("s",[0,1,0,0]),("1-2s",[1,-2,0,0]),
        ("9-2X",[9,0,-2,0]),("18-Y",[18,0,0,-1]),
        ("X-2",[-2,0,1,0]),("6X-Y",[0,0,6,-1]),
        ("3Y-34",[-34,0,0,3]),("9Y-34X",[0,0,-34,9]),
        ("3X-6s-5",[-5,-6,3,0]),("9+9X-2Y-18s",[9,-18,9,-2]),
        ("Y-2s-11",[-11,-2,0,1]),("1-2s-4X+Y",[1,-2,-4,1]),
        ("3X+3Y-6s-40",[-40,-6,3,3]),
    ],
    "II": [
        ("s",[0,1,0,0]),("1-2s",[1,-2,0,0]),
        ("9-X",[9,0,-1,0]),("9-Y",[9,0,0,-1]),
        ("X-2s-5",[-5,-2,1,0]),("1-2s+X-Y",[1,-2,1,-1]),
        ("3Y-6s-11",[-11,-6,0,3]),("9-18s-7X+9Y",[9,-18,-7,9]),
        ("3X-16",[-16,0,3,0]),("9X-8Y",[0,0,9,-8]),
        ("Y-4",[-4,0,0,1]),("3Y-2X",[0,0,-2,3]),
        ("3X+3Y-6s-28",[-28,-6,3,3]),
    ],
}
TEMPLATES = {
    "I": [(0,0,2),(0,1,-1),(0,1,1)] +
         [(1,m,n) for m in (-1,1) for n in (-3,-1,1)] +
         [(1,0,n) for n in (-2,0,2)],
    "II": [(0,1,-1),(0,1,1),(0,2,0)] +
          [(1,m,0) for m in (-2,0,2)] +
          [(1,m,n) for m in (-1,1,3) for n in (-1,1)],
}

def val(a, p):
    return Q(a[0])+sum(Q(c)*x for c,x in zip(a[1:],p))

def solve3(rows):
    A=[[Q(r[j+1]) for j in range(3)]+[-Q(r[0])] for r in rows]
    for c in range(3):
        k=next((i for i in range(c,3) if A[i][c]),None)
        if k is None: return None
        A[c],A[k]=A[k],A[c]
        d=A[c][c];A[c]=[x/d for x in A[c]]
        for j in range(3):
            if j!=c:
                factor=A[j][c]
                A[j]=[u-factor*v for u,v in zip(A[j],A[c])]
    return tuple(A[i][3] for i in range(3))

def vertices(facets):
    out=set()
    for tri in combinations(facets,3):
        p=solve3([f[1] for f in tri])
        if p is not None and all(val(a,p)>=0 for _,a in facets):
            out.add(p)
    return sorted(out)

def weights(typ,p):
    s,X,Y=p
    return (s,1-s,X-s,Y-s) if typ=="I" else (1-s,s,X-s,Y-s)

def T(p):
    _,X,Y=p
    return max(Q(1),X/6,Y/12,min(X/3,Y/6))

def Ttype(typ,p):
    _,X,Y=p
    return max(Q(1),X/3,Y/12) if typ=="I" else max(Q(1),X/6,Y/6)

def score(tmn,w):
    t,m,n=tmn
    h=(0,t,3*m,t+6*n)
    return max(Q(abs(h[i]-h[j]))/(w[i]+w[j])
               for i,j in combinations(range(4),2))

def port(tmn):
    t,m,n=tmn
    assert (m-n)%2==0
    v=(10*t-12*m+3*n,-5*t+7*m-2*n,t+(n-3*m)//2)
    return max(sum(max(x,0) for x in v),sum(max(-x,0) for x in v))

def fmt(x):
    return str(x)

def count(typ,p):
    w=weights(typ,p)
    assert min(w)>0
    return sum(score(t,w)*T(p)<Q(3,2) for t in TEMPLATES[typ])

def main():
    result={"schema":"X6_R114_FACE_STRATA_Q_CERTIFICATE_V1",
            "scope":"six-pair conditional BRC, strict cutoff, integer Port p>=196",
            "types":{}}
    for typ,facets in FACETS.items():
        vert=vertices(facets)
        assert len(vert)==15
        assert len(TEMPLATES[typ])==12
        assert max(map(port,TEMPLATES[typ]))<=196
        walls=[]
        for k,(name,a) in enumerate(facets,1):
            face=[v for v in vert if val(a,v)==0]
            assert len(face)>=3
            mid=tuple(sum(v[j] for v in face)/len(face) for j in range(3))
            assert sum(val(b,mid)==0 for _,b in facets)==1
            w=weights(typ,mid)
            assert min(w)>0 or k==1
            assert T(mid)==Ttype(typ,mid)
            ratios=[score(t,w)*T(mid) for t in TEMPLATES[typ]]
            survivor=sum(r<Q(3,2) for r in ratios)
            equality=sum(r==Q(3,2) for r in ratios)
            assert not any(r>Q(3,2) for r in ratios)
            assert survivor+equality==12
            assert equality>0 or k==1
            walls.append({"number":k,"plane":name,"positive":k!=1,
                          "midpoint_sXY":[fmt(x) for x in mid],
                          "survivors":survivor,"cutoff_equal":equality,
                          "equal_templates":[list(t) for t,r in zip(TEMPLATES[typ],ratios)
                                             if r==Q(3,2)]})
        losses=sorted(w["cutoff_equal"] for w in walls if w["positive"])
        assert losses==[1,2,2,2,2,2,3,3,8,8,9,9]
        edges=[]
        for a,b in combinations(vert,2):
            common=[i+1 for i,(_,f) in enumerate(facets)
                    if val(f,a)==0 and val(f,b)==0]
            if len(common)<2:continue
            mid=tuple((x+y)/2 for x,y in zip(a,b))
            if min(weights(typ,mid))<=0: continue
            edges.append({"facets":common,"midpoint_sXY":[fmt(x) for x in mid],
                          "survivors":count(typ,mid)})
        positive_vertices=[{"sXY":[fmt(x) for x in v],"survivors":count(typ,v)}
                           for v in vert if min(weights(typ,v))>0]
        assert len(edges)==20 and len(positive_vertices)==9
        edge_hist=dict(sorted(Counter(z["survivors"] for z in edges).items()))
        vertex_hist=dict(sorted(Counter(z["survivors"] for z in positive_vertices).items()))
        assert edge_hist=={3:4,4:4,8:3,9:1,10:8}
        assert vertex_hist=={3:2,4:2,8:2,10:3}
        result["types"][typ]={"polytope_vertices":15,"polytope_edges":26,
            "positive_facets":12,"positive_edges":20,"positive_vertices":9,
            "wall_losses":losses,"walls":walls,
            "edge_histogram":edge_hist,"vertex_histogram":vertex_hist,
            "edges":edges,"vertices":positive_vertices}
    with Path(__file__).with_name("x6_r114_facet_jump_results.json").open("w") as f:
        dump(result,f,indent=2,ensure_ascii=False)
    print("PASS: both types; 12 positive facets / 20 positive edges / 9 positive vertices.")
    print("Walls losses each: [1,2,2,2,2,2,3,3,8,8,9,9]")
    print("Edges survivors each: {3:4,4:4,8:3,9:1,10:8}")
    print("Vertices survivors each: {3:2,4:2,8:2,10:3}")

if __name__=="__main__":
    main()
