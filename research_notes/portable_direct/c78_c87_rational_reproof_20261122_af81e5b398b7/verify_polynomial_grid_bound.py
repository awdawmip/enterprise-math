"""Exact finite checks of the polynomial small-value grid bound."""
import json
from fractions import Fraction as Q
from pathlib import Path


def evaluate(poly, x, y):
    return sum(coefficient*x**i*y**j for (i, j), coefficient in poly.items())


def leading_data(poly):
    poly = {ij: coefficient for ij, coefficient in poly.items() if coefficient}
    d = max(i for i, j in poly)
    e = max(j for i, j in poly if i == d)
    return d, e, poly[d, e]


def main():
    cases = [
        ("X+Y-1", {(1, 0): Q(1), (0, 1): Q(1), (0, 0): Q(-1)}),
        ("(X-1/2)(Y-1/3)", {(1, 1): Q(1), (1, 0): Q(-1, 3),
                              (0, 1): Q(-1, 2), (0, 0): Q(1, 6)}),
        ("Y^3-1/8", {(0, 3): Q(1), (0, 0): Q(-1, 8)}),
        ("X+Y^9-1/2", {(1, 0): Q(1), (0, 9): Q(1), (0, 0): Q(-1, 2)}),
        ("(Y-1/2)X^2+Y^7*X-Y^2/3", {(2, 1): Q(1), (2, 0): Q(-1, 2),
                                      (1, 7): Q(1), (0, 2): Q(-1, 3)}),
        ("(2/7)(Y-1/4)^2*X^3+X*Y-1/11", {(3, 2): Q(2, 7),
            (3, 1): Q(-1, 7), (3, 0): Q(1, 56), (1, 1): Q(1), (0, 0): Q(-1, 11)})
    ]
    rows = []
    n = 24
    for name, polynomial in cases:
        d, e, leading = leading_data(polynomial)
        for h in (4, 16, 64):
            epsilon = abs(leading)/h**(d+e)
            count = sum(abs(evaluate(polynomial, Q(i, n), Q(j, n))) <= epsilon
                        for i in range(n+1) for j in range(n+1))
            s = 2*n//h+1
            bound = (d+e)*(n+1)*s
            assert count <= bound, (name, n, h, count, bound)
            rows.append({"polynomial": name, "N": n, "h": h, "d": d, "e": e,
                         "L": str(leading), "epsilon": str(epsilon),
                         "count": count, "bound": bound,
                         "effective_bound": min((n+1)**2, bound)})
    result = {"arithmetic": "fractions.Fraction", "experiments": len(rows),
              "all_checks_passed": True, "rows": rows,
              "scope": "finite formula checks; the universal statement has a finite algebraic proof"}
    output = Path(__file__).with_name("polynomial_grid_checks.json")
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
