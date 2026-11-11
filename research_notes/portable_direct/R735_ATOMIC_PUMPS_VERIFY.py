#!/usr/bin/env python3
"""R735: exact positive BRC/CNB primitive return-monoid checks. Stdlib only.
Run: python3 R735_ATOMIC_PUMPS_VERIFY.py > R735_ATOMIC_PUMPS_RESULTS.json
Science pin: a72226e2430ffa4786321ac86e7f0c599d5f0389.
"""
import itertools
import json
from collections import defaultdict
from math import comb

ROOT = "012"
TRIADS = ["".join(t) for t in itertools.combinations("01234", 3)]
UNIVERSE = [(u, v) for u in TRIADS for v in TRIADS if len(set(u) & set(v)) == 2]
MASKS = {"A": 211733226574, "B": 5363347296468}
assert len(UNIVERSE) == 60

def frame(path):
    f = {c: str(i) for i, c in enumerate(ROOT)}
    for u, v in zip(path, path[1:]):
        old = next(c for c in u if c not in v)
        new = next(c for c in v if c not in u)
        f[new] = f.pop(old)
    return "".join(f[c] for c in path[-1])

def is_cnb(path, arcs):
    m = len(path)-1
    return m >= 3 and path[0] == path[-1] == ROOT and all(
        (u, v) in arcs for u, v in zip(path, path[1:])
    ) and all(path[(j-1)%m] != path[(j+1)%m] for j in range(m))

def counts(path, index):
    n = [0]*15
    for e in zip(path, path[1:]):
        n[index[e]] += 1
    y = [0]*12
    for i, x in enumerate(n):
        y[i//12] += x
        y[i%12] += x
    return tuple(n), tuple(y)

def word_path(loops, word):
    path = [ROOT]
    for i in word:
        path.extend(loops[i][1:])
    return path

def det3(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
           -m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
           +m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))

def analyze(name, mask):
    arcs = [e for i, e in enumerate(UNIVERSE) if mask >> i & 1]
    assert len(arcs) == 15
    index = {e: i for i, e in enumerate(arcs)}
    aset = set(arcs)
    root_out = {v for u, v in arcs if u == ROOT}
    root_in = {u for u, v in arcs if v == ROOT}
    assert not (root_in & root_out)
    loops = [p for u in sorted(root_out) for v in TRIADS
             if (u,v) in aset and (v,ROOT) in aset
             for p in [(ROOT,u,v,ROOT)] if is_cnb(p,aset)]
    assert len(loops) == 3
    labels = [frame(p) for p in loops]
    assert sorted(labels) == sorted(["012", "021", "102"] if name == "A" else ["012", "021", "210"])
    identity = labels.index("012")
    transpositions = [i for i in range(3) if i != identity]
    p, q = transpositions
    loop_counts = [counts(l,index)[0] for l in loops]
    private = []
    for i,vec in enumerate(loop_counts):
        uniq = [j for j,x in enumerate(vec) if x and all(loop_counts[t][j]==0 for t in range(3) if t!=i)]
        assert uniq
        private.append(uniq)
    loop_ledgers = [counts(l,index)[1] for l in loops]
    minor = next(({"row_indices":list(rows),
                   "matrix":[[loop_ledgers[col][row] for col in range(3)] for row in rows],
                   "determinant":det3([[loop_ledgers[col][row] for col in range(3)] for row in rows])}
                  for rows in itertools.combinations(range(12),3)
                  if det3([[loop_ledgers[col][row] for col in range(3)] for row in rows])), None)
    assert minor and minor["determinant"]
    exact_grades = []
    for k in range(1,9):
        fibers = defaultdict(set)
        for word in itertools.product(range(3), repeat=k):
            path = word_path(loops,word)
            assert is_cnb(path,aset)
            n,y = counts(path,index)
            key = tuple(word.count(i) for i in range(3))
            assert all(n[j] == key[i] for i,js in enumerate(private) for j in js)
            fibers[key].add(frame(path))
        triple = sum(len(s)==3 for s in fibers.values())
        predicted = comb(k-2,2) if k>=4 else 0
        assert triple == predicted, (name,k,triple,predicted)
        assert max(map(len,fibers.values())) == (1 if k==1 else 2 if k<=3 else 3)
        for key,hs in fibers.items():
            assert (len(hs)==3) == (key[p]>=2 and key[q]>=2)
        exact_grades.append({"three_step_loops":k,"history_length":3*k,
                             "words":3**k,"distinct_count_fibers":len(fibers),
                             "three_holonomy_fibers":triple,
                             "max_holonomies_in_fiber":max(map(len,fibers.values()))})
    r_examples=[]
    for r in range(1,5):
        hs=defaultdict(int)
        for choose_p in itertools.combinations(range(4*r),2*r):
            choice=set(choose_p)
            word=tuple(p if j in choice else q for j in range(4*r))
            hs[frame(word_path(loops,word))]+=1
        assert sum(hs.values()) == comb(4*r,2*r)
        assert len(hs)==3
        r_examples.append({"r":r,"history_length":12*r,
                           "common_ledger_history_count":comb(4*r,2*r),
                           "named_holonomy_counts":dict(sorted(hs.items()))})
    witness={}
    for word in itertools.product((p,q), repeat=4):
        if word.count(p)==word.count(q)==2:
            path=word_path(loops,word)
            witness.setdefault(frame(path), {"word":list(word),"path":path})
    assert len(witness)==3
    signatures={counts(d["path"],index) for d in witness.values()}
    assert len(signatures)==1
    n,y=next(iter(signatures))
    return {"arc_mask":mask,"root_in":sorted(root_in),"root_out":sorted(root_out),
            "primitive_loops":[{"id":i,"path":list(t),"holonomy":labels[i],
                                 "arc_support":list(j for j,x in enumerate(loop_counts[i]) if x),
                                 "private_arc_indices":private[i]} for i,t in enumerate(loops)],
            "identity_loop":identity,"transposition_loops":transpositions,
            "port_ledger_injective_minor":minor,
            "exact_grades":exact_grades,"fixed_fiber_examples":r_examples,
            "first_monoid_triple_witness":{"length":12,"arc_counts":n,"pooled_four_port":y,
                                           "paths":witness},
            "all_k_ge_4_triple_fibers_lower_bound":"C(k-2,2); in fact equality inside this 3-loop submonoid",
            "all_r_ge_1_fixed_fiber_history_lower_bound":"C(4r,2r) at length 12r"}

def main():
    result={"schema":"R735_BRC_PRIMITIVE_PUMP_MONOID_V1",
            "source_frozen":"a72226e2430ffa4786321ac86e7f0c599d5f0389",
            "source_frontier":"R734@368f50c86c77451822d6e6b649535d297abcff25",
            "carrier":"positive rooted cyclic nonbacktracking 15-arc/V17 loop history",
            "observer":"full directed arc counts and pooled 12-counter 4-port PASS readout",
            "systems":{name:analyze(name,mask) for name,mask in MASKS.items()},
            "status":"PASS"}
    print(json.dumps(result,indent=2,ensure_ascii=False))

if __name__ == "__main__":
    main()
