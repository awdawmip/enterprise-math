#!/usr/bin/env python3
"""R740 exact BRC coordinate-path census, standard-library integer arithmetic.

Each history is a distinct positive-counted source branch. Signed edge current
is its declared native-coordinate observer, not positive BRC branch mass and
not an assertion about the physical V39 current.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations, product
from pathlib import Path
import json

AXES = (0, 1, 2)
PATTERNS = sorted(set(permutations((0, 0, 1, 1, 2, 2))))

def word(pattern, first_signs, axes=AXES):
    seen = {i: 0 for i in axes}
    out = []
    for i in pattern:
        out.append((i, first_signs[axes.index(i)] * (-1 if seen[i] else 1)))
        seen[i] += 1
    assert all(n == 2 for n in seen.values())
    return tuple(out)

def nb(w):
    return all(w[t] != (w[t-1][0], -w[t-1][1]) for t in range(1,len(w)))

def feature(w, axes=AXES):
    axes = tuple(sorted(axes))
    x = {i: 0 for i in axes}
    q = {}
    first = []
    J = {p: 0 for p in combinations(axes, 2)}
    flow = Counter()
    for i, sign in w:
        if i not in q:
            q[i] = sign
            first.append(i)
        for a, b in J:
            if i == b:
                J[a,b] += x[a]*sign
        y = x.copy()
        y[i] += sign
        lower = x if sign == 1 else y
        flow[(tuple(lower[a] for a in axes), i)] += sign
        x = y
    assert all(v == 0 for v in x.values())
    eps = (-1)**sum(first[i] > first[j] for i in range(3) for j in range(i+1,3))
    return (tuple(q[i] for i in axes),
            tuple(J[p] for p in combinations(axes,2)),
            eps, tuple(sorted((e,n) for e,n in flow.items() if n)))

def area(flow, axes=AXES):
    axes = tuple(sorted(axes))
    return tuple(sum(base[axes.index(a)]*n for (base,i),n in flow if i==b)
                 for a,b in combinations(axes,2))

def divergence_zero(flow, axes=AXES):
    axes = tuple(sorted(axes))
    div = Counter()
    for (base,i),n in flow:
        p = tuple(base)
        t = list(base)
        t[axes.index(i)] += 1
        div[p] += n
        div[tuple(t)] -= n
    return all(v==0 for v in div.values())

def support_type(flow, axes=AXES):
    axes = tuple(sorted(axes))
    if not flow:
        return "zero"
    if len(flow)==6:
        return "six-edge"
    assert len(flow)==4
    vertices = set()
    for (base,i),n in flow:
        assert abs(n)==1
        t=list(base)
        t[axes.index(i)]+=1
        vertices.update((tuple(base),tuple(t)))
    return "four-edge-rooted" if (0,0,0) in vertices else "four-edge-offset"

def printable(w):
    return " ".join(str(i)+("+" if s>0 else "-") for i,s in w)

def main():
    assert len(PATTERNS)==90
    words = [word(p,q) for q in product((-1,1),repeat=3) for p in PATTERNS]
    assert len(words)==720 and len(set(words))==720
    flows, nbflows, qj, qje = defaultdict(list),defaultdict(list),defaultdict(list),defaultdict(list)
    types = Counter()
    nbtypes = Counter()
    for w in words:
        q,J,e,j = feature(w)
        assert area(j)==J and divergence_zero(j)
        flows[j].append(w)
        types[support_type(j)] += 1
        if nb(w):
            nbflows[j].append(w)
            nbtypes[support_type(j)] += 1
            qj[(q,J)].append(w)
            qje[(q,J,e)].append(w)
    sizes = Counter(map(len,flows.values()))
    assert sizes=={1:240,10:24,240:1}
    assert len(flows)==265
    assert types=={"zero":240,"four-edge-rooted":240,"four-edge-offset":48,"six-edge":192}
    assert len(nbflows)==240 and all(len(z)==1 for z in nbflows.values())
    assert nbtypes=={"four-edge-offset":48,"six-edge":192}
    assert len(qj)==192 and Counter(map(len,qj.values()))=={1:144,2:48}
    assert len(qje)==240 and all(len(z)==1 for z in qje.values())

    # Complete NB census in all 20 three-axis native X6 coordinate slices.
    for axes in combinations(range(6),3):
        currents=set()
        for w in words:
            if not nb(w):
                continue
            mapped=tuple((axes[i],s) for i,s in w)
            f=feature(mapped,axes)
            assert area(f[3],axes)==f[1]
            assert f[3] not in currents
            currents.add(f[3])
        assert len(currents)==240

    # Five adjacent transpositions generate S6; verify 20*720*5 transports.
    gens=[tuple(i+1 if i==k else i-1 if i==k+1 else i for i in range(6))
          for k in range(5)]
    checks=0
    for axes in combinations(range(6),3):
        for w in words:
            w0=tuple((axes[i],s) for i,s in w)
            before=feature(w0,axes)[3]
            for g in gens:
                dst=tuple(sorted(g[i] for i in axes))
                shifted=Counter()
                for (base,a),n in before:
                    pos={g[axes[k]]:base[k] for k in range(3)}
                    shifted[(tuple(pos[k] for k in dst),g[a])] += n
                mapped=tuple(sorted((e,n) for e,n in shifted.items() if n))
                after=feature(tuple((g[i],s) for i,s in w0),dst)[3]
                assert mapped==after
                checks+=1
    assert checks==72000

    w=((0,1),(1,1),(2,1),(0,-1),(2,-1),(1,-1))
    v=((0,1),(2,1),(1,1),(0,-1),(1,-1),(2,-1))
    fq,fJ,fe,fj=feature(w)
    vq,vJ,ve,vj=feature(v)
    assert fq==vq==(1,1,1) and fJ==vJ==(1,1,0)
    assert fe!=ve and fj!=vj and nb(w) and nb(v)
    def serialized_flow(j):
        return [{"lower_vertex":list(base),"axis":i,"signed_flow":n}
                for (base,i),n in j]
    record={
        "schema":"R740_X6_ORIENTED_EDGE_FLOW_BRC_EXACT_V1",
        "scientific_pin":"a72226e2430ffa4786321ac86e7f0c599d5f0389",
        "scope":"one 3-axis native X6 slice, length six, each signed axis once; reembedded in all 20 triples",
        "BRC_branch_count":len(words),
        "current_distinct":len(flows),
        "current_fiber_sizes":{str(k):v for k,v in sorted(sizes.items())},
        "support_type_histories":dict(sorted(types.items())),
        "NB":len(nbflows),
        "NB_flow_classes":len(nbflows),
        "NB_support_type_histories":dict(sorted(nbtypes.items())),
        "NB_QJ_classes":len(qj),
        "NB_QJe_classes":len(qje),
        "axis_triples":20,
        "S6_generator_covariance_checks":checks,
        "area_projection_all_paths":True,
        "divergence_zero_all_paths":True,
        "witness":{"path_a":printable(w),"path_b":printable(v),
                   "shared_Q":list(fq),"shared_J":list(fJ),
                   "opposite_orientation":[fe,ve],
                   "edge_current_a":serialized_flow(fj),
                   "edge_current_b":serialized_flow(vj)},
        "V39_native_current_correspondence":"NOT_ESTABLISHED",
        "native_task_claim":"NOT_OBTAINED_SESSION_ISSUANCE_QUOTA",
        "formal_result":"NOT_FROZEN",
        "validation":"R740_X6_EDGE_CURRENT_BRC_EXACT_PASS"
    }
    out=Path(__file__).with_name("R740_X6_EDGE_CURRENT_RESULTS.json")
    out.write_text(json.dumps(record,ensure_ascii=False,indent=2,sort_keys=True)+"\n",
                   encoding="utf-8")
    print(record["validation"])
    print("path_count",len(words),"flow_classes",len(flows),
          "fiber_sizes",dict(sorted(sizes.items())))
    print("NB",len(nbflows),"S6_checks",checks)

if __name__=="__main__":
    main()
