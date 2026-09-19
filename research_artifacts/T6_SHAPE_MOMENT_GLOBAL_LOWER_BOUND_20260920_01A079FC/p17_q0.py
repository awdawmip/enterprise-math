"""Bounded next-prime input recovery and a static zero-coset criterion only."""
import hashlib
import json
from pathlib import Path

import p19_order9 as arithmetic


def main():
    from flint import fmpz_mat
    import flint

    p, dimension, budget = 17, 16, 2331
    weights = [p * r - 1 for r in range(1, p)]
    basis = [[int(i == j) for j in range(dimension)] for i in range(dimension)]
    for k in range(1, 7):
        modulus = p ** k
        coefficients = [arithmetic.inv(r ** k, modulus) for r in range(1, p)]
        values = [arithmetic.rem(arithmetic.dot(row, coefficients), modulus) for row in basis]
        pivot = next(i for i in range(dimension) if arithmetic.rem(values[i], p))
        inverse = arithmetic.inv(values[pivot], modulus)
        row_pivot = basis[pivot]
        replacement = []
        for i, row in enumerate(basis):
            if i == pivot:
                replacement.append([modulus * x for x in row])
            else:
                factor = arithmetic.rem(values[i] * inverse, modulus)
                replacement.append([x - factor * y for x, y in zip(row, row_pivot)])
        basis = replacement
    weighted = [[a * w for a, w in zip(row, weights)] for row in basis]
    proposal, change = fmpz_mat(weighted).lll(transform=True, gram="exact")
    reduced = [[int(proposal[i, j]) for j in range(dimension)] for i in range(dimension)]
    change = [[int(change[i, j]) for j in range(dimension)] for i in range(dimension)]
    assert arithmetic.matrix_product(change, weighted) == reduced
    assert abs(arithmetic.determinant(change)) == 1
    unweighted = [[arithmetic.exact(x, w) for x, w in zip(row, weights)] for row in reduced]
    assert abs(arithmetic.determinant(unweighted)) == p ** 21
    for row in unweighted:
        for k in range(1, 7):
            modulus = p ** k
            assert arithmetic.rem(sum(a * arithmetic.inv(r ** k, modulus)
                                      for r, a in enumerate(row, 1)), modulus) == 0
    small = [[arithmetic.inv(r ** k, p) for r in range(1, 7)] for k in range(1, 7)]
    assert arithmetic.rem(arithmetic.determinant(small), p) != 0
    norms, _ = arithmetic.gram_schmidt(reduced)
    radius_squared = 2 * budget ** 2
    static_clear = all(d.n > radius_squared * d.d for d in norms)
    minimum = norms[0]
    for d in norms[1:]:
        if d.n * minimum.d < minimum.n * d.d:
            minimum = d
    # A failed sufficient bound is not a negative result. Retain a real cheap
    # basis-row modular kernel if one is actually present; never assume one away.
    kernel = None
    for u, row in zip(unweighted, reduced):
        positive = sum(max(0, x) for x in row)
        negative = sum(max(0, -x) for x in row)
        if positive <= budget and negative <= budget:
            kernel = {"q0": u, "positive_mass": positive, "negative_mass": negative}
            break
    if static_clear:
        assert kernel is None
    result = {
        "schema": "T6_P17_Q0_STATIC_CERTIFICATE_V1", "prime": p,
        "status": "Q0_GLOBAL_CLEAR_BY_STATIC_GS_BOUND" if static_clear else "MODULAR_KERNEL_FOUND" if kernel else "INPUT_RECOVERED_STATIC_CRITERION_UNDETERMINED",
        "side_budget": budget, "lattice_index": p ** 21,
        "weighted_basis": reduced, "unweighted_basis": unweighted,
        "gram_schmidt_squared": [x.pair() for x in norms],
        "minimum_gram_schmidt_squared": minimum.pair(),
        "squared_norm_upper_bound": radius_squared, "kernel": kernel,
        "criterion": "Every nonzero integral lattice combination has norm squared at least min(D_i), using its highest nonzero coefficient",
        "scope": "Maximal p17 q0 only. Vertical orders1..16 and lower-prime completion are not checked.",
        "basis_proposal": "python-flint " + flint.__version__,
        "native_verification": "BRC-mediated determinant, congruences, exact Gram-Schmidt and integer cross comparison",
        "brc_evaluations": arithmetic.TRACE_COUNT,
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "arithmetic_source_sha256": hashlib.sha256(Path(arithmetic.__file__).read_bytes()).hexdigest(),
    }
    Path(__file__).with_name("p17_q0_certificate.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({k: v for k, v in result.items() if k not in {"weighted_basis", "unweighted_basis", "gram_schmidt_squared"}}))


if __name__ == "__main__":
    main()
