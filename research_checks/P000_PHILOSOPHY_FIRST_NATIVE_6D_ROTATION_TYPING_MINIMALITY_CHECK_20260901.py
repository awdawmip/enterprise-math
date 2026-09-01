from itertools import product

ZERO = (0, 0, 0, 0, 0, 0)
X = tuple(product((0, 1), repeat=6))


def obs(x):
    return x[:3]


def rot_equivalence(x):
    # Finite active Full-Cell equivalence witness: cyclic coordinate relabel/action.
    return x[1:] + x[:1]


def rot_update_zero_preserving(x):
    # Genuine noninvertible state-update witness; no classical rotation semantics imported.
    return (0,) + x[1:]


def rot_update_nonzero_generating(x):
    # P000-compatible extension witness only, not a current derived law.
    return (x[0] ^ 1,) + x[1:]


def image_size(f):
    return len({f(x) for x in X})


def is_injective(f):
    return image_size(f) == len(X)


def iter_map(f, x, n):
    for _ in range(n):
        x = f(x)
    return x


def main():
    assert len(X) == 64
    assert len({obs(x) for x in X}) == 8

    # Completion A: equivalence/automorphism-like semantics.
    assert image_size(rot_equivalence) == 64
    assert is_injective(rot_equivalence)
    assert rot_equivalence(ZERO) == ZERO
    assert all(iter_map(rot_equivalence, x, 6) == x for x in X)

    # Completion B: same Full-Cell carrier and observation, different rotation typing.
    assert image_size(rot_update_zero_preserving) == 32
    assert not is_injective(rot_update_zero_preserving)
    assert rot_update_zero_preserving(ZERO) == ZERO
    assert all(
        rot_update_zero_preserving(rot_update_zero_preserving(x))
        == rot_update_zero_preserving(x)
        for x in X
    )

    # Extension witness C: outside Q23's zero-preserving forward grammar.
    assert image_size(rot_update_nonzero_generating) == 64
    assert is_injective(rot_update_nonzero_generating)
    assert rot_update_nonzero_generating(ZERO) == (1, 0, 0, 0, 0, 0)
    assert all(
        rot_update_nonzero_generating(rot_update_nonzero_generating(x)) == x
        for x in X
    )

    # Observation-boundary witness: Full-Cell equivalence need not descend to the slice.
    x = (0, 0, 0, 0, 0, 0)
    y = (0, 0, 0, 1, 0, 0)
    assert obs(x) == obs(y)
    assert obs(rot_equivalence(x)) != obs(rot_equivalence(y))

    # Primitive-relation action is independent data from state action.
    parity_even = {x for x in X if sum(x) % 2 == 0}
    first_zero = {x for x in X if x[0] == 0}
    assert parity_even != first_zero
    assert {rot_equivalence(x) for x in parity_even} == parity_even

    print(
        "PASS P000_Q26_ROTATION_TYPING "
        "states=64 slice_states=8 "
        "equivalence_image=64 equivalence_injective=1 equivalence_zero=1 "
        "update_image=32 update_injective=0 update_zero=1 "
        "nonzero_candidate_image=64 nonzero_candidate_injective=1 nonzero_candidate_zero=0 "
        "slice_descent_counterexample=1 relation_action_independence=1 "
        "terminal=P000_ROTATION_TYPING_UNDERDETERMINED_WITH_EXACT_MISSING_DATA"
    )


if __name__ == "__main__":
    main()
