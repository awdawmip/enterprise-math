#!/usr/bin/env python3
"""Exact finite checker for P000 Philosophy-First Q29.

This checker certifies only the finite matched-countermodel claims stated in the
Q29 return.  It does not assert that native P000 Full-Cell coordinates are
binary and it does not import classical/continuous rotation semantics.
"""

from itertools import product

X = tuple(product((0, 1), repeat=6))
ZERO = (0, 0, 0, 0, 0, 0)
Y = tuple(product((0, 1), repeat=3))

# Shared finite comparison token monoid T=<r | r^7=r>.
# Normal forms are e=r^0 and r^1,...,r^6.
TOKENS = tuple(range(7))

def token_mul(a, b):
    n = a + b
    if n == 0:
        return 0
    return 1 + ((n - 1) % 6)

def token_pow(n):
    if n == 0:
        return 0
    return 1 + ((n - 1) % 6)

def E2_gen(x):
    # Order-2 active equivalence: swap 1<->2 and 4<->5.
    return (x[1], x[0], x[2], x[4], x[3], x[5])

def E3_gen(x):
    # Order-3 active equivalence: cycle each three-coordinate block.
    return (x[1], x[2], x[0], x[4], x[5], x[3])

def U_gen(x):
    # Genuine noninvertible update: overwrite the first primitive by zero.
    return (0, x[1], x[2], x[3], x[4], x[5])

def ID(x):
    return x

def apply_power(g, n, x):
    y = x
    for _ in range(n):
        y = g(y)
    return y

INDEX = {x: i for i, x in enumerate(X)}

def map_tuple(g, token):
    return tuple(apply_power(g, token, x) for x in X)

def compose_maps(a, b):
    # a after b
    return tuple(a[INDEX[y]] for y in b)

def map_rank(m):
    return len(set(m))

def map_fixed(m):
    return sum(1 for x, y in zip(X, m) if x == y)

def representation(g):
    return tuple(map_tuple(g, t) for t in TOKENS)

def representation_image_size(rho):
    unique = []
    for m in rho:
        if m not in unique:
            unique.append(m)
    return len(unique)

def assert_monoid():
    assert all(token_mul(0, a) == a == token_mul(a, 0) for a in TOKENS)
    assert all(
        token_mul(token_mul(a, b), c) == token_mul(a, token_mul(b, c))
        for a in TOKENS for b in TOKENS for c in TOKENS
    )
    assert token_pow(7) == 1
    assert token_pow(13) == 1

def assert_representation(rho):
    for a in TOKENS:
        for b in TOKENS:
            assert compose_maps(rho[a], rho[b]) == rho[token_mul(a, b)]

def O0(x):
    return (x[0], x[1], x[2])

def O1(x):
    # Alternate presentation frame for the passive-frame candidate.
    return (x[1], x[0], x[2])

def fibre_constancy(state_map, source_obs, target_obs):
    seen = {}
    for x in X:
        key = source_obs(x)
        value = target_obs(state_map[INDEX[x]])
        if key in seen and seen[key] != value:
            return False
        seen[key] = value
    return len(seen) == len(Y)

def all_token_descent(rho):
    return all(fibre_constancy(rho[t], O0, O0) for t in TOKENS)

def frame_map_tuple(token):
    # Generator flips two presentation labels. Since flip^7=flip, this is a T-action.
    return tuple(((f + token) % 2) for f in (0, 1))

def compose_frame_maps(a, b):
    return tuple(a[v] for v in b)

def assert_frame_representation():
    rho = tuple(frame_map_tuple(t) for t in TOKENS)
    for a in TOKENS:
        for b in TOKENS:
            assert compose_frame_maps(rho[a], rho[b]) == rho[token_mul(a, b)]
    return rho

def frame_all_token_descent():
    state_rho = representation(ID)
    for t in TOKENS:
        target_obs = O1 if (t % 2) else O0
        if not fibre_constancy(state_rho[t], O0, target_obs):
            return False
    return True

def zero_preserved(rho):
    z = INDEX[ZERO]
    return all(m[z] == ZERO for m in rho)

def main():
    assert_monoid()

    state_generators = {
        "E2": E2_gen,
        "E3": E3_gen,
        "U": U_gen,
        "F": ID,
    }
    rho = {name: representation(g) for name, g in state_generators.items()}
    for value in rho.values():
        assert_representation(value)

    frame_rho = assert_frame_representation()

    # Primitive/relation-action audit:
    # E2/E3 reindex six Boolean primitive coordinates exactly as their state maps;
    # U explicitly updates primitive 1 to 0 and leaves 2..6 fixed;
    # F leaves ontic primitives fixed and acts only on the presentation label.
    assert E2_gen((1,0,1,0,1,0)) == (0,1,1,1,0,0)
    assert E3_gen((1,0,0,0,1,0)) == (0,0,1,1,0,0)
    assert U_gen((1,1,0,1,0,1)) == (0,1,0,1,0,1)
    assert ID((1,0,1,0,1,0)) == (1,0,1,0,1,0)

    # Q23 zero-support boundary: every state action in every candidate fixes zero.
    assert all(zero_preserved(value) for value in rho.values())

    # Observation descent/fibre constancy.
    assert all_token_descent(rho["E2"])
    assert all_token_descent(rho["E3"])
    assert all_token_descent(rho["U"])
    assert frame_all_token_descent()

    state_image = {name: representation_image_size(value) for name, value in rho.items()}
    gen_rank = {name: map_rank(value[1]) for name, value in rho.items()}
    gen_fixed = {name: map_fixed(value[1]) for name, value in rho.items()}
    frame_image = len(set(frame_rho))

    assert state_image == {"E2": 2, "E3": 3, "U": 2, "F": 1}
    assert gen_rank == {"E2": 64, "E3": 64, "U": 32, "F": 64}
    assert gen_fixed == {"E2": 16, "E3": 4, "U": 32, "F": 64}
    assert frame_image == 2

    # Typed-law equivalence preserves the cardinality of the conjugacy image and
    # the rank multiset of its state maps. Hence E2 and E3 cannot be equivalent:
    # their state-representation images have cardinalities 2 and 3.
    assert state_image["E2"] != state_image["E3"]

    # The four candidates are pairwise separated by the exact signature below.
    # For F, the final coordinate records nontrivial presentation-only action.
    signatures = {
        "E2": (state_image["E2"], gen_rank["E2"], 1),
        "E3": (state_image["E3"], gen_rank["E3"], 1),
        "U":  (state_image["U"],  gen_rank["U"],  1),
        "F":  (state_image["F"],  gen_rank["F"],  frame_image),
    }
    assert len(set(signatures.values())) == 4

    print(
        "PASS P000_Q29_ROTATION_LAW_DISCRIMINATION "
        "tokens=7 states=64 candidates=4 "
        "E2_state_image=2 E3_state_image=3 U_state_image=2 F_state_image=1 "
        "E2_rank=64 E3_rank=64 U_rank=32 F_rank=64 "
        "E2_fixed=16 E3_fixed=4 U_fixed=32 F_fixed=64 "
        "frame_image=2 all_zero_preserving=1 all_slice_fibre_constant=1 "
        "pairwise_typed_signatures_distinct=1 "
        "terminal=NO_CANONICAL_ROTATION_LAW_SELECTED_BY_CURRENT_P000"
    )

if __name__ == "__main__":
    main()
