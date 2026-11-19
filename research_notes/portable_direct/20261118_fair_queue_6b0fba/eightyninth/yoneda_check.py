"""Finite exact checks for the one-coordinate graph pair on the Gaussian CM fibre."""
import itertools
import json
import math
from collections import Counter
import sympy as sp


NAMES = ['O', 'P_minus1', 'P_zero', 'P_plus1']


def primitive_columns(mat):
    """A deterministic integer basis for a rational kernel."""
    columns = []
    for v in mat.nullspace():
        den = math.lcm(*(int(a.as_numer_denom()[1]) for a in v))
        ints = [int(a * den) for a in v]
        divisor = math.gcd(*ints)
        columns.append([x // divisor for x in ints])
    return columns


def normal_map(slopes):
    columns = []
    weights = sp.diag(1, 1, sp.Rational(1, 3))
    graph = sp.diag(*slopes)
    for i, j in itertools.product(range(3), repeat=2):
        tangent = sp.zeros(3)
        tangent[i, j] = 1
        delta = weights * tangent.T - graph * tangent * graph
        columns.append(delta.reshape(9, 1))
    return sp.Matrix.hstack(*columns)


def wedge_graph(slopes):
    # Holomorphic forms occupy slots dz_0..dz_2,dw_0..dw_2, and their
    # conjugates the same order plus six. Ordered wedge is sorted with sign.
    choices = [[(j, -slopes[j]), (3 + j, 1)] for j in range(3)]
    choices += [[(6 + j, -slopes[j]), (9 + j, 1)] for j in range(3)]
    return [(tuple(x for x, _ in terms), math.prod(c for _, c in terms))
            for terms in itertools.product(*choices)]


def variation(slopes, a, b):
    deriv = Counter()
    for slots, coef in wedge_graph(slopes):
        for i, slot in enumerate(slots[:3]):
            if slot == a:
                target, scalar = 9 + b, 1
            elif slot == b + 3:
                target, scalar = 6 + a, sp.Rational(1, (1, 1, 3)[b])
            else:
                continue
            out = slots[:i] + (target,) + slots[i+1:]
            if len(set(out)) < 6:
                continue
            inversions = sum(x > y for x, y in itertools.combinations(out, 2))
            deriv[tuple(sorted(out))] += (-1)**inversions * scalar * coef
    return {k:v for k,v in deriv.items() if v}


def hodge_matrix(slopes):
    data = [variation(slopes, i, j) for i, j in itertools.product(range(3), repeat=2)]
    keys = sorted(set().union(*(v.keys() for v in data)))
    return sp.Matrix([[column.get(k, 0) for column in data] for k in keys])


def elliptic_residues():
    # y^2=x^3-x. The orders of x-e on E are 2 at P_e and -2 at O.
    x = sp.symbols('x')
    cubic = x**3-x
    assert sp.discriminant(cubic, x) == 4
    finite_points = [-1, 0, 1]
    for e in finite_points:
        assert cubic.subs(x, e) == 0 and sp.diff(cubic, x).subs(x, e) != 0
        quotient, remainder = sp.div(cubic, x-e, x)
        assert remainder == 0 and quotient.subs(x,e) == sp.diff(cubic, x).subs(x,e)
    rows = [[0] * 4]
    for e in finite_points:
        orders = [-2] + [2 * int(e == f) for f in finite_points]
        rows.append([int(sp.Rational(v, 2)) for v in orders])
    matrix = sp.Matrix(rows)
    assert matrix.rank() == 3
    assert matrix.T.nullspace() == [sp.eye(4).col(0)]
    assert matrix.nullspace() == [sp.ones(4, 1)]
    ternary = list(itertools.product((-1,0,1), repeat=4))
    histogram = Counter()
    for w in ternary:
        for g in ternary:
            residue_sum = sum(w[i] * (g[i] - g[0]) for i in range(1, 4))
            ordinary_product = sum(w[i] * matrix[i,j] * g[j] for i in range(4) for j in range(4))
            assert residue_sum == ordinary_product
            histogram[int(residue_sum)] += 1
    return dict(column_labels=NAMES, row_labels=['1','f_minus1','f_zero','f_plus1'],
                matrix=matrix.tolist(), bilinear_rank=matrix.rank(),
                left_radical=primitive_columns(matrix.T), right_radical=primitive_columns(matrix),
                ternary_pairs_checked=sum(histogram.values()), ternary_zero_pairs=histogram[0])


def dimensions():
    point_ideal = [1, 6, 6, 1]
    pic = [1, 3, 3, 1]
    whole_ideal = [sum(pic[i]*point_ideal[k-i] for i in range(4) if 0 <= k-i < 4)
                   for k in range(7)]
    whole_graph = [math.comb(6, k) for k in range(7)]
    assert whole_ideal[2] == 27 and whole_graph[2] == 15
    return dict(graph_self_ext_poincare=whole_graph, ideal_self_ext_poincare=whole_ideal,
                rank_of_tensor_to_pair_of_targets=1, tensor_map_kernel_dimension=15)


def tangent_checks():
    a, b = (1,1,1), (-1,1,1)
    da, db = normal_map(a), normal_map(b)
    ha, hb = hodge_matrix(a), hodge_matrix(b)
    assert ha.nullspace() == da.nullspace() and hb.nullspace() == db.nullspace()
    both = ha.col_join(hb)
    assert both.nullspace() == [sp.eye(9).col(0), sp.eye(9).col(4)]
    sample = sp.eye(9).col(1) - sp.eye(9).col(3)
    assert db * sample == sp.zeros(9, 1) and ha * sample != sp.zeros(ha.rows, 1)
    signs = [1, -1, 1]
    involution = sp.diag(*(x*y for x,y in itertools.product(signs, repeat=2)))
    assert involution * sample == -sample
    assert db.row(0) == sp.zeros(1,9)
    return dict(tangent_order='row-major T11,T12,...,T33', Hodge_derivative_ranks=[ha.rank(),hb.rank()],
                Hodge_kernel_equals_normal_kernel=True, both_rank=both.rank(),
                common_kernel=primitive_columns(both), kernel_of_graph_B=primitive_columns(db),
                anti_direction_delta_A=list(da*sample), anti_direction_delta_B=list(db*sample),
                anti_direction_Hodge_nonzero_entries_A=sum(bool(v) for v in ha*sample))


if __name__ == '__main__':
    result = dict(residues=elliptic_residues(), target_dimensions=dimensions(), tangent=tangent_checks())
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2, default=int))
