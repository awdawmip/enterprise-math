#!/usr/bin/env python3
"""
Exact checker for RS-GEO6-MAHLER-DUAL-SUPPORT-PRODUCT.

The checker validates:
1. typed finite-incidence Galois laws on every square binary context of size n<=3;
2. the Boolean anti-involution classification on every square binary relation of size n<=4;
3. the n=6 complement/self-dual model and its exact product spectrum;
4. the n=6 diagonal and closed-cycle comparison models;
5. rotation/permutation covariance on declared generators;
6. the exact refinement defect of the complement model.

No floating point, Euclidean metric, volume, convexity, or polarity is used.
"""

from itertools import permutations


def all_mask(n):
    return (1 << n) - 1


def d_obj_to_sup(a, n, rows):
    """Common-support operator A^perp: object subset bitmask -> support subset bitmask."""
    out = all_mask(n)
    for i in range(n):
        if (a >> i) & 1:
            out &= rows[i]
    return out


def d_sup_to_obj(b, n, rows):
    """Transpose common-support operator B^perp: support subset -> object subset."""
    out = all_mask(n)
    for j in range(n):
        if (b >> j) & 1:
            col = 0
            for i in range(n):
                if (rows[i] >> j) & 1:
                    col |= 1 << i
            out &= col
    return out


def transpose_rows(n, rows):
    cols = []
    for j in range(n):
        col = 0
        for i in range(n):
            if (rows[i] >> j) & 1:
                col |= 1 << i
        cols.append(col)
    return tuple(cols)


def is_symmetric(n, rows):
    return tuple(rows) == transpose_rows(n, rows)


def raw_d(a, n, rows):
    """Single-sort common-support map, meaningful as an endoduality when self-dual."""
    return d_obj_to_sup(a, n, rows)


def apply_perm(mask, p):
    out = 0
    for i, pi in enumerate(p):
        if (mask >> i) & 1:
            out |= 1 << pi
    return out


def rows_from_relation_bits(n, bits):
    m = all_mask(n)
    return tuple((bits >> (i * n)) & m for i in range(n))


def involutive_permutations(n):
    return [p for p in permutations(range(n)) if all(p[p[i]] == i for i in range(n))]


def complement_matching_rows(n, p):
    full = all_mask(n)
    return tuple(full ^ (1 << p[i]) for i in range(n))


def is_raw_involution(n, rows):
    return all(raw_d(raw_d(a, n, rows), n, rows) == a for a in range(1 << n))


def check_typed_galois_laws():
    contexts = 0
    assertions = 0
    for n in range(1, 4):
        for bits in range(1 << (n * n)):
            rows = rows_from_relation_bits(n, bits)
            contexts += 1
            for a in range(1 << n):
                da = d_obj_to_sup(a, n, rows)
                dda = d_sup_to_obj(da, n, rows)
                assert a & ~dda == 0
                ddda = d_obj_to_sup(dda, n, rows)
                assert ddda == da
                assertions += 2
            for b in range(1 << n):
                db = d_sup_to_obj(b, n, rows)
                ddb = d_obj_to_sup(db, n, rows)
                assert b & ~ddb == 0
                dddb = d_sup_to_obj(ddb, n, rows)
                assert dddb == db
                assertions += 2
            for a in range(1 << n):
                for b in range(1 << n):
                    if a & ~b == 0:
                        assert d_obj_to_sup(b, n, rows) & ~d_obj_to_sup(a, n, rows) == 0
                        assertions += 1
    return contexts, assertions


def check_boolean_anti_involution_classification():
    relation_counts = {}
    theorem_checks = 0
    for n in range(1, 5):
        actual = []
        for bits in range(1 << (n * n)):
            rows = rows_from_relation_bits(n, bits)
            if is_raw_involution(n, rows):
                actual.append(rows)
                assert is_symmetric(n, rows)
                theorem_checks += 1
        expected = {complement_matching_rows(n, p) for p in involutive_permutations(n)}
        assert set(actual) == expected
        relation_counts[n] = len(actual)
        theorem_checks += len(expected)
    assert relation_counts == {1: 1, 2: 2, 3: 4, 4: 10}
    return relation_counts, theorem_checks


