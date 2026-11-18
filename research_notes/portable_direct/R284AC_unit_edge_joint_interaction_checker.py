#!/usr/bin/env python3
"""Exact finite verification of R284AC rank-defect / joint-edit theorem.

No network calls, dependencies or floating point arithmetic are used.
The theorem for all k is algebraic; this tests the stated explicit systems.
"""
import json
from fractions import Fraction
from itertools import product
from math import prod


def determinant(a):
    a = [row[:] for row in a]
    n = len(a)
    sign, previous = 1, 1
    for j in range(n - 1):
        pivot_row = next((i for i in range(j, n) if a[i][j]), None)
        if pivot_row is None:
            return 0
        if pivot_row != j:
            a[j], a[pivot_row] = a[pivot_row], a[j]
            sign = -sign
        pivot = a[j][j]
        for i in range(j + 1, n):
            for h in range(j + 1, n):
                top = a[i][h] * pivot - a[i][j] * a[j][h]
                q, rem = divmod(top, previous)
                assert rem == 0
                a[i][h] = q
            a[i][j] = 0
        previous = pivot
    return sign * a[-1][-1] if n else 1


def rank(a):
    a = [[Fraction(x) for x in row] for row in a]
    n, m, p = len(a), len(a[0]), 0
    for j in range(m):
        pivot_row = next((i for i in range(p, n) if a[i][j]), None)
        if pivot_row is None:
            continue
        a[p], a[pivot_row] = a[pivot_row], a[p]
        d = a[p][j]
        for h in range(j, m):
            a[p][h] /= d
        for i in range(p + 1, n):
            if a[i][j]:
                f = a[i][j]
                for h in range(j, m):
                    a[i][h] -= f * a[p][h]
        p += 1
        if p == n:
            break
    return p


def port_matrix(k, r, on_mask, gate_version):
    # D=common denominator. All entries of D*W are integers.
    D = 256 * k
    W = [[0] * (4 * k) for _ in range(4 * k)]
    gates_g = [D // (8 if gate_version and i % 2 == 0 else 16) for i in range(k)]
    gates_h = [D // (8 if gate_version and i % 2 == 1 else 16) for i in range(k)]
    t = [4 if (on_mask >> i) & 1 else 0 for i in range(k-r)]
    for i in range(k):
        W[i][k + i] = gates_g[i]
        W[2*k + i][3*k + i] = gates_h[i]
        for j in range(k):
            W[k+i][k+j] = 1        # L=delta*J
            W[2*k+i][k+j] = 1      # D=delta*J
            W[2*k+i][2*k+j] = 1   # U=delta*J
            fixed = 4 if i == j and i < r-1 else 0
            active = t[i-(r-1)] if i == j and (r-1) <= i < k-1 else 0
            W[k+i][2*k+j] = 4 + fixed + active
    assert all(sum(row) < D for row in W)  # globally strict substochasticity
    S = list(range(k,3*k))
    rows = S + list(range(k))
    cols = S + list(range(3*k,4*k))
    M = [[(D if i == j else 0) - W[i][j] for j in cols] for i in rows]
    C = [[W[k+i][2*k+j] for j in range(k)] for i in range(k)]
    return D, M, C, t, gates_g, gates_h


def verify():
    rows = []
    matrix_cases = 0
    tested_pivot_ranks = 0
    examples = {}
    for k in range(2,7):
        for r in range(1,k):
            m = k-r
            total = 0
            full = (1 << m) - 1
            for mask in range(1 << m):
                for gate_version in (0,1):
                    D,M,C,t,g,h = port_matrix(k,r,mask,gate_version)
                    detC = determinant(C)
                    expected_detC = 4**r * prod(t)
                    assert detC == expected_detC
                    detP = determinant(M)
                    expected_detP = (-1 if k%2 else 1)*prod(g)*prod(h)*detC
                    assert detP == expected_detP
                    rankC = rank(C)
                    active = sum(bool(z) for z in t)
                    assert rankC == r+active
                    rankP = rank(M)
                    assert rankP == 2*k+rankC
                    tested_pivot_ranks += 2
                    if mask != full:
                        assert detP == 0
                    else:
                        assert detP != 0
                    if k == 3 and r == 1 and mask == full and gate_version == 0:
                        examples['k3_rank1_two_unit_edits_base_gates'] = {
                            'D':D,'core_det':str(Fraction(detC,D**k)),
                            'port_det':str(Fraction(detP,D**(3*k))),
                            'port_rank':rankP,
                        }
                    if k == 4 and r == 2 and mask == full and gate_version == 0:
                        examples['k4_rank2_two_unit_edits_base_gates'] = {
                            'D':D,'core_det':str(Fraction(detC,D**k)),
                            'port_det':str(Fraction(detP,D**(3*k))),
                            'port_rank':rankP,
                        }
                    total += 1
                    matrix_cases += 1
            rows.append({'k':k,'base_core_rank':r,'rank_defect':m,
                         'independent_single_edge_core_edits':m,
                         'binary_edit_masks':2**m,'gate_settings':2,
                         'full_port_determinant_checks':total,
                         'strict_substochasticity_checks':total,
                         'core_determinant_checks':total,
                         'core_and_port_rank_checks':2*total,
                         'all_proper_edit_faces_determinant_zero':True,
                         'all_active_determinant_nonzero':True})
    return {'schema':'R284AC_EXACT_PORT_RANK_DEFECT_UNIT_EDGE_INTERACTION_V2',
            'method':'Integer-scaled exact Bareiss determinants and Fraction Gaussian ranks',
            'scopes':'k=2..6; each base core rank r=1..k-1; every binary mask of k-r unit edits; 2 gate settings; positive feedback L,D,U',
            'status':'PASS','matrix_cases':matrix_cases,
            'rank_checks':tested_pivot_ranks,
            'numerical_floating_point_used':False,
            'external_network_requests':False,
            'families':rows,'examples':examples,
            'theorem_scope':'Symbolic proof for every integer k>=2, not inferred from enumeration'}

if __name__ == '__main__':
    print(json.dumps(verify(),indent=2,sort_keys=True))
