"""Exact joint moments of uniform multiset words and diagram cumulants, stdlib only."""
from collections import Counter
from fractions import Fraction as F
from itertools import permutations, product
from math import comb, factorial, lcm, prod
import json


def wedge(u, v):
    return [[u[i]*v[j]-v[i]*u[j] for j in range(len(v))] for i in range(len(u))]


def triangle(a, b, c, dimension=6):
    out = [[0]*dimension for _ in range(dimension)]
    for i, j in ((a, b), (b, c), (c, a)):
        out[i][j], out[j][i] = 1, -1
    return out


def combine(a, b, sign=1):
    return [[aa+sign*bb for aa, bb in zip(ra, rb)] for ra, rb in zip(a, b)]


def coefficients(matrix, weights):
    # The formula in unnormalized rational coordinates has no square roots.
    n = len(weights)
    a = [[F(matrix[i][j], weights[i]*weights[j]) for j in range(n)] for i in range(n)]
    p = [[sum(weights[k]*a[i][k]*a[j][k] for k in range(n)) for j in range(n)]
         for i in range(n)]
    trace4 = sum(weights[i]*weights[j]*p[i][j]**2 for i in range(n) for j in range(n))
    row_square = sum(weights[i]*p[i][i]**2 for i in range(n))
    triangle_sum = sum(weights[i]*weights[j]*a[i][j]**2*p[i][j]
                       for i in range(n) for j in range(i+1, n))
    return trace4/240, (4*triangle_sum-row_square)/120


def mixed_coefficients(a, b, weights):
    lhs = coefficients(combine(a, b), weights)
    rhs = coefficients(combine(a, b, -1), weights)
    first, second = coefficients(a, weights), coefficients(b, weights)
    return tuple((x+y-2*z-2*w)/12 for x, y, z, w in zip(lhs, rhs, first, second))


def word_moments(a, b, weights, scale):
    # Recurse on the last letter of the word. The DP stores integer unnormalized
    # moments of both scores and allows every full six-axis interleaving.
    dim = len(weights)
    stocks = tuple(scale*w for w in weights)
    edge_a = [[F(scale*a[i][j], 2*stocks[i]*stocks[j]) for j in range(dim)] for i in range(dim)]
    edge_b = [[F(scale*b[i][j], 2*stocks[i]*stocks[j]) for j in range(dim)] for i in range(dim)]
    den = lcm(*(v.denominator for mat in (edge_a, edge_b) for row in mat for v in row))
    int_a = [[int(den*v) for v in row] for row in edge_a]
    int_b = [[int(den*v) for v in row] for row in edge_b]
    powers = [(p,q) for p in range(3) for q in range(3)] + [(3,0),(4,0),(0,3),(0,4)]
    index = {power:i for i, power in enumerate(powers)}
    shifts = [[(i,j,index[i,j],comb(p,i)*comb(q,j)) for i in range(p+1) for j in range(q+1)]
              for p, q in powers]
    initial = (0,)*dim
    counts = {initial:(1,)+(0,)*(len(powers)-1)}
    for used in product(*(range(n+1) for n in stocks)):
        if used == initial:
            continue
        totals = [0]*len(powers)
        for last, count in enumerate(used):
            if not count:
                continue
            prev = list(used)
            prev[last] -= 1
            old = counts[tuple(prev)]
            dx = sum(prev[i]*int_a[i][last] for i in range(dim))
            dy = sum(prev[i]*int_b[i][last] for i in range(dim))
            px, py = [dx**p for p in range(5)], [dy**q for q in range(5)]
            for idx,(p,q) in enumerate(powers):
                totals[idx] += sum(c*px[p-i]*py[q-j]*old[k] for i,j,k,c in shifts[idx])
        counts[used] = tuple(totals)
    total = counts[stocks]
    assert total[0] == factorial(sum(stocks)) // prod(factorial(k) for k in stocks)
    return total[0], {(p,q):F(v,total[0]*den**(p+q)) for (p,q),v in zip(powers,total)}