def neq_rows(n):
    full = all_mask(n)
    return tuple(full ^ (1 << i) for i in range(n))


def eq_rows(n):
    return tuple(1 << i for i in range(n))


def closed_cycle_rows(n):
    rows = []
    for i in range(n):
        r = 0
        for j in ((i - 1) % n, i, (i + 1) % n):
            r |= 1 << j
        rows.append(r)
    return tuple(rows)


def check_n6_models():
    n = 6
    full = all_mask(n)

    rows = neq_rows(n)
    spectrum = {}
    for a in range(1 << n):
        da = raw_d(a, n, rows)
        assert da == (full ^ a)
        assert raw_d(da, n, rows) == a
        k = a.bit_count()
        if 0 < k < n:
            prod = k * da.bit_count()
            spectrum[prod] = spectrum.get(prod, 0) + 1
    assert spectrum == {5: 12, 8: 30, 9: 20}
    assert min(spectrum) == 5
    assert max(spectrum) == 9

    gens = [
        (1, 2, 3, 4, 5, 0),
        (0, 5, 4, 3, 2, 1),
    ]
    for p in gens:
        for a in range(1 << n):
            lhs = raw_d(apply_perm(a, p), n, rows)
            rhs = apply_perm(raw_d(a, n, rows), p)
            assert lhs == rhs

    rows_eq = eq_rows(n)
    closed_eq = []
    for a in range(1 << n):
        da = raw_d(a, n, rows_eq)
        dda = raw_d(da, n, rows_eq)
        if dda == a:
            closed_eq.append((a, a.bit_count() * da.bit_count()))
    closed_masks_eq = {a for a, _ in closed_eq}
    expected_closed_eq = {0, full} | {1 << i for i in range(n)}
    assert closed_masks_eq == expected_closed_eq
    assert {p for a, p in closed_eq if a not in (0, full)} == {1}

    rows_c6 = closed_cycle_rows(n)
    a = (1 << 0) | (1 << 2)
    da = raw_d(a, n, rows_c6)
    dda = raw_d(da, n, rows_c6)
    assert da == (1 << 1)
    assert dda == ((1 << 0) | (1 << 1) | (1 << 2))
    assert dda != a
    closed_c6_products = set()
    closed_c6_count = 0
    for x in range(1 << n):
        dx = raw_d(x, n, rows_c6)
        ddx = raw_d(dx, n, rows_c6)
        if ddx == x:
            closed_c6_count += 1
            if x not in (0, full):
                closed_c6_products.add(x.bit_count() * dx.bit_count())
    assert closed_c6_count == 20
    assert closed_c6_products == {3, 4}

    return spectrum, len(closed_eq), closed_c6_count, closed_c6_products


def check_refinement_defect():
    checks = 0
    for n in range(1, 6):
        for m in range(n + 1, 8):
            full_n = all_mask(n)
            full_m = all_mask(m)
            new = full_m ^ full_n
            for a in range(1 << n):
                dm = full_m ^ a
                embedded_dn = full_n ^ a
                assert dm == (embedded_dn | new)
                assert (dm ^ embedded_dn) == new
                assert new.bit_count() == m - n
                checks += 3
    return checks


def main():
    c, a = check_typed_galois_laws()
    counts, t = check_boolean_anti_involution_classification()
    spectrum, ceq, cc6, pc6 = check_n6_models()
    r = check_refinement_defect()
    print("PASS")
    print(f"typed_contexts={c}")
    print(f"typed_assertions={a}")
    print(f"raw_involution_counts={counts}")
    print(f"classification_checks={t}")
    print(f"n6_complement_product_spectrum={spectrum}")
    print(f"n6_eq_closed_count={ceq}")
    print(f"n6_cycle_closed_count={cc6}")
    print(f"n6_cycle_nontrivial_product_values={sorted(pc6)}")
    print(f"refinement_assertions={r}")


if __name__ == "__main__":
    main()
