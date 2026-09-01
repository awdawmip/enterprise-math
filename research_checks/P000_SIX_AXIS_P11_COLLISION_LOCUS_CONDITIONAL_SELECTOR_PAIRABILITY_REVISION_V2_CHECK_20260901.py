#!/usr/bin/env python3
"""Exact checker for P000 P11 pairability-filtered collision-locus revision V2.

Standard-library only.  The mathematical classification is symbolic; the bounded
enumeration below is a deterministic regression over a finite control domain.
"""
from collections import Counter, defaultdict
from itertools import combinations_with_replacement, permutations
from math import isqrt

PERMS = tuple(permutations(range(3)))
C1_PAIR = ((0, 2, 1), (1, 0, 2))  # 132 / 213
C2_PAIR = ((1, 2, 0), (2, 0, 1))  # 231 / 312

def canonical_K(H, T, perm):
    return tuple(sorted((H[i], T[perm[i]]) for i in range(3)))

def distinct_matchings(H, T):
    seen = {}
    for perm in PERMS:
        K = canonical_K(H, T, perm)
        seen.setdefault(K, perm)
    return [(perm, K) for K, perm in seen.items()]

def moment(H, T, perm, r, s):
    return sum((H[i] ** r) * (T[perm[i]] ** s) for i in range(3))

def pairable(h, t):
    delta = h*h - 4*t
    if delta < 0:
        return False
    d = isqrt(delta)
    return d*d == delta and (d-h) % 2 == 0

def packet_pairable(H, T, perm):
    return all(pairable(H[i], T[perm[i]]) for i in range(3))

def combinatorial_fibres(H, T):
    out = defaultdict(list)
    for perm, K in distinct_matchings(H, T):
        out[moment(H, T, perm, 1, 1)].append((perm, K))
    return out

def admissible_fibres(H, T):
    out = defaultdict(list)
    for perm, K in distinct_matchings(H, T):
        if packet_pairable(H, T, perm):
            out[moment(H, T, perm, 1, 1)].append((perm, K))
    return out

def collision_classes(H, T):
    if len(set(H)) < 3 or len(set(T)) < 3:
        return set()
    A, B = H[1]-H[0], H[2]-H[1]
    C, D = T[1]-T[0], T[2]-T[1]
    out = set()
    if A*C == B*D:
        out.add("C1")
    if A*D == B*C:
        out.add("C2")
    return out

def class_pair(cls):
    return C1_PAIR if cls == "C1" else C2_PAIR

def class_admissible_count(H, T, cls):
    return sum(packet_pairable(H, T, p) for p in class_pair(cls))

def power_sums(X):
    return [3, sum(X), sum(z*z for z in X), sum(z**3 for z in X), sum(z**4 for z in X)]

def gram3(X):
    r = power_sums(X)
    return [[r[0],r[1],r[2]],[r[1],r[2],r[3]],[r[2],r[3],r[4]]]

def det3(M):
    return (
        M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
        - M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
        + M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0])
    )

def adj3(M):
    return [
        [
            M[1][1]*M[2][2]-M[1][2]*M[2][1],
            -(M[0][1]*M[2][2]-M[0][2]*M[2][1]),
            M[0][1]*M[1][2]-M[0][2]*M[1][1],
        ],
        [
            -(M[1][0]*M[2][2]-M[1][2]*M[2][0]),
            M[0][0]*M[2][2]-M[0][2]*M[2][0],
            -(M[0][0]*M[1][2]-M[0][2]*M[1][0]),
        ],
        [
            M[1][0]*M[2][1]-M[1][1]*M[2][0],
            -(M[0][0]*M[2][1]-M[0][1]*M[2][0]),
            M[0][0]*M[1][1]-M[0][1]*M[1][0],
        ],
    ]

