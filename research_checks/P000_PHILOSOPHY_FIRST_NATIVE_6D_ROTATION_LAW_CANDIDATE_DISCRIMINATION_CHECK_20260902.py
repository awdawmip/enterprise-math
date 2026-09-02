#!/usr/bin/env python3
"""Exact finite checker for P000 Q29 rotation-law candidate discrimination.

The binary carrier is a finite logical countermodel only, following accepted Q26.
It is not promoted to native P000 ontology.
"""
from itertools import product

X = tuple(product((0, 1), repeat=6))
ZERO = (0, 0, 0, 0, 0, 0)
ID = {x: x for x in X}
EVEN = {x for x in X if sum(x) % 2 == 0}
ZERO_SET = {ZERO}


def obs0(x):
    return x[:3]


def perm_map(p):
    return {x: tuple(x[p[i]] for i in range(6)) for x in X}


def compose(f, g):
    """f after g."""
    return {x: f[g[x]] for x in X}


def powers(gen, n):
    out = []
    cur = ID
    for _ in range(n):
        out.append(cur)
        cur = compose(gen, cur)
    return out


def map_key(m):
    return tuple(m[x] for x in X)


def image_size(m):
    return len(set(m.values()))


def fixed_count(m):
    return sum(1 for x in X if m[x] == x)


def is_bijection(m):
    return image_size(m) == len(X)


def preserves_set(m, subset):
    return {m[x] for x in subset} == set(subset)


def fibre_descent(src_obs, tgt_obs, m):
    seen = {}
    for x in X:
        a = src_obs(x)
        b = tgt_obs(m[x])
        if a in seen and seen[a] != b:
            return False
        seen[a] = b
    return True


def first_failure_witness(src_obs, tgt_obs, m):
    buckets = {}
    for x in X:
        a = src_obs(x)
        b = tgt_obs(m[x])
        if a in buckets:
            y, by = buckets[a]
            if by != b:
                return y, x, by, b
        else:
            buckets[a] = (x, b)
    return None


def direct_image(m, subset):
    return {m[x] for x in subset}


# Matched structure-preserving equivalence candidates.
# Same carrier, same C6 token monoid, same observation, same primitive package.
# E2 generator swaps hidden coordinates 4 and 5.
# E3 generator cycles hidden coordinates 4 -> 5 -> 6 -> 4.
G2 = perm_map((0, 1, 2, 4, 3, 5))
G3 = perm_map((0, 1, 2, 5, 3, 4))
RHO2 = powers(G2, 6)
RHO3 = powers(G3, 6)

for rho in (RHO2, RHO3):
    assert map_key(rho[0]) == map_key(ID)
    for a in range(6):
        for b in range(6):
            assert map_key(rho[(a + b) % 6]) == map_key(compose(rho[a], rho[b]))
    for m in rho:
        assert is_bijection(m)
        assert m[ZERO] == ZERO
        assert preserves_set(m, EVEN)
        assert preserves_set(m, ZERO_SET)
        assert fibre_descent(obs0, obs0, m)

action_image_E2 = {map_key(m) for m in RHO2}
action_image_E3 = {map_key(m) for m in RHO3}
assert len(action_image_E2) == 2
assert len(action_image_E3) == 3
assert fixed_count(G2) == 32
assert fixed_count(G3) == 16

# Typed-law equivalence permits a C6-token automorphism and state conjugacy.
# The cardinality of the image of the state-action representation is invariant
# under both operations, so E2 and E3 cannot be equivalent.
C6_UNITS = (1, 5)
for u in C6_UNITS:
    precomposed_E2 = {map_key(RHO2[(u * k) % 6]) for k in range(6)}
    assert len(precomposed_E2) == 2
assert len(action_image_E3) == 3

# Genuine Full-Cell state/relation update candidate.
# Object M0 has unary primitive package (ZERO, EVEN); applying e sends it to
# the direct-image package on M1. E^2=E, so the typed update closes on M1.
E = {x: (0, x[1], x[2], x[3], x[4], x[5]) for x in X}
assert image_size(E) == 32
assert not is_bijection(E)
assert map_key(compose(E, E)) == map_key(E)
assert E[ZERO] == ZERO
assert fibre_descent(obs0, obs0, E)

RELATIONS_M0 = {
    "ZERO": ZERO_SET,
    "EVEN": EVEN,
    "FULL": set(X),
}
for subset in RELATIONS_M0.values():
    once = direct_image(E, subset)
    twice = direct_image(E, once)
    assert twice == once

# Passive frame/presentation candidate.
# Ontic state action is identity. A token a in C6 changes frame k to k+a.
# The frame-relative observation changes with k; descent is tested, not assumed.
def frame_action(a, k):
    return (k + a) % 6


def obs_frame(k):
    return lambda x: (x[k % 6], x[(k + 1) % 6], x[(k + 2) % 6])


for a in range(6):
    assert ID[ZERO] == ZERO
    for b in range(6):
        for k in range(6):
            assert frame_action(a, frame_action(b, k)) == frame_action((a + b) % 6, k)

passive_descent = fibre_descent(obs_frame(0), obs_frame(1), ID)
assert passive_descent is False
passive_witness = first_failure_witness(obs_frame(0), obs_frame(1), ID)
assert passive_witness == (
    (0, 0, 0, 0, 0, 0),
    (0, 0, 0, 1, 0, 0),
    (0, 0, 0),
    (0, 0, 1),
)

# Semantic inequivalence certificate.
# Under typed-law isomorphism (token-monoid isomorphism + Full-Cell/model
# isomorphism intertwining state actions, primitive actions and observations),
# the listed signature components are invariants.
sig_E2 = (6, 2, True, fixed_count(G2), True, True)
sig_E3 = (6, 3, True, fixed_count(G3), True, True)
sig_U = (2, 2, False, fixed_count(E), True, True)
sig_F = (6, 1, True, len(X), True, False)
assert len({sig_E2, sig_E3, sig_U, sig_F}) == 4

print(
    "PASS P000_Q29_ROTATION_CANDIDATE_DISCRIMINATION "
    f"states={len(X)} "
    f"E2_action_image=2 E2_fixed={fixed_count(G2)} E2_slice_descent=1 "
    f"E3_action_image=3 E3_fixed={fixed_count(G3)} E3_slice_descent=1 "
    f"update_image={image_size(E)} update_injective=0 update_idempotent=1 "
    "update_slice_descent=1 "
    "passive_state_action_image=1 passive_slice_descent=0 "
    "all_zero_preserving=1 matched_equivalence_countermodels=1 "
    "terminal=NO_CANONICAL_ROTATION_LAW_SELECTED_BY_CURRENT_P000"
)
