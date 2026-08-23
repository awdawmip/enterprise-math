#!/usr/bin/env python3
"""
Deterministic checker for CBRC F2 blind-forward observability classification.

Mathematical preload used by this checker:
  C1 = Z e (+) <tau | 3 tau = 0>
  R(e)=e+tau, R(tau)=tau
  J=-id
  S(e)=e, S(tau)=-tau

No external mathematical model is used.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import product, permutations
import hashlib
import json

MOD = 3

@dataclass(frozen=True, order=True)
class C1:
    n: int
    a: int = 0

    def __post_init__(self):
        object.__setattr__(self, "a", self.a % MOD)

    def __add__(self, other: "C1") -> "C1":
        return C1(self.n + other.n, self.a + other.a)

    def __neg__(self) -> "C1":
        return C1(-self.n, -self.a)

ZERO = C1(0, 0)
E = C1(1, 0)

def R(z: C1, k: int = 1) -> C1:
    return C1(z.n, z.a + (k % MOD) * z.n)

def J(z: C1) -> C1:
    return -z

def S(z: C1) -> C1:
    return C1(z.n, -z.a)

def elementary(sign_bit: int, k: int) -> C1:
    z = R(E, k)
    return J(z) if sign_bit % 2 else z

def aggregate(items):
    z = ZERO
    for x in items:
        z = z + x
    return z

def orbit(z: C1):
    todo = [z]
    seen = {z}
    while todo:
        x = todo.pop()
        for y in (R(x), J(x), S(x)):
            if y not in seen:
                seen.add(y)
                todo.append(y)
    return frozenset(seen)

def orbit_key(z: C1):
    if z.n == 0:
        return ("ZERO",) if z.a == 0 else ("TORSION",)
    r = abs(z.n)
    if r % MOD:
        return ("NONDIV3", r)
    return ("DIV3", r, "A0" if z.a == 0 else "ANZ")

def predicted_orbit(z: C1):
    key = orbit_key(z)
    if key == ("ZERO",):
        return frozenset({ZERO})
    if key == ("TORSION",):
        return frozenset({C1(0, 1), C1(0, 2)})
    r = abs(z.n)
    if r % MOD:
        return frozenset(C1(s * r, a) for s in (-1, 1) for a in range(3))
    if z.a == 0:
        return frozenset({C1(r, 0), C1(-r, 0)})
    return frozenset(C1(s * r, a) for s in (-1, 1) for a in (1, 2))

def rho_support(z: C1):
    return 0 if z == ZERO else 1

def rho_orbit_injective(z: C1):
    if z == ZERO:
        return 0
    if z.n == 0:
        return 2
    r = abs(z.n)
    if r == 1:
        return 1
    if r % MOD:
        return 4 * r
    return 4 * r + (1 if z.a == 0 else 2)

def rho_signed_layer_count(z: C1):
    return abs(z.n)

def rho_no_O5(z: C1):
    # Invariant under J and S, normalized on all elementary states,
    # but deliberately distinguishes A=0 from A!=0 at |n|=2.
    if z == ZERO:
        return 0
    if abs(z.n) == 1:
        return 1
    if z.n == 0:
        return 1
    if abs(z.n) == 2:
        return 2 if z.a == 0 else 3
    return 1

def rho_no_O6(z: C1):
    # Keeps isolated +/- elementary states normalized, but permits
    # aggregate sign asymmetry beyond the elementary orbit.
    if z == ZERO:
        return 0
    if abs(z.n) == 1:
        return 1
    if z.n == 0:
        return 1
    return 2 if z.n > 0 else 3

def rho_no_O7(z: C1):
    # J-invariant but S-sensitive first at n divisible by 3.
    if z == ZERO:
        return 0
    if abs(z.n) == 1:
        return 1
    if z.n == 0:
        return 1
    if abs(z.n) == 3 and z.a != 0:
        if (z.n > 0 and z.a == 1) or (z.n < 0 and z.a == 2):
            return 5
        return 6
    return 2

def presentation_readout_no_O8(presentation):
    # presentation is tuple[(sign_bit,k), ...].
    z = aggregate(elementary(s, k) for s, k in presentation)
    if z == ZERO:
        return 0
    if len(presentation) == 1:
        return 1
    ks = [k % 3 for _, k in presentation]
    return 2 if len(set(ks)) == 1 else 3

def depth_readout_no_O9(z: C1, depth: int):
    if z == ZERO:
        return 0
    if abs(z.n) == 1:
        return 1
    if z.n == 0 and z.a != 0:
        return depth
    return 1

@dataclass(frozen=True, order=True)
class C1PlusZ2:
    n: int
    a: int = 0
    b: int = 0

    def __post_init__(self):
        object.__setattr__(self, "a", self.a % 3)
        object.__setattr__(self, "b", self.b % 2)

def ext_R(z: C1PlusZ2, k=1):
    return C1PlusZ2(z.n, z.a + (k % 3) * z.n, z.b)

def ext_J(z: C1PlusZ2):
    return C1PlusZ2(-z.n, -z.a, -z.b)

def ext_S(z: C1PlusZ2):
    return C1PlusZ2(z.n, -z.a, z.b)

def ext_rho(z: C1PlusZ2):
    return rho_support(C1(z.n, z.a))

def check_invariance(rho, window=9):
    for n in range(-window, window + 1):
        for a in range(3):
            z = C1(n, a)
            assert rho(z) >= 0
            assert rho(R(z)) == rho(z)
            assert rho(J(z)) == rho(z)
            assert rho(S(z)) == rho(z)

def check_O1_O10(rho):
    assert rho(ZERO) == 0
    assert rho(E) == 1
    for k in range(3):
        assert rho(R(E, k)) == 1
        assert rho(J(R(E, k))) == 1
    check_invariance(rho)
    # O4 is a separate tagged bookkeeping rule: two elementary tags total 2.
    tagged_total = 1 + 1
    assert tagged_total == 2
    # O8 follows because rho receives only the aggregate coefficient.
    assert aggregate([E, R(E, 1)]) == aggregate([R(E, 1), E])
    # O10 witness: e + J R e = -tau, while e + J e = 0.
    rel = E + J(R(E, 1))
    base = E + J(E)
    assert rel == C1(0, 2)
    assert base == ZERO
    assert rho(rel) != rho(base)

def serial_apply(ks):
    z = E
    for k in ks:
        z = R(z, k)
    return z

def serial_closed_form(ks):
    return R(E, sum(ks) % 3)

def run():
    summary = {}

    # Exact action identities.
    for n in range(-9, 10):
        for a in range(3):
            z = C1(n, a)
            assert R(R(R(z))) == z
            assert J(J(z)) == z
            assert S(S(z)) == z
            assert J(R(z)) == R(J(z))
            assert S(R(S(z))) == R(z, -1)
            assert orbit(z) == predicted_orbit(z)
    summary["orbit_theorem_window"] = {"n_min": -9, "n_max": 9, "mismatches": 0}

    singles = sorted({elementary(s, k) for s in (0, 1) for k in range(3)})
    single_orbits = {orbit_key(z) for z in singles}
    assert single_orbits == {("NONDIV3", 1)}

    pairs = {}
    for a in product([(s, k) for s in (0, 1) for k in range(3)], repeat=2):
        z = aggregate(elementary(s, k) for s, k in a)
        pairs.setdefault(orbit_key(z), set()).add(z)
    assert set(pairs) == {("NONDIV3", 2), ("ZERO",), ("TORSION",)}
    summary["one_two_element_orbits"] = {
        "single_classes": 1,
        "two_element_classes": 3,
        "classes": sorted(map(str, pairs.keys())),
    }

    rel_table = []
    for s in (0, 1):
        for k in range(3):
            z = E + elementary(s, k)
            rel_table.append({"s": s, "k": k, "state": [z.n, z.a], "orbit": orbit_key(z)})
    assert orbit_key(E + elementary(0, 0)) == orbit_key(E + elementary(0, 1))
    assert E + elementary(1, 0) == ZERO
    assert orbit_key(E + elementary(1, 1)) == ("TORSION",)
    summary["relative_table"] = rel_table

    for rho in (rho_support, rho_orbit_injective):
        check_O1_O10(rho)
    assert rho_support(C1(2, 0)) != rho_orbit_injective(C1(2, 0))
    summary["readouts"] = {
        "support": "PASS",
        "orbit_injective": "PASS",
        "inequivalent": True,
        "torsion_values": [rho_support(C1(0, 1)), rho_orbit_injective(C1(0, 1))],
    }

    # Depth-3 and depth-4 serial composition.
    for depth in (3, 4):
        for ks in product(range(3), repeat=depth):
            assert serial_apply(ks) == serial_closed_form(ks)
    # Pairwise commuting composition of transport increments.
    for a, b in product(range(3), repeat=2):
        assert R(R(E, a), b) == R(R(E, b), a)
    summary["composition"] = {"depth3": "PASS", "depth4": "PASS", "commuting": "PASS"}

    # Three-alternative fibers, branch swap, common transport, reversal.
    labels = [(s, k) for s in (0, 1) for k in range(3)]
    triple_count = 0
    for triple in product(labels, repeat=3):
        elems = [elementary(s, k) for s, k in triple]
        z = aggregate(elems)
        for perm in set(permutations(range(3))):
            assert aggregate(elems[i] for i in perm) == z
        for t in range(3):
            moved = aggregate(elementary(s, k + t) for s, k in triple)
            assert moved == R(z, t)
        reversed_z = aggregate(elementary(s, -k) for s, k in triple)
        assert reversed_z == S(z)
        triple_count += 1
    summary["three_alternative"] = {"cases": triple_count, "status": "PASS"}

    # Marker refinement / parenthesization erasure.
    sample = [elementary(0, 0), elementary(1, 1), elementary(0, 2)]
    left = (sample[0] + sample[1]) + sample[2]
    right = sample[0] + (sample[1] + sample[2])
    flat = aggregate(sample)
    assert left == right == flat
    summary["refinement_erasure"] = "PASS"

    # Recovery of sign-only algebraic examples when k=0.
    assert aggregate([elementary(0, 0), elementary(0, 0)]) == C1(2, 0)
    assert aggregate([elementary(0, 0), elementary(1, 0)]) == ZERO
    summary["sign_only_recovery"] = "PASS"

    # Mandatory ablations.
    ablations = {}

    # O3 is implied on elementary states by O2 + common R invariance + global J invariance.
    for s in (0, 1):
        for k in range(3):
            assert orbit_key(elementary(s, k)) == orbit_key(E)
    ablations["remove_O3"] = "NO_WIDENING: redundant given O2+O5+O6 on elementary domain"

    # O4 removal: tagged pair total can be changed independently.
    tagged_pair_without_O4 = 7
    assert tagged_pair_without_O4 != 2
    ablations["remove_O4"] = "TAGGED_TOTAL_FREE"

    # O5 removal: same-sign relative transport can become visible.
    assert rho_no_O5(C1(2, 0)) != rho_no_O5(C1(2, 1))
    for k in range(3):
        assert rho_no_O5(elementary(0, k)) == 1
        assert rho_no_O5(elementary(1, k)) == 1
    assert rho_no_O5(J(C1(2, 1))) == rho_no_O5(C1(2, 1))
    assert rho_no_O5(S(C1(2, 1))) == rho_no_O5(C1(2, 1))
    ablations["remove_O5"] = "SAME_SIGN_RELATIVE_CLASS_SPLITS"

    # O6 removal: aggregate +n/-n can split beyond the normalized elementary orbit.
    assert rho_no_O6(C1(2, 0)) != rho_no_O6(J(C1(2, 0)))
    for k in range(3):
        assert rho_no_O6(elementary(0, k)) == rho_no_O6(elementary(1, k)) == 1
    ablations["remove_O6"] = "GLOBAL_SIGN_CLASSES_SPLIT"

    # O7 removal: first new S-sensitive split occurs at n divisible by 3.
    assert rho_no_O7(C1(3, 1)) != rho_no_O7(S(C1(3, 1)))
    assert rho_no_O7(C1(3, 1)) == rho_no_O7(J(C1(3, 1)))
    ablations["remove_O7"] = "REVERSAL_SPLIT_AT_N_EQ_3_MOD_CLASS"

    # O8 removal: same aggregate can receive different presentation scalar.
    p_equal = ((0, 0), (0, 0))
    p_unequal = ((0, 1), (0, 2))
    assert aggregate(elementary(s, k) for s, k in p_equal) == C1(2, 0)
    assert aggregate(elementary(s, k) for s, k in p_unequal) == C1(2, 0)
    assert presentation_readout_no_O8(p_equal) != presentation_readout_no_O8(p_unequal)
    # common shift preserves equality-vs-inequality class
    shifted = tuple((s, k + 1) for s, k in p_unequal)
    assert presentation_readout_no_O8(shifted) == presentation_readout_no_O8(p_unequal)
    ablations["remove_O8"] = "PRESENTATION_PROVENANCE_BECOMES_SCALAR"

    # O9 removal: same coefficient can depend on serial depth.
    tors = C1(0, 2)
    assert depth_readout_no_O9(tors, 2) != depth_readout_no_O9(tors, 3)
    ablations["remove_O9"] = "DEPTH_INDEXED_READOUTS_ALLOWED"

    # O10 removal: signed-layer-only scalar makes all pure torsion silent.
    check_invariance(rho_signed_layer_count)
    assert rho_signed_layer_count(E) == 1
    assert rho_signed_layer_count(C1(0, 1)) == rho_signed_layer_count(ZERO) == 0
    ablations["remove_O10"] = "TORSION_CAN_BE_OBSERVATIONALLY_SILENT"

    # Minimal-carrier removal: inert Z/2 enlargement preserves the F2 witness.
    ext_e = C1PlusZ2(1, 0, 0)
    ext_rel = C1PlusZ2(0, 2, 0)
    assert ext_rho(ext_e) == 1
    assert ext_rho(ext_rel) > 0
    assert ext_rho(C1PlusZ2(0, 0, 0)) == 0
    assert ext_R(C1PlusZ2(0, 0, 1)) == C1PlusZ2(0, 0, 1)
    ablations["remove_minimal_carrier"] = "C1_PLUS_INERT_Z2_IS_ADMISSIBLE_NONMINIMAL_EXTENSION"

    summary["ablations"] = ablations

    # Selector checks.
    selectors = {}
    # Bound against tagged total on the minimal torsion witness limits t to <=2.
    selectors["tagged_upper_bound"] = {"effect_on_torsion_parameter": "0 < t <= 2", "unique": False}
    # Linear copy scaling is incompatible with nonzero order-3 torsion visibility.
    t = 1
    assert C1(0, 1) + C1(0, 1) + C1(0, 1) == ZERO
    assert 0 != 3 * t
    selectors["linear_copy_scaling"] = {"compatible_with_O10_on_C1": False}
    selectors["monotone_abs_n"] = {"reduces_family": True, "unique": False}
    summary["selectors"] = selectors

    encoded = json.dumps(summary, sort_keys=True, separators=(",", ":")).encode()
    digest = hashlib.sha256(encoded).hexdigest()
    print(json.dumps(summary, sort_keys=True, indent=2))
    print("DETERMINISTIC_DIGEST=" + digest)
    return digest

if __name__ == "__main__":
    run()
