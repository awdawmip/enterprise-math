"""Consume the p17 certificate using native integer/BRC checks, without FLINT."""
import hashlib
import json
from pathlib import Path

import p19_order9 as arithmetic


def main():
    directory = Path(__file__).resolve().parent
    path = directory.joinpath("p17_q0_certificate.json")
    data = json.loads(path.read_text())
    assert data["prime"] == 17 and data["side_budget"] == 2331
    assert data["arithmetic_source_sha256"] == hashlib.sha256(Path(arithmetic.__file__).read_bytes()).hexdigest()
    assert data["source_sha256"] == hashlib.sha256(directory.joinpath("p17_q0.py").read_bytes()).hexdigest()
    basis = data["weighted_basis"]
    assert len(basis) == 16 and all(len(row) == 16 for row in basis)
    weights = [17 * r - 1 for r in range(1, 17)]
    unweighted = [[arithmetic.exact(x, w) for x, w in zip(row, weights)] for row in basis]
    assert unweighted == data["unweighted_basis"]
    assert abs(arithmetic.determinant(unweighted)) == 17 ** 21 == data["lattice_index"]
    for k in range(1, 7):
        modulus = 17 ** k
        c = [arithmetic.inv(r ** k, modulus) for r in range(1, 17)]
        assert all(arithmetic.rem(arithmetic.dot(row, c), modulus) == 0 for row in unweighted)
    small = [[arithmetic.inv(r ** k, 17) for r in range(1, 7)] for k in range(1, 7)]
    assert arithmetic.rem(arithmetic.determinant(small), 17) != 0
    norms, _ = arithmetic.gram_schmidt(basis)
    assert [d.pair() for d in norms] == data["gram_schmidt_squared"]
    bound = 2 * 2331 ** 2
    assert bound == data["squared_norm_upper_bound"]
    assert all(d.n > bound * d.d for d in norms)
    assert data["status"] == "Q0_GLOBAL_CLEAR_BY_STATIC_GS_BOUND" and data["kernel"] is None
    print(json.dumps({"status": "P17_Q0_DIRECT_INTEGER_CERTIFICATE_PASS",
                      "scope": "No Driver acceptance or whole-p17 claim",
                      "brc_evaluations": arithmetic.TRACE_COUNT,
                      "certificate_sha256": hashlib.sha256(path.read_bytes()).hexdigest()}))


if __name__ == "__main__":
    main()
