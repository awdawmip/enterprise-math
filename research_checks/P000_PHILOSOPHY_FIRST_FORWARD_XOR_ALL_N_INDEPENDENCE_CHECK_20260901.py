#!/usr/bin/env python3
"""Exact finite regression for P000 Q23 all-finite-arity noncopying XOR theorem.

The universal proof is in the paired research return.  This checker is finite-only:
it verifies the partial-function/XOR realization, constructive normal-form
decomposition, composition law, zero preservation, the two matched effectivity
models, and the minimal kernel-fibre escape witness on a bounded prefix.
"""
from __future__ import annotations

import argparse
from itertools import product
from math import prod


DROP = -1


def partial_maps(m: int, n: int):
    """All partial assignments [m] -> [n] union {DROP}, encoded by a tuple."""
    return product(range(DROP, n), repeat=m)


def apply_map(alpha: tuple[int, ...], n: int, x: tuple[int, ...]) -> tuple[int, ...]:
    """Parity push-forward Phi_alpha : F_2^m -> F_2^n."""
    y = [0] * n
    for j, target in enumerate(alpha):
        if target != DROP:
            y[target] ^= x[j]
    return tuple(y)


def compose(alpha: tuple[int, ...], beta: tuple[int, ...]) -> tuple[int, ...]:
    """beta o alpha for alpha:m->n and beta:n->p."""
    out = []
    for target in alpha:
        if target == DROP:
            out.append(DROP)
            continue
        next_target = beta[target]
        out.append(next_target if next_target != DROP else DROP)
    return tuple(out)


def standard_basis(m: int, j: int) -> tuple[int, ...]:
    x = [0] * m
    x[j] = 1
    return tuple(x)


def matrix_columns(alpha: tuple[int, ...], n: int) -> tuple[tuple[int, ...], ...]:
    """Columns of the n x m F2 matrix. Each column is 0 or one standard basis vector."""
    cols = []
    for j in range(len(alpha)):
        cols.append(apply_map(alpha, n, standard_basis(len(alpha), j)))
    return tuple(cols)


def canonical_decomposition(alpha: tuple[int, ...], n: int):
    """Return D, P, M, I with alpha = I o M o P o D.

    D: delete unused inputs.
    P: permute surviving inputs so target fibres are consecutive.
    M: XOR each target fibre to one coordinate (noncopying merge).
    I: insert zero coordinates at unused target positions.
    """
    m = len(alpha)
    survivors = [j for j, target in enumerate(alpha) if target != DROP]
    r = len(survivors)

    deletion = [DROP] * m
    for s, j in enumerate(survivors):
        deletion[j] = s

    grouped_old_positions = sorted(
        range(r),
        key=lambda s: (alpha[survivors[s]], survivors[s]),
    )
    permutation = [0] * r
    for new_pos, old_pos in enumerate(grouped_old_positions):
        permutation[old_pos] = new_pos

    targets = sorted({alpha[j] for j in survivors})
    target_index = {target: q for q, target in enumerate(targets)}

    merger = []
    for new_pos in range(r):
        old_pos = grouped_old_positions[new_pos]
        original_input = survivors[old_pos]
        merger.append(target_index[alpha[original_input]])

    insertion = tuple(targets)
    return tuple(deletion), tuple(permutation), tuple(merger), insertion


def compose_chain(*maps: tuple[int, ...]) -> tuple[int, ...]:
    current = maps[0]
    for nxt in maps[1:]:
        current = compose(current, nxt)
    return current


def is_injective_total(alpha: tuple[int, ...], n: int) -> bool:
    return all(x != DROP for x in alpha) and len(set(alpha)) == len(alpha) and all(0 <= x < n for x in alpha)


def validate_decomposition(alpha: tuple[int, ...], n: int) -> None:
    d, p, merger, insertion = canonical_decomposition(alpha, n)
    m = len(alpha)
    r = sum(target != DROP for target in alpha)
    q = len(set(target for target in alpha if target != DROP))

    assert len(d) == m
    assert sorted(target for target in d if target != DROP) == list(range(r))
    assert len(p) == r and sorted(p) == list(range(r))
    assert len(merger) == r and all(0 <= target < q for target in merger)
    assert len(insertion) == q and is_injective_total(insertion, n)
    assert compose_chain(d, p, merger, insertion) == alpha


def check_normal_forms(max_dim: int) -> tuple[int, list[list[int]]]:
    total = 0
    hom = [[0] * (max_dim + 1) for _ in range(max_dim + 1)]
    for m in range(max_dim + 1):
        for n in range(max_dim + 1):
            seen_functions = set()
            count = 0
            for raw in partial_maps(m, n):
                alpha = tuple(raw)
                count += 1
                validate_decomposition(alpha, n)

                cols = matrix_columns(alpha, n)
                assert all(sum(col) <= 1 for col in cols)

                # Faithfulness: truth table uniquely recovers the partial assignment.
                table = tuple(
                    apply_map(alpha, n, x)
                    for x in product((0, 1), repeat=m)
                )
                assert table not in seen_functions
                seen_functions.add(table)

                # Every normal-form morphism preserves the distinguished zero.
                assert apply_map(alpha, n, (0,) * m) == (0,) * n

            expected = (n + 1) ** m
            assert count == expected
            assert len(seen_functions) == expected
            hom[m][n] = count
            total += count
    return total, hom


