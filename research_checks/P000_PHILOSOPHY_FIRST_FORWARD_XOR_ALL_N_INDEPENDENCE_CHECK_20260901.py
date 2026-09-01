#!/usr/bin/env python3
"""Regression checker for P000 Philosophy-First Q23.

The universal proof is in the research return.  This checker only verifies the
finite-dimensional regression surface up to MAX_DIM and records explicit
boundary witnesses.  It intentionally does not use finite enumeration as a
substitute for the all-finite-arity proof.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from itertools import combinations, product
from typing import Iterable

Map = tuple[int, ...]


def identity(m: int) -> Map:
    return tuple(range(1, m + 1))


def apply_map(a: Map, target_dim: int, x: tuple[int, ...]) -> tuple[int, ...]:
    assert len(a) == len(x)
    y = [0] * target_dim
    for i, target in enumerate(a):
        if target:
            assert 1 <= target <= target_dim
            y[target - 1] ^= x[i]
    return tuple(y)


def compose(a: Map, middle_dim: int, b: Map, target_dim: int) -> Map:
    """Return b ∘ a for a:C2^m->C2^middle_dim, b:C2^middle_dim->C2^target_dim."""
    assert len(b) == middle_dim
    return tuple(0 if target == 0 else b[target - 1] for target in a)


def adjacent_swap(m: int, i: int) -> Map:
    a = list(identity(m))
    a[i], a[i + 1] = a[i + 1], a[i]
    return tuple(a)


def delete_coordinate(m: int, deleted: int) -> Map:
    out: list[int] = []
    for i in range(m):
        if i == deleted:
            out.append(0)
        elif i < deleted:
            out.append(i + 1)
        else:
            out.append(i)
    return tuple(out)


def insert_zero(m: int, slot: int) -> Map:
    """C2^m -> C2^(m+1), inserting zero in the 0-based output slot."""
    return tuple(i + 1 if i < slot else i + 2 for i in range(m))


def fuse_pair(m: int, left: int, right: int) -> Map:
    """C2^m -> C2^(m-1), XORing two source coordinates into one output."""
    assert 0 <= left < right < m
    group_to_target: dict[int, int] = {}
    target = 0
    for i in range(m):
        if i == right:
            continue
        target += 1
        group_to_target[i] = target
    return tuple(
        group_to_target[left] if i == right else group_to_target[i]
        for i in range(m)
    )


def primitive_generators(max_dim: int) -> dict[tuple[int, int], set[Map]]:
    gens: dict[tuple[int, int], set[Map]] = defaultdict(set)
    for m in range(max_dim + 1):
        gens[(m, m)].add(identity(m))
        for i in range(max(0, m - 1)):
            gens[(m, m)].add(adjacent_swap(m, i))
        if m >= 1:
            for deleted in range(m):
                gens[(m, m - 1)].add(delete_coordinate(m, deleted))
            for left, right in combinations(range(m), 2):
                gens[(m, m - 1)].add(fuse_pair(m, left, right))
        if m < max_dim:
            for slot in range(m + 1):
                gens[(m, m + 1)].add(insert_zero(m, slot))
    return gens


def generated_closure(max_dim: int) -> dict[tuple[int, int], set[Map]]:
    hom = primitive_generators(max_dim)
    changed = True
    while changed:
        changed = False
        snapshot = {key: tuple(values) for key, values in hom.items()}
        for (m, n), fs in snapshot.items():
            for (n2, p), gs in snapshot.items():
                if n2 != n:
                    continue
                for f in fs:
                    for g in gs:
                        h = compose(f, n, g, p)
                        if h not in hom[(m, p)]:
                            hom[(m, p)].add(h)
                            changed = True
    return hom


def normal_forms(m: int, n: int) -> set[Map]:
    # 0 means discard; j in 1..n means send that input basis coordinate to output j.
    return set(product(range(n + 1), repeat=m))


def factor_assignment(a: Map, target_dim: int) -> tuple[tuple[Map, int], ...]:
    """Construct delete -> permute -> block-fuse -> zero-insert factorization."""
    source_dim = len(a)
    retained = [i for i, target in enumerate(a) if target != 0]
    retained_dim = len(retained)

    retained_position = {source: pos + 1 for pos, source in enumerate(retained)}
    deletion = tuple(retained_position.get(i, 0) for i in range(source_dim))

    grouped_old_positions = sorted(
        range(retained_dim),
        key=lambda old_pos: (a[retained[old_pos]], retained[old_pos]),
    )
    new_position = {old_pos: new_pos + 1 for new_pos, old_pos in enumerate(grouped_old_positions)}
    permutation = tuple(new_position[old_pos] for old_pos in range(retained_dim))

    used_targets = sorted({target for target in a if target != 0})
    fused_dim = len(used_targets)
    target_to_block = {target: block + 1 for block, target in enumerate(used_targets)}
    block_fusion = tuple(
        target_to_block[a[retained[old_pos]]]
        for old_pos in grouped_old_positions
    )

    zero_insertion = tuple(used_targets)
    return (
        (deletion, retained_dim),
        (permutation, retained_dim),
        (block_fusion, fused_dim),
        (zero_insertion, target_dim),
    )


def compose_factorization(factors: tuple[tuple[Map, int], ...]) -> Map:
    current, current_target = factors[0]
    for nxt, nxt_target in factors[1:]:
        current = compose(current, current_target, nxt, nxt_target)
        current_target = nxt_target
    return current


def zero_vector(n: int) -> tuple[int, ...]:
    return (0,) * n


def zero_support(x: tuple[int, ...]) -> bool:
    return all(bit == 0 for bit in x)


def all_effective(_: tuple[int, ...]) -> bool:
    return True


def bit_vectors(n: int) -> Iterable[tuple[int, ...]]:
    return product((0, 1), repeat=n)


def run(max_dim: int) -> str:
    if not (0 <= max_dim <= 5):
        raise SystemExit("--max-dim must lie in 0..5; default 4 is the intended regression size")

    hom = generated_closure(max_dim)
    checks = 0
    total_morphisms = 0
    hom_matrix: list[list[int]] = []

    # 1. Generated grammar == arbitrary partial-coordinate-assignment/XOR normal forms.
    for m in range(max_dim + 1):
        row: list[int] = []
        for n in range(max_dim + 1):
            expected = normal_forms(m, n)
            actual = hom[(m, n)]
            assert actual == expected, (m, n, len(actual), len(expected), sorted(expected - actual)[:3])
            assert len(actual) == (n + 1) ** m
            row.append(len(actual))
            total_morphisms += len(actual)
            checks += 2
        hom_matrix.append(row)

    # 2. Every finite regression morphism has the constructive four-stage factorization.
    factorized = 0
    for m in range(max_dim + 1):
        for n in range(max_dim + 1):
            for a in normal_forms(m, n):
                factors = factor_assignment(a, n)
                assert compose_factorization(factors) == a
                # Each factor must itself be generated by the frozen primitive grammar.
                current_source = m
                for factor, factor_target in factors:
                    assert factor in hom[(current_source, factor_target)]
                    current_source = factor_target
                assert current_source == n
                factorized += 1
                checks += 1

    # 3. Zero preservation and zero-support forward naturality.
    zero_preserved = 0
    for m in range(max_dim + 1):
        for n in range(max_dim + 1):
            for a in hom[(m, n)]:
                image = apply_map(a, n, zero_vector(m))
                assert image == zero_vector(n)
                assert (not zero_support(zero_vector(m))) or zero_support(image)
                assert (not all_effective(zero_vector(m))) or all_effective(image)
                zero_preserved += 1
                checks += 1

    # 4. Neutral zero insertion/deletion, permutation invariance, and glue for Z.
    for m in range(max_dim + 1):
        for x in bit_vectors(m):
            for slot in range(m + 1):
                inserted = x[:slot] + (0,) + x[slot:]
                assert zero_support(x) == zero_support(inserted)
                checks += 1
            if m >= 2:
                swapped = (x[1], x[0]) + x[2:]
                assert zero_support(x) == zero_support(swapped)
                checks += 1
    for m in range(max_dim + 1):
        for n in range(max_dim + 1 - m):
            assert zero_support(zero_vector(m))
            assert zero_support(zero_vector(n))
            assert zero_support(zero_vector(m) + zero_vector(n))
            checks += 1

    # 5. Matched-model countermodel witness: same structure, different nonzero effectivity.
    for n in range(1, max_dim + 1):
        witness = (1,) + (0,) * (n - 1)
        assert not zero_support(witness)
        assert all_effective(witness)
        checks += 1

    # 6. Minimal semantic escape witness: backward reflection across a nontrivial XOR fibre.
    xor2: Map = (1, 1)  # C2^2 -> C2
    kernel_witness = (1, 1)
    assert apply_map(xor2, 1, kernel_witness) == (0,)
    assert zero_support((0,))
    assert not zero_support(kernel_witness)
    checks += 1

    # 7. Minimal map-level escape witness: a constant/affine 1 primitive would not preserve zero.
    # There is no assignment tuple for C2^0 -> C2^1 that produces 1; the grammar has only the zero map.
    assert normal_forms(0, 1) == {()}
    constant_one_image = (1,)
    assert not zero_support(constant_one_image)
    checks += 1

    # 8. Copying breaks the noncopying normal form but *not* the zero-support obstruction.
    # No normal-form map C2 -> C2^2 sends 1 to (1,1).
    diagonal_image_of_one = (1, 1)
    assert all(apply_map(a, 2, (1,)) != diagonal_image_of_one for a in normal_forms(1, 2))
    # Yet the diagonal itself is zero-preserving, so adding copying alone would still preserve Z.
    diagonal_image_of_zero = (0, 0)
    assert zero_support(diagonal_image_of_zero)
    checks += 2

    q20_prefix = 0
    if max_dim >= 3:
        q20_prefix = sum((n + 1) ** m for m in range(4) for n in range(4))
        assert q20_prefix == 144
        checks += 1

    matrix_text = "/".join(",".join(str(v) for v in row) for row in hom_matrix)
    return (
        "PASS P000_Q23_FORWARD_XOR_ALL_N; "
        f"checks={checks}; max_dim={max_dim}; morphisms={total_morphisms}; "
        f"factorized={factorized}; zero_preserving={zero_preserved}; "
        f"hom_matrix={matrix_text}; q20_prefix={q20_prefix}; "
        "normal_form=(target_dimension+1)^source_dimension; "
        "category=finite_partial_functions_on_basis_indices; "
        "matched_models=zero_support,all_effective; "
        "escape=backward_nontrivial_fibre_or_nonzero_generating_primitive_or_direct_nonzero_axiom; "
        "copying=breaks_noncopying_normal_form_but_preserves_zero_support; "
        "terminal=ALL_FINITE_ARITY_NONCOPYING_XOR_NORMAL_FORM_AND_ZERO_SUPPORT_INDEPENDENCE"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-dim", type=int, default=4)
    args = parser.parse_args()
    print(run(args.max_dim))


if __name__ == "__main__":
    main()
