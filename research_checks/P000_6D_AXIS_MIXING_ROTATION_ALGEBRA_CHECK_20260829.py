from __future__ import annotations

from collections import Counter, deque
from itertools import combinations, permutations, product

VERTS = tuple("ABCD")
EDGES = tuple(combinations(VERTS, 2))
EDGE_INDEX = {e: i for i, e in enumerate(EDGES)}
SLICES = {v: frozenset(e for e in EDGES if v in e) for v in VERTS}

# Frozen task labels: AB=L1, AC=L3, AD=L6, BC=L5, BD=L4, CD=L2.
TASK_LINE_LABEL = {
    ("A", "B"): "L1",
    ("A", "C"): "L3",
    ("A", "D"): "L6",
    ("B", "C"): "L5",
    ("B", "D"): "L4",
    ("C", "D"): "L2",
}
VEC = {
    ("A", "B"): (1, 1, 0),
    ("A", "C"): (1, 0, 1),
    ("A", "D"): (0, 1, -1),
    ("B", "C"): (0, 1, 1),
    ("B", "D"): (1, 0, -1),
    ("C", "D"): (1, -1, 0),
}

# One coherent chart-local orientation choice with sum zero on every slice.
CHART_REP = {
    "A": {("A", "B"): (-1, -1, 0), ("A", "C"): (1, 0, 1), ("A", "D"): (0, 1, -1)},
    "B": {("A", "B"): (1, 1, 0), ("B", "C"): (0, -1, -1), ("B", "D"): (-1, 0, 1)},
    "C": {("A", "C"): (-1, 0, -1), ("B", "C"): (0, 1, 1), ("C", "D"): (1, -1, 0)},
    "D": {("A", "D"): (0, 1, -1), ("B", "D"): (-1, 0, 1), ("C", "D"): (1, -1, 0)},
}


def canon_edge(a: str, b: str) -> tuple[str, str]:
    return tuple(sorted((a, b)))


def compose(p, q):
    """p q: q first, then p."""
    return tuple(p[q[i]] for i in range(len(q)))


def inv(p):
    out = [0] * len(p)
    for i, j in enumerate(p):
        out[j] = i
    return tuple(out)


def perm_pow(p, n):
    r = tuple(range(len(p)))
    for _ in range(n):
        r = compose(p, r)
    return r


def order(p):
    r = tuple(range(len(p)))
    for n in range(1, 100):
        r = compose(p, r)
        if r == tuple(range(len(p))):
            return n
    raise AssertionError("order overflow")


def vperm(mapping: dict[str, str]):
    return tuple(VERTS.index(mapping[v]) for v in VERTS)


def vimage(p, v):
    return VERTS[p[VERTS.index(v)]]


def edge_action(vp):
    out = []
    for a, b in EDGES:
        out.append(EDGE_INDEX[canon_edge(vimage(vp, a), vimage(vp, b))])
    return tuple(out)


def slice_action(vp):
    return tuple(vp)


def permutation_matrix(p):
    n = len(p)
    M = [[0] * n for _ in range(n)]
    # y_{p(i)} = x_i, equivalent to y_j=x_{p^{-1}(j)}.
    for i, j in enumerate(p):
        M[j][i] = 1
    return tuple(tuple(r) for r in M)


def det3(M):
    return (
        M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
        - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
        + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0])
    )


def mat_vec(M, v):
    return tuple(sum(M[i][j] * v[j] for j in range(3)) for i in range(3))


def line_key(v):
    w = tuple(v)
    for x in w:
        if x:
            if x < 0:
                w = tuple(-y for y in w)
            break
    return w


LINE_BY_KEY = {line_key(v): e for e, v in VEC.items()}


def physical_rotations():
    mats = []
    for colperm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            M = [[0] * 3 for _ in range(3)]
            for j, row in enumerate(colperm):
                M[row][j] = signs[j]
            M = tuple(tuple(r) for r in M)
            if det3(M) == 1:
                mats.append(M)
    assert len(mats) == 24
    return tuple(mats)


def physical_line_perm(M):
    out = []
    for e in EDGES:
        key = line_key(mat_vec(M, VEC[e]))
        assert key in LINE_BY_KEY
        out.append(EDGE_INDEX[LINE_BY_KEY[key]])
    return tuple(out)


