"""Rebuild the Q and standard normal cones with regina==7.4.1."""
from collections import Counter
from importlib.metadata import version
from itertools import product
from math import gcd, prod
import json

import regina as R

CASES = {
    "S3": "bkaagj", "Bing-S3": "cMcabbgdv", "L(3,1)": "cMcabbjak",
    "L(5,2)": "bkaajn", "L(8,3)": "cMcabbjqs", "S2xS1": "cMcabbjaj",
    "Poincare": "fvPQcdecedekrsnrs",
    "Weeks-A": "jLvAMPQadfgghhiiijaqgjqxims",
    "Weeks-B": "jLvAzQQcfeghighiiuquanobwwr",
    "Figure8(5,1)": "jLLvQPQcdfhghigiihshhgfifme",
    "T12": "mLLzwALQQcdcehijlklkklhsnqtadfswbnn",
}


def coordinates(s, n):
    q = [s.quads(i, j).longValue() for i in range(n) for j in range(3)]
    t = [s.triangles(i, j).longValue() for i in range(n) for j in range(4)]
    return q, t


def choices(q):
    return [tuple(j for j in range(3) if q[i+j]) or (0, 1, 2)
            for i in range(0, len(q), 3)]


def cone_survey(t):
    n = t.size()
    counts = {}
    valid = {}
    for mode, coord in (("Q", R.NS_QUAD), ("standard", R.NS_STANDARD)):
        accepted = set()
        surfaces = R.NormalSurfaces(t, coord)
        for s in surfaces:
            q, tr = coordinates(s, n)
            if not any(q):
                assert s.isVertexLinking()
                continue
            chi = s.eulerChar().longValue()
            if mode == "Q":
                assert gcd(*q) == 1 and min(tr) == 0 and s.isConnected()
                support = [a for a, x in enumerate(tr) if chi - 2*x > 0]
            else:
                support = [a for a, x in enumerate(tr) if x == 0 and chi > 0]
            if not support:
                continue
            assert all(x in (0, 1, 2) for block in choices(q) for x in block)
            for leaf in product(*choices(q)):
                accepted.update((leaf, a) for a in support)
        counts[mode] = surfaces.size()
        valid[mode] = accepted
    assert valid["Q"] == valid["standard"]
    return {"rays": counts, "leaf_repair_pairs": (3**n)*4*n,
            "positive_pairs": len(valid["Q"]),
            "positive_leaves": len({x for x, _ in valid["Q"]})}


def matrix_entries(matrix):
    return [[matrix.entry(i,j).longValue() for j in range(matrix.columns())]
            for i in range(matrix.rows())]


def witness(t):
    n = t.size()
    surfaces = [s for s in R.NormalSurfaces(t, R.NS_QUAD)
                if s.eulerChar().longValue() == -4]
    assert len(surfaces) == 1
    s = surfaces[0]
    q, tr = coordinates(s, n)
    assert gcd(*q) == 1 and min(tr) == 0
    assert s.isConnected() and s.isOrientable()
    B = matrix_entries(R.makeMatchingEquations(t, R.NS_QUAD))
    assert all(sum(a*b for a,b in zip(row,q)) == 0 for row in B)
    leaf = tuple(block[0] for block in choices(q))
    restrict = [[row[3*i+j] for i,j in enumerate(leaf)] for row in B]
    v = [q[3*i+j] for i,j in enumerate(leaf)]
    full = matrix_entries(R.makeMatchingEquations(t, R.NS_STANDARD))
    def full_lift(tau):
        return [x for i in range(n) for x in
                [*(tr[4*i+j]-tr[tau] for j in range(4)), *q[3*i:3*i+3]]]
    marked = []
    for tau in range(4*n):
        x = full_lift(tau)
        assert x[7*(tau//4)+tau%4] == 0
        assert all(sum(a*b for a,b in zip(row,x))==0 for row in full)
        marked.append(-4-2*tr[tau])
    smith = R.MatrixInt(restrict)
    R.smithNormalForm(smith)
    diag = [smith.entry(i,i).longValue() for i in range(n)]
    assert diag == [1]*(n-1)+[0]
    g = [abs(z) for z in marked]
    assert all(x>2 for x in g)
    odd_survive = [a for a,x in enumerate(g) if all(x%p for p in (3,5,7))]
    pure_two = [a for a,x in enumerate(g) if x & (x-1)==0]
    assert odd_survive == pure_two
    def dead(m):
        return all(2 % gcd(m,z) != 0 for z in g)
    assert all(dead(m) == (m%60 == 0) for m in range(1, 1001))
    assert all(sum((a*b) for a,b in zip(row,v))==0 for row in restrict)
    counts = Counter()
    for ext in product(*choices(q)):
        J = [3*i+j for i,j in enumerate(ext)]
        cm = R.MatrixInt([[r[j] for j in J] for r in B])
        counts[n-cm.rank()] += 1
    return {"isoSig":t.isoSig(),"leaf":list(leaf),"quad_generator_in_leaf":v,
            "triangles_canonical":tr,"chi":-4,"connected":True,"orientable":True,
            "q_smith_diagonal":diag,"signed_repair_images":marked,
            "generators_histogram":dict(sorted(Counter(g).items())),
            "surviving_repairs_at_all_odd_primes":pure_two,
            "least_single_modulus_killing_whole_leaf":60,
            "tested_single_moduli":1000,"differing_extensions_by_nullity":dict(sorted(counts.items()))}


def main():
    rows = {}
    for name,sig in CASES.items():
        tri=R.Triangulation3.fromIsoSig(sig)
        assert tri.isValid() and tri.isClosed() and tri.isOrientable() and tri.countVertices()==1
        row=cone_survey(tri)
        rows[name]={"isoSig":sig,"tetrahedra":tri.size(),**row}
    out={"regina_package":version("regina"),"cases":rows,
         "pair_total":sum(z["leaf_repair_pairs"] for z in rows.values()),
         "positive_pair_total":sum(z["positive_pairs"] for z in rows.values()),
         "witness":witness(R.Triangulation3.fromIsoSig(CASES["T12"]))}
    print(json.dumps(out,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
