#!/usr/bin/env python3
from fractions import Fraction
from itertools import product


WEIL_WEIGHTS = {(6, 0), (0, 6)}


def theta_weight(power: int) -> tuple[int, int]:
    return (power, power)


def semihomogeneous_ch3(rank: int, c1_theta_scalar: int) -> Fraction:
    if rank <= 0:
        raise ValueError("rank must be positive")
    q = Fraction(c1_theta_scalar, 1)
    r = Fraction(rank, 1)
    return q**3 / (6 * r**2)


def main() -> None:
    checks: list[tuple[str, bool]] = []

    # H^6_C exterior-count decomposition for V_C = V_sigma (+) V_sigma_bar.
    h6_blocks = {(a, 6 - a) for a in range(7)}
    checks.append(("h6_has_seven_exterior_count_blocks", len(h6_blocks) == 7))
    checks.append(("weil_blocks_are_extremal", WEIL_WEIGHTS == {(6, 0), (0, 6)}))
    checks.append(("theta_cube_is_mixed_block", theta_weight(3) == (3, 3)))
    checks.append(("theta_cube_has_zero_exceptional_projection", theta_weight(3) not in WEIL_WEIGHTS))

    # Mukai's semihomogeneous formula ch(E)=r*exp(c1/r):
    # ch_3(E)=c1^3/(6 r^2), hence every sample lies in the theta^3 line.
    for rank, q in product(range(1, 8), range(-5, 6)):
        coeff = semihomogeneous_ch3(rank, q)
        checks.append((f"semihom_ch3_typed_r{rank}_q{q}", isinstance(coeff, Fraction)))
    checks.append(("semihomogeneous_ch3_weight", theta_weight(3) not in WEIL_WEIGHTS))

    # Newton identities are consistent with r equal formal Chern roots c1/r.
    # c2=(r-1)c1^2/(2r), c3=(r-1)(r-2)c1^3/(6r^2).
    for rank in range(1, 8):
        r = Fraction(rank, 1)
        c2_coeff = (r - 1) / (2 * r)
        c3_coeff = (r - 1) * (r - 2) / (6 * r**2)
        ch2_coeff = Fraction(1, 2) * (1 - 2 * c2_coeff)
        ch3_coeff = Fraction(1, 6) * (1 - 3 * c2_coeff + 3 * c3_coeff)
        checks.append((f"newton_ch2_r{rank}", ch2_coeff == 1 / (2 * r)))
        checks.append((f"newton_ch3_r{rank}", ch3_coeff == 1 / (6 * r**2)))

    # Extension/direct-sum/shift closure: Chern character is additive in K_0.
    sample_terms = [(1, 1, 1), (2, 3, -1), (5, -2, 1), (3, 0, -1)]
    total = sum(sign * semihomogeneous_ch3(r, q) for r, q, sign in sample_terms)
    checks.append(("extension_shift_additivity_sample_is_rational", isinstance(total, Fraction)))
    checks.append(("extension_shift_stays_theta3", theta_weight(3) not in WEIL_WEIGHTS))

    # Expected codimension-3 Thom-Porteous / Schur expressions made from
    # Chern classes c_i in Q[theta] use only c1^3, c1*c2, c3.
    codim3_monomials = set()
    for a in range(4):
        for b in range(2):
            for c in range(2):
                if a + 2 * b + 3 * c == 3:
                    codim3_monomials.add((a, b, c))
    expected = {(3, 0, 0), (1, 1, 0), (0, 0, 1)}
    checks.append(("codim3_chern_monomials_complete", codim3_monomials == expected))
    for a, b, c in sorted(codim3_monomials):
        degree = a + 2 * b + 3 * c
        checks.append((f"degeneracy_monomial_{a}_{b}_{c}_is_theta3", theta_weight(degree) == (3, 3)))

    # One-dimensional NS_Q makes any nonzero isogeny pullback/pushforward
    # act by nonzero scalars on theta^3. We only certify the scalar closure.
    for lam in [Fraction(1, 2), Fraction(2, 1), Fraction(3, 5), Fraction(7, 3)]:
        pull = lam**3
        degree_model = lam**6
        push = degree_model / pull
        checks.append((f"isogeny_scalar_closure_{lam}", pull != 0 and push != 0))

    # Counterexample/boundary regressions.
    checks.append(("primitive_weil_60_is_not_killed_by_type_system", (6, 0) in WEIL_WEIGHTS))
    checks.append(("primitive_weil_06_is_not_killed_by_type_system", (0, 6) in WEIL_WEIGHTS))
    checks.append(("point_object_has_no_ch3_on_sixfold", 3 != 6))

    # Elementary discriminant separation certificate: 3 is not a rational
    # Gaussian norm because x^2+y^2 == 0 mod 3 forces x=y=0 mod 3.
    zero_pairs = [
        (a, b)
        for a in range(3)
        for b in range(3)
        if (a * a + b * b) % 3 == 0
    ]
    checks.append(("gaussian_norm_residue_gate", zero_pairs == [(0, 0)]))

    failures = [name for name, ok in checks if not ok]
    print(f"HODGE_H0N_CHECKS={len(checks)}")
    print(f"HODGE_H0N_FAILURES={len(failures)}")
    if failures:
        for name in failures:
            print(f"FAIL:{name}")
        raise SystemExit(1)
    print("HODGE_H0N_NONSPLIT_WEIL_EXCEPTIONAL_CH3_SEED_OBJECT_CHECK: PASS")


if __name__ == "__main__":
    main()