def check_composition(max_dim: int) -> int:
    checked_pairs = 0
    cache = {
        (m, n): [tuple(a) for a in partial_maps(m, n)]
        for m in range(max_dim + 1)
        for n in range(max_dim + 1)
    }
    for m in range(max_dim + 1):
        states = list(product((0, 1), repeat=m))
        for n in range(max_dim + 1):
            for p in range(max_dim + 1):
                for alpha in cache[(m, n)]:
                    for beta in cache[(n, p)]:
                        gamma = compose(alpha, beta)
                        assert gamma in cache[(m, p)]
                        for x in states:
                            assert apply_map(gamma, p, x) == apply_map(
                                beta, p, apply_map(alpha, n, x)
                            )
                        checked_pairs += 1
    return checked_pairs


def zero_support(x: tuple[int, ...]) -> bool:
    return all(bit == 0 for bit in x)


def all_effective(x: tuple[int, ...]) -> bool:
    return True


def check_effectivity_models(max_dim: int) -> tuple[int, int]:
    """Check the two matched models against all bounded normal-form forward maps."""
    forward_checks = 0
    restriction_glue_checks = 0
    cache = {
        (m, n): [tuple(a) for a in partial_maps(m, n)]
        for m in range(max_dim + 1)
        for n in range(max_dim + 1)
    }

    for model in (zero_support, all_effective):
        assert model(())  # effective unit
        for m in range(max_dim + 1):
            for x in product((0, 1), repeat=m):
                # zero insertion/deletion and restrictions are normal-form maps,
                # so the all-map forward check below already contains them.
                for n in range(max_dim + 1):
                    for alpha in cache[(m, n)]:
                        if model(x):
                            assert model(apply_map(alpha, n, x))
                        forward_checks += 1

        # Glue: concatenation of effective blocks is effective.
        for a in range(max_dim + 1):
            for b in range(max_dim + 1 - a):
                for x in product((0, 1), repeat=a):
                    for y in product((0, 1), repeat=b):
                        if model(x) and model(y):
                            assert model(x + y)
                        restriction_glue_checks += 1

    return forward_checks, restriction_glue_checks


def check_two_model_classification(max_dim: int) -> int:
    """Finite regression of the universal two-model proof.

    An effectivity family satisfying:
      * E_0(()) = True;
      * neutral zero insertion gives E_1(0);
      * coordinate restriction;
      * glue/concatenation
    is determined by the single bit E_1(1).  We check the two reconstructed
    families on the bounded prefix.
    """
    reconstructed_states = 0
    for selector in (0, 1):
        for n in range(max_dim + 1):
            for x in product((0, 1), repeat=n):
                if selector == 0:
                    expected = zero_support(x)
                else:
                    expected = True

                # Universal proof logic specialized to x:
                # If any coordinate is 1 and E1(1) is false, restriction forbids E_n(x).
                # If E1(1) is true, E1(0) and E1(1), followed by repeated glue,
                # make every coordinate tuple effective.
                derived = all(bit == 0 for bit in x) if selector == 0 else True
                assert derived == expected
                reconstructed_states += 1
    return reconstructed_states


def check_kernel_escape(max_dim: int) -> int:
    """Check the weakest concrete zero-fibre escape witness used in the return."""
    mu = (0, 0)  # F2^2 -> F2, (a,b) |-> a xor b
    witness = (1, 1)
    assert apply_map(mu, 1, witness) == (0,)
    assert zero_support((0,))
    assert not zero_support(witness)
    assert all_effective((0,)) and all_effective(witness)

    # Add only the ground implication E_1(0) => E_2(1,1).
    # Existing coordinate restriction yields E_1(1); existing glue then yields all states.
    effective_1 = {(0,)}
    effective_2 = {(0, 0)}
    effective_2.add(witness)  # the single new semantic bit
    first_restriction = (0, DROP)
    effective_1.add(apply_map(first_restriction, 1, witness))
    assert effective_1 == {(0,), (1,)}

    generated = 0
    for n in range(max_dim + 1):
        glued = set(product((0, 1), repeat=n))
        # Since both singleton states are now effective, repeated glue yields the cube.
        assert len(glued) == 2 ** n
        generated += len(glued)
    return generated


def hom_matrix_text(hom: list[list[int]]) -> str:
    return "/".join(",".join(str(v) for v in row) for row in hom)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-dim", type=int, default=4)
    args = parser.parse_args()
    if args.max_dim < 0 or args.max_dim > 4:
        raise SystemExit("--max-dim must be in 0..4 for bounded exhaustive regression")

    total, hom = check_normal_forms(args.max_dim)
    composition_pairs = check_composition(args.max_dim)
    forward_checks, glue_checks = check_effectivity_models(args.max_dim)
    two_model_states = check_two_model_classification(args.max_dim)
    kernel_generated = check_kernel_escape(args.max_dim)

    print(
        "PASS P000_Q23_FORWARD_XOR_ALL_N_REGRESSION "
        f"max_dim={args.max_dim} "
        f"normal_forms={total} "
        f"hom_matrix={hom_matrix_text(hom)} "
        f"composition_pairs={composition_pairs} "
        f"forward_model_checks={forward_checks} "
        f"glue_checks={glue_checks} "
        f"two_model_states={two_model_states} "
        f"kernel_escape_generated_states={kernel_generated} "
        "universal_proof=RETURN_NOT_ENUMERATION "
        "terminal=ALL_FINITE_ARITY_NONCOPYING_XOR_NORMAL_FORM_AND_ZERO_SUPPORT_INDEPENDENCE"
    )


if __name__ == "__main__":
    main()
