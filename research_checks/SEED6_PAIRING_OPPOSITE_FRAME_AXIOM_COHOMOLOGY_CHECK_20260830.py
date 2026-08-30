#!/usr/bin/env python3
"""Exact checker for RS-SEED6-PAIRING-OPPOSITE-FRAME-AXIOM-COHOMOLOGY.

This checker is intentionally task-local.  It verifies the finite-cell/cochain
claims used in the research return:
  * the support-typed resonance CW complex over F2;
  * flat C2 connection, gauge, and H^1 counts;
  * the carrier-height cocycle and its resonance periods;
  * an explicit operator/height independence witness;
  * the S4 -> S3 quotient / V4 lift boundary.

No floating point arithmetic is used.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, permutations, product
from math import comb, gcd

CHECKS = 0

def check(cond: bool, msg: str = "") -> None:
    global CHECKS
    CHECKS += 1
    if not cond:
        raise AssertionError(msg or f"check {CHECKS} failed")

def gf2_rank(rows: list[int]) -> int:
    """Rank of bit-packed row vectors over F2."""
    basis: dict[int, int] = {}
    rank = 0
    for x0 in rows:
        x = x0
        while x:
            p = x.bit_length() - 1
            if p in basis:
                x ^= basis[p]
            else:
                basis[p] = x
                rank += 1
                break
    return rank

def parity(x: int) -> int:
    return x.bit_count() & 1

class DSU:
    def __init__(self, n: int):
        self.p = list(range(n))
    def find(self, x: int) -> int:
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x
    def union(self, a: int, b: int) -> bool:
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        self.p[b] = a
        return True

@dataclass(frozen=True)
class ComplexData:
    a: int
    b: int
    R: tuple[int, ...]
    A: int
    B: int
    pinches: tuple[tuple[int, int, int], ...]  # (At, Bt, t)
    vertices: tuple[tuple[str, int], ...]      # pre-quotient typed vertices
    qindex: tuple[int, ...]                    # pre-vertex -> quotient vertex
    edges: tuple[tuple[str, int, int], ...]    # (kind,u_pre,v_pre)
    faces: tuple[tuple[int, int, int, int], ...]
    boundary1_cols: tuple[int, ...]            # edge boundaries in quotient C0
    boundary2_cols: tuple[int, ...]            # face boundaries in C1
    equality: bool

    @property
    def V(self) -> int:
        return 1 + max(self.qindex) if self.qindex else 0
    @property
    def E(self) -> int:
        return len(self.edges)
    @property
    def F(self) -> int:
        return len(self.faces)
    @property
    def m(self) -> int:
        return len(self.pinches)

def reduced_pair(a: int, b: int) -> tuple[int, int]:
    d = gcd(a, b)
    return a // d, b // d

def resonance_pinches(a: int, b: int, R: tuple[int, ...]) -> tuple[tuple[int,int,int], ...]:
    A, B = reduced_pair(a, b)
    if A == B:
        return ()
    S = set(R)
    out = []
    M = max(R, default=0)
    for t in range(1, M // max(1, min(A, B)) + 1):
        if A*t in S and B*t in S:
            out.append((A*t, B*t, t))
    return tuple(out)

def build_complex(a: int, b: int, R0) -> ComplexData:
    R = tuple(sorted(set(R0)))
    A, B = reduced_pair(a, b)
    if A == B:
        vertices = tuple(("a", r) for r in R)
        vi = {v:i for i,v in enumerate(vertices)}
        edges = []
        for i, r in enumerate(R):
            for s in R[i+1:]:
                edges.append(("h_a", vi[("a",r)], vi[("a",s)]))
        n = len(vertices)
        qindex = tuple(range(n))
        b1 = tuple((1<<u) ^ (1<<v) for _,u,v in edges)
        return ComplexData(a,b,R,A,B,(),vertices,qindex,tuple(edges),(),b1,(),True)

    vertices = tuple([("a", r) for r in R] + [("b", r) for r in R])
    vi = {v:i for i,v in enumerate(vertices)}
    dsu = DSU(len(vertices))
    pinches = resonance_pinches(a,b,R)

    touched = set()
    for At, Bt, t in pinches:
        x = vi[("b", At)]
        y = vi[("a", Bt)]
        check(x not in touched and y not in touched, "typed resonance family must be a matching")
        touched.add(x); touched.add(y)
        check(dsu.union(x,y), "each legal pinch must merge a new typed pair")

    roots = {}
    qindex = []
    for i in range(len(vertices)):
        r = dsu.find(i)
        if r not in roots:
            roots[r] = len(roots)
        qindex.append(roots[r])

    edges = []
    h_a = {}
    h_b = {}
    v = {}
    for row in ("a","b"):
        for i,r in enumerate(R):
            for s in R[i+1:]:
                idx = len(edges)
                edges.append((f"h_{row}",vi[(row,r)],vi[(row,s)]))
                (h_a if row=="a" else h_b)[(r,s)] = idx
    for r in R:
        idx = len(edges)
        edges.append(("v", vi[("a",r)], vi[("b",r)]))
        v[r] = idx

    faces = []
    b2 = []
    for i,r in enumerate(R):
        for s in R[i+1:]:
            face = (h_a[(r,s)], v[s], h_b[(r,s)], v[r])
            faces.append(face)
            bits = 0
            for e in face:
                bits ^= 1 << e
            b2.append(bits)

    b1 = []
    for _, up, vp in edges:
        u, w = qindex[up], qindex[vp]
        b1.append((1<<u) ^ (1<<w))

    return ComplexData(
        a,b,R,A,B,pinches,vertices,tuple(qindex),tuple(edges),tuple(faces),
        tuple(b1),tuple(b2),False
    )

def betti_and_ranks(X: ComplexData) -> tuple[int,int,int]:
    r1 = gf2_rank(list(X.boundary1_cols))
    r2 = gf2_rank(list(X.boundary2_cols))
    beta1 = X.E - r1 - r2
    return r1, r2, beta1

def edge_index(X: ComplexData, kind: str, r: int, s: int | None = None) -> int:
    target = {r} if s is None else {r,s}
    for i,(k,u,v) in enumerate(X.edges):
        if k != kind:
            continue
        vu, vv = X.vertices[u], X.vertices[v]
        labels = {vu[1],vv[1]}
        if labels == target:
            return i
    raise KeyError((kind,r,s))

def alpha_height(X: ComplexData) -> int:
    bits = 0
    if X.equality:
        return 0
    for i,(kind,_,_) in enumerate(X.edges):
        if kind == "v":
            bits |= 1 << i
    return bits

def is_closed(X: ComplexData, c: int) -> bool:
    return all(parity(c & f) == 0 for f in X.boundary2_cols)

def coboundary(X: ComplexData, lam: int) -> int:
    out = 0
    for e, bcol in enumerate(X.boundary1_cols):
        if parity(lam & bcol):
            out |= 1 << e
    return out

def is_exact(X: ComplexData, c: int) -> bool:
    gens = [coboundary(X, 1<<v) for v in range(X.V)]
    return gf2_rank(gens + [c]) == gf2_rank(gens)

def resonance_loop_bits(X: ComplexData, At: int, Bt: int) -> int:
    check(not X.equality, "no resonance loop in equality stratum")
    return (1 << edge_index(X,"v",At)) ^ (1 << edge_index(X,"h_a",At,Bt))

def backbone_triangle_bits(X: ComplexData, r: int, s: int, t: int) -> int:
    bits = 0
    for x,y in ((r,s),(s,t),(r,t)):
        bits ^= 1 << edge_index(X,"h_a",x,y)
    return bits

def all_flat_cochains(X: ComplexData) -> list[int]:
    return [c for c in range(1<<X.E) if is_closed(X,c)]

def gauge_orbits(X: ComplexData) -> list[set[int]]:
    flats = set(all_flat_cochains(X))
    gauge = {coboundary(X,lam) for lam in range(1<<X.V)}
    orbits = []
    while flats:
        c = min(flats)
        orb = {c ^ g for g in gauge}
        check(orb <= flats, "gauge must preserve flatness")
        flats -= orb
        orbits.append(orb)
    return orbits

def check_complex_formulas(X: ComplexData) -> None:
    k = len(X.R)
    r1,r2,beta = betti_and_ranks(X)
    if X.equality:
        expected_beta = (k-1)*(k-2)//2
        check(X.V == k)
        check(X.E == comb(k,2))
        check(X.F == 0)
        check(r1 == max(0,k-1))
        check(r2 == 0)
        check(beta == expected_beta)
        check(alpha_height(X) == 0)
        check(is_closed(X,0) and is_exact(X,0))
        check(X.E-r2 == comb(k,2))
        check((X.V-1 if X.V else 0) == max(0,k-1))
        return

    m = X.m
    expected_beta0 = (k-1)*(k-2)//2
    expected_beta = expected_beta0 + m
    check(X.V == 2*k-m)
    check(X.E == k*k)
    check(X.F == comb(k,2))
    check(r1 == X.V-1)
    check(r2 == X.F)
    check(beta == expected_beta)
    check(X.E-r2 == k*(k+1)//2)
    check(r1 == 2*k-m-1)
    check((X.E-r2)-r1 == expected_beta)

    alpha = alpha_height(X)
    check(is_closed(X,alpha))
    check(is_exact(X,alpha) == (m == 0))
    for At,Bt,t in X.pinches:
        gam = resonance_loop_bits(X,At,Bt)
        check(parity(alpha & gam) == 1, f"height period failed at t={t}")

def explicit_small_orbit_checks() -> None:
    cases = [
        build_complex(2,3,[2,3]),
        build_complex(2,3,[2,3,5]),
        build_complex(2,3,[5,7,11]),
        build_complex(5,5,[1,2,3]),
    ]
    for X in cases:
        _,_,beta = betti_and_ranks(X)
        flats = all_flat_cochains(X)
        orbs = gauge_orbits(X)
        check(len(flats) == 1 << (X.E-X.F))
        check(len(orbs) == 1 << beta)
        expected_orbit = 1 << (X.V-1) if X.V else 1
        check(all(len(o)==expected_orbit for o in orbs))

def independence_witness() -> None:
    X = build_complex(2,3,[2,3,5])
    check(X.m == 1)
    check(betti_and_ranks(X)[2] == 2)
    alpha = alpha_height(X)
    c = (1 << edge_index(X,"h_a",2,5)) | (1 << edge_index(X,"h_b",2,5))
    check(is_closed(X,c))
    check(not is_exact(X,c))
    gam = resonance_loop_bits(X,2,3)
    tri = backbone_triangle_bits(X,2,3,5)
    check(parity(alpha & gam)==1)
    check(parity(alpha & tri)==0)
    check(parity(c & gam)==0)
    check(parity(c & tri)==1)
    check(not is_exact(X,alpha ^ c))

def resonance_parametrization_checks() -> None:
    for a in range(2,17):
        for b in range(2,17):
            A,B = reduced_pair(a,b)
            for r in range(1,31):
                for s in range(1,31):
                    lhs1 = b*r == a*s
                    lhs2 = a*r == b*s
                    p1 = (r % A == 0 and s % B == 0 and r//A == s//B)
                    p2 = (r % B == 0 and s % A == 0 and r//B == s//A)
                    check(lhs1 == p1)
                    check(lhs2 == p2)
                    if A != B:
                        check(not (lhs1 and lhs2))
                    else:
                        check((A,B)==(1,1))
                        check(lhs1 == (r==s) and lhs2 == (r==s))

def exhaustive_cw_census() -> None:
    universe = tuple(range(1,9))
    subsets = []
    for q in range(2,6):
        subsets.extend(combinations(universe,q))
    for a in range(2,13):
        for b in range(2,13):
            for R in subsets:
                X = build_complex(a,b,R)
                check_complex_formulas(X)
                check(X.pinches == resonance_pinches(a,b,tuple(R)))
    named = [
        ("NO_RESONANCE",2,3,[5,7,11],0),
        ("SINGLE_RESONANCE",2,3,[2,3],1),
        ("MULTI_RESONANCE",2,3,[2,3,4,6],2),
        ("C1_PRIME_POWER_THICK",8,18,[4,8,9,18],2),
        ("C2_MULTISUPPORT",6,35,[6,12,35,70],2),
        ("O1_COMMON_BASE",6,10,[3,5,6,9,10,15],3),
        ("O2_RANK2",12,18,[2,3,4,6,8,12],3),
        ("E_EQUALITY",5,5,[1,2,3,4],0),
    ]
    for name,a,b,R,m in named:
        X = build_complex(a,b,R)
        check(X.m == m, name)
        check_complex_formulas(X)

PM = (
    frozenset((frozenset((0,1)),frozenset((2,3)))),
    frozenset((frozenset((0,2)),frozenset((1,3)))),
    frozenset((frozenset((0,3)),frozenset((1,2)))),
)
S4 = tuple(permutations(range(4)))
S3 = tuple(permutations(range(3)))
ID4 = (0,1,2,3)
ID3 = (0,1,2)

def compose(p,q):
    return tuple(p[q[i]] for i in range(len(q)))

def inv(p):
    out = [0]*len(p)
    for i,j in enumerate(p):
        out[j]=i
    return tuple(out)

def pcycle_type(p):
    seen=set(); lens=[]
    for i in range(len(p)):
        if i in seen: continue
        j=i; n=0
        while j not in seen:
            seen.add(j); n+=1; j=p[j]
        if n>1: lens.append(n)
    return tuple(sorted(lens, reverse=True))

def phi(p):
    images=[]
    for M in PM:
        M2=frozenset(frozenset((p[x] for x in pair)) for pair in M)
        images.append(PM.index(M2))
    return tuple(images)

def subgroup_generated(gens, identity):
    H={identity}
    changed=True
    while changed:
        changed=False
        for h in tuple(H):
            for g in gens:
                for x in (compose(h,g),compose(g,h)):
                    if x not in H:
                        H.add(x); changed=True
    return H

def s4_boundary_checks() -> None:
    kernel = {p for p in S4 if phi(p)==ID3}
    check(len(kernel)==4)
    check({pcycle_type(p) for p in kernel} == {(),(2,2)})
    for q in S3:
        fib=[p for p in S4 if phi(p)==q]
        check(len(fib)==4)
    tau=(0,2,1)
    fib=[p for p in S4 if phi(p)==tau]
    check(len(fib)==4)
    check(sum(pcycle_type(p)==(2,) for p in fib)==2)

    complements=[]
    for subset in combinations(S4,6):
        H=set(subset)
        if ID4 not in H: continue
        if any(compose(x,y) not in H for x in H for y in H):
            continue
        if {phi(x) for x in H} == set(S3):
            complements.append(frozenset(H))
    complements=list(dict.fromkeys(complements))
    check(len(complements)==4)

    def conj(v,H):
        vi=inv(v)
        return frozenset(compose(compose(v,h),vi) for h in H)
    orbit={conj(v,complements[0]) for v in kernel}
    check(set(complements)==orbit)

    for H in complements:
        sec={phi(h):h for h in H}
        check(len(sec)==6)
        for x in S3:
            for y in S3:
                check(compose(sec[x],sec[y]) == sec[compose(x,y)])

def main() -> None:
    resonance_parametrization_checks()
    exhaustive_cw_census()
    explicit_small_orbit_checks()
    independence_witness()
    s4_boundary_checks()
    print(
        "PASS "
        f"checks={CHECKS}; "
        "C2_flat_connections=Z1; gauge_classes=H1; "
        "one_typed_pinch_adds_one_H1_bit_without_adding_raw_edge_choice; "
        "height_periods=1_on_every_resonance_generator; "
        "operator_height_independence_witness=PASS; "
        "S4_kernel=V4_size4; sections=4; marked_transposition_lifts=4_with_2_atom_transpositions"
    )

if __name__ == "__main__":
    main()
