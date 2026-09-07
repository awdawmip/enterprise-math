"""Independent finite guard checks for the analytic energy audit, not an RH test.

No author code is imported. Convergence and holomorphy are proved in the
accompanying note; rational exponent checks cannot prove those theorems.
"""
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCES = (
    "OWNER_RH_ENERGY_DOMAIN_AUDIT_20260907.md",
    "owner_rh_energy_domain_20260907_check.py",
    "RH_X6_BRC_TRANSPORT_FRONTIER_20260906.md",
    Path(__file__).name,
)


def hashes():
    return {name: sha256((HERE / name).read_bytes()).hexdigest() for name in SOURCES}


def mobius_by_divisor_recurrence(limit):
    mu = [0] * (limit + 1)
    mu[1] = 1
    for n in range(2, limit + 1):
        mu[n] = -sum(mu[d] for d in range(1, n) if n % d == 0)
    return mu


def determinant(matrix):
    rows = [list(map(Q, row)) for row in matrix]
    value = Q(1)
    for j in range(len(rows)):
        pivot = next((i for i in range(j, len(rows)) if rows[i][j]), None)
        if pivot is None:
            return Q(0)
        if pivot != j:
            rows[j], rows[pivot] = rows[pivot], rows[j]
            value = -value
        scale = rows[j][j]
        value *= scale
        for i in range(j + 1, len(rows)):
            factor = rows[i][j] / scale
            rows[i] = [a - factor * b for a, b in zip(rows[i], rows[j])]
    return value


def run():
    initial = hashes()
    radius = Q(1, 16)
    lower = 1 - Q(1, 4) - Q(1, 2) - (1 + Q(1, 3)) * radius
    assert lower == Q(1, 6)
    divergence = []
    for j in range(1, 9):
        # sigma=5/2, epsilon=1/(16*4^j); exact square roots are rational.
        eps = radius / 4**j
        inverse_root = 4 * 2**j
        bound = lower**2 * 2 * (inverse_root - 4)
        assert bound == Q(2, 9) * (2**j - 1)
        divergence.append({"epsilon": str(eps), "energy_lower_bound": str(bound)})

    domain = []
    for sigma in map(Q, (-1, 0, Q(1, 2), 1, Q(3, 2), 2, Q(5, 2))):
        zero_exponent, positive_tail_exponent = 1 - sigma, -sigma
        zero_finite = zero_exponent > -1
        absolute_tail_finite = positive_tail_exponent < -1
        assert (zero_finite and absolute_tail_finite) == (1 < sigma < 2)
        domain.append({"sigma": str(sigma), "zero_integrable": zero_finite,
                       "positive_carrier_tail_integrable": absolute_tail_finite})

    mellin = []
    for u in (Q(1, 8), Q(1, 4), Q(1, 2), Q(5, 8), Q(11, 16), Q(23, 32)):
        sigma = Q(5, 4) - u
        exponent = 2 * u + sigma - 3
        assert Q(1, 2) < sigma < 2 - 2 * u < 2 and exponent < -1
        mellin.append({"Re_s": str(u), "chosen_sigma": str(sigma),
                       "CS_tail_exponent": str(exponent)})
    assert 2 * Q(3, 4) + Q(1, 2) - 3 == -1  # excluded endpoint

    l2_count = 0
    for theta in (Q(1, 4), Q(1, 2), Q(3, 4), Q(1), Q(5, 4)):
        for sigma in (Q(3, 4), Q(1), Q(5, 4), Q(3, 2), Q(7, 4)):
            if theta >= sigma:
                continue
            first_exponent = 2 * (theta - 2) + 2 * (2 - sigma)
            second_exponent = 2 * (theta - sigma)
            assert first_exponent == second_exponent < 0
            assert 2 - sigma > 0 and sigma - theta > 0
            l2_count += 1

    # At sigma=1, the actual integrated kernel is 1/(m^2+n^2).
    mu = mobius_by_divisor_recurrence(8)
    grams = []
    determinants = []
    for n in range(1, 9):
        kernel = tuple(tuple(Q(1, m*m + k*k) for k in range(1, n + 1))
                       for m in range(1, n + 1))
        det = determinant(kernel)
        assert det > 0
        determinants.append(str(det))
        value = sum(Q(mu[m] * mu[k], m*m + k*k)
                    for m in range(1, n + 1) for k in range(1, n + 1))
        assert value > 0
        grams.append(str(value))
    assert Q(grams[0]) == Q(1, 2) and Q(grams[1]) == Q(9, 40)
    assert Q(grams[1]) - Q(grams[0]) == -Q(11, 40)

    # Gamma recurrence gives Gamma(-1/2)/Gamma(1/2)=-2.
    # The continued diagonal at sigma=5/2 is therefore -2*sqrt(2*pi).
    continued_diagonal_factor = 1 / Q(-1, 2)
    assert continued_diagonal_factor == -2
    # The source paper's variable s=1/4 has a divergent lower endpoint:
    paper_s = Q(1, 4)
    assert -paper_s - 1 < -1 and 2 * paper_s + 2 == Q(5, 2)
    # Gamma(-1/4)=Gamma(3/4)/(-1/4), so its continued RHS is negative.
    assert 1 / (-paper_s) == -4

    result = {"status": "PASS", "source_hashes_sha256": initial,
              "scope": "finite exact guards only; analytic proofs are in the independent note; no RH conclusion",
              "zero_lower_on_0_to_1_over_16": str(lower),
              "sigma_5_over_2_divergence": divergence,
              "integrability_exponent_table": domain,
              "mellin_CS_parameter_examples": mellin,
              "L2_squared_tail_exponent_cases": l2_count,
              "sigma_1_finite_grams_N1_to_N8": grams,
              "sigma_1_leading_principal_determinants": determinants,
              "N2_minus_N1_Gram": "-11/40",
              "continued_sigma_5_over_2_diagonal_over_sqrt_2pi": "-2",
              "source_Lemma_2_4_counterexample": {"k": 2, "s": "1/4",
                    "ordinary_integral": "diverges to +infinity at zero; tail absolutely convergent",
                    "continued_RHS": "Gamma(-1/4)/zeta(5/2), finite negative"},
              "global_knowledge_sync": "main@4fa7d7d / GLOBAL_KNOWLEDGE_V1"}
    assert hashes() == initial, "audited bytes changed during execution"
    return result


if __name__ == "__main__":
    print(json.dumps(run(), ensure_ascii=False, indent=2))