def one_word_joint(a, b):
    def score(word, matrix):
        return F(sum(matrix[i][j] for pos, i in enumerate(word) for j in word[pos+1:]),2)
    joint = Counter((score(word, a), score(word, b)) for word in permutations(range(6)))
    x_counts, y_counts = Counter(), Counter()
    for (x,y), n in joint.items():
        x_counts[x] += n
        y_counts[y] += n
    indep = all(joint[x,y]*720 == x_counts[x]*y_counts[y] for x in x_counts for y in y_counts)
    return indep, [[str(x),str(y),n] for (x,y),n in sorted(joint.items())]


def check_case(a, b, weights, scales):
    assert all(sum(row) == 0 for m in (a,b) for row in m)
    mixed = mixed_coefficients(a,b,weights)
    results = []
    for n in scales:
        number, moment = word_moments(a,b,weights,n)
        assert moment[1,0] == moment[0,1] == 0
        xy = moment[1,1]
        cov_sq = moment[2,2]-moment[2,0]*moment[0,2]
        cumul = cov_sq-2*xy**2
        assert cumul == mixed[0]+mixed[1]/n
        for matrix, fourth, var in ((a,moment[4,0],moment[2,0]),(b,moment[0,4],moment[0,2])):
            leading, correction = coefficients(matrix,weights)
            assert fourth-3*var**2 == leading+correction/n
        results.append({"N":n, "uniform_complete_words":number, "var_x":str(moment[2,0]),
                        "var_y":str(moment[0,2]), "cov_xy":str(xy), "E_x2_y2":str(moment[2,2]),
                        "cov_x2_y2":str(cov_sq), "cumulant_22":str(cumul)})
    return {"weights":weights,"mixed_cumulant_limit":str(mixed[0]),"coefficient_of_1_over_N":str(mixed[1]),
            "exact_word_moments":results}


def main():
    t = triangle(0,1,2)
    overlap = triangle(2,3,4)
    disjoint = triangle(3,4,5)
    a = wedge((1,-1,0,0,0,0),(0,0,1,-1,0,0))
    b = wedge((1,1,0,0,-2,0),(0,0,1,1,0,-2))
    pooled = [[0]*6 for _ in range(6)]
    for i in (0,1,2):
        pooled[i][3], pooled[3][i] = 1,-1
        pooled[4][i], pooled[i][4] = 1,-1
    pooled[3][4], pooled[4][3] = 3,-3
    unit = (1,)*6
    cases = {"orthogonal_but_dependent": (a,b,unit,(1,2,3)),
             "one_shared_axis_original": (t,overlap,unit,(1,2)),
             "disjoint_original": (t,disjoint,unit,(1,2)),
             "three_shared_pooled": (t,pooled,unit,(1,2)),
             "unequal_inventories": (combine(t,a),combine(overlap,b),(1,2,1,1,2,1),(1,2))}
    out = {name:check_case(*case) for name,case in cases.items()}
    for name in ("orthogonal_but_dependent","three_shared_pooled","one_shared_axis_original"):
        first, second = cases[name][:2]
        indep, joint = one_word_joint(first,second)
        out[name]["N1_joint_independent"] = indep
        out[name]["N1_joint_x_y_multiplicity"] = joint
    assert not out["orthogonal_but_dependent"]["N1_joint_independent"]
    assert out["three_shared_pooled"]["N1_joint_independent"]
    assert out["one_shared_axis_original"]["N1_joint_independent"]
    assert (out["orthogonal_but_dependent"]["mixed_cumulant_limit"],
            out["orthogonal_but_dependent"]["coefficient_of_1_over_N"]) == ("0","-2/15")
    assert (out["one_shared_axis_original"]["mixed_cumulant_limit"],
            out["one_shared_axis_original"]["coefficient_of_1_over_N"]) == ("1/90","-1/90")
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
