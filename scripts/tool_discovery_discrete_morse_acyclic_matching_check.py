#!/usr/bin/env python3
"""Deterministic exact checker for RS-TD-DM.

No floating arithmetic is used.  The checker exercises legal unit cancellation,
closed-gradient-path rejection, integer nonunit refusal, rational field-only
cancellation, torsion information loss, exact SDR identities, relabeling
invariance, two distinct Enterprise application families, and malformed
certificate rejection.
"""

from __future__ import annotations

import argparse
import copy
import json
import pathlib
import sys
from fractions import Fraction
from itertools import combinations
from math import gcd

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from enterprise_math.discrete_morse_collapse import (  # noqa: E402
    CertificateError,
    ChainComplexError,
    CyclicMatchingError,
    FiniteChainComplex,
    MatchingPair,
    NonUnitIncidenceError,
    MorseReductionCertificate,
    morse_reduce,
    rank_one_integer_torsion_guard,
    relabel_complex,
    relabel_matching,
    validate_matching,
    verify_certificate,
)


def _det_int(matrix):
    """Exact determinant by fraction-free Bareiss elimination."""
    n = len(matrix)
    if n == 0:
        return 1
    a = [list(map(int, row)) for row in matrix]
    if any(len(row) != n for row in a):
        raise ValueError("determinant requires square matrix")
    sign = 1
    prev = 1
    for k in range(n - 1):
        pivot = next((r for r in range(k, n) if a[r][k] != 0), None)
        if pivot is None:
            return 0
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            sign *= -1
        p = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (a[i][j] * p - a[i][k] * a[k][j]) // prev
        prev = p
        for i in range(k + 1, n):
            a[i][k] = 0
    return sign * a[n - 1][n - 1]


