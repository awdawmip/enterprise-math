#!/usr/bin/env python3
"""Exact check for the R284AF positive Port delayed-activation chain.

Python 3, SymPy 1.14; deterministic exhaustive finite grids; no floats.
"""
import json
from itertools import product
from fractions import Fraction
import sympy as S


def core(q, ts):
    k = q + 1
    c = S.Rational(1, 16*k)
    C = c*S.ones(k, k)
    for i in range(q-1):
        C[i, i+1] += c
    for i, t in enumerate(ts):
        C[i, i] += t
    return C, c


def port(C):
    k = C.rows
    delta = S.Rational(1, 256*k)
    gate = S.Rational(1, 16)
    J = delta*S.ones(k, k)
    I = S.eye(k)
    O = S.zeros(k,k)
    # Rows are (A,B,P); columns (A,B,Q).
    return S.BlockMatrix([[I-J, -C, O], [-J, I-J, -gate*I], [-gate*I, O, O]]).as_explicit(), gate, delta


def row_bounds(C, gate, delta):
    k = C.rows
    return (max(sum(C[i,j] for j in range(k)) + k*delta for i in range(k)) < 1
            and 2*k*delta + gate < 1 and gate < 1)


def verify():
    count_core = count_rank = count_port = 0
    samples = []
    for q in range(1,7):
        C0,c = core(q, [0]*q)
        assert C0.rank() == q
        for selections in product((0,1,2), repeat=q):
            ts = [c*S.Rational(v,2) for v in selections]
            C,_ = core(q,ts)
            expected = c*S.prod(ts)
            assert C.det(method='bareiss') == expected, (q,selections)
            count_core += 1
            # Rank of a one-dimensional kernel persists on every proper face.
            assert C.rank() == (q+1 if all(ts) else q), (q,selections)
            count_rank += 1
        if q <= 3:
            for selections in product((0,1), repeat=q):
                ts = [c*v for v in selections]
                C,_ = core(q,ts)
                P,g,d = port(C)
                assert row_bounds(C,g,d)
                assert P.det(method='bareiss') == (-1)**(q+1)*g**(2*(q+1))*c*S.prod(ts)
                assert P.rank() == (3*(q+1) if all(ts) else 3*(q+1)-1)
                count_port += 1
        if q in (2,3,5,6):
            t = [c]*q
            C,_ = core(q,t)
            samples.append(dict(q=q, c=str(c), fully_activated_core_det=str(C.det()), baseline_rank=q,
                                full_rank=q+1, first_nonzero_total_degree=q,
                                full_port_det_factor=f"(-1)^({q+1})*(1/16)^(2*{q+1})*{c}*product(t_i)"))
    # A nontrivial non-grid rational parameter point, independently checked.
    q=4
    C,c=core(q,[c1 for c1 in [S.Rational(1,101), S.Rational(1,113), S.Rational(1,127), S.Rational(1,139)]])
    assert C.det(method='bareiss') == c*S.prod([S.Rational(1,101),S.Rational(1,113),S.Rational(1,127),S.Rational(1,139)])
    return dict(schema='R284AF_EXACT_CHAIN_VERIFICATION_V1', status='PASS',
                arithmetic='SymPy Rational exact Bareiss determinant and rank',
                core_parameter_grid='q=1..6; each named t_i in {0,c/2,c}',
                core_det_checks=count_core, core_rank_checks=count_rank,
                full_port_parameter_grid='q=1..3; each named t_i in {0,c}',
                full_port_det_rank_stability_checks=count_port,
                additional_off_grid_core_det_checks=1,
                witnesses=samples,
                source='R284AF_CORANK_ONE_ARBITRARILY_DELAYED_PORT_ACTIVATION_20261119.md',
                limitation='finite exact checks for the published algebraic proof, no independent reviewer')


if __name__ == '__main__':
    print(json.dumps(verify(), indent=2, ensure_ascii=False, sort_keys=True))