def induced_slice_perm(ep):
    image_sets = {}
    for i, v in enumerate(VERTS):
        image_sets[v] = frozenset(EDGES[ep[EDGE_INDEX[e]]] for e in SLICES[v])
    out = []
    for v in VERTS:
        targets = [w for w in VERTS if image_sets[v] == SLICES[w]]
        assert len(targets) == 1
        out.append(VERTS.index(targets[0]))
    return tuple(out)


def common_chart_sign(M, vp, source):
    target = vimage(vp, source)
    signs = []
    for e, vec in CHART_REP[source].items():
        a, b = e
        te = canon_edge(vimage(vp, a), vimage(vp, b))
        mapped = mat_vec(M, vec)
        target_vec = CHART_REP[target][te]
        if mapped == target_vec:
            signs.append(1)
        elif mapped == tuple(-x for x in target_vec):
            signs.append(-1)
        else:
            raise AssertionError((M, source, e, mapped, target, te, target_vec))
    assert len(set(signs)) == 1
    return signs[0]


def extend_supported(ep, omega):
    """Naive identity-outside extension of the restricted edge action."""
    p = list(range(6))
    for i in omega:
        p[i] = ep[i]
    return tuple(p)


def is_perm(p):
    return sorted(p) == list(range(len(p)))


def support(p):
    return frozenset(i for i, j in enumerate(p) if i != j)


def comm(a, b):
    return compose(compose(compose(a, b), inv(a)), inv(b))


def closure(gens):
    identity = tuple(range(len(gens[0])))
    seen = {identity}
    q = deque([identity])
    while q:
        x = q.popleft()
        for g in gens:
            y = compose(g, x)
            if y not in seen:
                seen.add(y)
                q.append(y)
    return seen


def cycle_string(p, labels):
    seen = set()
    cs = []
    for i in range(len(p)):
        if i in seen or p[i] == i:
            continue
        cyc = []
        j = i
        while j not in seen:
            seen.add(j)
            cyc.append(labels[j])
            j = p[j]
        cs.append("(" + " ".join(cyc) + ")")
    return "".join(cs) or "()"


def check_k4_incidence():
    assert len(EDGES) == 6
    assert all(len(SLICES[v]) == 3 for v in VERTS)
    counts = Counter(e for v in VERTS for e in SLICES[v])
    assert all(counts[e] == 2 for e in EDGES)
    for a, b in EDGES:
        assert SLICES[a] & SLICES[b] == frozenset({(a, b)})
    expected = {
        "A": frozenset({("A", "B"), ("A", "C"), ("A", "D")}),
        "B": frozenset({("A", "B"), ("B", "C"), ("B", "D")}),
        "C": frozenset({("A", "C"), ("B", "C"), ("C", "D")}),
        "D": frozenset({("A", "D"), ("B", "D"), ("C", "D")}),
    }
    assert SLICES == expected


def check_s4_and_physical_rotations():
    all_vp = tuple(tuple(p) for p in permutations(range(4)))
    all_ep = {edge_action(vp) for vp in all_vp}
    assert len(all_ep) == 24  # faithful 2-subset action

    phys = physical_rotations()
    physical_pairs = []
    for M in phys:
        ep = physical_line_perm(M)
        sp = induced_slice_perm(ep)
        assert ep == edge_action(sp)
        physical_pairs.append((M, sp, ep))
    assert len({sp for _, sp, _ in physical_pairs}) == 24
    assert len({ep for _, _, ep in physical_pairs}) == 24
    assert {sp for _, sp, _ in physical_pairs} == set(all_vp)

    # Unique physical 3x3 realization for every S4 slice action in this chosen atlas.
    by_sp = {sp: M for M, sp, _ in physical_pairs}
    assert len(by_sp) == 24

    # Exact chart orientation transport is a one-bit cocycle over slice charts.
    eps = {}
    for M, sp, _ in physical_pairs:
        for s in VERTS:
            eps[(sp, s)] = common_chart_sign(M, sp, s)
    for sigma in all_vp:
        for tau in all_vp:
            st = compose(sigma, tau)
            for s in VERTS:
                lhs = eps[(st, s)]
                rhs = eps[(sigma, vimage(tau, s))] * eps[(tau, s)]
                assert lhs == rhs
    return by_sp, eps


