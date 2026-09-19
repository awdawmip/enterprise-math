"""Two exact finite checks of the newly derived UR elimination formulas.

This is a task-specific transcription check, not a uniform proof, a replay of
the old 77-prime experiment, or a reusable hypergeometric software family.
"""
from __future__ import annotations

from fractions import Fraction as Q
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src"))
from enterprise_math.precision import (  # existing finite integer quotient API
    precision_detail, project_precision, recompose_precision,
)


def add(*polys):
    out = [Q(0)] * max(map(len, polys))
    for poly in polys:
        for k, value in enumerate(poly):
            out[k] += value
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def scale(poly, value):
    return [value * a for a in poly]


def mul(a, b):
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] += ai * bj
    return out


def deriv(poly):
    return [k * poly[k] for k in range(1, len(poly))] or [Q(0)]


def power(poly, k):
    out = [Q(1)]
    for _ in range(k):
        out = mul(out, poly)
    return out


def legendre_truncated(a, N):
    # Sum c_k ((x-1)/2)^k; c_(k+1)/c_k=(a-k)(a+k+1)/(k+1)^2.
    out, term, coefficient = [Q(0)], [Q(1)], Q(1)
    z = [Q(-1, 2), Q(1, 2)]
    for k in range(N + 1):
        out = add(out, scale(term, coefficient))
        if k < N:
            coefficient *= (a-k)*(a+k+1)/Q((k+1)**2)
            term = mul(term, z)
    return out, coefficient


def reflected(poly):
    return [(-1)**k * value for k, value in enumerate(poly)]