def smith_cokernel_invariants(matrix, nrows=None, ncols=None):
    """Exact Smith invariants via determinantal divisors.

    Returns coker(A: Z^ncols -> Z^nrows) as free rank plus torsion invariant
    factors.  This bounded checker uses all exact minors, avoiding floating rank.
    """
    if nrows is None:
        nrows = len(matrix)
    if ncols is None:
        ncols = len(matrix[0]) if matrix else 0
    if len(matrix) != nrows or any(len(row) != ncols for row in matrix):
        raise ValueError("matrix shape mismatch")
    maxk = min(nrows, ncols)
    deltas = [1]
    rank = 0
    for k in range(1, maxk + 1):
        g = 0
        for rows in combinations(range(nrows), k):
            for cols in combinations(range(ncols), k):
                minor = [[matrix[i][j] for j in cols] for i in rows]
                g = gcd(g, abs(_det_int(minor)))
        if g == 0:
            break
        deltas.append(g)
        rank = k
    invariant_factors = [deltas[k] // deltas[k - 1] for k in range(1, rank + 1)]
    assert all(x > 0 for x in invariant_factors)
    assert all(invariant_factors[i + 1] % invariant_factors[i] == 0 for i in range(len(invariant_factors) - 1))
    return {
        "rank": rank,
        "free_rank": nrows - rank,
        "torsion": tuple(x for x in invariant_factors if x != 1),
        "invariant_factors": tuple(invariant_factors),
        "determinantal_divisors": tuple(deltas),
    }


def boundary_matrix(complex_, upper_degree):
    upper = complex_.basis_by_degree.get(upper_degree, ())
    lower = complex_.basis_by_degree.get(upper_degree - 1, ())
    return [[int(complex_.boundary[u].get(l, 0)) for u in upper] for l in lower], len(lower), len(upper)


def graph_homology_normal_form(complex_):
    """Exact H1/H0 for a 1-dimensional integral complex (no C2)."""
    assert complex_.ring == "Z"
    assert not complex_.basis_by_degree.get(2, ())
    matrix, rows, cols = boundary_matrix(complex_, 1)
    h0 = smith_cokernel_invariants(matrix, rows, cols)
    h1_free_rank = cols - h0["rank"]  # kernel of map between free Z-modules is free
    return {
        "H1_free_rank": h1_free_rank,
        "H1_torsion": (),
        "H0_free_rank": h0["free_rank"],
        "H0_torsion": h0["torsion"],
        "d1_smith": h0,
    }


def interval_complex(ring="Z"):
    return FiniteChainComplex(
        ring,
        {1: ("e",), 0: ("v0", "v1")},
        {"e": {"v1": 1, "v0": -1}, "v0": {}, "v1": {}},
    )


def threshold_support_simplex():
    """Application A: an actual weighted threshold/support complex.

    Vertices a,b have weight 1, vertices c,d have weight 2, and a face is
    admitted when its weight sum is <=3.  The nonempty faces are the four
    vertices and five edges ab, ac, ad, bc, bd; edge cd and every triangle are
    excluded.  Thus this is a genuine threshold complex with H1 of rank 2,
    not a full-simplex toy.
    """
    return FiniteChainComplex(
        "Z",
        {1: ("eab", "eac", "ead", "ebc", "ebd"), 0: ("va", "vb", "vc", "vd")},
        {
            "eab": {"vb": 1, "va": -1},
            "eac": {"vc": 1, "va": -1},
            "ead": {"vd": 1, "va": -1},
            "ebc": {"vc": 1, "vb": -1},
            "ebd": {"vd": 1, "vb": -1},
            "va": {},
            "vb": {},
            "vc": {},
            "vd": {},
        },
    )


def threshold_matching():
    # Cancel a spanning-tree set of unit incidences; ebc and ebd remain as
    # critical cycle generators.
    return (
        MatchingPair("vb", "eab"),
        MatchingPair("vc", "eac"),
        MatchingPair("vd", "ead"),
    )


def relation_collapse_complex():
    """Application B: exact relation/syzygy complex, not a threshold complex.

    r1 and r2 impose the same degree-0 relation x and s records their degree-2
    syzygy.  y is an independent surviving relation-state generator.
    """
    return FiniteChainComplex(
        "Z",
        {2: ("s",), 1: ("r1", "r2"), 0: ("x", "y")},
        {
            "s": {"r1": 1, "r2": -1},
            "r1": {"x": 1},
            "r2": {"x": 1},
            "x": {},
            "y": {},
        },
    )


def relation_matching():
    return (MatchingPair("r1", "s"), MatchingPair("x", "r2"))


def cyclic_complex():
    return FiniteChainComplex(
        "Z",
        {1: ("e1", "e2"), 0: ("v1", "v2")},
        {
            "e1": {"v1": 1, "v2": 1},
            "e2": {"v1": 1, "v2": 1},
            "v1": {},
            "v2": {},
        },
    )


def cyclic_matching():
    return (MatchingPair("v1", "e1"), MatchingPair("v2", "e2"))


def nonunit_complex(ring="Z"):
    return FiniteChainComplex(
        ring,
        {1: ("e",), 0: ("v",)},
        {"e": {"v": 2}, "v": {}},
    )


def check_known_interval_homology(cert):
    original = graph_homology_normal_form(cert.source)
    reduced = graph_homology_normal_form(cert.reduced)
    assert original["H1_free_rank"] == reduced["H1_free_rank"] == 0
    assert original["H0_free_rank"] == reduced["H0_free_rank"] == 1
    assert original["H0_torsion"] == reduced["H0_torsion"] == ()
    return {"H1": "0", "H0": "Z"}


def check_known_threshold_homology(cert):
    assert verify_certificate(cert)
    original = graph_homology_normal_form(cert.source)
    reduced = graph_homology_normal_form(cert.reduced)
    for data in (original, reduced):
        assert data["H1_free_rank"] == 2 and data["H1_torsion"] == ()
        assert data["H0_free_rank"] == 1 and data["H0_torsion"] == ()
    assert cert.reduced.boundary["ebc"] == {}
    assert cert.reduced.boundary["ebd"] == {}
    return {"H1": "Z^2", "H0": "Z"}


def check_known_relation_homology(cert):
    # d1=[1 1;0 0]. Exact Smith invariants give rank 1 and H0=Z.
    d1, rows, cols = boundary_matrix(cert.source, 1)
    d1_smith = smith_cokernel_invariants(d1, rows, cols)
    assert d1_smith["rank"] == 1
    assert d1_smith["free_rank"] == 1 and d1_smith["torsion"] == ()
    # ker(d1)=Z*(r1-r2); d2(s)=r1-r2, so in this exact kernel basis the
    # induced d2 coordinate matrix is [1]. Its Smith form kills H1 with no
    # torsion, while injectivity gives H2=0.
    kernel_quotient = smith_cokernel_invariants([[1]], 1, 1)
    assert kernel_quotient["free_rank"] == 0 and kernel_quotient["torsion"] == ()
    assert cert.reduced.basis_by_degree == {0: ("y",)}
    assert verify_certificate(cert)
    return {"H2": "0", "H1": "0", "H0": "Z"}


def run_suite(verbose=True):
    checks = 0
    mismatches = []

    def check(name, fn):
        nonlocal checks
        checks += 1
        try:
            fn()
            if verbose:
                print(f"PASS {name}")
        except Exception as exc:  # exact regression harness; collect all mismatches
            mismatches.append((name, f"{type(exc).__name__}: {exc}"))
            if verbose:
                print(f"FAIL {name}: {type(exc).__name__}: {exc}")

    def unit_interval():
        c = interval_complex()
        cert = morse_reduce(c, [MatchingPair("v1", "e")])
        assert len(c.generators) == 3 and len(cert.reduced.generators) == 1
        assert cert.critical_generators == ("v0",)
        assert verify_certificate(cert)
        assert check_known_interval_homology(cert) == {"H1": "0", "H0": "Z"}

    check("unit cancellation + exact SDR + known integral homology", unit_interval)

    def morse_boundary():
        cert = morse_reduce(threshold_support_simplex(), threshold_matching())
        cert.reduced.validate()  # includes d^2=0 exact check
        assert cert.reduced.boundary["ebc"] == {} and cert.reduced.boundary["ebd"] == {}
        assert check_known_threshold_homology(cert) == {"H1": "Z^2", "H0": "Z"}

    check("exact Morse boundary and d^2=0", morse_boundary)

    def cyclic_rejection():
        try:
            validate_matching(cyclic_complex(), cyclic_matching())
        except CyclicMatchingError as exc:
            witness = exc.cycle
            assert witness[0] == witness[-1]
            assert {"v1", "e1", "v2", "e2"}.issubset(witness)
            return
        raise AssertionError("cyclic matching was accepted")

    check("closed gradient cycle rejected with witness", cyclic_rejection)

    def nonunit_integer():
        try:
            morse_reduce(nonunit_complex("Z"), [MatchingPair("v", "e")])
        except NonUnitIncidenceError:
            return
        raise AssertionError("integer coefficient 2 was cancelled")

    check("nonunit integer incidence refused", nonunit_integer)

    def field_only_and_torsion():
        qcert = morse_reduce(nonunit_complex("Q"), [MatchingPair("v", "e")])
        assert qcert.field_only is True
        assert qcert.reduced.generators == ()
        guard = rank_one_integer_torsion_guard(2)
        snf = smith_cokernel_invariants([[2]], 1, 1)
        assert snf["free_rank"] == 0 and snf["torsion"] == (2,)
        assert guard == {
            "coefficient": 2,
            "integral_h0": "Z/2Z",
            "integral_h1": "0",
            "torsion_order": 2,
            "rational_h0_dimension": 0,
            "rational_h1_dimension": 0,
        }

    check("field-only cancellation cannot erase Z/2 torsion claim", field_only_and_torsion)

    def bad_greedy():
        c = cyclic_complex()
        # Each pair is locally legal by itself.
        validate_matching(c, [MatchingPair("v1", "e1")])
        validate_matching(c, [MatchingPair("v2", "e2")])
        # Greedily taking both makes a global cycle and must fail.
        try:
            validate_matching(c, cyclic_matching())
        except CyclicMatchingError:
            return
        raise AssertionError("globally cyclic greedy union was accepted")

    check("locally legal greedy pairs can be globally cyclic", bad_greedy)

    def malformed_certificate():
        cert = morse_reduce(interval_complex(), [MatchingPair("v1", "e")])
        payload = cert.to_dict()
        payload["projection"]["v0"] = {}  # destroys P I = id and replay equality
        forged = MorseReductionCertificate.from_dict(payload)
        try:
            verify_certificate(forged)
        except CertificateError:
            return
        raise AssertionError("malformed certificate was accepted")

    check("malformed project/lift/homotopy certificate rejected", malformed_certificate)

    def two_domains():
        a = morse_reduce(threshold_support_simplex(), threshold_matching())
        b = morse_reduce(relation_collapse_complex(), relation_matching())
        assert (len(a.source.generators), len(a.reduced.generators)) == (9, 3)
        assert (len(b.source.generators), len(b.reduced.generators)) == (5, 1)
        assert check_known_threshold_homology(a) == {"H1": "Z^2", "H0": "Z"}
        assert check_known_relation_homology(b) == {"H2": "0", "H1": "0", "H0": "Z"}

    check("cross-domain reuse: threshold/support + relation/syzygy", two_domains)

    def dependent_composition():
        c = FiniteChainComplex(
            "Z",
            {1: ("e1", "e2"), 0: ("v1", "v2")},
            {"e1": {"v1": 1, "v2": 1}, "e2": {"v2": 1}, "v1": {}, "v2": {}},
        )
        m = (MatchingPair("v1", "e1"), MatchingPair("v2", "e2"))
        cert = morse_reduce(c, m)
        # e1->v2 creates a real dependency between matched pairs, so exact
        # sink-order cancellation must take (v2,e2) first.
        assert cert.cancellation_order == (MatchingPair("v2", "e2"), MatchingPair("v1", "e1"))
        assert cert.reduced.generators == ()
        assert verify_certificate(cert)

    check("dependent multi-step cancellation composes SDR certificate", dependent_composition)

    def graph_nonapplicability():
        try:
            FiniteChainComplex.from_dict({"nodes": ["a", "b"], "edges": [["a", "b"]]})
        except ChainComplexError:
            return
        raise AssertionError("arbitrary graph payload was inferred to be a chain complex")

    check("arbitrary state graph rejected without grading/incidence semantics", graph_nonapplicability)

    def operation_semantics_boundary():
        cert = morse_reduce(interval_complex(), [MatchingPair("v1", "e")])
        # An external operation OBSERVE_V1 requiring generator v1 cannot factor
        # through the reduced basis because v1 is not a critical generator.
        declared_required_generator = "v1"
        assert declared_required_generator in cert.source.generators
        assert declared_required_generator not in cert.reduced.generators
        # This is a precise non-applicability flag, not a claim of T6 safety.

    check("homology preservation does not imply operation/observation safety", operation_semantics_boundary)

    def relabeling_invariance():
        c = threshold_support_simplex()
        m = threshold_matching()
        rename = {
            "eab": "E0",
            "eac": "E1",
            "ead": "E2",
            "ebc": "E3",
            "ebd": "E4",
            "va": "p",
            "vb": "q",
            "vc": "r",
            "vd": "s",
        }
        a = morse_reduce(c, m)
        b = morse_reduce(relabel_complex(c, rename), relabel_matching(m, rename))
        assert len(a.source.generators) == len(b.source.generators)
        assert len(a.reduced.generators) == len(b.reduced.generators) == 3
        assert b.critical_generators == tuple(rename[g] for g in a.critical_generators)
        assert check_known_threshold_homology(a) == {"H1": "Z^2", "H0": "Z"}
        # The theorem-level SDR/reduction result is equivariant when the supplied
        # matching is relabeled.  This does not make a greedy matching canonical.
        assert verify_certificate(b)

    check("relabeling invariance of theorem-level supplied-matching output", relabeling_invariance)

    def greedy_not_canonical():
        # Presentation-order greedy on the interval can choose either endpoint.
        c = interval_complex()
        left = morse_reduce(c, [MatchingPair("v0", "e")])
        right = morse_reduce(c, [MatchingPair("v1", "e")])
        assert left.critical_generators == ("v1",)
        assert right.critical_generators == ("v0",)
        assert verify_certificate(left) and verify_certificate(right)
        assert check_known_interval_homology(right)["H0"] == "Z"

    check("greedy matching presentation dependence is not called canonical", greedy_not_canonical)

    def no_geometry_inference():
        # The relation complex is accepted because grading and d are declared;
        # no embedding, metric, manifold, or geometric dimension is inferred.
        c = relation_collapse_complex()
        assert set(c.to_dict()) == {"ring", "basis_by_degree", "boundary"}
        assert morse_reduce(c, relation_matching()).reduced.generators == ("y",)

    check("implementation geometry is not inferred as native topology", no_geometry_inference)

    if verbose:
        for name, message in mismatches:
            print(f"MISMATCH {name}: {message}")
        print(f"checks={checks}")
        print(f"mismatch_count={len(mismatches)}")
    return checks, mismatches


def demo_unit():
    cert = morse_reduce(interval_complex(), [MatchingPair("v1", "e")])
    print(json.dumps(cert.to_dict(), indent=2, sort_keys=True))


def demo_cyclic():
    try:
        morse_reduce(cyclic_complex(), cyclic_matching())
    except CyclicMatchingError as exc:
        print(json.dumps({"accepted": False, "obstruction": "closed-gradient-path", "cycle": list(exc.cycle)}, indent=2))
        return 0
    print(json.dumps({"accepted": True, "error": "cyclic matching unexpectedly accepted"}))
    return 1


def demo_nonunit():
    z_refused = False
    try:
        morse_reduce(nonunit_complex("Z"), [MatchingPair("v", "e")])
    except NonUnitIncidenceError:
        z_refused = True
    qcert = morse_reduce(nonunit_complex("Q"), [MatchingPair("v", "e")])
    result = {
        "Z_unit_required_and_refused": z_refused,
        "Q_same_pivot_cancelled": qcert.reduced.generators == (),
        "Q_field_only": qcert.field_only,
        "integral_torsion_guard": rank_one_integer_torsion_guard(2),
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if all([z_refused, qcert.field_only, qcert.reduced.generators == ()]) else 1


def check_json(path):
    payload = json.loads(pathlib.Path(path).read_text(encoding="utf-8"))
    if "certificate" in payload:
        cert = MorseReductionCertificate.from_dict(payload["certificate"])
        verify_certificate(cert)
        print(json.dumps({"valid": True, "mode": "certificate", "critical_generators": list(cert.critical_generators)}))
        return 0
    if "source" in payload and "matching" in payload:
        source = FiniteChainComplex.from_dict(payload["source"])
        matching = tuple(MatchingPair.from_obj(p) for p in payload["matching"])
        cert = morse_reduce(source, matching)
        print(json.dumps({"valid": True, "mode": "reduce-spec", "certificate": cert.to_dict()}, sort_keys=True))
        return 0
    raise ChainComplexError("JSON must contain either certificate or source+matching")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--self-test", action="store_true")
    group.add_argument("--demo-unit", action="store_true")
    group.add_argument("--demo-cyclic", action="store_true")
    group.add_argument("--demo-nonunit", action="store_true")
    group.add_argument("--check", metavar="JSON_PATH")
    args = parser.parse_args(argv)

    if args.demo_unit:
        demo_unit()
        return 0
    if args.demo_cyclic:
        return demo_cyclic()
    if args.demo_nonunit:
        return demo_nonunit()
    if args.check:
        return check_json(args.check)
    # No flag defaults to the required deterministic regression; --self-test is
    # an explicit synonym convenient for taskbook replay.
    _, mismatches = run_suite(verbose=True)
    return 1 if mismatches else 0


if __name__ == "__main__":
    raise SystemExit(main())
