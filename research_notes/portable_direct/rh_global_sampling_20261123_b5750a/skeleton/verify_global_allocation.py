"""Exact finite checks for global point-sample allocation; no external packages."""
from fractions import Fraction as Q
from itertools import product
import json
from pathlib import Path


def phi(b, k):
    u, v = divmod(b, k)
    return (k-v)*u**5 + v*(u+1)**5 - b


def compositions(b):
    if b == 0:
        yield ()
    else:
        for h in range(1, b+1):
            for rest in compositions(b-h):
                yield (h,) + rest


def cost(blocks, ks):
    return sum((Q(phi(b, k), x**4)
                for (x, b), k in zip(blocks, ks)), Q(0))


def greedy_curve(blocks):
    ks = [1]*len(blocks)
    curve = {sum(ks): (cost(blocks, ks), tuple(ks))}
    while any(k < b for (x, b), k in zip(blocks, ks)):
        available = [i for i, ((x, b), k) in enumerate(zip(blocks, ks))
                     if k < b]
        i = max(available, key=lambda i:
                Q(phi(blocks[i][1], ks[i])-phi(blocks[i][1], ks[i]+1),
                  blocks[i][0]**4))
        ks[i] += 1
        curve[sum(ks)] = (cost(blocks, ks), tuple(ks))
    return curve


def exhaustive_curve(blocks):
    curve, count = {}, 0
    for ks in product(*(range(1, b+1) for x, b in blocks)):
        count += 1
        k, c = sum(ks), cost(blocks, ks)
        if k not in curve or c < curve[k][0]:
            curve[k] = (c, ks)
    return curve, count


def balanced_nodes(x, b, k):
    u, v = divmod(b, k)
    nodes = [x]
    for j in range(k):
        nodes.append(nodes[-1] + u + (j < v))
    return nodes


def hidden_road(blocks, ks):
    end = blocks[-1][0] + blocks[-1][1]
    q = [Q(0)]*(end+2)
    samples = set()
    for (x, b), k in zip(blocks, ks):
        nodes = balanced_nodes(x, b, k)
        samples.update(nodes)
        for l, r in zip(nodes, nodes[1:]):
            h = r-l
            for n in range(l, r+1):
                q[n] = Q((n-l)**2*(r-n)**2, 8*x*h*h)
    return q, samples


def encode(value):
    if isinstance(value, Q):
        return {"numerator": str(value.numerator),
                "denominator": str(value.denominator),
                "approx": float(value)}
    raise TypeError(type(value).__name__)


def main():
    composition_count = 0
    for b in range(1, 13):
        minima = {}
        for hs in compositions(b):
            composition_count += 1
            value = sum(h**5-h for h in hs)
            k = len(hs)
            minima[k] = min(value, minima.get(k, value))
        assert minima == {k: phi(b, k) for k in range(1, b+1)}
        gains = [phi(b, k)-phi(b, k+1) for k in range(1, b)]
        assert all(g >= 0 for g in gains)
        assert all(a >= b for a, b in zip(gains, gains[1:]))

    datasets = [[(8, 8), (16, 16), (32, 32)],
                [(5, 5), (10, 10), (20, 7)]]
    allocation_checks = []
    for blocks in datasets:
        brute, count = exhaustive_curve(blocks)
        greedy = greedy_curve(blocks)
        assert set(brute) == set(greedy)
        assert all(brute[k][0] == greedy[k][0] for k in brute)
        allocation_checks.append({
            "blocks": blocks, "all_allocations": count,
            "budgets_verified": len(brute),
            "selected_curve": {
                str(k): {"allocation": list(greedy[k][1]),
                         "shape_cost": greedy[k][0]}
                for k in sorted({len(blocks), 6, 12, 18,
                                 sum(b for x, b in blocks)}) if k in greedy}})

    blocks = datasets[0]
    curve = greedy_curve(blocks)
    road_checks = []
    for budget in [3, 6, 12, 18, 30, 55, 56]:
        shape, ks = curve[budget]
        q, samples = hidden_road(blocks, ks)
        end = blocks[-1][0] + blocks[-1][1]
        assert all(q[n] == 0 for n in samples)
        max_source_ratio = max(
            abs(q[n+1]-2*q[n]+q[n-1])*n for n in range(1, end+1))
        assert max_source_ratio <= 1
        energy = sum((q[n]*q[n]/(n*n)
                      for n in range(blocks[0][0], end+1)), Q(0))
        lower, upper = shape/161280, shape/120
        assert lower <= energy <= upper
        road_checks.append({"budget_intervals": budget,
                            "sample_count": len(samples),
                            "allocation": list(ks),
                            "max_n_abs_second_difference": max_source_ratio,
                            "lower": lower, "actual_hidden_energy": energy,
                            "upper": upper})
    result = {"status": "all exact checks passed",
              "composition_count": composition_count,
              "allocation_checks": allocation_checks,
              "road_checks": road_checks,
              "scope": "finite rational formula, greedy, saturation and source-join checks; unbounded theorems use proof.md"}
    out = Path(__file__).with_name("global_allocation_certificate.json")
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2,
                              default=encode)+"\n")
    print(json.dumps({"status": result["status"],
                      "composition_count": composition_count,
                      "allocation_counts": [x["all_allocations"]
                                            for x in allocation_checks],
                      "road_checks": len(road_checks),
                      "output": str(out)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