def at_t(poly):
    return tuple(sum((poly[k] * Q(1, 2)**(k//2)
                      for k in range(parity, len(poly), 2)), Q(0))
                 for parity in (0, 1))


def mod_q(value, modulus):
    return value.numerator * pow(value.denominator, -1, modulus) % modulus


def mod_pair(pair, modulus):
    return [mod_q(x, modulus) for x in pair]


def legal_divided_pair(pair, p, exponent):
    modulus = p ** (exponent + 1)
    residues = mod_pair(pair, modulus)
    quotient = []
    for residue in residues:
        assert precision_detail(residue, 1, p**exponent) == 0
        digit = project_precision(residue, 1, p**exponent)
        assert recompose_precision(digit, 0, 1, p**exponent) == residue
        quotient.append(digit)
    return quotient


def divisible(poly, modulus):
    return all(mod_q(x, modulus) == 0 for x in poly)


def main():
    x, D, z = [Q(0), Q(1)], [Q(-1), Q(0), Q(1)], [Q(-1, 2), Q(1, 2)]
    rows = []
    for p in (13, 19):
        n, N = (p-1)//3, p-1
        A, _ = legendre_truncated(Q(2, 3), N)
        B, cN = legendre_truncated(Q(-1, 3), N)
        C, _ = legendre_truncated(Q(-4, 3), N)
        P, _ = legendre_truncated(Q(n), n)
        P2, _ = legendre_truncated(Q(2*n), 2*n)
        s, zN = deriv(B), power(z, p)
        recurrence = add(scale(A, 2), scale(mul(x, B), -1), scale(C, -1))
        assert add(recurrence, scale(zN, 2*cN)) == [0]
        assert add(scale(A, 2), scale(mul(x, B), -2),
                   scale(mul(D, s), -3), scale(zN, (6*p-2)*cN)) == [0]
        assert add(C, scale(mul(x, B), -1), scale(mul(D, s), -3),
                   scale(zN, (6*p-4)*cN)) == [0]
        assert divisible(deriv(recurrence), p**3)
        assert mod_q(cN / p**2, p) == 1
        assert divisible(add(scale(B, 3), scale(P2, -1), scale(P, -2)), p**2)
        alpha = scale(add(A, reflected(A)), Q(1, p**2))
        beta = scale(add(B, scale(reflected(B), -1)), Q(1, p**2))
        gamma = scale(add(C, reflected(C)), Q(1, p**2))
        for defect in (alpha, beta, gamma):
            assert all(q.denominator % p != 0 for q in defect)
        assert divisible(add(scale(alpha, 2), scale(mul(x, beta), -2),
                             scale(mul(D, deriv(beta)), -3), [Q(2)]), p)
        assert divisible(add(gamma, scale(mul(x, beta), -1),
                             scale(mul(D, deriv(beta)), -3), [Q(4)]), p)
        assert divisible(add(scale(alpha, 2), scale(mul(x, beta), -1),
                             scale(gamma, -1), [Q(-2)]), p)
        # This identity eliminates the adjacent first jets as well as values.
        W = add(mul(A, deriv(C)), scale(mul(C, deriv(A)), -1))
        W_formula = add(scale(mul(add([Q(1)], scale(power(x, 2), -1)), mul(B, s)), Q(3,2)),
                        scale(mul(x, mul(B, B)), Q(-1,3)),
                        scale(mul(mul(x, add([Q(1)], scale(power(x, 2), -1))), mul(s,s)), Q(3,2)))
        assert divisible(add(W, scale(W_formula, -1)), p**2)
        K = add(scale(W, 4), scale(mul(x, mul(s, s)), -3))
        # New structural reduction: keep the derivative-invisible x^p term.
        H = scale(add(P2, scale(P, -1)), Q(1, 3*p))
        assert all(value.denominator % p != 0 for value in H)
        assert len(H)-1 <= 2*n and sum(H) == 0
        assert add(H, scale(reflected(H), -1)) == [0]
        assert divisible(add(B, scale(P,-1), scale(H,-p)), p**2)
        PP = mul(P, P)
        I = [Q(0)] + [value / Q(k+1) for k, value in enumerate(PP)]
        assert sum(I) == Q(1, 2*n+1)
        V = mul([Q(1), Q(0), Q(-1)],
                add(mul(P, deriv(H)), scale(mul(deriv(P), H), -1)))
        assert add(deriv(V), scale(mul(P,P2), Q(n,3))) == [0]
        assert len(V)-1 <= p
        assert divisible(add(V, scale(I, Q(-1,9)), scale(power(x,p), Q(1,3))), p)
        u_pair = tuple(value / p for value in at_t(P))
        # P is even and P' is odd; this is the exact base-field expression.
        norm_digit = mod_q(at_t(I)[1], p)
        ordinary_residual = mod_q(9*u_pair[0]*at_t(deriv(P))[1] - 2*at_t(I)[1] - 3, p)
        assert ordinary_residual == 0
        q_digit = legal_divided_pair(at_t(B), p, 1)
        K_digit = legal_divided_pair(at_t(K), p, 1)
        obstruction = mod_pair((at_t(K)[0] / p, at_t(K)[1] / p + 1), p)
        # Targets are evaluated only as finite examples, not assumed in identities.
        target = add(scale(mul(B, deriv(P)), 3), scale(x, p))
        norm_jet = add(scale(mul(P,deriv(P)),9), scale(I,-2*p), scale(x,-3*p))
        assert len(norm_jet)-1 <= 2*n+1 < p
        assert mod_pair(at_t(add(norm_jet,scale(target,-3))),p**2) == [0,0]
        target_at_t = mod_pair(at_t(target), p**2)
        assert obstruction == [0, 0] and target_at_t == [0, 0]
        rows.append({"p": p, "n": n, "exact_recurrence_and_both_contiguities": True,
                     "differentiated_recurrence_mod_p3": True,
                     "all_defect_elimination_polynomials_mod_p": True,
                     "Wronskian_elimination_polynomial_mod_p2": True,
                     "degree_p_Wronskian_and_Frobenius_constant": True,
                     "exact_Lagrange_identity": True,
                     "low_degree_certificate_degree": len(norm_jet)-1,
                     "norm_jet_target_equivalence_mod_p2_at_CM": True,
                     "Legendre_norm_primitive_at_1_exact": str(sum(I)),
                     "ordinary_Pn_over_p_mod_p_pair": legal_divided_pair(at_t(P),p,1),
                     "Legendre_norm_primitive_at_t_over_t_mod_p": norm_digit,
                     "ordinary_Legendre_one_scalar_residual": ordinary_residual,
                     "barycentric_mod_p2": True,
                     "q_mod_p_pair": q_digit,
                     "beta_mod_p_pair": mod_pair(at_t(beta), p),
                     "beta_prime_mod_p_pair": mod_pair(at_t(deriv(beta)), p),
                     "d_mod_p_pair": mod_pair(at_t(deriv(P)), p),
                     "K_over_p_mod_p_pair": K_digit,
                     "extra_jet_obstruction_pair": obstruction,
                     "target_mod_p2_pair": target_at_t})
    payload = {"scope": "EXACT_FINITE_TRANSCRIPTION_CHECK_ONLY",
               "uniform_proof": False, "old_77_prime_replay": False,
               "native_integer_precision_api_executed": ["precision_detail", "project_precision", "recompose_precision"],
               "quadratic_pair_basis": ["1", "t"], "relation": "2*t^2=1", "rows": rows}
    Path(__file__).with_name("elimination_check.json").write_text(json.dumps(payload, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