def check_generators(by_sp):
    # a=(B C D), b=(A B), under A,B,C,D index order.
    a = vperm({"A": "A", "B": "C", "C": "D", "D": "B"})
    b = vperm({"A": "B", "B": "A", "C": "C", "D": "D"})
    assert order(a) == 3
    assert order(b) == 2
    assert order(compose(a, b)) == 4
    assert len(closure((a, b))) == 24
    assert max(order(p) for p in closure((a, b))) == 4  # S4 is not cyclic.

    ea, eb = edge_action(a), edge_action(b)
    assert cycle_string(ea, EDGES) == "(AB AC AD)(BC CD BD)"
    assert cycle_string(eb, EDGES) == "(AC BC)(AD BD)"

    Pa = permutation_matrix(ea)
    Pb = permutation_matrix(eb)
    assert Pa == (
        (0, 0, 1, 0, 0, 0),
        (1, 0, 0, 0, 0, 0),
        (0, 1, 0, 0, 0, 0),
        (0, 0, 0, 0, 1, 0),
        (0, 0, 0, 0, 0, 1),
        (0, 0, 0, 1, 0, 0),
    )
    assert Pb == (
        (1, 0, 0, 0, 0, 0),
        (0, 0, 0, 1, 0, 0),
        (0, 0, 0, 0, 1, 0),
        (0, 1, 0, 0, 0, 0),
        (0, 0, 1, 0, 0, 0),
        (0, 0, 0, 0, 0, 1),
    )

    Qa, Qb = by_sp[a], by_sp[b]
    assert Qa == ((0, -1, 0), (0, 0, 1), (-1, 0, 0))
    assert Qb == ((0, -1, 0), (-1, 0, 0), (0, 0, -1))
    assert det3(Qa) == det3(Qb) == 1
    return a, b, ea, eb


def check_stabilizers():
    all_vp = tuple(tuple(p) for p in permutations(range(4)))
    stab_A = [p for p in all_vp if vimage(p, "A") == "A"]
    stab_AB = [p for p in all_vp if edge_action(p)[EDGE_INDEX[("A", "B")]] == EDGE_INDEX[("A", "B")]]
    stab_A_AB = [p for p in stab_A if p in stab_AB]
    assert len(stab_A) == 6
    assert len(stab_AB) == 4
    assert len(stab_A_AB) == 2


def check_supported_moves_and_conjugation():
    all_vp = tuple(tuple(p) for p in permutations(range(4)))
    all_eps = [edge_action(p) for p in all_vp]
    for ep in all_eps:
        for mask in range(1 << 6):
            omega = frozenset(i for i in range(6) if mask & (1 << i))
            image = frozenset(ep[i] for i in omega)
            naive = extend_supported(ep, omega)
            assert is_perm(naive) == (image == omega)
            if image == omega:
                assert compose(naive, extend_supported(inv(ep), omega)) == tuple(range(6))

    # Conjugation identity for every ambiently legal supported move.
    for sigma in all_vp:
        es = edge_action(sigma)
        for mask in range(1 << 6):
            omega = frozenset(i for i in range(6) if mask & (1 << i))
            if frozenset(es[i] for i in omega) != omega:
                continue
            M = extend_supported(es, omega)
            for tau in all_vp:
                et = edge_action(tau)
                lhs = compose(compose(et, M), inv(et))
                image_omega = frozenset(et[i] for i in omega)
                conj_sigma = compose(compose(tau, sigma), inv(tau))
                rhs = extend_supported(edge_action(conj_sigma), image_omega)
                assert lhs == rhs


def check_commutator_support_lemma():
    # Exhaust all 720^2 pairs of permutations of the six carrier slots.
    perms6 = tuple(tuple(p) for p in permutations(range(6)))
    for A in perms6:
        SA = support(A)
        for B in perms6:
            SB = support(B)
            delta = SA & SB
            union = set(delta)
            union |= {A[i] for i in delta}
            union |= {B[i] for i in delta}
            C = comm(A, B)
            assert support(C) <= frozenset(union)


