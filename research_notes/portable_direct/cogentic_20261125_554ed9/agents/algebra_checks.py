"""Exact finite checks for selected Cogentic extraction; no main-theorem audit claim."""
from fractions import Fraction as Q
from itertools import product
import json


def moment(states, powers):
    return sum(Q(product_value(x ** a for x, a in zip(u, powers)), len(states)) for u in states)


def product_value(values):
    out = 1
    for value in values:
        out *= value
    return out


positive = [(2, 1, 0), (1, 0, 2), (0, 2, 1)]
negative = [(2, 0, 1), (1, 2, 0), (0, 1, 2)]
moments = []
for powers in product(range(3), repeat=3):
    if sum(powers) <= 2:
        left, right = moment(positive, powers), moment(negative, powers)
        assert left == right
        moments.append({"powers": powers, "common_value": str(left)})


def orientation(u):
    x, y, z = u
    return (x-y)*(x-z)*(y-z)


orient_p = sum(map(orientation, positive)) // len(positive)
orient_n = sum(map(orientation, negative)) // len(negative)
assert (orient_p, orient_n) == (2, -2)

a = [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]
b = [tuple(-t for t in row) for row in a]
mu, sigma = Q(1, 2), Q(1, 2)
sign = [[mu + sigma * sum(ax[k] * by[k] for k in range(3)) for by in b] for ax in a]
assert sign == [[Q(-1 if x == y else 1) for y in range(4)] for x in range(4)]
tensor = [[[sum(Q(by[k] * by[i] * by[j], 4) for by in b)
            for j in range(3)] for i in range(3)] for k in range(3)]
for ax in a:
    for k in range(3):
        quadratic = sum(sigma * sigma * ax[i] * ax[j] * tensor[k][i][j]
                        for i in range(3) for j in range(3))
        assert -2 * mu * sigma * ax[k] == quadratic

matrix = [[2, 3], [3, 2]]
solution = [4, 5]
rhs = [sum(row[j] * solution[j] for j in range(2)) % 6 for row in matrix]
assert rhs == [5, 4]
row_transform = [[-1, 1], [-3, 2]]
transformed = [[sum(row_transform[i][k] * matrix[k][j] for k in range(2)) % 6
                for j in range(2)] for i in range(2)]
assert transformed == [[1, 5], [0, 1]]

# F_2^2 subspace distribution, represented by the tuple of its elements.
def add_span(span, v):
    return tuple(sorted(set(span) | {x ^ v for x in span}))


dist = [Q(1, 10), Q(2, 10), Q(3, 10), Q(4, 10)]
ell, K = 4, 2
space_law = {(0,): Q(1)}
for shift in [0] * (K * ell) + [1] * ell + [2] * ell:
    next_law = {}
    for span, probability in space_law.items():
        for v, weight in enumerate(dist):
            new_span = add_span(span, v ^ shift)
            next_law[new_span] = next_law.get(new_span, Q(0)) + probability * weight
    space_law = next_law
failure = sum(probability for span, probability in space_law.items() if len(span) < 4)
bound = Q(2*K, 2**ell)
assert failure <= bound

report = {
    "scope": "Exact finite checks of portable identities; not certification of the three main theorems.",
    "moment_matching": {"positive": positive, "negative": negative, "moments_through_degree_2": moments,
                        "orientation_expectations": [orient_p, orient_n]},
    "boolean_cubic": {"sign_matrix": [[int(x) for x in row] for row in sign], "mu": str(mu),
                      "sigma": str(sigma), "identity_checks": len(a)*3, "all_passed": True},
    "composite_modulus": {"modulus": 6, "matrix": matrix, "rhs": rhs, "solution": solution,
                          "bezout_row_transform": row_transform, "triangular_matrix": transformed},
    "distribution_free_rank_sample": {"field": "F_2", "dimension": K, "ell": ell,
                                      "distribution": list(map(str, dist)), "exact_failure_probability": str(failure),
                                      "lemma_bound": str(bound)}
}
print(json.dumps(report, ensure_ascii=False, indent=2))
