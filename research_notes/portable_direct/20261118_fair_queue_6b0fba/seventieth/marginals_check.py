"""Sharp finite-population moment bounds on one exposed PFSS block. Python 3.10+."""
import argparse
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
import json
from math import comb, prod
from pathlib import Path


def geometry(path):
    with path.open("rb") as source:
        line = next(source)
    digest = sha256(line).hexdigest()
    assert digest == "fcfc138fbbddacd089c228b4cb3783e55064b9c9879d84f5de642911ebc860a0"
    cell = json.loads(line)
    assert (cell["X"], cell["upper"]) == (100000, 101000)
    rows = {row["p"]: row for row in cell["rows"]}
    by_address = {}
    for p, row in rows.items():
        for q in range(row["qlo"], row["qhi"] + 1):
            by_address.setdefault(q, set()).add(p)
    target = {q: row_ids for q, row_ids in by_address.items() if q % 30 == 29}
    duplicate = {q for q, row_ids in target.items() if len(row_ids) > 1}
    assert duplicate == {419} and by_address[419] == {239, 241}
    # The only repeated address in this residue is the known prime 419.
    assert all(419 % j for j in range(2, 21))
    count = sum(row["q_mod_30_counts"][29] for row in rows.values()) - 1
    size = len(target)
    inside = sum(2 in row_ids for row_ids in target.values())
    assert (size, count, inside, len(by_address)) == (69, 29, 17, 2016)
    return size, count, inside, digest


def interpolating_weights(weights, nodes):
    """Integrals of Lagrange basis functions under the reference distribution."""
    missing = set(range(len(weights))).difference(nodes)
    denominator = sum(weights)
    result = []
    for node in nodes:
        other = [v for v in nodes if v != node]
        divisor = prod(node - v for v in other)
        mass = Fraction(weights[node], denominator)
        mass += sum(Fraction(weights[i] * prod(i - v for v in other),
                             denominator * divisor) for i in missing)
        result.append(mass)
    return result


def bounds(weights, t):
    degree = len(weights) - 1
    lower, upper = Fraction(0), Fraction(1)
    lower_roots, upper_roots = None, None
    for nodes in combinations(range(1, degree + 1), t):
        # Q(x) = product_i (i-x)/i has Q(0)=1.
        q_denominator = prod(nodes)
        q_values = [prod(v - x for v in nodes) for x in range(1, degree + 1)]
        majorizes = min(q_values) >= 0
        minorizes = max(q_values) <= 0
        if not (majorizes or minorizes):
            continue
        numerator = q_denominator * weights[0] + sum(
            value * w for value, w in zip(q_values, weights[1:]))
        mean = Fraction(numerator, q_denominator * sum(weights))
        if majorizes and mean <= upper:
            upper, upper_roots = mean, nodes
        if minorizes and mean >= lower:
            lower, lower_roots = mean, nodes
    assert upper_roots is not None
    return [(lower, lower_roots), (upper, upper_roots)]


def certificate(weights, t, bound, nodes):
    if nodes is None:
        # A degree-14 quadrature entirely on positive integers serves every t <= 14.
        assert t <= 14 and bound == 0
        support = tuple(range(1, 15)) + (16,)
    else:
        support = (0,) + nodes
    probabilities = interpolating_weights(weights, support)
    assert min(probabilities) >= 0
    distribution = dict(zip(support, probabilities))
    assert distribution.get(0, 0) == bound
    for k in range(t + 1):
        prior = Fraction(sum(w * comb(i, k) for i, w in enumerate(weights)), sum(weights))
        assert sum(p * comb(i, k) for i, p in distribution.items()) == prior
    return {"empty_probability": str(bound),
            "dual": "zero polynomial" if nodes is None else {"roots": list(nodes), "value_at_zero": 1},
            "primal": {str(i): str(p) for i, p in distribution.items() if p}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path,
                        default=Path("research_artifacts/PFSSV_REVISION_20260908/cell_profiles.jsonl"))
    size, count, inside, digest = geometry(parser.parse_args().source)
    weights = [comb(inside, i) * comb(size - inside, count - i) for i in range(inside + 1)]
    assert sum(weights) == comb(size, count)
    rows = []
    for t in range(inside + 1):
        (lo, lo_nodes), (hi, hi_nodes) = bounds(weights, t)
        rows.append({"t": t, "lower": certificate(weights, t, lo, lo_nodes),
                     "upper": certificate(weights, t, hi, hi_nodes)})
    positive_order = next(v["t"] for v in rows if Fraction(v["lower"]["empty_probability"]) > 0)
    unique_order = next(v["t"] for v in rows
                        if v["lower"]["empty_probability"] == v["upper"]["empty_probability"])
    assert (positive_order, unique_order) == (15, 17)
    print(json.dumps({"source_first_line_sha256": digest, "size": size, "occupied": count,
                      "row_addresses": inside, "first_strict_lower_bound": positive_order,
                      "first_unique_empty_probability": unique_order, "bounds": rows},
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