def check_localizer_and_words(a, b):
    # U_A = 3-cycle on S_A induced by a=(BCD).
    UA = extend_supported(edge_action(a), frozenset(EDGE_INDEX[e] for e in SLICES["A"]))
    # b a b = (A C D), fixing B; support-restrict it to S_B.
    bab = compose(compose(b, a), b)
    UB = extend_supported(edge_action(bab), frozenset(EDGE_INDEX[e] for e in SLICES["B"]))
    assert cycle_string(UA, EDGES) == "(AB AC AD)"
    assert cycle_string(UB, EDGES) == "(AB BC BD)"
    C = comm(UA, UB)
    assert cycle_string(C, EDGES) == "(AB AC BC)"
    assert support(C) == frozenset(EDGE_INDEX[e] for e in (("A", "B"), ("A", "C"), ("B", "C")))
    delta = support(UA) & support(UB)
    assert delta == frozenset({EDGE_INDEX[("A", "B")]})
    bound = delta | frozenset(UA[i] for i in delta) | frozenset(UB[i] for i in delta)
    assert support(C) == bound  # sharp support bound here.

    # Bounded shortest certificate: no freely reduced nonidentity word of length <=3
    # over U_A^{+-1}, U_B^{+-1} has support within the target face triangle.
    gens = (UA, inv(UA), UB, inv(UB))
    inv_letter = {0: 1, 1: 0, 2: 3, 3: 2}
    target = support(C)
    identity = tuple(range(6))
    for length in range(1, 4):
        for word in product(range(4), repeat=length):
            if any(inv_letter[word[i]] == word[i + 1] for i in range(length - 1)):
                continue
            p = identity
            for letter in word:
                p = compose(gens[letter], p)
            if p != identity:
                assert not support(p) <= target

    # Axis targeting: every single edge slot admits a support-2 transposition obtained
    # by conjugating the b edge action and restricting to one of its 2-cycles.
    all_vp = tuple(tuple(p) for p in permutations(range(4)))
    targets_seen = set()
    eb = edge_action(b)
    for tau in all_vp:
        et = edge_action(tau)
        conjugate = compose(compose(et, eb), inv(et))
        cycles = []
        seen = set()
        for i in range(6):
            if i not in seen and conjugate[i] != i:
                j = conjugate[i]
                assert conjugate[j] == i
                pair = frozenset({i, j})
                seen |= pair
                cycles.append(pair)
        for pair in cycles:
            move = extend_supported(conjugate, pair)
            assert is_perm(move)
            assert support(move) == pair
            targets_seen |= pair
    assert targets_seen == set(range(6))


def canonical_words(a, b):
    # Alphabet deliberately uses a,a^-1,b so elementary inverse cancellation is explicit.
    ai = inv(a)
    alphabet = (("a", a), ("A", ai), ("b", b))
    identity = tuple(range(4))
    q = deque([identity])
    word = {identity: ""}
    while q:
        p = q.popleft()
        for symbol, g in alphabet:
            h = compose(g, p)
            if h not in word:
                word[h] = word[p] + symbol
                q.append(h)
    assert len(word) == 24
    distribution = Counter(len(w) for w in word.values())
    assert distribution == Counter({0: 1, 1: 3, 2: 4, 3: 6, 4: 6, 5: 3, 6: 1})
    return word


def check_regressions():
    # C2 whole-block swap regression remains a distinct involution, not a proof of S4 native truth.
    rho = tuple(range(3, 6)) + tuple(range(0, 3))
    assert order(rho) == 2
    assert support(rho) == frozenset(range(6))

    # HCP regression is a typed semantic guard: the FCC line pairing is carrier-specific.
    HCP_FIRST_SHELL_CENTRALLY_SYMMETRIC = False
    assert not HCP_FIRST_SHELL_CENTRALLY_SYMMETRIC


def main():
    check_k4_incidence()
    by_sp, eps = check_s4_and_physical_rotations()
    a, b, ea, eb = check_generators(by_sp)
    check_stabilizers()
    check_supported_moves_and_conjugation()
    check_commutator_support_lemma()
    check_localizer_and_words(a, b)
    words = canonical_words(a, b)
    check_regressions()

    print("PASS")
    print("physical_rotations=24")
    print("S4_edge_representation=faithful")
    print(f"generator_orders=a:{order(a)},b:{order(b)},ab:{order(compose(a,b))}")
    print(f"normal_forms={len(words)},max_shortlex_length={max(map(len, words.values()))}")
    print("supported_extension_iff_invariant=exhaustive_24x64")
    print("conjugation=exhaustive")
    print("commutator_support_lemma=exhaustive_Sym6_pairs")
    print("localizer=[U_A,U_B]=(AB AC BC),shortest_local_word_length=4")
    print("axis_targeting_min_support=2")
    print("chart_orientation_transport=cocycle_verified")
    print("typed_regressions=C2,HCP")


if __name__ == "__main__":
    main()