def quadratic_coefficients(nodes, mass_sum, mixed_first, mass_square_sum):
    G = gram3(nodes)
    A = adj3(G)
    Delta = det3(G)
    qa = A[2][2]
    qb = 2*(A[0][2]*mass_sum + A[1][2]*mixed_first)
    qc = (
        A[0][0]*mass_sum*mass_sum
        + 2*A[0][1]*mass_sum*mixed_first
        + A[1][1]*mixed_first*mixed_first
        - Delta*mass_square_sum
    )
    return qa, qb, qc, Delta

def q21_coeffs(H, T, p11):
    return quadratic_coefficients(H, sum(T), p11, sum(t*t for t in T))

def q12_coeffs(H, T, p11):
    return quadratic_coefficients(T, sum(H), p11, sum(h*h for h in H))

def qeval(q, x):
    a,b,c,_ = q
    return a*x*x+b*x+c

def assert_class_resolvent(H, T, cls):
    pair = class_pair(cls)
    p = moment(H,T,pair[0],1,1)
    assert p == moment(H,T,pair[1],1,1)
    xs = [moment(H,T,u,2,1) for u in pair]
    ys = [moment(H,T,u,1,2) for u in pair]
    qx = q21_coeffs(H,T,p)
    qy = q12_coeffs(H,T,p)
    assert all(qeval(qx,x) == 0 for x in xs)
    assert all(qeval(qy,y) == 0 for y in ys)
    assert xs[0] != xs[1] and ys[0] != ys[1]
    admissible = [packet_pairable(H,T,u) for u in pair]
    return p, xs, ys, admissible

def main():
    # 1. Direct pairability-filtered exhaustive control.
    values = (-30, -12, -4, -2, -1, 0, 1, 2, 4, 7)
    triples = tuple(combinations_with_replacement(values, 3))
    direct_cases = 0
    direct_valid_fibres = 0
    direct_doubletons = 0
    algebraic_counts = Counter()
    repeated_valid_max = 0
    max_adm_fibre = 0
    resolvent_collision_checks = 0

    for H in triples:
        for T in triples:
            CF = combinatorial_fibres(H,T)
            AF = admissible_fibres(H,T)
            assert max((len(v) for v in CF.values()), default=0) <= 2
            local_adm_max = max((len(v) for v in AF.values()), default=0)
            max_adm_fibre = max(max_adm_fibre, local_adm_max)
            assert local_adm_max <= 2
            direct_valid_fibres += len(AF)
            direct_doubletons += sum(len(v)==2 for v in AF.values())
            if len(set(H)) < 3 or len(set(T)) < 3:
                repeated_valid_max = max(repeated_valid_max, local_adm_max)
                assert local_adm_max <= 1

            classes = collision_classes(H,T)
            for cls in classes:
                pair = class_pair(cls)
                p = moment(H,T,pair[0],1,1)
                assert p == moment(H,T,pair[1],1,1)
                n = class_admissible_count(H,T,cls)
                algebraic_counts[(cls,n)] += 1
                assert len(AF.get(p,())) == n
                # Candidate resolvent remains the same before/after admissibility.
                _, xs, ys, adm = assert_class_resolvent(H,T,cls)
                assert sum(adm) == n
                if n == 1:
                    # Exactly one algebraic root reconstructs an admissible packet.
                    assert sum(packet_pairable(H,T,pair[j]) for j in range(2)) == 1
                elif n == 2:
                    # Root-order relation retained exactly on genuine doubletons.
                    dx = xs[0]-xs[1]
                    dy = ys[0]-ys[1]
                    if cls == "C1":
                        assert dx*dy > 0
                    else:
                        assert dx*dy < 0
                resolvent_collision_checks += 1
            direct_cases += 1

    assert max_adm_fibre <= 2
    assert repeated_valid_max <= 1

    # 2. Mandatory Driver falsifier: algebraic doubles, admissible singletons.
    H = (-2,0,2)
    T = (-1,0,1)
    assert collision_classes(H,T) == {"C1","C2"}
    p1,x1,y1,a1 = assert_class_resolvent(H,T,"C1")
    p2,x2,y2,a2 = assert_class_resolvent(H,T,"C2")
    assert p1 == 2 and a1 == [False, True]
    assert p2 == -2 and a2 == [False, True]
    assert len(admissible_fibres(H,T)[2]) == 1
    assert len(admissible_fibres(H,T)[-2]) == 1
    assert x1 == [-4,4] and y1 == [-2,2]
    assert x2 == [-4,4] and y2 == [2,-2]

    # 3. Both C1 and C2 may hold while their admissible cardinalities differ.
    #    Hence selector cost is per P11 level, not per (H,T) collision flag.
    H = (1,4,7)
    T = (-60,-30,0)
    assert collision_classes(H,T) == {"C1","C2"}
    p1,_,_,a1 = assert_class_resolvent(H,T,"C1")
    p2,_,_,a2 = assert_class_resolvent(H,T,"C2")
    assert (p1,a1) == (-270,[False,True])
    assert (p2,a2) == (-450,[True,True])
    assert len(admissible_fibres(H,T)[p1]) == 1
    assert len(admissible_fibres(H,T)[p2]) == 2

    # 4. Retained B=6 genuine two-admissible witnesses and branch relation.
    witnesses = {
        "C1": ((-1,1,4),(-30,-12,0),-18),
        "C2": ((-4,-1,1),(-30,-12,0),18),
    }
    witness_checks = 0
    for cls,(H,T,p_expected) in witnesses.items():
        assert cls in collision_classes(H,T)
        p,xs,ys,adm = assert_class_resolvent(H,T,cls)
        assert p == p_expected and adm == [True,True]
        if cls == "C1":
            assert xs == [-222,-42] and ys == [-324,756]
            assert (xs[0]-xs[1])*(ys[0]-ys[1]) > 0
        else:
            assert xs == [-222,-42] and ys == [324,-756]
            assert (xs[0]-xs[1])*(ys[0]-ys[1]) < 0
        witness_checks += 1

    # 5. Homogeneous scaling preserves pairability and doubleton status.
    scale_checks = 0
    for cls,(H0,T0,_) in witnesses.items():
        for m in range(1,13):
            H = tuple(m*h for h in H0)
            T = tuple(m*m*t for t in T0)
            pair = class_pair(cls)
            assert cls in collision_classes(H,T)
            assert all(packet_pairable(H,T,p) for p in pair)
            p = moment(H,T,pair[0],1,1)
            assert len(admissible_fibres(H,T)[p]) == 2
            scale_checks += 1

    # Root-box B=6 minimality is retained from the frozen Gen1 exact checker
    # and Driver review; this revision rechecks the two endpoint witnesses.
    print(
        "PASS P000_P11_PAIRABILITY_FILTERED_V2 "
        f"direct_cases={direct_cases} valid_fibres={direct_valid_fibres} "
        f"direct_doubletons={direct_doubletons} max_adm_fibre={max_adm_fibre} "
        f"repeated_valid_max={repeated_valid_max} "
        f"algebraic_C1_0={algebraic_counts[('C1',0)]} "
        f"algebraic_C1_1={algebraic_counts[('C1',1)]} "
        f"algebraic_C1_2={algebraic_counts[('C1',2)]} "
        f"algebraic_C2_0={algebraic_counts[('C2',0)]} "
        f"algebraic_C2_1={algebraic_counts[('C2',1)]} "
        f"algebraic_C2_2={algebraic_counts[('C2',2)]} "
        f"resolvent_collision_checks={resolvent_collision_checks} "
        f"witness_checks={witness_checks} scale_checks={scale_checks} "
        "driver_falsifier=C1:1|C2:1 mixed_levels=C1:1|C2:2 "
        "retained_rootbox_min=B6 selector_bits=log2_admissible_fibre"
    )

if __name__ == "__main__":
    main()
